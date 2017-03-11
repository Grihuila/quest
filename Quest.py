from constructor import all_quests
from tools import *
from Objects import *
start(user)
getting_in_qs()
print_available_quest(all_quests)
response = input("[ ВАШ ХОД ] >>> ")
count_quest = len(all_quests)
if response == "*":
    print("invent") #допилить
elif response == "#":
    help(user)
else:
    i_res = int(response)-1
    run_quest(all_quests[i_res])
