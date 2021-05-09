from controler.TournamentControler import *

db = TinyDB("tournament.json", ensure_ascii=False, encoding="utf8", indent=4)


if __name__ == "__main__":
    lancement = TournamentControler(db)

    a = lancement.new_tournament_created(db)
    lancement.run_rounds(lancement.run_first_round(lancement.init_players(a)))

    # lancement2 = TournamentControler(db)

    # b = lancement.new_tournament_created(db)
    # (lancement2.init_players(b))


# maîtriser les fonction db.truncate(), db.all(), db.search, db.insert() sur les tables
# régler le problème de la date
# seulement 3 joueurs dans les players, pourquoi ? --> seulement quand 2 tournois lancés

# rentrer chaque player dans une liste d'acteurs
# créer plusieurs tournois --> sorties de classe, même doc
# ménage sur le TournamentController

# si un tournoi écrase l'autre : est ce à cause de la mise à jour de tournament.table ?
# update plutôt qu'insert ?
