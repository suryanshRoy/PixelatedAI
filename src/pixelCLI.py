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
import random

console = Console()

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

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="cli-corners"): # for corner color of cli and all vertical contents
            for i in range(50):
                yield Static(f"Example {i+1} of scroll working")
            yield Static("Main content here in the box!")

        with HorizontalGroup(id="input-container"):
            yield Label("> ", id="prompt-label")
            yield Input(
                placeholder="Create a image of a lion...", 
                id="user-input", 
                suggester=SuggestFromList(self.AVAILABLE_COMMANDS, case_sensitive=False)
            )

        yield OptionList(
            "clear - Start a new session",
            "quit - Quit Pixelated AI",
            "models - Choose a different model",
            "mcp - Configure mcp server settings",
            "resume - Resume a past conversations",
            id="menuCmds",
            classes="hidden",
            disabled=False
        )

    def on_input_changed(self, event: Input.Changed) -> None:
        menuCmds = self.query_one("#menuCmds", OptionList)

        if event.value.startswith("/"):
            menuCmds.remove_class("hidden")
        else:
            menuCmds.add_class("hidden")

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        inpWidget = self.query_one("#user-input", Input)
        command = str(event.option.prompt).split(" - ")[0]
        inpWidget.value = f"/{command} "
        inpWidget.focus()

        self.query_one("#menuCmds", OptionList).add_class("hidden")

if __name__ == "__main__":
    app = PixelatedCLI()
    app.run()