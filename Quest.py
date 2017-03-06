"""
Thomas
Welcome to Quest
"""
from tools import *
user = {
    "name": "",
    "xp": 40,
    "attack": 10,
    "defence": 5
}
enemy = {
    "name": "зэк",
    "xp": 10,
    "attack": 10,
    "defence": 5
}

quest("Go ili zassal?", {
    "GO": [lambda: print("VI V HATE! CONGRUTS!")],
    "else": lambda: exit(0)
})
print("Вечер в хату! Как звать тебя?\nВведите ваше имя>>")
user["name"] = input()
print("Ну здарова,"+user["name"])
print("Твоя задача выжить в хате!")
"""
for_input -> переменная для хранения большего текста для вывода
используйте ее, если надо вывести большой текст
"""
for_input = """
(1) Ясно, я все понял
(2) Пошел ты!
(Вы должны указать цифру или символ, который находиться в скобках)
"""
quest(for_input, {
    "1": [lambda: print("Заходи в хату")],
    "2": [lambda: print("Ты получаешь дубинкой по башке"),
          lambda: change_chartics(user, {"xp": lambda this: this-5})
          ],
    "else": lambda: print("Ти шо тупой?Я же сказал, что нужно писать то, что в скобках")
})
for_input = """"В хате, как известно, всем нужно прописаться. Тебе указывают на койку и говорят, что она твоя. Твои действия?")
(1) Пойти обустраиваться
(2) Стоять, как истукан"""
quest(for_input, {
    "1": [lambda: print("Тебе нужно было стоять и ждать, куда укажет тебе смотрящий в хате. Ты получаешь -15 к жизням, но за дерзость +5 к атаке"),
          lambda: change_chartics(user,{"xp": lambda this: this-5, "attack": lambda this: this+3})
         ],
    "2": [lambda: print("Ты сделал правильно! Смотрящий через пару секунд указал тебе на место, где обустраиваться. Ты получаешь +5 к атаке и +10 к жизни"),
          lambda: change_chartics(user, {"xp": lambda this: this+10, "attack": lambda this: this+5})
         ],
    "else": [lambda: print("Ти шо тупой?Я же сказал, что нужно писать то, что в скобках")]
})
