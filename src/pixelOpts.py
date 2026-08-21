import typer
from typing import Annotated
from pixelCLI import PixelatedCLI

app = typer.Typer(name="Pixelated AI",add_completion=False, rich_markup_mode="markdown")

@app.command()
def cli_opts(
    prompt: Annotated[str, typer.Option(help="Prompt for your AI: ")] ="",
    model: Annotated[str, typer.Option(help="Enter the model you want to use: ")] = "",
    mode: Annotated[str, typer.Option(show_default="Auto", help=f"Select AI mode:\n    Plan: Enter the planning mode before designing anything\n    Auto: Enter the automatic mode to automatic design, research and provide an design")] = "",
    resume: Annotated[str, typer.Option(help="Show past sessions.")] = "",
    mcp: Annotated[str, typer.Option(help="Show and configure all available mcp supports.", show_default="None")] = "",
    keybindings: Annotated[str, typer.Option(help="Show and configure all the default key bindings.")] = "",
    path: Annotated[str, typer.Option(help="Enter the path where you want all your files(images) to be saved: ", show_default="Current directory")]= ""
): 
    selected_mode = "auto"
    if mode.lower() == "auto":
        selected_mode = "auto"
    elif mode.lower() == "plan":
        selected_mode = "plan"

    sendTUI = PixelatedCLI(initial_mode=selected_mode)
    sendTUI.run()
    
if __name__ == "__main__":
    app()