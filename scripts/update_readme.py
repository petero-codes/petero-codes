"""
Script to automatically update the 'daily-insight' section of README.md.
Runs without third-party dependencies using standard library modules.
"""

from datetime import datetime, timezone, timedelta
import random
import re
from pathlib import Path

# Professional software engineering & computer science quotes/insights
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
        "quote": "Good code is its own best documentation. As you're about to add a comment, ask yourself: 'How can I improve the code so that this comment isn't needed?'",
        "author": "Steve McConnell",
    },
    {
        "quote": "It is not enough for code to work. It must be clean, maintainable, and resilient.",
        "author": "Clean Code Philosophy",
    },
]


def get_daily_insight():
    # Use day of the year to cycle through insights deterministically, or pick pseudo-randomly
    day_of_year = datetime.now(timezone.utc).timetuple().tm_yday
    return INSIGHTS[day_of_year % len(INSIGHTS)]


def generate_block():
    insight = get_daily_insight()
    # Nairobi is UTC+3
    eat_tz = timezone(timedelta(hours=3))
    now_eat = datetime.now(eat_tz)
    date_str = now_eat.strftime("%d %b %Y")
    time_str = now_eat.strftime("%H:%M EAT")

    content = f"""<!-- DAILY-INSIGHT:START -->
## `> daily-insight`

> *"{insight['quote']}"*
>
> — **{insight['author']}**
>
> <sub>*⚡ Auto-synced daily via GitHub Actions • {date_str} • Nairobi (UTC+03:00)*</sub>
<!-- DAILY-INSIGHT:END -->"""
    return content


def update_readme():
    readme_path = Path(__file__).resolve().parent.parent / "README.md"
    content = readme_path.read_text(encoding="utf-8")

    new_block = generate_block()
    pattern = r"<!-- DAILY-INSIGHT:START -->[\s\S]*?<!-- DAILY-INSIGHT:END -->"

    if re.search(pattern, content):
        updated_content = re.sub(pattern, new_block, content)
    else:
        # If marker doesn't exist yet, insert right before '## `> current-focus.yaml`' or after 'whoami'
        target = "## `> current-focus.yaml`"
        if target in content:
            updated_content = content.replace(target, f"{new_block}\n\n<br>\n\n{target}")
        else:
            updated_content = content + f"\n\n{new_block}\n"

    readme_path.write_text(updated_content, encoding="utf-8")
    print("README.md successfully updated with daily insight.")


if __name__ == "__main__":
    update_readme()
