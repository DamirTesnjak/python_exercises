def get_character_record(name, server, level, rank):
    player = {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}"
    }

    return player