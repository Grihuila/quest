"""
Thomas
Welcome to Quest
"""
from tools import quest
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
    "GO": lambda: print("VI V HATE! CONGRUTS!"),
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
    "1": lambda: print("Заходи в хату"),
    "2": lambda: print("Ты получаешь дубинкой по башке"),
    "else": lambda: print("Ти шо тупой?Я же сказал, что нужно писать то, что в скобках")
})
