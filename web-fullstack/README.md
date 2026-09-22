<h1>Full-Stack Web Skills</h1>

<p>Project skills for full-stack web applications, grouped by product archetype. Each skill documents one real project end to end (design system, architecture, code structure, tooling) and is loaded on-demand via the <a href="https://opencode.ai/docs/skills">OpenCode <code>skill</code> tool</a>.</p>

<table>
  <thead>
    <tr>
      <th>Archetype</th>
      <th>Directory</th>
      <th>Skill</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Portfolio</td>
      <td><code>portfolio/</code></td>
      <td><code>xscriptor</code></td>
      <td>Editorial portfolio and blog: design intent, component system, content, styling, static export, SEO, i18n</td>
    </tr>
    <tr>
      <td>DevTools</td>
      <td><code>devtools/</code></td>
      <td><code>devx</code></td>
      <td>Developer-facing UI: visual system, tokens, typography, layout, motion, accessibility, platform mapping</td>
    </tr>
    <tr>
      <td>Platform</td>
      <td><code>platform/</code></td>
      <td><code>samurai</code></td>
      <td>Cybersecurity platform: design system, frontend/backend patterns, database schema, export system</td>
    </tr>
  </tbody>
</table>

<p>Sibling tiers in this repo: <code>content/</code> (content systems such as <code>linkedin</code>), <code>senior/</code> (reference packs).</p>

<h2>Installation</h2>

<pre><code># Clone this repo
git clone --depth 1 https://github.com/xscriptor-ai/skills.git
cd skills

# Web project skills (installed flat, so each directory equals the skill name)
cp -r web-fullstack/portfolio/xscriptor web-fullstack/devtools/devx web-fullstack/platform/samurai ~/.config/opencode/skills/

# Content skills
cp -r content/linkedin ~/.config/opencode/skills/

# Senior reference packs
cp -r senior/* ~/.config/opencode/skills/</code></pre>

<h2>Usage</h2>

<p>Skills are loaded automatically when the agent determines they are relevant. You can also invoke them directly:</p>

<pre><code>/xscriptor
/devx
/samurai
/linkedin</code></pre>

<h2>Structure</h2>

<pre><code>web-fullstack/
  portfolio/
    xscriptor/
      SKILL.md
      references/
  devtools/
    devx/
      SKILL.md
      README.md
      references/
  platform/
    samurai/
      SKILL.md
      references/</code></pre>

<h2>Deep Dive References</h2>

<p>For in-depth development of each skill with minimalist examples and extended documentation:</p>

<ul>
  <li><a href="https://dev.xscriptor.com/en/resources/ai/skills/devx/">dev.xscriptor.com/en/resources/ai/skills/devx/</a></li>
  <li><a href="https://dev.xscriptor.com/en/resources/ai/skills/xscriptor/">dev.xscriptor.com/en/resources/ai/skills/xscriptor/</a></li>
  <li><a href="https://dev.xscriptor.com/en/resources/ai/skills/samurai/">dev.xscriptor.com/en/resources/ai/skills/samurai/</a></li>
</ul>

<h2>Related Resources</h2>

<ul>
  <li><a href="https://opencode.ai/docs/skills">OpenCode Skills Documentation</a></li>
  <li><a href="https://github.com/xscriptor-ai/agents">Agents</a></li>
  <li><a href="https://github.com/xscriptor-ai/skills">github.com/xscriptor-ai/skills</a></li>
  <li><a href="https://dev.xscriptor.com/en/resources/ai/">dev.xscriptor.com/en/resources/ai/</a></li>
</ul>

<div id="x" align="center">
<h2>X</h2>

<a href="https://dev.xscriptor.com">
  <img src="https://xscriptor.github.io/icons/icons/code/product-design/xsvg/verified-filled.svg" width="24" alt="X Web" />
</a>
 & 
<a href="https://github.com/xscriptor">
  <img src="https://xscriptor.github.io/icons/icons/code/product-design/xsvg/github.svg" width="24" alt="X Github Profile" />
</a>
 & 
<a href="https://www.xscriptor.com">
  <img src="https://xscriptor.github.io/icons/icons/code/product-design/xsvg/quotes.svg" width="24" alt="Xscriptor web" />
</a>

</div>
