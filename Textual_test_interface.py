from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Container
from textual import events


class MohammedAutomationApp(App):
    """A Textual app for Mohammed's Automation interface."""

    CSS = """
        Screen {
            layout: vertical;
        }
        
        #header {
            dock: top;
            height: 3;
            content-align: center middle;
            background: $accent;
        }
        
        #body {
            width: 100%;
            height: 100%;
            padding: 1;
        }
        
        #footer {
            dock: bottom;
            height: 1;
            background: $panel;
        }
        """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark", "Toggle dark mode"),
        ("s", "show_sales", "Show Sales"),
        ("t", "show_tasks", "Show Tasks"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(id="header")
        self.body_container = Container(Static("Welcome to Mohammed's Automation App", id="welcome-message"), id="body")
        yield self.body_container
        yield Footer(id="footer")

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_show_sales(self) -> None:
        self.body_container.clear()
        self.body_container.mount(Static("Sales Dashboard Content"))

    def action_show_tasks(self) -> None:
        self.body_container.clear()
        self.body_container.mount(Static("Tasks Dashboard Content"))

if __name__ == "__main__":
    app = MohammedAutomationApp()
    app.run()