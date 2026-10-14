"""
Script to automatically generate a Glassmorphic & Mirrormorphic developer insight SVG
and update README.md cleanly and silently.
Runs without third-party dependencies using standard library modules.
"""

from datetime import datetime, timezone, timedelta
import html
from pathlib import Path
import re
import textwrap

# Curated engineering & computer science principles
INSIGHTS = [
    {
        "quote": "Simplicity is prerequisite for reliability.",
        "author": "Edsger W. Dijkstra",
    },
    {
        "quote": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
        "author": "Martin Fowler",
    },
    {
        "quote": "First, solve the problem. Then, write the code.",
        "author": "John Johnson",
    },
    {
        "quote": "Make it work, make it right, make it fast.",
        "author": "Kent Beck",
    },
    {
        "quote": "Premature optimization is the root of all evil in programming.",
        "author": "Donald Knuth",
    },
    {
        "quote": "The function of good software is to make the complex appear to be simple.",
        "author": "Grady Booch",
    },
    {
        "quote": "Walking on water and developing software from a specification are easy if both are frozen.",
        "author": "Edward V. Berard",
    },
    {
        "quote": "Truth can only be found in one place: the code.",
        "author": "Robert C. Martin",
    },
    {
        "quote": "Programs must be written for people to read, and only incidentally for machines to execute.",
        "author": "Harold Abelson",
    },
    {
        "quote": "Talk is cheap. Show me the code.",
        "author": "Linus Torvalds",
    },
    {
        "quote": "Testing leads to failure, and failure leads to understanding.",
        "author": "Burt Rutan",
    },
    {
        "quote": "The only way to go fast, is to go well.",
        "author": "Robert C. Martin",
    },
    {
        "quote": "Before software can be reusable it first has to be usable.",
        "author": "Ralph Johnson",
    },
    {
        "quote": "Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away.",
        "author": "Antoine de Saint-Exupéry",
    },
    {
        "quote": "Good code is its own best documentation. Improve the code so comments aren't needed.",
        "author": "Steve McConnell",
    },
    {
        "quote": "It is not enough for code to work. It must be clean, maintainable, and resilient.",
        "author": "Clean Code Philosophy",
    },
]


def get_daily_insight():
    day_of_year = datetime.now(timezone.utc).timetuple().tm_yday
    return INSIGHTS[day_of_year % len(INSIGHTS)]


