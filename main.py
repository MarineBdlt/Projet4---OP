from controler.TournamentControler import *

db = TinyDB("tournament.json", ensure_ascii=False, encoding="utf8", indent=4)
actors_db = TinyDB("actors.json", ensure_ascii=False, encoding="utf8", indent=4)


if __name__ == "__main__":

    lancement5 = TournamentControler()

    tournament_table = lancement5.new_tournament_created(db)

    lancement5.init_players(tournament_table, actors_db)
    lancement5.run_first_round(tournament_table, actors_db)
    lancement5.run_rounds(tournament_table, actors_db)


# régler le problème de la date

# rentrer chaque player dans une liste d'acteurs
# créer plusieurs tournois --> sorties de classe, même doc
# ménage sur le TournamentController

# si un tournoi écrase l'autre : est ce à cause de la mise à jour de tournament.table