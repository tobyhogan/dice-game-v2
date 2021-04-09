from random import randint
# random is used to generate random numbers for the rolling of dice for each player
from tkinter import *
# tkinter is used to create the GUI components
from PIL import ImageTk, Image

# PIl is used to modify images, and process them so they can be used in the GUI

root = Tk()
root.geometry("0x0")

# creates the base window, where all other toplevel windows will be "placed" on

global player_one_score
global player_two_score

# makes player one and player two's scores accessible from anywhere in the program

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# gets the width and height of the device the program is being run on

window_width = 800
window_height = 650

# variables used to define the size of the actual game window

x_origin = (screen_width / 2) - (window_width / 2)
y_origin = (screen_height / 2) - (window_height / 2)

# finds where to place the window, so it appears in the middle of the user's screen

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]

# creates a list of all the characters in the alphabet, this is used to randomly generate codes to save games

menu_x = 85
menu_y = 80
check_x = 100
check_y = 40
outcome_x = 50
outcome_y = 100

login_menu_x = 65
login_menu_y = 140

# assigns values to variables to define the padding that will be used in different pages

player_one_score = 0
player_two_score = 0

# assigns values to variables used to store the current score of players one and two

player_one_roll = 0
player_two_roll = 0

# variables store the roll of each player

round = 1

# stores the current round number

dice_images = [ImageTk.PhotoImage(Image.open("/Users/tobyhogan/Downloads/dice1.jpg")),
               ImageTk.PhotoImage(Image.open("/Users/tobyhogan/Downloads/dice2.jpg")),
               ImageTk.PhotoImage(Image.open("/Users/tobyhogan/Downloads/dice2.jpg")),
               ImageTk.PhotoImage(Image.open("/Users/tobyhogan/Downloads/dice4.jpg")),
               ImageTk.PhotoImage(Image.open("/Users/tobyhogan/Downloads/dice5.jpg")),
               ImageTk.PhotoImage(Image.open("/Users/tobyhogan/Downloads/dice6.jpg"))]


# a list that stores each dice image needed to display numbers 1 to 6


class a_game:
    """A class that consolidates related information about a game that is currently being played"""

    def __init__(self, round, player_1, player_2, player_one_score, player_two_score, players_go):
        self.round = round
        self.players = players
        self.player_one_score = player_one_score
        self.player_two_score = player_two_score
        self.player_1 = player_1
        self.players_go = players_go
        self.player_2 = player_2


class player:
    """A class that consolidates related information about a player that is logged in"""

    def __init__(self, number, username, password):
        self.password = password
        self.logged_in = False
        self.number = number
        self.score = 0
        self.username = username


player_1 = player(1, "", "")
player_2 = player(2, "", "")

# creates instances of players, to be used as the 1st and 2nd players

players = [player_1, player_2]


# makes a list of the two players

def high_scores_exit_procedure(player):
    """A function that is executed when the highscores window is left, the function removes the window and
    changes to the login options window"""
    high_scores_window.destroy()
    login_options_menu(player)


