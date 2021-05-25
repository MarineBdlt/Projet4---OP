from tinydb import where


def actors_list(actors_db):
    """ Fonction qui place prénom, nom et élo de chaque acteur dans une liste """
    actors_tables = actors_db.tables()
    list_names = []
    for name in actors_tables:
        list_names.append(name)
    all_data = []
    for actor_name in list_names:
        actor_table = actors_db.table(actor_name)
        actor_data = actor_table.search(where("Name") == actor_name)
        actor = []
        for key, value in actor_data[0].items():
            if key == "Surname" or key == "Name" or key == "ELO":
                actor.append(value)
            if actor not in all_data:
                all_data.append(actor)
    return all_data


def report_actors_alpha(all_data):
    """ Fonction qui print la liste des acteurs par ordre alphabétique """
    list_actors = []
    for data in all_data:
        actor = " ".join(data)
        list_actors.append(actor)
    sorted_list = sorted(list_actors)
    str_list = "\n\n".join(sorted_list)
    return f"List of actors by alphabetical order \n-----------------------\n{str_list}"


def report_actors_elo(all_data):
    """ Fonction qui print la liste des acteurs par rang de ELO """

    list_actors = []
    for data in all_data:
        print(data)
        data.reverse()
        data[0] = int(data[0])
        list_actors.append(data)
        print(data)
    sorted_list = sorted(list_actors, key=lambda x: x[0])
    print(sorted_list)

    str_list = []
    for element in sorted_list:
        e = f"{element[0]} {element[1]} {element[2]}\n"
        str_list.append(e)
    return " ".join(str_list)


def report_tournaments(db):
    """ Fonction qui print la liste de tous les tournois """
    tournaments_tables = db.tables()
    list_names = []
    for name in tournaments_tables:
        list_names.append(name)

    all_data = []
    for t_name in list_names:
        t_table = db.table(t_name)
        t_data = t_table.search(where("Name") == t_name)
        tournament = []
        for key, value in t_data[0].items():
            if key == "Name" or key == "Date" or key == "Type":
                tournament.append(value)
            if tournament not in all_data:
                all_data.append(tournament)

    list_tournaments = []
    for data in all_data:
        tournament = " ".join(data)
        list_tournaments.append(tournament)
    str_list = "\n\n".join(list_tournaments)
    return f"List of tournaments :\n---------------------\n{str_list}"


def report_players(db, tournament_name):
    """ Fonction qui place nom, prénom et élo des players d'un tournoi dans une liste """
    tournament_table = db.table(f"{tournament_name}")
    serialized_tournament = tournament_table.search(where("Name") == tournament_name)
    players = []
    for info in serialized_tournament:
        players.append(info["Players"])

    serialized_players = players[0]
    all_data = []
    for s_player in serialized_players:
        one_player = []
        for key, value in s_player.items():
            if key == "Name" or key == "Surname" or key == "ELO":
                one_player.append(value)
            if one_player not in all_data:
                all_data.append(one_player)
    return all_data


def report_players_alpha(all_data, tournament_name):
    """ Fonction qui print les players d'un tournoi par odre alphabétique """
    list_players = []
    for data in all_data:
        str_player = " ".join(data)
        list_players.append(str_player)
    sorted_list = sorted(list_players)
    str_list = "\n\n".join(sorted_list)
    return (
        f"List of players in alphabetical order :\n-----------------------\n{str_list}"
    )


def report_players_elo(all_data, tournament_name):
    """ Fonction qui print les players d'un tournoi par rang de ELO """
    list_players = []
    for data in all_data:
        data.reverse()
        player = " ".join(data)
        list_players.append(player)
    sorted_list = sorted(list_players)
    str_list = "\n\n".join(sorted_list)
    return f"List of all players in elo range :\n-------------------\n{str_list}"


def report_rounds(db, tournament_name):
    """ Fonction qui print tous les rounds d'un tournoi """
    tournament_table = db.table(f"{tournament_name}")
    serialized_tournament = tournament_table.search(where("Name") == tournament_name)
    rounds = []
    for info in serialized_tournament:
        rounds.append(info["Rounds"])

    serialized_rounds = rounds[0]
    all_data = []
    for s_round in serialized_rounds:
        one_round = []
        for key, value in s_round.items():
            if key == "Name" or key == "Round start-time":
                one_round.append(value)
            if one_round not in all_data:
                all_data.append(one_round)

    list_rounds = []
    for data in all_data:
        str_round = " ".join(data)
        list_rounds.append(str_round)
    str_list = "\n\n".join(list_rounds)
    return f"Rounds of {tournament_name} :\n----------------\n{str_list}"


def report_matchs(db, tournament_name):
    """Fonction qui instancie les matchs du tournoi à partir du .json """
    tournament_table = db.table(f"{tournament_name}")
    serialized_tournament = tournament_table.search(where("Name") == tournament_name)
    rounds = []
    for info in serialized_tournament:
        rounds.append(info["Rounds"])

    serialized_rounds = rounds[0]
    all_data = []
    for s_round in serialized_rounds:
        matchs = ""
        for key, value in s_round.items():
            if key == "Round Matchs":
                matchs = value
            if matchs not in all_data:
                all_data.append(matchs)

    list_matchs = []
    for data in all_data:
        for match in data:
            i = 0
            one_match = []
            while i < 4:
                for key, value in match.items():
                    if str(value) not in one_match:
                        one_match.append(str(value))
                i += 1
            if "0.5" in one_match:
                one_match.append("0.5")
            if one_match not in list_matchs:
                list_matchs.append(" | ".join(one_match))
    str_data = "\n\n".join(list_matchs)
    return f"Matchs of {tournament_name} :\n---------------------\n{str_data}"
