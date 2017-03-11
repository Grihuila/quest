"""
Thomas tools module
"""

"""
Функция для генерации квестов:
@question -> вопрос, который мы собираемся задавать
@option -> варианты ответа, этот параметр является словарем
В @option храняться ключи, значение которых являются массивом lambda-функции,
которые будут исполняться при выборе одного из ответов
"""
def run_quest(option):
    print(option["for_input"])
    response = input("[ Ваш ход ] >>> ")
    for res in option.keys():
        if res.upper() == response.upper():
            for fn in option[res]:
                fn()
            break
    else:
        if option.get("else") is None:
            print("Ти шо тупой?Я же сказал, что нужно писать то, что в скобках")
        else:
            for fn in option["else"]:
                fn()

"""
Эта функция меняет характеристики обьектов
Первым параметром мы передаем обьект, который будем изменять
Вторым параметром передаем те характеристики, которые нужно изменить
Второй параметр представляет собой словарь, ключами которого являются характеристики
А значением ключей является lambda функция, которая обязательным параметром получает this
This - это ссылка на ту характеристику, которую мы будем изменять
В теле lambda функции мы поможем производить измения на this, которые потом отобразяться на характеристику
Например> change_chartics(user, {"xp": lambda this: this+10} -> Данная вункция увеличивает характеристику
хр на 10 в обьекте user
"""
def change_chartics(obj, param):
    for key in param.keys():
        obj[key] = param[key](obj[key])
def start(gamer):
    print("[ Охраник ]: Добро пожаловать в игру")
    print("(Укажите ваше имя) >>> ")
    name = input()
    gamer["name"] = name
    print("Добро пожаловать в хату, "+name)
    print("[ Охраник ]: Твоя задача выжить в хате")

"""
qs => quest system
справка о геймплеи(кек)
"""
def getting_in_qs():
    print("Перед вами список всех задач, которые нужно выполнить, чтобы выжить")
    print("Укажите цифру в скобках, перед квестом, который хотите пройти")
    print("Например, введите цифру 1 после инструкции [ ВАШ ХОД ] >>> ")
"""
Печатает все квесты на экран, которые есть в constructor
"""
def print_available_quest(quests):
    for quest in quests:
        option_answer = "[ (" + str(quests.index(quest) + 1) + ")"
        title = quest["title"] + " ]"
        print(option_answer+title)
    print("[ (*)Показать инвентарь ]")
    print("[ (#)Показать характеристики ]")

def help(user):
    print("Жизни: ", user["xp"])
    print("Урон: ", user["attack"])
    print("Защита: ", user["defence"])
