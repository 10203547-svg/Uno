#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain = Brain()

# Robot configuration code
brain_inertial = Inertial()
motor_1 = Motor(Ports.PORT1, False)
motor_5 = Motor(Ports.PORT5, True)


# Wait for sensor(s) to fully initialize
wait(100, MSEC)

# generating and setting random seed
def initializeRandomSeed():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    systemTime = brain.timer.system() * 100
    urandom.seed(int(xaxis + yaxis + zaxis + systemTime)) 

# Initialize random seed 
initializeRandomSeed()

#endregion VEXcode Generated Robot Configuration
# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode EXP Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code

# Create events
FWD = Event()
RT = Event()
LT = Event()

# Functions
def when_started():
    FWD.broadcast_and_wait()
    LT.broadcast_and_wait()
    FWD.broadcast_and_wait()
    RT.broadcast_and_wait()
    FWD.broadcast_and_wait()

def motor1_move_forward():
    #motor_1.spin_for(FORWARD, 425, DEGREES)
    print("motor1 FWD 425")
def motor5_move_forward():
    #motor_5.spin_for(FORWARD, 425, DEGREES)
    print("motor5 FWD 425")
def motor1_turn_right():
    #motor_1.spin_for(FORWARD, 220, DEGREES)
    print("motor1 FRW 220")
def motor5_turn_right():
    #motor_5.spin_for(REVERSE, 220, DEGREES)
    print("motor5 RAV 220")
def motor1_turn_left():
    #motor_1.spin_for(REVERSE, 220, DEGREES)
    print("motor1 RAV 220")
def motor5_turn_left():
    #motor_5.spin_for(FORWARD, 220, DEGREES)
    print("motor5 FRW 220")

# Register callback functions to the events
FWD(motor1_move_forward)
FWD(motor5_move_forward)
RT(motor1_turn_right)
RT(motor5_turn_right)
LT(motor1_turn_left)
LT(motor5_turn_left)
wait(15, MSEC)

# Start the program!
from vex import *
import random

# Initialize Brain
brain = Brain()

COLORS = ["Red", "Yellow", "Green", "Blue"]
VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Skip", "Reverse", "Draw Two"]

# ==========================================
# CARD CLASS
# ==========================================
class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