def sort(arr):
    """A function that sorts a list, using the bubble sort method"""
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def high_scores(player):
    """A function that creates a window that shows the 10 highest scores achieved by players, the player
    has an option to head back to the main menu after they have seen this"""
    global high_scores_window

    global names

    options_window.destroy()
    high_scores_window = Toplevel(root)
    high_scores_window.title("HIGHSCORES - PLAYER: " + str(player))
    high_scores_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))

    f = open("scores.txt", "r+")

    scores = []
    names = []

    for x in f:
        scores.append(int(x.split(" ")[1]))
        names.append(str(x.split(" ")[0]))

    scores = sort(scores)

    high_scores_exit_button = Button(high_scores_window, text="OK", command=lambda: high_scores_exit_procedure(player),
                                     height=2, width=20)
    high_scores_exit_button.pack(side="bottom", pady=20)

    title_high_scores_label = Label(high_scores_window, text=" - ALL TIME HIGHSCORES - ", anchor="w")
    title_high_scores_label.pack(pady=30)

    if len(scores) >= 10:
        top_ten_entry = Label(high_scores_window, text=(
                "1 -  " + str(names[0]) + ": " + str(scores[0]) + "\n \n \n 2 -  " + str(names[1]) + ": " + str(
            scores[1]) + "\n \n \n 3 -  " + str(names[2]) + ": " + str(scores[2]) + "\n \n \n 4 -  " + str(
            names[3]) + ": " + str(scores[3]) + "\n \n \n 5 -  " + str(names[4]) + ": " + str(
            scores[4]) + "\n \n \n 6 -  " + str(names[5]) + ": " + str(scores[5]) + "\n \n \n 7-  " + str(
            names[6]) + ": " + str(scores[6]) + "\n \n \n 8-  " + str(names[7]) + ": " + str(
            scores[7]) + "\n \n \n 9 -  " + str(names[8]) + ": " + str(scores[8]) + "\n \n \n 10 -  " + str(
            names[9]) + ": " + str(scores[9])))
        top_ten_entry.pack()

    else:
        top_ten_entry = Label(high_scores_window, text="There are not enough scores to display :(")
        top_ten_entry.pack()


def after_rules_close(player):
    """A function that executes after the player has viewed the rules page, and wants to leave it, the
    function removes teh window, and goes back to the main menu(login options menu)"""
    rules_window.destroy()
    login_options_menu(int(player))


def rules(player):
    """A function that creates the rules window, the rules window provides addtional infromation to players about
    how the game works and how they can play it"""
    global rules_window

    options_window.destroy()
    rules_window = Toplevel(root)
    rules_window.title("RULES - PLAYER: " + str(player))
    rules_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))

    header_rules_label = Label(rules_window, text="THE GAME RULES: ").pack(pady=50)

    rules_label = Label(rules_window,
                        text="The points rolled on each player's dice are added to their score \n - If the total is an even number, and additional 10 points are added to their score \n - If the total is an odd number, 5 points are subtracted from their score. \n - If they roll a double, they get to roll one extra die and get the number of points \nrolled added to their score \n - The score of a player cannot go below 0 at any point. \n - The person with the highest score at the end of the 5 rounds wins. \n - If both players have the same score at the end of 5 rounds \n they each roll 1 die and whoever gets the \n highest score wins(this repeats until someone wins.",
                        anchor="w")
    rules_label.config(anchor=CENTER)
    rules_label.pack()

    rules_confirm_button = Button(rules_window, text="OK", width=25, height=2, highlightbackground="grey",
                                  command=lambda: after_rules_close(player)).pack(pady=100)


def after_bad_saved_input(player):
    """A function that executes after the bad input window is displayed to the player, removing it and going
    back to the main menu"""
    bad_input_window.destroy()

    login_options_menu(player)


def bad_input_saved(player):
    """A function that creates a window telling the player the input they have entered is not valid, becuase, for
    instance, they have not entered a valid username"""
    global bad_input_window

    bad_input_window = Toplevel(root)
    bad_input_window.title("INVALID INPUT")
    bad_input_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))

    bad_input_message = Label(bad_input_window, text="Invalid input detected").pack()
    bad_input_button_ok = Button(bad_input_window, text="OK", command=lambda: after_bad_saved_input(player))
    bad_input_button_ok.pack()


def check_players_save(player, gamesave_string, player_1_password, player_2_password):
    """A function that loads saves if the information entered is correct, if it's not, then the bad
    input window is made to appear"""
    start_game_window.destroy()

    file = open("logins.txt", "r+")

    gamesave_string = gamesave_string.split(" ")

    valid_check = False

    for n in file:

        if n.strip() == (str(gamesave_string[3]) + " " + str(player_1_password)).strip():

            valid_check = True


        else:
            pass

    if valid_check == True:
        game(int(gamesave_string[1]), gamesave_string[3], gamesave_string[4], int(gamesave_string[7]),
             int(gamesave_string[8]),
             int(gamesave_string[2]))


    else:
        bad_input_saved(player)


