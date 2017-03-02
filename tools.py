#Thomas tools module
#@question -> вопрос, который мы собираемся задавать
#@option -> варианты ответа, этот параметр является словарем
def quest(question,option):
    response = input(question+"\nВаш ответ>")
    for res in option.keys():
        if res.upper() == response.upper():
            option[res]()
            break
    else:
        option['else']()