def draw_card_full_screen(card_str, color_code):
    brain.screen.clear_screen()
    if color_code == 'R': brain.screen.set_fill_color(Color.RED)
    elif color_code == 'G': brain.screen.set_fill_color(Color.GREEN)
    elif color_code == 'B': brain.screen.set_fill_color(Color.BLUE)
    elif color_code == 'Y': brain.screen.set_fill_color(Color.YELLOW)
    else: brain.screen.set_fill_color(Color.BLACK)
    brain.screen.set_pen_color(Color.WHITE)
    for i in range(5):
        brain.screen.draw_rectangle(0+i, 0+i, 159-(i*2), 107-(i*2))
   
    card = card_str[1:]
    if card == "0":
        for i in range(15):
            brain.screen.draw_rectangle(20+i, 20+i, 119-(i*2), 67-(i*2))
    elif card == "8":
        for i in range(15):
            brain.screen.draw_rectangle(20+i, 20+i, 119-(i*2), 67-(i*2))
        for i in range(15):
            brain.screen.draw_line(72+i, 20, 72+i, 85)
    elif card == "1":
        for i in range(15):
            brain.screen.draw_line(20, 47+i, 139, 47+i)
    elif card == "3":
        for i in range(15):
            brain.screen.draw_line(20, 20+i, 139, 20+i)
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
    elif card == "2":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 20+i, 72, 20+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 73+i, 139, 73+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "5":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "6":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
            brain.screen.draw_line(72, 73+i, 139, 73+i)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "9":
        for i in range(15):
            brain.screen.draw_line(20+i, 20, 20+i, 87)
            brain.screen.draw_line(20, 20+i, 72, 20+i)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
            brain.screen.draw_line(125+i, 20, 125+i, 87)
        for i in range(3):
            brain.screen.draw_line(145+i, 20, 145+i, 87)
    elif card == "4" and "D" not in card_str:
        for i in range(15):
            brain.screen.draw_line(20, 20+i, 72, 20+i)
            brain.screen.draw_line(20, 73+i, 72, 73+i)
            brain.screen.draw_line(72+i, 20, 72+i, 87)
            brain.screen.draw_line(72, 20+i, 139, 20+i)
    elif card == "7":
        for i in range(15):
            brain.screen.draw_line(20, 20+i, 139, 20+i)
            brain.screen.draw_line(20+i, 20, 20+i, 87)
    elif card == "Rv":
        for i in range(15):
            brain.screen.draw_line(62+i, 30, 62+i, 87)
            brain.screen.draw_line(69, 20, 52+i, 40)
            brain.screen.draw_line(69, 20, 82-i, 40)
            brain.screen.draw_line(82+i, 20, 82+i, 77)
            brain.screen.draw_line(89, 87, 74+i, 67)
            brain.screen.draw_line(89, 87, 104-i, 67)
    elif card == "S":
        for i in range(15):
            brain.screen.draw_rectangle(40+i, 20+i, 82-(i*2), 67-(i*2))
        for i in range(15):
            brain.screen.draw_line(52+i, 20, 92+i, 80)
    elif card == "D2":
        brain.screen.set_fill_color(Color.WHITE)
        for i in range(40):
            brain.screen.draw_circle(60+i, 42+(i/2), 30)
        if color_code == 'R': brain.screen.set_fill_color(Color.RED)
        elif color_code == 'G': brain.screen.set_fill_color(Color.GREEN)
        elif color_code == 'B': brain.screen.set_fill_color(Color.BLUE)
        elif color_code == 'Y': brain.screen.set_fill_color(Color.YELLOW)
        brain.screen.draw_rectangle(47, 32, 40, 25)
        brain.screen.draw_rectangle(73, 52, 40, 25)
        for i in range(5):
            brain.screen.draw_line(18+i, 85, 18+i, 95)
            brain.screen.draw_line(14, 88+i, 26, 88+i)
            brain.screen.draw_line(10+i, 66, 10+i, 79)
            brain.screen.draw_line(10, 66+i, 20, 66+i)
            brain.screen.draw_line(18+i, 66, 18+i, 79)
            brain.screen.draw_line(20, 75+i, 30, 75+i)
            brain.screen.draw_line(26+i, 66, 26+i, 79)

            brain.screen.draw_line(159-18-i, 107-85, 159-18-i, 107-95)
            brain.screen.draw_line(159-14, 107-88-i, 159-26, 107-88-i)
            brain.screen.draw_line(159-10-i, 107-66, 159-10-i, 107-79)
            brain.screen.draw_line(159-10, 107-66-i, 159-20, 107-66-i)
            brain.screen.draw_line(159-18-i, 107-66, 159-18-i, 107-79)
            brain.screen.draw_line(159-20, 107-75-i, 159-30, 107-75-i)
            brain.screen.draw_line(159-26-i, 107-66, 159-26-i, 107-79)
    elif card_str == "W":
        brain.screen.set_fill_color(Color.BLUE)
        brain.screen.draw_rectangle(50, 20, 30, 32)
        brain.screen.set_fill_color(Color.RED)
        brain.screen.draw_rectangle(50, 52, 30, 32)
        brain.screen.set_fill_color(Color.GREEN)
        brain.screen.draw_rectangle(80, 20, 30, 32)
        brain.screen.set_fill_color(Color.YELLOW)
        brain.screen.draw_rectangle(80, 52, 30, 32)
        brain.screen.set_fill_color(Color.TRANSPARENT)
        brain.screen.set_pen_width(3)
        for i in range(15):
            brain.screen.draw_circle(80, 52, 30-(i/5))
        brain.screen.set_pen_color(Color.BLACK)
        for i in range(65):
            brain.screen.draw_circle(80, 52, 31+(i/5))
        brain.screen.set_pen_width(1)
    elif card_str == "D4":
        brain.screen.set_fill_color(Color.YELLOW)
        brain.screen.draw_rectangle(78, 42, 40, 25)
        brain.screen.set_fill_color(Color.GREEN)
        brain.screen.draw_rectangle(60, 28, 40, 25)
        brain.screen.set_fill_color(Color.BLUE)
        brain.screen.draw_rectangle(42, 42, 40, 25)
        brain.screen.set_fill_color(Color.RED)
        brain.screen.draw_rectangle(60, 56, 40, 25)
        for i in range(5):
            brain.screen.draw_line(18+i, 85, 18+i, 95)
            brain.screen.draw_line(14, 88+i, 26, 88+i)
            brain.screen.draw_line(10, 75+i, 20, 75+i)
            brain.screen.draw_line(16+i, 75, 16+i, 66)
            brain.screen.draw_line(10, 66+i, 30, 66+i)

            brain.screen.draw_line(159-18-i, 107-85, 159-18-i, 107-95)
            brain.screen.draw_line(159-14, 107-88-i, 159-26, 107-88-i)
            brain.screen.draw_line(159-10, 107-75-i, 159-20, 107-75-i)
            brain.screen.draw_line(159-16-i, 107-75, 159-16-i, 107-66)
            brain.screen.draw_line(159-10, 107-66-i, 159-30, 107-66-i)
    else:
        brain.screen.set_fill_color(Color.RED)
        brain.screen.set_pen_color(Color.RED)
        for i in range(40):
            brain.screen.draw_circle(60+i, 42+(i/2), 30)
        brain.screen.set_pen_color(Color.YELLOW)
        for i in range(5):
            brain.screen.draw_line(75, 50+i-5, 85, 50+i-5)
            brain.screen.draw_line(75, 50+i+5, 85, 50+i+5)
            brain.screen.draw_line(75, 50+i+5, 85, 50+i-5)

            brain.screen.draw_line(75, 50+i-15, 85, 50+i-15)
            brain.screen.draw_line(75+(i/2), 50-15, 75+(i/2), 50-25)
            brain.screen.draw_line(83+(i/2), 50-15, 83+(i/2), 50-25)
            brain.screen.draw_line(75, 50+i-25, 85, 50+i-25)

            brain.screen.draw_line(75, 50+i+15, 85, 50+i+15)
            brain.screen.draw_line(83+(i/2), 50+15, 83+(i/2), 50+25)
            brain.screen.draw_line(75, 50+i+25, 85, 50+i+25)
    brain.screen.set_fill_color(Color.TRANSPARENT)


    def to_short(self):
        col_code = str(self.color)[0] if self.color in COLORS else "W"
        if str(self.value) == "Draw Two":
            val_code = "+2"
        elif str(self.value) == "Draw Four":
            val_code = "+4"
        elif str(self.value) == "Reverse":
            val_code = "R"
        elif str(self.value) == "Skip":
            val_code = "S"
        elif str(self.value) == "Wild":
            val_code = "W"
        else:
            val_code = str(self.value)[0]
        return col_code + val_code