def check_save(player, code):
    """A function that creates a window that asks for player's usernames and passwords if they have
    entered correct information into the load save page"""
    f = open("gamesaves.txt", "r+")

    global start_game_window

    code_found = False

    string_found = ""

    for y in f:

        if y.split(" ")[0] == code.strip():
            code_found = True

            string_found = y

        else:
            pass

    if code_found == True:

        save_window.destroy()
        start_game_window = Toplevel(root)
        start_game_window.title("LOAD GAME - PLAYER: " + str(player))
        start_game_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))
        # format: code round, player go, player 1 name, player 2 name, player_1_password, player_2_password,
        # player 1 score, player 2 score

        player_1_enter_label = Label(start_game_window,
                                     text="Player 1: " + (y.split(" "))[3] + "\n \n Enter your password: ").pack(
            pady=30)
        player_1_password_entry = Entry(start_game_window, show="*")
        player_1_password_entry.pack(pady=30)

        player_2_enter_label = Label(start_game_window,
                                     text="Player 2: " + (y.split(" "))[4] + "\n \n Enter your password: ").pack(
            pady=30)
        player_2_password_entry = Entry(start_game_window, show="*")
        player_2_password_entry.pack(pady=30)

        load_game_passwords_button = Button(start_game_window, text="OK", height=2, width=14,
                                            command=lambda: check_players_save(player, string_found,
                                                                               player_1_password_entry.get(),
                                                                               player_2_password_entry.get()))
        load_game_passwords_button.pack()

    else:

        save_window.destroy()
        start_game_window = Toplevel(root)
        start_game_window.title("LOAD GAME - PLAYER: " + str(player))
        start_game_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))

        save_game_not_recognised_label = Label(start_game_window, text="The code you entered was not recognised").pack(
            pady=50)
        save_game_not_recognised_confirm_button = Button(start_game_window, text="OK",
                                                         command=lambda: login_options_menu(player), width=14,
                                                         height=2).pack(pady=50)


def load_save(player):
    """A function that asks the players for information about a saved game, if the information they enter
    is correct, then they can load a saved game and play it"""
    global save_window

    options_window.destroy()

    player = str(player).upper()
    save_window = Toplevel(root)
    save_window.title("LOAD_SAVES - PLAYER: " + player)
    save_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))

    exit_save_button = Button(save_window, text="EXIT", command=lambda: login_options_menu(player), width=10,
                              height=2).pack(side="top", anchor="nw", pady=20, padx=20)

    gamecode_prompt_label = Label(save_window, text="Enter your 3 digit game code: ").pack(side="top", pady=60)
    gamecode_entry = Entry(save_window)
    gamecode_entry.pack(side="top", pady=70)

    gamecode_confirm_button = Button(save_window, text="OK", width=15, height=2,
                                     command=lambda: check_save(player, gamecode_entry.get()))
    gamecode_confirm_button.pack(pady=50)


def player_1_or_2_create(player, username, password):
    """A function allows player one or two to create a new account"""
    f = open("logins.txt", "a+")

    if validate(username, 15, 3) and validate(password, 15, 3):

        f.write("\n" + username + " " + password)
        create_account_window.destroy()

        if int(player) == 1:
            player_1.username = username
            login_options_menu(2)
        elif int(player) == 2:
            player_2.username = username

            game(1, player_1.username, player_2.username, player_1.score, player_2.score, "player one")
        else:
            print("player")

    else:
        create_account_window.destroy()
        bad_create_window = Toplevel(root)
        bad_create_window.title("OUTCOME - PLAYER: " + str(player))
        bad_create_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))

        bad_create_label = Label(bad_create_window,
                                 text="Invalid input detected, please retry \n \n "
                                      "Text must be shorter than 15 characters but no longer than 3").pack(
            pady=100)

        bad_create_button = Button(bad_create_window, text="OK", width=25, height=5,
                                   command=lambda: login_options_menu(player))
        bad_create_button.pack(pady=outcome_y, padx=outcome_x)


