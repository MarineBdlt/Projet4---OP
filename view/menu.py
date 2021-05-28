from controler.TournamentControler import TournamentControler
import controler.GenerateReports as r
import view.tournament as vt
import view.player as vp
from tinydb import TinyDB

import tkinter

db = TinyDB("tournament.json", ensure_ascii=False, encoding="utf8", indent=4)
actors_db = TinyDB("actors.json", ensure_ascii=False, encoding="utf8", indent=4)

app = tkinter.Tk()
app.geometry("690x200")
app.title("Chess Tournaments")
app.config(background="black")

# app.iconbitmap("chesslogo.ico")


lancement = TournamentControler()

mainmenu = tkinter.Menu()
first_menu = tkinter.Menu(mainmenu, tearoff=0)
actors_menu = tkinter.Menu(first_menu)
tournament_menu = tkinter.Menu(first_menu)
tournament_name = "Tournoi des 7 nations"


def show_tournaments_list():
    list_tournaments = r.report_tournaments(db)
    about_window = tkinter.Toplevel(app)
    about_window.title("Liste des tournois")

    lb = tkinter.Label(
        about_window, text=(f"{list_tournaments}"), fg="white", font="Monserrat"
    )
    lb.config(background="black")
    lb.pack()


def show_actors_alpha():
    list_actors_alpha = r.report_actors_alpha(r.actors_list(actors_db))
    about_window = tkinter.Toplevel(app)
    about_window.title("Liste des acteurs")

    lb = tkinter.Label(
        about_window, text=list_actors_alpha, fg="white", font="Monserrat"
    )
    lb.config(background="black")
    lb.pack()


def show_actors_elo():
    list_actors_elo = r.report_actors_elo(r.actors_list(actors_db))
    about_window = tkinter.Toplevel(app)
    about_window.title("Liste des acteurs")

    lb = tkinter.Label(
        about_window,
        text=list_actors_elo,
        fg="white",
        font="Monserrat",
    )
    lb.config(background="black")
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
        fg="white",
        font="Monserrat",
    )
    lb.config(background="black")
    lb.pack()


def show_rounds():
    name = vt.get_tournament_name()
    list_tournament_rounds = r.report_rounds(db, name)
    list_tournament_matchs = r.report_matchs(db, name)
    about_window = tkinter.Toplevel(app)
    about_window.title("Rounds and Matchs")

    lb = tkinter.Label(
        about_window,
        text=f"{list_tournament_rounds}\n\n\n{list_tournament_matchs}",
        fg="white",
        font="Monserrat",
    )
    lb.config(background="black")
    lb.pack()


def run_new_tournament():
    lancement.run_new_tournament(db, actors_db)


def resume_tournament():
    name = vt.get_tournament_name()
    lancement.run_ungoing_tournament(db, name, actors_db)


def change_elo():
    vp.change_elo_actor(actors_db)


def run_menu():
    actors_menu.add_command(
        label="Alphabetical order", font="Monserrat", command=show_actors_alpha
    )
    actors_menu.add_command(
        label="ELO ranking", font="Monserrat", command=show_actors_elo
    )
    actors_menu.add_command(label="Change ELO", font="Monserrat", command=change_elo)
    actors_menu.config(background="black")
    actors_menu.config(fg="white")

    tournament_menu.add_command(label="Players", font="Monserrat", command=show_players)
    tournament_menu.add_command(label="Rounds", font="Monserrat", command=show_rounds)
    tournament_menu.config(background="black")
    tournament_menu.config(fg="white")

    first_menu.add_command(
        label="Tournaments list", font="Monserrat", command=show_tournaments_list
    )
    first_menu.add_cascade(label="Actors list", font="Monserrat", menu=actors_menu)
    first_menu.add_cascade(
        label="Check specific tournament", font="Monserrat", menu=tournament_menu
    )
    first_menu.config(background="black")
    first_menu.config(fg="white")

    mainmenu.add_cascade(label="Reports", font="Monserrat", menu=first_menu)
    mainmenu.add_command(
        label="Run a new tournament", font="Monserrat", command=run_new_tournament
    )
    mainmenu.add_command(
        label="Resume a tournament", font="Monserrat", command=resume_tournament
    )
    mainmenu.add_command(label="Quit", font="Monserrat", command=app.quit)
    mainmenu.config(background="black")
    mainmenu.config(fg="white", relief="groove")

    app.config(menu=mainmenu)
    app.mainloop()
