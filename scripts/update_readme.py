"""Atualiza a seção entre <!-- LIVE:START --> e <!-- LIVE:END --> do README.

Os dados vêm da API pública do GitHub, lidos pelo próprio Pydoll num Chrome headless.
Se o Pydoll falhar por qualquer motivo, cai para urllib e o rodapé diz isso.
"""
import asyncio
import json
import os
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USER = "thalissonvs"
REPO = "autoscrape-labs/pydoll"
README = Path(__file__).resolve().parent.parent / "README.md"
API = "https://api.github.com"
URLS = {
    "repo": f"{API}/repos/{REPO}",
    "release": f"{API}/repos/{REPO}/releases/latest",
    "prs": f"{API}/search/issues?q=author:{USER}+is:pr+is:merged+is:public&sort=updated&order=desc&per_page=5",
}


def _find_value(obj):
    """Acha o 'value' dentro da resposta CDP do Runtime.evaluate, seja qual for o aninhamento."""
    if isinstance(obj, dict):
        if "value" in obj and isinstance(obj["value"], str):
            return obj["value"]
        for v in obj.values():
            found = _find_value(v)
            if found is not None:
                return found
    return None


async def fetch_with_pydoll() -> dict:
    from pydoll.browser.chromium import Chrome
    from pydoll.browser.options import ChromiumOptions

    options = ChromiumOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    data = {}
    async with Chrome(options=options) as browser:
        tab = await browser.start()
        for key, url in URLS.items():
            await tab.go_to(url)
            raw = _find_value(await tab.execute_script("return document.body.innerText"))
            data[key] = json.loads(raw)
    return data


def fetch_with_urllib() -> dict:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": USER}
    if token := os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    data = {}
    for key, url in URLS.items():
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
                data[key] = json.load(r)
        except urllib.error.HTTPError:
            if key != "release":  # repo sem release publicada devolve 404, e tudo bem
                raise
            data[key] = {}
    return data


def fmt_date(iso: str) -> str:
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).strftime("%b %d, %Y")


def render(data: dict, source: str) -> str:
    repo, rel, prs = data["repo"], data.get("release") or {}, data["prs"].get("items", [])
    lines = [
        f"**[Pydoll](https://github.com/{REPO})** has **{repo['stargazers_count']:,}** stars and "
        f"**{repo['forks_count']:,}** forks"
        + (f", latest release **[{rel['tag_name']}]({rel['html_url']})** on {fmt_date(rel['published_at'])}." if rel.get("tag_name") else "."),
        "",
    ]
    if prs:
        lines += ["**Recently merged**", ""]
        for pr in prs:
            repo_name = pr["repository_url"].split("/repos/")[1]
            lines.append(f"- [{pr['title']}]({pr['html_url']}) in `{repo_name}`, {fmt_date(pr['closed_at'])}")
        lines.append("")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines.append(f"<sub>Updated {now} by a GitHub Action {source}.</sub>")
    return "\n".join(lines)


def main():
    try:
        data = asyncio.run(fetch_with_pydoll())
        source = "that reads this data with Pydoll itself"
    except Exception as exc:  # noqa: BLE001
        print(f"Pydoll falhou, usando urllib: {exc!r}")
        data = fetch_with_urllib()
        source = "(Pydoll was taking a day off, so plain urllib did the job)"

    text = README.read_text(encoding="utf-8")
    new = re.sub(
        r"(<!-- LIVE:START -->).*?(<!-- LIVE:END -->)",
        lambda m: f"{m.group(1)}\n{render(data, source)}\n{m.group(2)}",
        text,
        flags=re.S,
    )
    README.write_text(new, encoding="utf-8")
    print("README atualizado")


if __name__ == "__main__":
    main()