def create_account(player):
    """A function that actually creates a new account, if the credentials entered on the "player_1_or_2
    page were correct, once verified the information is added to the "logins.txt" file"""
    global create_account_window

    options_window.destroy()
    create_account_window = Toplevel(root)
    create_account_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))
    create_account_window.title("CREATE ACCOUNT - PLAYER: " + str(player).upper())

    create_username_label = Label(create_account_window, text="New Username: ").pack(side="top", pady=30)

    create_username_entry = Entry(create_account_window)
    create_username_entry.pack(side="top", pady=30)

    create_password_label = Label(create_account_window, text="New Password: ").pack(side="top", pady=30)

    create_password_entry = Entry(create_account_window, show="*")
    create_password_entry.pack(side="top", pady=30)

    create_confirm_details_button = Button(create_account_window, text="OK", width=12, height=2,
                                           command=lambda: player_1_or_2_create(player, create_username_entry.get(),
                                                                                create_password_entry.get())).pack(
        pady=50)


def after_save_game(player):
    """A function that is executed after the player choses to close the save game window,
    the function removes the window, and sends the player back the main menu by referencing its
    function"""
    save_game_window.destroy()
    login_options_menu(1)


def is_bad_code(code, other_codes):
    """A function that compares a generated code to all the other codes that have already been generated
    to ensure that it has not been used already, as this would not be a sustainable way to generate
    codes"""
    bad = False

    for x in other_codes:
        if code == x:
            bad = True
        else:
            pass

    return bad


def save_game():
    """A function that creates the save game page, the save game page gives the player information
    about their game after they save it, the save game also generates a unique code and gives
    it to the player, so they can use it to continue playing the game"""
    global save_game_window

    game_window.destroy()

    save_game_window = Toplevel(root)
    save_game_window.title("GAME SAVED")
    save_game_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))

    gamecodes = []
    gamecode_is_total = True

    f = open("gamesaves.txt", "r+")

    for r in f:
        gamecodes.append(r[0])

    bad = True

    while bad:

        code_1 = alphabet[randint(0, 25)]
        code_2 = alphabet[randint(0, 25)]
        code_3 = alphabet[randint(0, 25)]

        total_code = str(code_1) + str(code_2) + str(code_3)

        if is_bad_code(total_code, gamecodes):
            bad = True

        else:
            bad = False

    f.write(str(total_code) + " " + str(game_1.round) + " " + str(game_1.players_go) + " " + str(
        game_1.player_1) + " " + str(game_1.player_2) + " " + str(player_1.password) + " " + str(
        player_2.password) + " " + str(game_1.player_one_score) + " " + str(game_1.player_two_score) + " \n")

    save_game_title_label = Label(save_game_window, text="GAME SAVED").pack(pady=40)

    save_game_label = Label(save_game_window,
                            text="\n" + game_1.player_1 + " and " + game_1.player_2 + "\'s game has been saved. \n"
                                                                                      " \n At round number: " + str(
                                game_1.round) + " \n \n  It's currently " + str(
                                game_1.players_go) + "\'s go. \n \n The scores are currently: \n \n Player One: " + str(
                                game_1.player_one_score) + " and Player Two: " + str(
                                game_1.player_two_score) + "\n \n Your game code is: " + str(
                                total_code) + " (remember this)")
    save_game_label.pack(pady=40)

    save_game_button = Button(save_game_window, text="OK", command=lambda: after_save_game(1), width=25, height=2)
    save_game_button.pack()


def destroy_results_window_and_login():
    """A function that executes after the user choses to close the results window and go back to the
    main menu, the function removes the results window and reopens the login page"""
    results_window.destroy()
    login_options_menu(1)


