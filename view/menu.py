# créer un main menu dans une fonction lançable dans le main
# nouveau tournoi | reprendre un tournoi | voir les différents rapports | quitter

from controler.TournamentControler import *
import controler.GenerateReports as r

import tkinter

db = TinyDB("tournament.json", ensure_ascii=False, encoding="utf8", indent=4)
actors_db = TinyDB("actors.json", ensure_ascii=False, encoding="utf8", indent=4)


# création de la fenètre + paramétrage
# création d'une classe générale


# infos sur un tournoi : input "nom du tournoi" # sous menu : liste des players, des rounds, des matchs
# def report_matchs(db, tournament_name): def report_rounds(db, tournament_name): report_players(db, tournament_name):
# def report_players_alpha(all_data, tournament_name): def report_players_elo(all_data, tournament_name):

app = tkinter.Tk()
app.geometry("540x45")
app.title("Chess Tournaments")
# app.iconbitmap("logo.ico")
app.config(background="black")


lancement = TournamentControler()
# report = Report()


mainmenu = tkinter.Menu()
first_menu = tkinter.Menu(mainmenu, tearoff=0)
actors_menu = tkinter.Menu(first_menu)
tournament_menu = tkinter.Menu(first_menu)
tournament_name = "Tournoi des 7 nations"


def show_tournaments_list():
    list_tournaments = r.report_tournaments(db)
    about_window = tkinter.Toplevel(app)
    about_window.title("Liste des tournois")
    lb = tkinter.Label(about_window, text=(f"{list_tournaments}"))
    lb.pack()


def show_actors_alpha():
    list_actors_alpha = r.report_actors_alpha(r.actors_list(actors_db))
    about_window = tkinter.Toplevel(app)
    about_window.title("Liste des acteurs")
    lb = tkinter.Label(about_window, text=list_actors_alpha)
    lb.pack()


def show_actors_elo():
    list_actors_elo = r.report_actors_elo(r.actors_list(actors_db))
    about_window = tkinter.Toplevel(app)
    about_window.title("Liste des acteurs")
    lb = tkinter.Label(about_window, text=list_actors_elo)
    lb.pack()


def show_players():
    name = vt.get_tournament_name()
    list_players_alpha = r.report_players_alpha(r.report_players(db, name), name)
    list_players_elo = r.report_players_elo(r.report_players(db, name), name)
    about_window = tkinter.Toplevel(app)
    about_window.title("Players")
    lb = tkinter.Label(
        about_window,
        text=f"{list_players_alpha}\n\n\n{list_players_elo}",
    )
    lb.pack()


def show_rounds():
    name = vt.get_tournament_name()
    list_tournament_rounds = r.report_rounds(db, name)
    list_tournament_matchs = r.report_matchs(db, name)
    about_window = tkinter.Toplevel(app)
    about_window.title("Rounds and Matchs")
    lb = tkinter.Label(
        about_window, text=f"{list_tournament_rounds}\n\n\n{list_tournament_matchs}"
    )
    lb.pack()


def run_new_tournament():
    lancement.run_new_tournament(db, actors_db)


def resume_tournament():
    name = vt.get_tournament_name()
    lancement.run_ungoing_tournament(db, name, actors_db)


def run_menu():
    actors_menu.add_command(
        label="Alphabetical order", command=show_actors_alpha
    )  # command=show_actors_alpha())
    actors_menu.add_command(
        label="Elo ranking", command=show_actors_elo
    )  # command=show_actors_elo())

    tournament_menu.add_command(label="Players", command=show_players)
    tournament_menu.add_command(label="Rounds", command=show_rounds)

    first_menu.add_command(label="Tournaments list", command=show_tournaments_list)
    first_menu.add_cascade(label="Actors list", menu=actors_menu)
    first_menu.add_cascade(label="Check specific tournament", menu=tournament_menu)

    # show_players run_new_tournament = lancement.run_new_tournament(db, actors_db)

    mainmenu.add_cascade(label="Reports", menu=first_menu)
    mainmenu.add_command(label="Run a new tournament", command=run_new_tournament)
    mainmenu.add_command(label="Resume a tournament", command=resume_tournament)
    mainmenu.add_command(label="Quit", command=app.quit)

    app.config(menu=mainmenu)
    app.mainloop()


# add command pour les autres


# nouveau tournoi
# def run_new_tournament(self, db, actors_db)

# reprendre un tournoi
# proposer les tournois non finis ou entrer le nom du tournoi
# def run_ungoing_tournament(self, db, tournament_name, actors_db):

# voir les rapports
# sous menu
# liste des tournois : def report_tournaments(db):
# liste des acteurs : # sous menu : par ordre alphabétique, par élo

# quitter


# couleurs