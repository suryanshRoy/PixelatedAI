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
      █▄▄▄▄▄█ █▄▄▄▄▄▟
"""

class Logo(Static):
    def render(self):
        logo_text = Text(UNHUMAN, justify="left")
        logo_text.stylize("bold #D4FF33")
        
        return Panel(
            logo_text,
            title="[bold #48C9B0]Pixelated AI[/]",
            border_style="#15EDC2",
            expand=False,
            padding=(0, 2)
        )