def result():
    """A function that creates a result window that appears after a game has finished, the window displays
    the players' scores adn gives the option to head back to the main menu
    """
    global results_window

    results_window = Toplevel(root)
    results_window.title("GAME OVER - " + (str(winning(player_one_score, player_two_score))).upper() + " WINS!")
    results_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))

    results_label = Label(results_window, text="Congratulations " + str(
        winning(game_1.player_one_score, game_1.player_two_score)) + ", after " + str(
        game_1.round - 1) + " rounds you won! \n  \n Both players scores have been saved.").pack(
        side="top", pady=50)
    ok_button = Button(results_window, command=(lambda: destroy_results_window_and_login()), text="OK",
                       highlightbackground="grey", height=5,
                       width=25)
    ok_button.pack(side="bottom", pady=50)


def winning(p1_score, p2_score):
    """A function that determines which player is currently winning based of each player's scores"""
    if p1_score > p2_score:
        return "Player One"
    elif p2_score > p1_score:
        return "Player Two"
    else:
        return "Scores are Tied"


def algorithm(number):
    """A function that determines the operations that occur to a roll of dice in the game, depending on
    whether each dice has the same number(a double) and whether the sum of the roll is odd or even"""
    if number % 2 == 0:
        return number + 10
    elif number % 2 != 0 and number - 5 >= 0:
        return number - 5
    else:
        return 0


def roll(player):
    """A function that is called when a player attempts to roll their dice, the function determines which player
    is rolling and changes their dice images according to what their roll was"""
    f = open("scores.txt", "a+")

    if int(game_1.round) <= 5 or game_1.player_one_score == game_1.player_two_score:
        rand1 = randint(1, 6)
        rand2 = randint(1, 6)

        if player == "player one":
            game_1.players_go = "1"

            round_number_label.configure(text="ROUND: " + str(game_1.round))

            game_1.player_one_score += algorithm(rand1 + rand2)
            player_1_score_label.configure(text="Player One Score: " + str(game_1.player_one_score))

            player_1_roll_button["state"] = "disabled"
            player_2_roll_button["state"] = "normal"

            p1_dice_label_1.configure(image=dice_images[rand1 - 1])
            p1_dice_label_2.configure(image=dice_images[rand2 - 1])
            game_1.round += 1
            winning_label.configure(text="Winning: " + winning(game_1.player_one_score, game_1.player_two_score))
        else:
            game_1.players_go = "1"

            game_1.player_two_score += algorithm(rand1 + rand2)
            player_2_score_label.configure(text="Player Two Score: " + str(game_1.player_two_score))
            round_number_label.configure(text="ROUND: " + str(game_1.round))
            player_2_roll_button["state"] = "disabled"
            player_1_roll_button["state"] = "normal"

            p2_dice_label_1.configure(image=dice_images[rand1 - 1])
            p2_dice_label_2.configure(image=dice_images[rand2 - 1])
            winning_label.configure(text="Winning: " + winning(game_1.player_one_score, game_1.player_two_score))
    else:
        f.write(str(game_1.player_1) + " " + str(game_1.player_one_score) + " \n")
        f.write(str(game_1.player_2) + " " + str(game_1.player_two_score) + " \n")
        game_window.destroy()
        result()


