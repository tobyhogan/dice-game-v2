from tkinter import *
from colorama import Fore
from random import randint
from time import sleep

menu_x = 85
menu_y = 80
check_x = 50
check_y = 50
outcome_x = 50
outcome_y = 100

root = Tk()
root.geometry("0x0")


class player:
    def __init__(self, number, username):
        self.logged_in = False
        self.number = number
        self.score = 0
        self.username = username


player_1 = player(1, "")
player_2 = player(2, "")

players = [player_1, player_2]


def login_and_break(player, again):
    if again:
        outcome_window.destroy()
        login_options_menu(player)

    elif not (again) and player_1.logged_in and not (player_2.logged_in):
        outcome_window.destroy()
        login_options_menu(2)
    else:
        outcome_window.destroy()
        game()


def outcome(status, player, again):
    global outcome_window

    outcome_window = Toplevel(root)
    outcome_window.title("OUTCOME - PLAYER: " + player)
    outcome_window.geometry("800x500")

    outcome_label = Label(outcome_window, text=status).pack(pady=100)

    outcome_ok_button = Button(outcome_window, text="OK", width=25, height=5,
                               command=lambda: login_and_break(player, again))
    outcome_ok_button.pack(pady=outcome_y, padx=outcome_x)


def authorize(username, password, player):
    f = open("logins.txt", "r+")
    for x in f:
        if x.strip() == (username + " " + password).strip():
            players[int(player) - 1].logged_in = True
        else:
            pass

    check_window.destroy()

    if players[int(player) - 1].logged_in:
        outcome("Congratulations, you're in! ", str(player), False)
    else:
        outcome("Sorry, the details entered were not recognised", str(player), True)


def user_check(player):
    global password_entry
    global username_entry
    global check_window

    options_window.destroy()

    check_window = Toplevel(root)
    check_window.geometry("800x500")
    check_window.title("DICE GAME - CHECK - PLAYER: " + str(player))

    username_label = Label(check_window, text="username: ").pack(padx=check_x, pady=check_y)
    username_entry = Entry(check_window)
    username_entry.pack()

    password_label = Label(check_window, text="password: ").pack(padx=check_x, pady=check_y)
    password_entry = Entry(check_window, show="*")
    password_entry.pack()

    confirm_button = Button(check_window, text="Confirm", width=21, height=2,
                            command=lambda: authorize(str(username_entry.get()), str(password_entry.get()), player))
    confirm_button.pack(padx=check_x, pady=check_y)


def login_options_menu(player):
    global options_window

    options_window = Toplevel(root)
    options_window.geometry("800x500")
    options_window.title("DICE GAME - MENU - PLAYER: " + str(player))

    login_button = Button(options_window, width=25, height=5, text="LOGIN", command=lambda: user_check(player)).grid(
        row=0, column=0,
        padx=menu_x,
        pady=menu_y)
    create_account_button = Button(options_window, width=25, height=5, text="CREATE ACCOUNT",
                                   command=lambda: alkdf()).grid(row=0, column=1, padx=menu_x, pady=menu_y)

    exit_button = Button(options_window, width=25, height=5, text="EXIT", command=options_window.destroy).grid(row=1,
                                                                                                               column=0,
                                                                                                               padx=menu_x,
                                                                                                               pady=menu_y)
    high_scores_button = Button(options_window, width=25, height=5, text="HIGH SCORES",
                                command=lambda: after_login(2)).grid(row=1, column=1, padx=menu_x, pady=menu_y)

def game():

    game_window = Toplevel(root)
    game_window.title("GAME - "+player_1.username+"VS "+player_2.username)
    game_window.geometry("1000x500")

    player_1_title_label = Label(game_window, text = "Player One").grid(row = 0, column = 0)
    space_label = Label(game_window, text = "              ").grid(row = 0, column = 1)
    player_2_title_label = Label(game_window, text = "Player Two").grid(row = 0, column = 2)


login_options_menu(1)


mainloop()
