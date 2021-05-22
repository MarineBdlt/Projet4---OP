from controler.TournamentControler import *
import controler.GenerateReports as r
import tkinter

db = TinyDB("tournament.json", ensure_ascii=False, encoding="utf8", indent=4)
actors_db = TinyDB("actors.json", ensure_ascii=False, encoding="utf8", indent=4)
app = tkinter.Tk()


class Report:
    def __init__(self):
        self.tournament_name = "Tournoi des 7 nations"

    def show_players(self):
        list_players_alpha = r.report_players_alpha(
            r.report_players(db, self.tournament_name), self.tournament_name
        )
        list_players_elo = r.report_players_elo(
            r.report_players(db, self.tournament_name), self.tournament_name
        )
        about_window = tkinter.Toplevel(app)
        about_window.title("Infos du tournoi")
        lb = tkinter.Label(
            about_window,
            text=f"{list_players_alpha}\n\n\n{list_players_elo}",
        )
        lb.pack()

    def show_rounds(self):
        list_tournament_rounds = r.report_rounds(db, self.tournament_name)
        list_tournament_matchs = r.report_matchs(db, self.tournament_name)
        about_window = tkinter.Toplevel(app)
        about_window.title("Infos du tournoi")
        lb = tkinter.Label(
            about_window, text=f"{list_tournament_rounds}\n\n\n{list_tournament_matchs}"
        )
        lb.pack()

    def show_tournaments_list(self):
        list_tournaments = r.report_tournaments(db)
        about_window = tkinter.Toplevel(app)
        about_window.title("Liste des tournois")
        lb = tkinter.Label(about_window, text=(f"{list_tournaments}"))
        lb.pack()

    def show_actors_alpha(self):
        list_actors_alpha = r.report_actors_alpha(r.actors_list(actors_db))
        about_window = tkinter.Toplevel(app)
        about_window.title("Liste des acteurs")
        lb = tkinter.Label(about_window, text=list_actors_alpha)
        lb.pack()

    def show_actors_elo(self):
        list_actors_elo = r.report_actors_elo(r.actors_list(actors_db))
        about_window = tkinter.Toplevel(app)
        about_window.title("Liste des acteurs")
        lb = tkinter.Label(about_window, text=list_actors_elo)
        lb.pack()