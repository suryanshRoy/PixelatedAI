import typer
from typing import Annotated

app = typer.Typer(name="Pixelated AI",add_completion=False)

@app.command()
def cli_opts(
    prompt: Annotated[str, typer.Option(help="Prompt for your AI: ")] ="",
    model: Annotated[str, typer.Option(help="Enter the model you want to use: ")] = "",
    mode: Annotated[str, typer.Option(show_default="Auto", help=f"Select AI mode:\n    Plan: Enter the planning mode before designing anything\n    Auto: Enter the automatic mode to automatic design, research and provide an design")] = "",
    resume: Annotated[str, typer.Option(help="Show past sessions.")] = "",
    mcp: Annotated[str, typer.Option(help="Show and configure all available mcp supports.", show_default="None")] = "",
    keybindings: Annotated[str, typer.Option(help="Show and configure all the default key bindings.")] = "",
    path: Annotated[str, typer.Option(help="Enter the path where you want all your files(images) to be saved: ")]= ""
): 
    if mode.lower() == "auto":
        return "auto"
    elif mode.lower() == "plan":
        return "plan"
    
if __name__ == "__main__":
    app()