def game(round, player_1, player_2, player_one_score, player_two_score, players_go):
    """A function that creates the main game page itself, on the page dice are shown for each player
    and there are buttons that give each player the option to roll them"""
    global game_window
    global player_1_frame
    global player_2_frame
    global header_frame
    global player_1_score_label
    global player_2_score_label
    global round_number_label
    global player_1_roll_button
    global player_2_roll_button
    global winning_label
    global p1_dice_label_1
    global p1_dice_label_2
    global p2_dice_label_1
    global p2_dice_label_2
    global player_go
    global game_1

    game_1 = a_game(round, player_1, player_2, player_one_score, player_two_score, players_go)

    player_go = "player_one"
    game_window = Toplevel(root)
    game_window.title("GAME - Player 1 VS Player 2")
    game_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))

    header_frame = Frame(game_window, width=1000, height=120)
    header_frame.pack(fill="both", side="top")

    header_exit_button = Button(header_frame, text="EXIT", command=lambda: root.destroy(), width=10, height=3)
    header_exit_button.pack(side="right", pady=20, padx=20)

    save_game_button = Button(header_frame, text="SAVE GAME", width=10, height=3,
                              command=save_game)
    save_game_button.pack(side="left", pady=20, padx=20)

    player_1_frame = LabelFrame(game_window, text="Player 1 - " + game_1.player_1)
    player_1_frame.pack(fill="both", expand="yes", side="left", padx=20, pady=20)

    player_2_frame = LabelFrame(game_window, text="Player 2 - " + game_1.player_2)
    player_2_frame.pack(fill="both", expand="yes", side="right", padx=20, pady=20)

    player_1_score_label = Label(player_1_frame, text="Player One Score: " + str(player_one_score))
    player_1_score_label.pack(side="top")

    player_2_score_label = Label(player_2_frame, text="Player Two Score: " + str(player_two_score))
    player_2_score_label.pack(side="top")

    player_1_roll_button = Button(player_1_frame, text="ROLL", height=5, width=25, command=lambda: roll("player one"))
    player_1_roll_button.pack(side="bottom", pady=10)

    player_2_roll_button = Button(player_2_frame, text="ROLL", height=5, width=25, command=lambda: roll("player two"))
    player_2_roll_button.pack(side="bottom", pady=10)
    player_2_roll_button['state'] = "disabled"

    p1_dice_label_1 = Label(player_1_frame, image=dice_images[0])
    p1_dice_label_1.pack()

    p1_dice_label_2 = Label(player_1_frame, image=dice_images[0])
    p1_dice_label_2.pack()

    p2_dice_label_1 = Label(player_2_frame, image=dice_images[0])
    p2_dice_label_1.pack()

    p2_dice_label_2 = Label(player_2_frame, image=dice_images[0])
    p2_dice_label_2.pack()

    winning_label = Label(header_frame, text="Winning: " + winning(player_one_score, player_two_score))
    winning_label.pack(side="top", pady=10)

    round_number_label = Label(header_frame, text="ROUND: " + str(game_1.round))
    round_number_label.pack()


def login_and_break(player, again):
    """A function that is called when the player choses to leave the outcome window and go back
    to the main menu, the function removes the outcomes window, and depending on which players are logged in
    goes back to the main menu, as either player one or player two"""
    if again:
        outcome_window.destroy()
        login_options_menu(player)

    elif not (again) and player_1.logged_in and not (player_2.logged_in):
        outcome_window.destroy()
        login_options_menu(2)
    else:
        outcome_window.destroy()
        game(1, player_1.username, player_2.username, player_1.score, player_2.score, "player one")


def outcome(status, player, again):
    """A function that gives the outcome of a players attempt to login, if it was successful
    it congratulates the player, if not, it tells the player the input they entered is invalid """
    global outcome_window

    outcome_window = Toplevel(root)
    outcome_window.title("OUTCOME - PLAYER: " + player)
    outcome_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))

    outcome_label = Label(outcome_window, text=status).pack(pady=100)

    outcome_ok_button = Button(outcome_window, text="OK", width=25, height=5,
                               command=lambda: login_and_break(player, again))
    outcome_ok_button.pack(pady=outcome_y, padx=outcome_x)


def validate(string, max_len, min_len):
    """A function that validates input against certain criteria that are specified by the parameters,
    the function evaluates the inputs length"""
    if len(string) > max_len or len(string) < min_len:

        return False
    else:
        return True


