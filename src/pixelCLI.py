import argparse
import time
from textual.app import App, ComposeResult
from textual.widgets import Button, Digits, Static, Input, LoadingIndicator, OptionList, Label
from textual.containers import HorizontalGroup, VerticalScroll, Container
import typer
from rich.console import Console, ConsoleOptions, RenderResult

console = Console()

class PixelatedCLI(App):
    """A basic CLI for Pixelated AI"""

    CSS_PATH = "Pixelated.tcss"

    BINDINGS = [
        ("ctrl+c", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        with VerticalScroll(id="cli-corners"): # for corner color of cli and all vertical contents
            for i in range(50):
                yield Static(f"Example {i+1} of scroll working")
            yield Static("Main content here in the box!")

        with HorizontalGroup(id="input-container"):
            yield Label("> ", id="prompt-label")
            yield Input(placeholder="Imagine like you have never before...", id="user-input")

if __name__ == "__main__":
    app = PixelatedCLI()
    app.run()