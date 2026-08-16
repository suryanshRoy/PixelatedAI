import time
from textual.app import App, ComposeResult
from textual.widgets import Button, Digits, Static, Input, LoadingIndicator, OptionList, Label, Placeholder, Footer
from textual.containers import HorizontalGroup, VerticalScroll, Container, Horizontal
import typer
from textual.screen import Screen
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
            elif event.key == "down":
                event.prevent_default()
                event.stop()
                menuCmds.action_cursor_down()
                return

            elif event.key == "up":
                event.prevent_default()
                event.stop()
                menuCmds.action_cursor_up()
                return

        super()._on_key(event) # Call the original _on_key method for other keys

class PixelatedCLI(App):
    """A basic CLI for Pixelated AI"""

    CSS_PATH = "Pixelated.tcss"
    ENABLE_COMMAND_PALETTE = False
    current_use_mode = "Manual" #TODO need to change this

    # TODO need to add more bindings
    BINDINGS: list[BindingType] = [
        Binding("shift+tab", "current_mode", f"-> {current_use_mode} Mode", show=True, priority=True),
        Binding("question_mark", "show_help", "-> help", priority=True, show=True, key_display="?"),
        Binding("ctrl+c", "quit", "-> Quit", priority=True, show=True),
        Binding("ctrl+d", "quit", "Quit Pixelated AI", show=False),
        Binding("down", "cursor_down", "Down", show=False),
        Binding("end", "last", "Last", show=False),
        Binding("enter", "select", "Select", show=False),
        Binding("home", "first", "First", show=False),
        Binding("pagedown", "page_down", "Page Down", show=False),
        Binding("pageup", "page_up", "Page Up", show=False),
        Binding("up", "cursor_up", "Up", show=False)
    ]

    AVAILABLE_COMMANDS = ["/clear", "/quit", "/models", "/mcp", "/resume", "/keybindings"]
    COMMAND_DESCRIPTIONS = {
        "/clear": "/clear - Start a new session",
        "/quit": "/quit - Quit Pixelated AI",
        "/models": "/models - Choose a different model",
        "/mcp": "/mcp - Configure mcp server settings",
        "/resume": "/resume - Resume past conversation",
        "/keybinding": "/keybinding - Customise keybindings"
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

        with HorizontalGroup(id="FooterBtn-cont"):
            yield Button(label=f"{self.current_use_mode} Mode", variant="primary")
            yield Button(label="Quit", variant="primary")

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
                menuCmds.highlighted = 0
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

    def on_input_submitted(self, event: Input.Submitted) -> None:
        submittedText = event.value.strip().lower()

        if submittedText in ("/quit", "/exit"):
            self.exit()
        event.input.value = ""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button))

if __name__ == "__main__":
    app = PixelatedCLI()
    app.run()