def authorize(username, password, player):
    """A function that is used to authorize users attempting to login, the functin will check the username
    and password they've entered against the logins file(logins.txt) and see if they are present, if they
    are the player will be allowed to move on to the main menu, if they aren't, then the player will be sent
    back to the login page"""
    f = open("logins.txt", "r+")
    if player == 1:
        for x in f:
            if x.strip() == (username + " " + password).strip():
                player_1.logged_in = True
                player_1.password = str(password)
            else:
                pass

        check_window.destroy()
        if player_1.logged_in:
            outcome("Congratulations, you're in! ", str(player), False)
            player_1.username = str(username)
        else:
            outcome("Sorry, the details entered were not recognised", str(player), True)

    else:
        print(username, player_1.username)
        for x in f:
            if x.strip() == ((username + " " + password).strip()) and validate(username, 15, 3) and validate(password,
                                                                                                             15,
                                                                                                             3) \
                    and str(player_1.username) != str(
                username):
                player_2.logged_in = True
                player_2.password = str(password)
            else:
                pass

        check_window.destroy()
        if player_2.logged_in:
            outcome("Congratulations, you're in! ", str(player), False)
            player_2.username = str(username)
        else:
            outcome("Sorry, the details entered were not recognised", str(player), True)


def user_check(player):
    """A function that serves as a medium for allowing users to enter their username and password, for them
    to be checked, ensuring that users who play the game are authorized, as specified in the project brief"""
    global password_entry
    global username_entry
    global check_window

    options_window.destroy()

    check_window = Toplevel(root)
    check_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))
    check_window.title("DICE GAME - CHECK - PLAYER: " + str(player))

    username_label = Label(check_window, text="username: ").pack(padx=check_x, pady=check_y)
    username_entry = Entry(check_window)
    username_entry.pack(pady=check_y)

    password_label = Label(check_window, text="password: ").pack(padx=check_x, pady=check_y)
    password_entry = Entry(check_window, show="*")
    password_entry.pack(pady=check_y)

    confirm_button = Button(check_window, text="Confirm", width=21, height=2,
                            command=lambda: authorize(str(username_entry.get()), str(password_entry.get()), player))
    confirm_button.pack(padx=check_x, pady=check_y)


def login_options_menu(player):
    """A funciton that initially provides the with options they can take, users can login, create an account,
    exit, look at the rules, or play the game by loading a save"""
    global options_window

    player_1.logged_in = False
    player_2.logged_in = False

    options_window = Toplevel(root)
    options_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_origin, y_origin))
    options_window.title("DICE GAME - MENU - PLAYER: " + str(player))

    login_button = Button(options_window, width=15, height=3, text="LOGIN", command=lambda: user_check(player),
                          highlightbackground="light blue").grid(
        row=0, column=0, padx=login_menu_x, pady=login_menu_y)

    create_account_button = Button(options_window, width=15, height=3, text="CREATE ACCOUNT",
                                   command=lambda: create_account(player), highlightbackground="light blue") \
        .grid(row=0,
              column=1,
              padx=login_menu_x,
              pady=login_menu_y)

    exit_button = Button(options_window, width=15, height=3, text="EXIT", command=lambda: root.destroy(),
                         highlightbackground="light blue").grid(row=0,
                                                                column=2,
                                                                padx=login_menu_x,
                                                                pady=login_menu_y)

    high_scores_button = Button(options_window, width=15, height=3, text="HIGH SCORES",
                                command=lambda: high_scores(1), highlightbackground="light blue"). \
        grid(row=1, column=0,
             padx=login_menu_x,
             pady=login_menu_y)

    rules_button = Button(options_window, width=15, height=3, text="GAME RULES", command=lambda: rules(player),
                          highlightbackground="light blue").grid(
        row=1, column=1, padx=login_menu_x, pady=login_menu_y)

    load_save_button = Button(options_window, width=15, height=3, text="LOAD SAVE",
                              command=lambda: load_save(player), highlightbackground="light blue"). \
        grid(row=1, column=2,
             padx=login_menu_x,
             pady=login_menu_y)


login_options_menu(1)

# the login options menu function is called to start the program

mainloop()
