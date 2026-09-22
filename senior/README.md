<h1>Senior Reference Packs</h1>

<p>Exhaustive, on-demand domain knowledge for senior agents in <a href="https://github.com/xscriptor-ai/agents">xscriptor-ai/agents</a> and for direct orchestration. Each pack is a standard OpenCode skill: <code>senior/&lt;name&gt;/SKILL.md</code> plus a <code>references/</code> directory with the full depth.</p>

<h2>Layout</h2>

<pre><code>senior/
  &lt;pack&gt;/
    SKILL.md          # entrypoint: triggers, core rules, reference index, port
    references/
      NN-topic.md     # numbered deep references, one topic each
</code></pre>

<p>Rules: the directory name must equal the frontmatter <code>name</code> (OpenCode requirement). No executables, no scripts, no side effects. Every reference listed in the <code>SKILL.md</code> index must exist.</p>

<h2>Port Contract</h2>

<p>Every pack exposes the same stable port so consumers can depend on it <strong>optionally</strong>. The port is declared in frontmatter <code>metadata</code> (all values are strings) and documented in the <code>## Port</code> section of the <code>SKILL.md</code>.</p>

<pre><code>---
name: python
description: "Python reference pack (3.12-3.14): language core, typing, async, web frameworks, data layer, testing, tooling, performance, security, deployment. Use when writing or reviewing non-trivial Python."
license: MIT
metadata:
  port: "skill://senior/python"
  port-version: "2.0.0"
  kind: "reference-pack"
  domain: "language"
  consumers: "senior-python,senior-data-ml,orchestrator"
  optional: "true"
  entrypoint: "SKILL.md"
  stability: "stable"
---

# Python

...domain overview, core rules, reference index...

## Port

- **Port id** — `skill://senior/python` (version in `metadata.port-version`).
- **Kind** — read-only reference pack; no side effects, no tools required.
- **Entrypoint** — this `SKILL.md`; depth lives in `references/`.
- **Load modes**
  1. Installed agent: `skill({ name: "python" })` in OpenCode; Claude Code reads `<skills-dir>/python/SKILL.md`.
  2. Orchestrator: read `SKILL.md`, then load only the references the task needs.
  3. Not installed: consumers MUST degrade gracefully using their own guidance and report the degraded mode. Never block on the pack.
- **Consumer contract** — `metadata.consumers` lists the agents that may load it; consumers reference it as `load skill python (optional)`.
- **Stability** — `stable`; breaking changes bump `port-version` major.
</code></pre>

<h3>Port fields</h3>

<table>
  <thead>
    <tr><th>Field</th><th>Meaning</th><th>Allowed values</th></tr>
  </thead>
  <tbody>
    <tr><td><code>port</code></td><td>Stable logical id, independent of install path</td><td><code>skill://senior/&lt;name&gt;</code></td></tr>
    <tr><td><code>port-version</code></td><td>Semver of the consumed interface</td><td><code>MAJOR.MINOR.PATCH</code></td></tr>
    <tr><td><code>kind</code></td><td>Artifact type</td><td><code>reference-pack</code></td></tr>
    <tr><td><code>domain</code></td><td>Classification for orchestration</td><td><code>language</code>, <code>platform</code>, <code>practice</code></td></tr>
    <tr><td><code>consumers</code></td><td>Agents that may load the pack</td><td>comma-separated agent names, always includes <code>orchestrator</code></td></tr>
    <tr><td><code>optional</code></td><td>May be absent without breaking consumers</td><td><code>true</code></td></tr>
    <tr><td><code>entrypoint</code></td><td>File a consumer starts from</td><td><code>SKILL.md</code></td></tr>
    <tr><td><code>stability</code></td><td>Lifecycle state</td><td><code>draft</code>, <code>stable</code>, <code>deprecated</code></td></tr>
  </tbody>
</table>

<h3>Usage modes</h3>

<ol>
  <li><strong>Agent + pack installed</strong> — the agent loads the pack on demand with the native skill tool and pulls references as needed. Deepest mode.</li>
  <li><strong>Orchestrator</strong> — the orchestrator reads <code>SKILL.md</code> directly and injects only the needed references into subagent context.</li>
  <li><strong>Agent without the pack</strong> — the agent proceeds with its embedded guidance, states the degraded mode, and never invents content that only the pack would provide.</li>
</ol>

<h2>Authoring Rules</h2>

