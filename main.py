from view.menu import run_menu
from tinydb import TinyDB

db = TinyDB("tournament.json", ensure_ascii=False, encoding="utf8", indent=4)
actors_db = TinyDB("actors.json", ensure_ascii=False, encoding="utf8", indent=4)


if __name__ == "__main__":

    run_menu()
