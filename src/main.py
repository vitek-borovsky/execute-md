from textual.app import App, ComposeResult
from textual.widgets import Button, Footer, Header, Static
import subprocess

def run_cmd(cmd) -> str:
    return subprocess.run(cmd.split(" "), capture_output=True, text=True).stdout

class MainScreen(Static):
    def compose(self) -> ComposeResult:
        yield Button("Run")
        yield Static(run_cmd("ls"))


class StopwatchApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode")
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield MainScreen()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
