"""
Thomas tools module

@question -> вопрос, который мы собираемся задавать
@option -> варианты ответа, этот параметр является словарем
"""


def quest(question, option):
    response = input(question+"\nВаш ответ>")
    for res in option.keys():
        if res.upper() == response.upper():
            for fn in option[res]:
                fn()
            break
    else:
        option['else']()


def change_chartics(obj, param):
    for key in param.keys():
        obj[key] = param[key](obj[key])
