import sys
from random import randint


def start():
    player = 0
    diller = 0
    print("\nНажмите Enter чтобы сделать первый бросок")
    a = input()
    player = randint(1, 11)
    diller = randint(1, 11)
    play(player, diller)


def play(player_ochk, diller_ochk):
    while True:
        if player_ochk == 21:
            print("------------------------------------")
            print("Выиграл игрок")
            print("------------------------------------")
            win_player(player_ochk, diller_ochk)
            break

        elif player_ochk > 21:
            print("------------------------------------")
            print("Выиграл диллер")
            print("------------------------------------")
            win_diller(diller_ochk, player_ochk)

        else:
            print(f"Ваши очки : {player_ochk}")
            a = input("""Сделать бросок?
            Да - сделать бросок
            Нет - не делать бросок
            """)
            if a.lower() == "да":
                player_ochk += randint(1, 11)
            elif a.lower() == "нет":
                while diller_ochk <= 16:
                    diller_ochk += randint(1, 11)
                    if diller_ochk >= 17:
                        kordinator(player_ochk, diller_ochk)
                        break
            else:pass


def kordinator(player, diller):
    if player > 21:
        print("------------------------------------")
        print("Игрок перебрал, выиграл диллер")
        print("------------------------------------")
        win_diller(diller, player)
        return

    if diller > 21:
        print("------------------------------------")
        print("Диллер перебрал, выиграл игрок")
        print("------------------------------------")
        win_player(player, diller)
        return

    elif player < 21 and diller < 21:
        if player > diller:
            print("------------------------------------")
            print("Выиграл игрок")
            print("------------------------------------")
            win_player(player, diller)
            return

        elif diller > player:
            print("------------------------------------")
            print("Выиграл диллер")
            print("------------------------------------")
            win_diller(diller, player)
            return
        else:
            print("------------------------------------")
            print("НИЧЬЯ")
            print("------------------------------------")
            friend_ship(player, diller)
            return


def friend_ship(pl, dl):
    print("------------------------------------")
    print(f"Очки диллера: {dl}")
    print(f"Очки игрока: {pl}")
    print("------------------------------------")
    a = input("""Хотите сыграть еще?
        Да - сыграть еще
        Нет - выйти из игры
        """)
    if a.lower() == "нет":
        s = randint(1, 100)
        print("Пока, пока" if s > 50 else "До встречи, мой дорогой друг!")
        sys.exit()

    elif a.lower() == "да":
        start()
    else:
        print('Дайте корректный ответ')


def win_diller(ochk_diller, ochk_player):
    print("------------------------------------")
    print(f"Очки диллера: {ochk_diller}")
    print(f"Очки игрока: {ochk_player}")
    print("------------------------------------")
    a = input("""Хотите сыграть еще?
    Да - сыграть еще
    Нет - выйти из игры
    """)
    if a.lower() == "нет":
        s = randint(1, 100)
        print("Пока, пока" if s > 50 else "До встречи, мой дорогой друг!")
        sys.exit()
    elif a.lower() == "да":
        start()
    else:
        print('Дайте корректный ответ')


def win_player(ochk_player, ochk_diller):
    print("------------------------------------")
    print(f"Очки игрока: {ochk_player}")
    print(f"Очки диллера: {ochk_diller}")
    print("------------------------------------")
    a = input("""Хотите сыграть еще?
    Да - сыграть еще
    Нет - выйти из игры
    """)
    if a.lower() == "нет":
        s = randint(1, 100)
        print("Пока, пока" if s > 50 else "До встречи, мой дорогой друг!")
        sys.exit()

    elif a.lower() == "да":
        start()
    else:
        print('Дайте корректный ответ')


start()