# ==========================================
# SCREEN RENDERER (MAX 12 CHARS/LINE)
# ==========================================
def get_vex_color(color_name):
    if color_name == "Red":
        return Color.RED
    elif color_name == "Yellow":
        return Color.YELLOW
    elif color_name == "Green":
        return Color.GREEN
    elif color_name == "Blue":
        return Color.BLUE
    elif color_name == "Wild":
        return Color.PURPLE
    return Color.BLACK


def render_screen(color_name, lines):
    bg_color = get_vex_color(color_name)
    text_color = Color.BLACK if color_name == "Yellow" else Color.WHITE

    try:
        brain.screen.clear_screen(bg_color)
        brain.screen.set_fill_color(bg_color)
        brain.screen.set_pen_color(text_color)
    except Exception:
        brain.screen.clear_screen()

    for idx, text in enumerate(lines[:5]):
        formatted = str(text)[:12]
        brain.screen.set_cursor(idx + 1, 1)
        brain.screen.print(formatted)


# ==========================================
# DECK & RULES
# ==========================================
def shuffle_list(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]


def build_deck():
    deck = []
    for color in COLORS:
        deck.append(Card(color, 0))
        for val in VALUES[1:]:
            deck.append(Card(color, val))
            deck.append(Card(color, val))
    for _ in range(4):
        deck.append(Card("Wild", "Wild"))
        deck.append(Card("Wild", "Draw Four"))
    shuffle_list(deck)
    return deck


def draw_card(deck, discard_pile):
    if not deck:
        if len(discard_pile) > 1:
            top_card = discard_pile.pop()
            deck.extend(discard_pile)
            discard_pile.clear()
            discard_pile.append(top_card)
            shuffle_list(deck)
        else:
            return None
    return deck.pop()


def can_play(card, top_card, active_color, pending_draws):
    if pending_draws > 0:
        if str(top_card.value) == "Draw Two" and str(card.value) == "Draw Two":
            return True
        if str(top_card.value) == "Draw Four" and str(card.value) == "Draw Four":
            return True
        return False

    if card.color == "Wild" or card.color == active_color:
        return True
    if card.value == top_card.value:
        return True
    return False


def get_playable_indices(hand, top_card, active_color, pending_draws):
    return [i for i, c in enumerate(hand) if can_play(c, top_card, active_color, pending_draws)]


