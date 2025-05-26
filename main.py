# HIYA :3

from textual.app import App
from textual.events import Key

class MainHub(App):
    def on_key(self, event: Key) -> None:
        if event.key == "q":
            self.exit()

if __name__ == "__main__":
    
    Main = MainHub()
    Main.run()

