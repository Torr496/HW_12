import json


def get_candidates():
    with open("data/candidates.json", "r") as fp:
        """
        Функция получает из файла список кандидатов
        """

        candidates = json.load(fp)
        return candidates


def get_candidates_by_id(can_id):
    candidates = get_candidates()

    for can in candidates:
        if can_id == can["id"]:
            return can


def get_settings():
    with open("data/settings.json", "r") as fp:
        """
        Функция словарь с настройками
        """

        settings = json.load(fp)
        return settings


def get_candidates_by_name(name):
    candidates_found = []

    candidates = get_candidates()
    settings = get_settings()

    for can in candidates:
        if settings["case-sensitive"]:
            if name in can["name"]:
                candidates_found.append(can)
        else:
            if name.lower in can["name"].lower:
                candidates_found.append(can)

    return candidates_found
