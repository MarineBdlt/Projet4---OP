from controler.TournamentControler import *

db = TinyDB("tournament.json", ensure_ascii=False, encoding="utf8", indent=4)
actors_db = TinyDB("actors.json", ensure_ascii=False, encoding="utf8", indent=4)


if __name__ == "__main__":

    lancement = TournamentControler()
    # lancement.run_ungoing_tournament(db, "Tournamentencours", actors_db)

    lancement.run_ungoing_tournament(db, "Tournamentencours", actors_db)

    """
    tournament_name = "Tournamentencours"
    tournament_table = db.table(f"{tournament_name}")
    lancement.instanciation_tournament(tournament_table, tournament_name)
    lancement.instanciation_rounds()
    lancement.instanciation_matchs(0)
    """

    # lancement.instanciation_matchs(2)


# régler le problème de la date

# mettre les winners dans tournament
# rajouter current score + opponents | les supprimer dans actros.json

# algo et reinstanciation des tournois

# lancer le menu :
# créer un nouveau tournoi | reprendre un tournoi | voir les différents rapports | quitter

# reprendre un tournoi :
# tri : quels sont les tournois qui ne sont pas terminés ?
# boucle sur le json
# présentation des noms des tournois en cours
# créer un cheminement - récréer l'ensemble des instances à partir du .json - tournoi - players - rounds déjà fait

# créer deux fonctions :
# run new tournament
# run ungoing tournament
