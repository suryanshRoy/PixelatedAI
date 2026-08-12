import argparse
import time
from textual.app import App, ComposeResult
from textual.widgets import Button, Digits, Static, Input, LoadingIndicator, OptionList, Label
from textual.containers import HorizontalGroup, VerticalScroll, Container
import typer
from textual.binding import Binding
from rich.console import Console, ConsoleOptions, RenderResult

console = Console()

class PixelatedCLI(App):
    """A basic CLI for Pixelated AI"""

    CSS_PATH = "Pixelated.tcss"
    ENABLE_COMMAND_PALETTE = False

    # TODO need to add more bindings like ctrl d
    BINDINGS = [
        Binding("ctrl+c", "quit", "Exit Pixelated AI", priority=True)]

    def compose(self) -> ComposeResult:
        with VerticalScroll(id="cli-corners"): # for corner color of cli and all vertical contents
            for i in range(50):
                yield Static(f"Example {i+1} of scroll working")
            yield Static("Main content here in the box!")

        with HorizontalGroup(id="input-container"):
            yield Label("> ", id="prompt-label")
            yield Input(placeholder="Imagine like you have never before...", id="user-input")

        yield OptionList(
            "clear - Start a new session",
            "exit - Quit Pixelated AI",
            id="menuCmds",
            classes="hidden"
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