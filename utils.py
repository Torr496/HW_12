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
    print(candidates)
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