def generate_svg(insight, date_str, time_str):
    quote = html.escape(insight["quote"])
    author = html.escape(insight["author"])

    # Wrap text cleanly for SVG rendering
    lines = textwrap.wrap(quote, width=70)
    if len(lines) == 1:
        start_y = 100
        dy = 0
    elif len(lines) == 2:
        start_y = 88
        dy = 24
    else:
        start_y = 80
        dy = 22

    tspan_elements = []
    for i, line in enumerate(lines):
        line_dy = 0 if i == 0 else dy
        tspan_elements.append(f'<tspan x="82" dy="{line_dy}">{line}</tspan>')
    tspan_markup = "\n      ".join(tspan_elements)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="100%" height="100%" fill="none">
  <defs>
    <!-- Background Ambient Glowing Orbs for Glassmorphism -->
    <radialGradient id="orbBlue" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#58A6FF" stop-opacity="0.40"/>
      <stop offset="100%" stop-color="#58A6FF" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="orbPurple" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#bc8cff" stop-opacity="0.32"/>
      <stop offset="100%" stop-color="#bc8cff" stop-opacity="0"/>
    </radialGradient>

    <!-- Translucent Frosted Glass Surface Gradient -->
    <linearGradient id="glassSurface" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#161b22" stop-opacity="0.82"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0.94"/>
    </linearGradient>

    <!-- Glassmorphic Border with Specular Edge Sheen -->
    <linearGradient id="glassBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.50"/>
      <stop offset="25%" stop-color="#58A6FF" stop-opacity="0.35"/>
      <stop offset="70%" stop-color="#161b22" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.10"/>
    </linearGradient>

    <!-- Mirrormorphic Specular Glare (diagonal light streak across glass) -->
    <linearGradient id="specularGlare" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.14"/>
      <stop offset="28%" stop-color="#ffffff" stop-opacity="0.04"/>
      <stop offset="55%" stop-color="#ffffff" stop-opacity="0.0"/>
    </linearGradient>

    <!-- Mirrormorphic Floor Reflection Gradient Mask -->
    <linearGradient id="mirrorFade" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.35"/>
      <stop offset="45%" stop-color="#ffffff" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.0"/>
    </linearGradient>
    <mask id="mirrorMask">
      <rect x="25" y="196" width="800" height="54" fill="url(#mirrorFade)"/>
    </mask>
  </defs>

  <style>
    .mono {{ font-family: 'Fira Code', 'SF Mono', Consolas, Monaco, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }}
  </style>

  <!-- Ambient Light Orbs behind the frosted glass -->
  <circle cx="150" cy="70" r="140" fill="url(#orbBlue)"/>
  <circle cx="700" cy="130" r="130" fill="url(#orbPurple)"/>

  <!-- ================= MIRRORMORPHISM: FLOOR REFLECTION ================= -->
  <g mask="url(#mirrorMask)" opacity="0.45" transform="translate(0, 392) scale(1, -1)">
    <rect x="25" y="20" width="800" height="175" rx="16" fill="url(#glassSurface)" stroke="url(#glassBorder)" stroke-width="1.2"/>
    <line x1="25" y1="56" x2="825" y2="56" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>
  </g>

  <!-- ================= GLASSMORPHISM: MAIN FROSTED GLASS CARD ================= -->
  <g id="main-glass-card">
    <!-- Base Glass Surface -->
    <rect x="25" y="20" width="800" height="175" rx="16" fill="url(#glassSurface)" stroke="url(#glassBorder)" stroke-width="1.2"/>

    <!-- Mirrormorphic Specular Reflection Flare across glass top-left -->
    <path d="M 25 36 Q 25 20 41 20 L 460 20 L 300 195 L 25 195 Z" fill="url(#specularGlare)"/>

    <!-- Top Window Bar Divider -->
    <line x1="25" y1="56" x2="825" y2="56" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

    <!-- Terminal Window Controls (macOS style dots) -->
    <circle cx="50" cy="38" r="5" fill="#ff5f56" opacity="0.85"/>
    <circle cx="68" cy="38" r="5" fill="#ffbd2e" opacity="0.85"/>
    <circle cx="86" cy="38" r="5" fill="#27c93f" opacity="0.85"/>

    <!-- Window Title -->
    <text x="110" y="42" fill="#8b949e" font-size="12" class="mono">&gt; engineering-principles // core-philosophy</text>

    <!-- Quote Decorative Marks -->
    <text x="50" y="105" fill="#58a6ff" font-size="34" font-weight="800" opacity="0.6" class="sans">“</text>

    <!-- Dynamic Quote Lines -->
    <text x="82" y="{start_y}" fill="#e6edf3" font-size="15" font-weight="500" class="sans">
      {tspan_markup}
    </text>

    <!-- Author & Attribution -->
    <text x="82" y="148" fill="#58a6ff" font-size="13.5" font-weight="600" class="sans">— {author}</text>

    <!-- Clean Footer -->
    <text x="82" y="172" fill="#6e7681" font-size="10.5" class="mono">// Peter Njuguna · Software Engineering &amp; Systems Architecture</text>
  </g>
</svg>
"""
    return svg_content


def update_readme():
    root_dir = Path(__file__).resolve().parent.parent
    assets_dir = root_dir / "assets"
    assets_dir.mkdir(exist_ok=True)

    insight = get_daily_insight()
    eat_tz = timezone(timedelta(hours=3))
    now_eat = datetime.now(eat_tz)
    date_str = now_eat.strftime("%d %b %Y")
    time_str = now_eat.strftime("%H:%M EAT")

    # Generate and save the clean Glassmorphic SVG card
    svg_content = generate_svg(insight, date_str, time_str)
    svg_path = assets_dir / "daily-insight.svg"
    svg_path.write_text(svg_content, encoding="utf-8")
    print(f"Generated clean glassmorphic SVG card at: {svg_path}")

    # Embed card into README.md silently
    readme_path = root_dir / "README.md"
    content = readme_path.read_text(encoding="utf-8")

    new_block = f"""<!-- DAILY-INSIGHT:START -->
<div align="center">

<img src="assets/daily-insight.svg" alt="Engineering Principles - Peter Njuguna" width="850" />

</div>
<!-- DAILY-INSIGHT:END -->"""

    pattern = r"<!-- DAILY-INSIGHT:START -->[\s\S]*?<!-- DAILY-INSIGHT:END -->"

    if re.search(pattern, content):
        updated_content = re.sub(pattern, new_block, content)
    else:
        target = "## 02 — Technical Skills"
        if target in content:
            updated_content = content.replace(target, f"{new_block}\n\n<br>\n\n{target}")
        else:
            updated_content = content + f"\n\n{new_block}\n"

    readme_path.write_text(updated_content, encoding="utf-8")
    print("README.md successfully updated cleanly.")


if __name__ == "__main__":
    update_readme()
