# HIYA :3

# This is on hiatus while I deal with stage 1

from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget
from textual.events import Key


class MainHub(App):

    def on_key(self, event: Key) -> None:
        if event.key == "q":
            self.exit()

    def compose(self):
        yield MainPage()


class MainPage(Widget):

    def render(self) -> RenderResult:
        return "Hello, [b]World[/b]!"


if __name__ == "__main__":
    
    Main = MainHub()
    Main.run()

