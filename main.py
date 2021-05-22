from controler.TournamentControler import *
import controler.GenerateReports as r
from view.menu import *

db = TinyDB("tournament.json", ensure_ascii=False, encoding="utf8", indent=4)
actors_db = TinyDB("actors.json", ensure_ascii=False, encoding="utf8", indent=4)


if __name__ == "__main__":

    run_menu()


# régler le problème de la date - tournament (ne passe pas dans .json)
# round end-time (same)

# resume tournament problème parfois in TournamentControler
# liste actors/players par elo rank in GenerateReports : ne trie pas avec int car str