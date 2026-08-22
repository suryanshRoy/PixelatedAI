from textual.widgets import Static
from rich.text import Text
from rich.color import Color
from rich.panel import Panel
from rich.table import Table
import random
import os

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

rich_color = Color.from_rgb(random.randint(80, 255), random.randint(80, 255), random.randint(80, 255))

class Logo(Static):
    def __init__(self, model: str = "None", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    def render(self):
        logo_text = Text(UNHUMAN, justify="left", no_wrap=True)
        logo_text.stylize(style=rich_color.name)
        
        is_small_screen = 0 < self.size.width < 75

        statusTxt = Text()
        if not is_small_screen:
            statusTxt.append("\n\n") #match the upper head starting
        statusTxt.append("Model: ", style="bold red")
        statusTxt.append(f"{self.model}\n", style="dim white")
        statusTxt.append("Directory: ", style="bold red")
        statusTxt.append(f"{os.getcwd()}\n", style="dim white")
        
        grid = Table.grid(padding=(0, 2))
        if is_small_screen:
            grid.add_column()
            grid.add_row(logo_text)
            grid.add_row(statusTxt)
        else:
            grid.add_column(no_wrap=True) # for logo
            grid.add_column() # for status text of models and directory
            grid.add_row(logo_text, statusTxt)

        return Panel(
            grid,
            title=f"[bold color({random.randint(1, 9)})]Pixelated AI[/]",
            border_style=f"bold color({random.randint(1, 5)})",
            expand=True,
            padding=(0, 2)
        )