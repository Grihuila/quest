"""
Thomas module
Constructor quests
"""
from tools import change_chartics
from Objects import *
all_quests = [{
        "title": "Войти в хату",
        "for_input": """Охранник открывает дверь и говорит вам, чтоб вы берегли очко
                     (1) Ясно, я все понял
                     (2) Пошел ты!\n(Вы должны указать цифру или символ, который находиться в скобках)""",
        "1": [lambda: print("[Охранник]: Заходи в хату")],
        "2": [lambda: print("Ты получаешь дубинкой по башке и теряешь 5xp"),
              lambda: change_chartics(user, {"xp": lambda this: this-5})], }]
