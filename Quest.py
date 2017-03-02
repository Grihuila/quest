#Thomas
#Welcome to Quest
from tools import quest
attack = 15
user_xp = 40
pahan_xp = 30
defence = 0
enemy_xp = [10, 10, 10]
quest("Go ili zassal?", {
    'GO': lambda: print("VI V HATE! CONGRUTS!"),
    'else': lambda: exit(0)
})

