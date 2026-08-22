from textual.widgets import Static
from rich.text import Text
from rich.color import Color
from rich.panel import Panel
import random

UNHUMAN = """
         ░░░░░░░░   
        ▒▒▒▒▒▒▒▒▒▒  
        ▌  ◝   ◜  ▌ 
       ╭▌  ⊙   ⊙  ▌╮
       ╰▌    !    ▌╯
        ▌  ╰===╯  ▌ 
      █▀▀▀▀▀▀▀▀▀▀▀▀▀█
ミ▄▄▄▄█             █▄▄▄▄彡
      █             █
      █             █
      █▀▀▀▀▀▀▀▀▀▀▀▀▀█
      █             █
      █             █
      █      |      █
      █      |      █
      █     ▟ ▙     █
      █▄▄▄▄▄█ █▄▄▄▄▄█
"""

rich_color = Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Logo(Static):
    def render(self):
        logo_text = Text(UNHUMAN, justify="left")
        logo_text.stylize(style=rich_color.name)
        
        return Panel(
            logo_text,
            title=f"[bold color({random.randint(1, 9)})]Pixelated AI[/]",
            border_style=f"bold color({random.randint(1, 5)})",
            expand=False,
            padding=(0, 2)
        )