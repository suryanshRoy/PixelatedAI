import argparse
import time
from textual.app import App, ComposeResult
from textual.widgets import Button, Digits, Static, Input, LoadingIndicator, OptionList, Label
from textual.containers import HorizontalGroup, VerticalScroll, Container
import typer
from textual.binding import Binding, BindingType
from rich.console import Console, ConsoleOptions, RenderResult
from textual.suggester import SuggestFromList
from textual.widgets.option_list import Option
from textual import events
import random

console = Console()

class CustomInput(Input):
    def _on_key(self, event: events.Key) -> None:
        app = self.app
        menuCmds = app.query_one("#menuCmds", OptionList)
        
        if not menuCmds.has_class("hidden") and menuCmds.option_count > 0:
            if event.key in ("tab", "enter"):
                event.prevent_default()
                event.stop()
                
                highlightedCmds = menuCmds.highlighted
                if highlightedCmds is None:
                    highlightedCmds = 0
                
                selectedOpts = menuCmds.get_option_at_index(highlightedCmds)
                command = str(selectedOpts.prompt).split(" - ")[0]
                
                self.value = f"{command} "
                self.cursor_position = len(self.value)
                menuCmds.add_class("hidden")
                return

        super()._on_key(event) # Call the original _on_key method for other keys

class PixelatedCLI(App):
    """A basic CLI for Pixelated AI"""

    CSS_PATH = "Pixelated.tcss"
    ENABLE_COMMAND_PALETTE = False

    # TODO need to add more bindings
    BINDINGS: list[BindingType] = [
        Binding("ctrl+c", "quit", "Quit Pixelated AI", priority=True),
        Binding("ctrl+d", "quit", "Quit Pixelated AI", priority=True),
        Binding("down", "cursor_down", "Down", show=False),
        Binding("end", "last", "Last", show=False),
        Binding("enter", "select", "Select", show=False),
        Binding("home", "first", "First", show=False),
        Binding("pagedown", "page_down", "Page Down", show=False),
        Binding("pageup", "page_up", "Page Up", show=False),
        Binding("up", "cursor_up", "Up", show=False)
    ]

    AVAILABLE_COMMANDS = ["/quit", "/clear", "/models", "/mcp", "/resume"]
    COMMAND_DESCRIPTIONS = {
        "/clear": "/clear - Start a new session",
        "/quit": "/quit - Quit Pixelated AI",
        "/models": "/models - Choose a different model",
        "/mcp": "/mcp - Configure mcp server settings",
        "/resume": "/resume - Resume a past conversation"
    }

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="cli-corners"): # for corner color of cli and all vertical contents
            for i in range(50):
                yield Static(f"Example {i+1} of scroll working")
            yield Static("Main content here in the box!")

        with HorizontalGroup(id="input-container"):
            yield Label("> ", id="prompt-label")
            yield CustomInput(
                placeholder="Create a image of a lion...", 
                id="user-input", 
                suggester=SuggestFromList(self.AVAILABLE_COMMANDS, case_sensitive=False)
            )

        yield OptionList(
            *[Option(desc) for desc in self.COMMAND_DESCRIPTIONS.values()],
            id="menuCmds",
            classes="hidden",
            disabled=False
        )

    def on_input_changed(self, event: Input.Changed) -> None:
        menuCmds = self.query_one("#menuCmds", OptionList)
        menuCmds.clear_options() 

        if event.value.startswith("/"):
            searchedInp = event.value[1:].lower() # everything after /
            matches = [
                desc for cmd, desc in self.COMMAND_DESCRIPTIONS.items() 
                if searchedInp in cmd[1:].lower()
            ]
            sort_matches = sorted(
                matches, 
                key = lambda desc: not desc.split(" - ")[0][1:].lower().startswith(searchedInp)
            )
            finalOpts = [
                Option(desc) for desc in (sort_matches if searchedInp else self.COMMAND_DESCRIPTIONS.values())
            ]

            if finalOpts:
                menuCmds.add_options(finalOpts)
                menuCmds.remove_class("hidden")
            else:
                menuCmds.add_class("hidden")
        else:
            menuCmds.add_class("hidden")


    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        inpWidget = self.query_one("#user-input", Input)
        command = str(event.option.prompt).split(" - ")[0]
        inpWidget.value = f"{command} "
        inpWidget.focus()

        self.query_one("#menuCmds", OptionList).add_class("hidden")

if __name__ == "__main__":
    app = PixelatedCLI()
    app.run()