# ==========================================
# FULLY AUTONOMOUS MULTI-ROBOT GAME LOOP
# ==========================================
def run_autonomous_multi_robot_game():
    num_robots = 3  # Robot 1, Robot 2, Robot 3
    deck = build_deck()
    discard_pile = []

    # Deal 7 cards to each robot
    hands = [[draw_card(deck, discard_pile) for _ in range(7)] for _ in range(num_robots)]

    top_card = draw_card(deck, discard_pile)
    while top_card and top_card.color == "Wild":
        deck.append(top_card)
        shuffle_list(deck)
        top_card = draw_card(deck, discard_pile)

    discard_pile.append(top_card)
    active_color = top_card.color if top_card else "Red"
    pending_draws = 0
    current_bot = 0
    direction = 1

    lines = [
        "GAME START",
        "ROBOTS: " + str(num_robots),
        "TOP: " + top_card.to_short(),
        "CLR: " + active_color[:3],
        "PLAYING..."
    ]
    render_screen(active_color, lines)
    wait(2, SECONDS)

    while True:
        bot_id = current_bot + 1
        hand = hands[current_bot]
        top_card = discard_pile[-1]
        playable = get_playable_indices(hand, top_card, active_color, pending_draws)

        played_card = None

        # 1. ATTACKED (+2 / +4) -> Draw penalty cards without physical movement
        if pending_draws > 0 and not playable:
            lines = [
                "BOT " + str(bot_id) + " ATTACK",
                "PENALTY +" + str(pending_draws),
                "DRAWING...",
                "CLR: " + active_color[:3],
                "HAND: " + str(len(hand))
            ]
            render_screen("Red", lines)

            for _ in range(pending_draws):
                drawn = draw_card(deck, discard_pile)
                if drawn:
                    hand.append(drawn)
            pending_draws = 0
            wait(1.5, SECONDS)

        # 2. NO MATCH -> Draw 1 card without physical movement
        elif not playable:
            lines = [
                "BOT " + str(bot_id) + " NO CARD",
                "DRAWING...",
                "TOP: " + top_card.to_short(),
                "CLR: " + active_color[:3],
                "HAND: " + str(len(hand))
            ]
            render_screen(active_color, lines)

            drawn = draw_card(deck, discard_pile)
            if drawn:
                hand.append(drawn)
                if can_play(drawn, top_card, active_color, 0):
                    played_card = hand.pop()
                    discard_pile.append(played_card)
                    if str(played_card.value) == "Draw Two":
                        pending_draws = 2
                    elif str(played_card.value) == "Draw Four":
                        pending_draws = 4
                    active_color = random.choice(COLORS) if played_card.color == "Wild" else played_card.color

                    lines = [
                        "BOT " + str(bot_id) + " PLAYED",
                        "CARD: " + played_card.to_short(),
                        "TOP: " + played_card.to_short(),
                        "CLR: " + active_color[:3],
                        "HAND: " + str(len(hand))
                    ]
                    render_screen(active_color, lines)
                    wait(1.5, SECONDS)

        # 3. PLAY MATCHING CARD
        else:
            play_idx = playable[0]
            played_card = hand.pop(play_idx)
            discard_pile.append(played_card)

            if str(played_card.value) == "Draw Two":
                pending_draws += 2
            elif str(played_card.value) == "Draw Four":
                pending_draws += 4

            active_color = random.choice(COLORS) if played_card.color == "Wild" else played_card.color

            lines = [
                "BOT " + str(bot_id) + " PLAYED",
                "CARD: " + played_card.to_short(),
                "TOP: " + played_card.to_short(),
                "CLR: " + active_color[:3],
                "HAND: " + str(len(hand))
            ]
            render_screen(active_color, lines)
            wait(1.5, SECONDS)

        # WIN CHECK
        if len(hand) == 0:
            lines = [
                "= GAME OVER =",
                "BOT " + str(bot_id) + " WINS!",
                "UNO!",
                "",
                ""
            ]
            render_screen("Green", lines)
            break

        # ACTION CARD TURN ROTATION
        skip_next = False
        if played_card:
            if str(played_card.value) == "Skip":
                skip_next = True
            elif str(played_card.value) == "Reverse":
                direction *= -1

        step = 2 if skip_next else 1
        current_bot = (current_bot + (direction * step)) % num_robots


# Start Autonomous Game
run_autonomous_multi_robot_game()