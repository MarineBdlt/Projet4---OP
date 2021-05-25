from controler.TournamentControler import *
import controler.GenerateReports as r
from view.menu import *

db = TinyDB("tournament.json", ensure_ascii=False, encoding="utf8", indent=4)
actors_db = TinyDB("actors.json", ensure_ascii=False, encoding="utf8", indent=4)


if __name__ == "__main__":

    # r.report_actors_elo(r.actors_list(actors_db))
    run_menu()

# régler le problème de la date - tournament (ne passe pas dans .json)
# round end-time (same) # str
# pep8 Flake html


# comment améliorer : - proposition des tournois en cours - reprendre la liste d'acteurs existants pour instancier les joueurs