<ul>
  <li><strong>Exhaustive</strong> — each reference is 150-350 lines of dense content; a pack is a small book on its domain, not a cheatsheet.</li>
  <li><strong>Current</strong> — content reflects the state of the ecosystem in 2026. State version floors (for example Python 3.12-3.14) and prefer stable APIs. Do not invent exact version numbers: use ranges and say "verify upstream" when uncertain.</li>
  <li><strong>Practical</strong> — decision tables, minimal runnable snippets, anti-patterns, checklists, migration notes for deprecated advice.</li>
  <li><strong>Indexed</strong> — <code>SKILL.md</code> is the map: triggers, core rules, and a table listing every reference with scope and "load when". The depth lives in <code>references/</code>.</li>
  <li><strong>Links</strong> — references cross-link each other with relative paths (<code>./02-async.md</code>); every link must resolve.</li>
  <li><strong>Language</strong> — English. No emojis.</li>
</ul>

<h2>Registry</h2>

<table>
  <thead>
    <tr><th>Pack</th><th>Domain</th><th>Consumers</th><th>Status</th></tr>
  </thead>
  <tbody>
    <tr><td><code>api-design</code></td><td>practice</td><td>senior-backend, senior-architecture, senior-python, senior-node-backend, orchestrator</td><td>stable</td></tr>
    <tr><td><code>architecture</code></td><td>practice</td><td>senior-architecture, senior-fullstack, orchestrator</td><td>stable</td></tr>
    <tr><td><code>cloud</code></td><td>platform</td><td>senior-cloud-native, senior-devops, orchestrator</td><td>stable</td></tr>
    <tr><td><code>deployment</code></td><td>practice</td><td>senior-devops, senior-cloud-native, senior-node-backend, orchestrator</td><td>stable</td></tr>
    <tr><td><code>go</code></td><td>language</td><td>senior-go, orchestrator</td><td>stable</td></tr>
    <tr><td><code>java-kotlin</code></td><td>language</td><td>senior-jvm, orchestrator</td><td>stable</td></tr>
    <tr><td><code>mobile</code></td><td>platform</td><td>senior-mobile, orchestrator</td><td>stable</td></tr>
    <tr><td><code>monorepo</code></td><td>practice</td><td>senior-architecture, senior-devops, senior-frontend-ts, senior-node-backend, orchestrator</td><td>stable</td></tr>
    <tr><td><code>observability</code></td><td>practice</td><td>senior-devops, senior-cloud-native, senior-systems, orchestrator</td><td>stable</td></tr>
    <tr><td><code>performance</code></td><td>practice</td><td>senior-architecture, senior-frontend, senior-backend, senior-python, orchestrator</td><td>stable</td></tr>
    <tr><td><code>python</code></td><td>language</td><td>senior-python, senior-data-ml, orchestrator</td><td>stable</td></tr>
    <tr><td><code>rust</code></td><td>language</td><td>senior-rust, orchestrator</td><td>stable</td></tr>
    <tr><td><code>secure-coding</code></td><td>practice</td><td>senior-appsec, senior-pentest, all coding agents, orchestrator</td><td>stable</td></tr>
    <tr><td><code>security</code></td><td>practice</td><td>senior-appsec, senior-pentest, senior-cloud-native, orchestrator</td><td>stable</td></tr>
    <tr><td><code>systems</code></td><td>platform</td><td>senior-systems, orchestrator</td><td>stable</td></tr>
    <tr><td><code>testing</code></td><td>practice</td><td>senior-testing, all senior agents, orchestrator</td><td>stable</td></tr>
    <tr><td><code>typescript</code></td><td>language</td><td>senior-frontend-ts, senior-fullstack-ts, senior-node-backend, orchestrator</td><td>stable</td></tr>
    <tr><td><code>web</code></td><td>platform</td><td>senior-frontend, senior-fullstack, senior-python, senior-frontend-ts, senior-fullstack-ts, senior-node-backend, orchestrator</td><td>stable</td></tr>
  </tbody>
</table>

<h2>Validation</h2>

<ul>
  <li><code>name</code> equals the directory name and matches <code>^[a-z0-9]+(-[a-z0-9]+)*$</code>.</li>
  <li>Frontmatter includes <code>description</code>, <code>license</code>, and all port fields in <code>metadata</code>.</li>
  <li><code>SKILL.md</code> has a <code>## Port</code> section and an index table whose files all exist in <code>references/</code>.</li>
  <li>Every file in <code>references/</code> is referenced from the index.</li>
  <li>Relative links inside references resolve.</li>
</ul>

<h2>License</h2>

<p>MIT</p>
