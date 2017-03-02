import random
def play():
    enemy_sum = [0,0] 
    user_sum = [0,0]
    print("Зэк предлагает вам сыграть в кости")
    print("Ходит зэк")
    for i in range(2):
        enemy_sum[i] = random.randint(1,6)
    print("Выпадает {0[0]} и {0[1]}".format(enemy_sum))
    for i in range(2):
        user_sum[i] = random.randint(1,6)
    print("Выпадает {0[0]} и {0[1]}".format(user_sum))
    if sum(enemy_sum) < sum(user_sum):
        print("Конгратс, ю виннер")
    else: 
        print("НУ и лошара")
