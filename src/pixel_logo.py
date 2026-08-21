from textual.widgets import Static
from rich.text import Text
from rich.panel import Panel

UNHUMAN = """
         ░░░░░░░░   
        ▒▒▒▒▒▒▒▒▒▒  
        ▆▆▆▆▆▆▆▆▆▆  
        ▌  ◝   ◜  ▌ 
       ╭▌  ⊙   ⊙  ▌╮
       ╰▌    !    ▌╯
        ▌  ╰===╯  ▌ 
        ▌         ▌ 
      █▀▀▀▀▀▀▀▀▀▀▀▀▀█
ミ▄▄▄▄█             █▄▄▄▄彡
      █             █
      █             █
      █             █
      █             █
      █             █
      █▀▀▀▀▀▀▀▀▀▀▀▀▀█
      █             █
      █             █
      █      |      █
      █      |      █
      █      |      █
      █      |      █
      █      |      █
      █      |      █
      █      |      █
      █     ▟ ▙     █
      █▄▄▄▄▄█ █▄▄▄▄▄█
"""

class Logo(Static):
    def render(self):
        logo_text = Text(UNHUMAN, justify="left")
        logo_text.stylize("bold dim red")
        
        return Panel(
            logo_text,
            title="[bold red]Pixelated AI[/]",
            border_style="cyan",
            expand=False,
            padding=(0, 2)
        )