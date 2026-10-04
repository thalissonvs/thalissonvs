## Hi, I'm Thalison 👋

I build the browser side of web scraping: infrastructure that renders, survives and scales on pages designed to block automation.

Right now I'm a Lead Software Engineer at [Crustdata](https://crustdata.com), where I built and own the browser platform behind our SERP, page fetch and Google Maps APIs. It runs as a fleet of browser workers on Kubernetes and handles around a million requests a day. Before that I worked on fault-tolerant crawling pipelines for enterprise clients at [Zyte](https://www.zyte.com), and before that I co-founded a company that ran scrapers against Instagram, TikTok and Facebook for about a thousand paying customers.

### Pydoll


I created and maintain [Pydoll](https://github.com/autoscrape-labs/pydoll), an async Python library that drives Chromium straight over the DevTools Protocol, with no WebDriver and nothing that gives the automation away. It started as a rewrite of a production crawler that Selenium could no longer keep alive, and reached #1 on GitHub trending and the front page of Hacker News at launch.

[![Stars](https://img.shields.io/github/stars/autoscrape-labs/pydoll?style=flat-square&label=stars&color=1a73e8)](https://github.com/autoscrape-labs/pydoll)
[![PyPI downloads](https://img.shields.io/pypi/dm/pydoll-python?style=flat-square&label=downloads&color=188038)](https://pypi.org/project/pydoll-python/)
[![Docs](https://img.shields.io/badge/docs-pydoll.tech-5f6368?style=flat-square)](https://pydoll.tech)


### Live

<!-- LIVE:START -->
**[Pydoll](https://github.com/autoscrape-labs/pydoll)** has **7,106** stars and **409** forks, latest release **[3.0.0](https://github.com/autoscrape-labs/pydoll/releases/tag/3.0.0)** on Sep 29, 2026.

**Recently merged**

- [docs: explain why the User-Agent major must equal the binary, and say…](https://github.com/autoscrape-labs/pydoll/pull/465) in `autoscrape-labs/pydoll`, Sep 29, 2026
- [fix(playwright): fractional clicks, geolocation accuracy, stale frames, wire headers and console handles](https://github.com/autoscrape-labs/pydoll/pull/464) in `autoscrape-labs/pydoll`, Sep 29, 2026
- [feat(sync): generated synchronous API for pydoll](https://github.com/autoscrape-labs/pydoll/pull/462) in `autoscrape-labs/pydoll`, Sep 29, 2026
- [Fix/fingerprint header order and coherence](https://github.com/autoscrape-labs/pydoll/pull/461) in `autoscrape-labs/pydoll`, Sep 16, 2026
- [Fix/fingerprint worker webgpu and sw refetch](https://github.com/autoscrape-labs/pydoll/pull/460) in `autoscrape-labs/pydoll`, Sep 15, 2026

<sub>Updated 2026-10-04 21:02 UTC by a GitHub Action that reads this data with Pydoll itself.</sub>
<!-- LIVE:END -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/thalissonvs/thalissonvs/output/snake-dark.svg">
  <img alt="Snake eating my contribution graph" src="https://raw.githubusercontent.com/thalissonvs/thalissonvs/output/snake.svg" width="100%">
</picture>


### What I work with

Python (asyncio, FastAPI, Django), the Chrome DevTools Protocol, Kubernetes on EKS with KEDA, Redis, PostgreSQL, Docker, and OpenTelemetry with Grafana and Datadog for seeing what's actually happening in production.

<details>
<summary><b>Other things I've built</b></summary>
<br>

**Browser worker platform.** Seven worker types on a single Helm chart, queue-based scheduling with a circuit breaker in front of the workers, a four-level health recovery hierarchy, and autoscaling on queue depth. A Bing SERP service on top of it sustains around 1,000 requests per minute with stable tail latency while browsers restart and proxies rotate underneath.

**Document processing pipeline.** Takes multi-gigabyte archives of scanned traffic fines, runs CPU-optimized OCR, uses an LLM to pull out fields from documents with no standard layout, and reconciles everything against the database. Cut the manual work, previously done by freelancers, by more than 80%.

**Signature fraud detection.** A YOLO model trained on a hand-labeled dataset to find and crop signatures on driver's licenses in any format or orientation, followed by an LLM comparison guided by the rules of the manual process. Served through FastAPI and ran in production at close to 100% accuracy.

</details>

### Get in touch

[thalissfernandes99@gmail.com](mailto:thalissfernandes99@gmail.com). Fala português? Pode mandar mensagem em português mesmo.
