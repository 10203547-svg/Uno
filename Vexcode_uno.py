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

# Initialize Motors (Ports 1 and 5)
try:
    motor1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
    motor5 = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
except Exception:
    motor1 = None
    motor5 = None

COLORS = ["Red", "Yellow", "Green", "Blue"]
VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Skip", "Reverse", "Draw Two"]
TYPES = ["NUMBER", "+2 ATK", "+4 ATK"]

# ==========================================
# CARD CLASS
# ==========================================
class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def short_text(self):
        c = str(self.color)[0] if self.color in COLORS else "W"
        v = str(self.value)
        if v == "Draw Two": v = "+2"
        elif v == "Draw Four": v = "+4"
        elif v == "Reverse": v = "R"
        elif v == "Skip": v = "S"
        elif v == "Wild": v = "W"
        else: v = v[0]
        return (c + v)[:3]


# ==========================================
# CUSTOM SHUFFLE (MicroPython safe)
# ==========================================
def shuffle_list(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]


# ==========================================
# DUAL MOTOR DRIVE (CENTER AND BACK)
# ==========================================
def drive_wheels():
    if motor1 and motor5:
        try:
            motor1.spin(FORWARD, 50, PERCENT)
            motor5.spin(FORWARD, 50, PERCENT)
            wait(1, SECONDS)

            motor1.stop(BRAKE)
            motor5.stop(BRAKE)
            wait(0.2, SECONDS)

            motor1.spin(REVERSE, 50, PERCENT)
            motor5.spin(REVERSE, 50, PERCENT)
            wait(1, SECONDS)

            motor1.stop(BRAKE)
            motor5.stop(BRAKE)
        except Exception:
            pass


# ==========================================
# DECK BUILDER & GAME RULES
# ==========================================
def create_deck():
    deck = []
    for c in COLORS:
        deck.append(Card(c, 0))
        for v in VALUES[1:]:
            deck.append(Card(c, v))
            deck.append(Card(c, v))
    for _ in range(4):
        deck.append(Card("Wild", "Wild"))
        deck.append(Card("Wild", "Draw Four"))
    
    shuffle_list(deck)
    return deck


def can_play(card, top_card, active_color):
    if card.color == "Wild" or card.color == active_color:
        return True
    if card.value == top_card.value:
        return True
    return False


def get_text_color(color_name):
    if color_name == "Red": return Color.RED
    elif color_name == "Yellow": return Color.YELLOW
    elif color_name == "Green": return Color.GREEN
    elif color_name == "Blue": return Color.BLUE
    elif color_name == "Wild": return Color.PURPLE
    return Color.WHITE


def wait_for_check():
    """Waits for physical Check button press or screen touch tap."""
    while True:
        try:
            if hasattr(brain, "buttonCheck") and brain.buttonCheck.pressing():
                break
        except Exception:
            pass
        try:
            if brain.screen.pressing():
                break
        except Exception:
            pass
        wait(50, MSEC)

    while True:
        pressed = False
        try:
            if hasattr(brain, "buttonCheck") and brain.buttonCheck.pressing():
                pressed = True
        except Exception:
            pass
        try:
            if brain.screen.pressing():
                pressed = True
        except Exception:
            pass
        if not pressed:
            break
        wait(20, MSEC)


# ==========================================
# INITIAL TOP CARD SELECTOR
# ==========================================
def select_initial_top_card():
    """Allows user to set the table's initial top card and attack state."""
    # Step 1: Select Color
    c_idx = 0
    while True:
        try:
            brain.screen.set_fill_color(Color.BLACK)
            brain.screen.clear_screen()
            brain.screen.set_pen_color(Color.WHITE)
            brain.screen.set_cursor(1, 1)
            brain.screen.print("SET TOP CLR:")

            c_name = COLORS[c_idx]
            brain.screen.set_pen_color(get_text_color(c_name))
            brain.screen.set_cursor(2, 1)
            brain.screen.print(c_name.upper()[:12])

            brain.screen.set_pen_color(Color.YELLOW)
            brain.screen.set_cursor(4, 1)
            brain.screen.print("TAP=NEXT")
            brain.screen.set_cursor(5, 1)
            brain.screen.print("CHK=CONFIRM")
        except Exception:
            pass

        while True:
            t_pressed = False
            c_pressed = False
            try:
                if brain.screen.pressing(): t_pressed = True
            except Exception: pass
            try:
                if hasattr(brain, "buttonCheck") and brain.buttonCheck.pressing(): c_pressed = True
            except Exception: pass

            if t_pressed or c_pressed: break
            wait(50, MSEC)

        if c_pressed:
            while hasattr(brain, "buttonCheck") and brain.buttonCheck.pressing(): wait(20, MSEC)
            selected_color = COLORS[c_idx]
            break

        if t_pressed:
            while brain.screen.pressing(): wait(20, MSEC)
            c_idx = (c_idx + 1) % len(COLORS)

    # Step 2: Select Card Type (NUMBER, +2 ATK, +4 ATK)
    t_idx = 0
    while True:
        try:
            brain.screen.set_fill_color(Color.BLACK)
            brain.screen.clear_screen()
            brain.screen.set_pen_color(Color.WHITE)
            brain.screen.set_cursor(1, 1)
            brain.screen.print("SET TOP TYPE:")

            t_name = TYPES[t_idx]
            brain.screen.set_cursor(2, 1)
            brain.screen.print(t_name[:12])

            brain.screen.set_pen_color(Color.YELLOW)
            brain.screen.set_cursor(4, 1)
            brain.screen.print("TAP=NEXT")
            brain.screen.set_cursor(5, 1)
            brain.screen.print("CHK=START")
        except Exception:
            pass

        while True:
            t_pressed = False
            c_pressed = False
            try:
                if brain.screen.pressing(): t_pressed = True
            except Exception: pass
            try:
                if hasattr(brain, "buttonCheck") and brain.buttonCheck.pressing(): c_pressed = True
            except Exception: pass

            if t_pressed or c_pressed: break
            wait(50, MSEC)

        if c_pressed:
            while hasattr(brain, "buttonCheck") and brain.buttonCheck.pressing(): wait(20, MSEC)
            selected_type = TYPES[t_idx]
            break

        if t_pressed:
            while brain.screen.pressing(): wait(20, MSEC)
            t_idx = (t_idx + 1) % len(TYPES)

    # Convert selection into Card object & attack penalty
    if selected_type == "+2 ATK":
        return Card(selected_color, "Draw Two"), selected_color, 2
    elif selected_type == "+4 ATK":
        return Card("Wild", "Draw Four"), selected_color, 4
    else:
        return Card(selected_color, "Number"), selected_color, 0


# ==========================================
# CARD PICKER INTERFACE
# ==========================================
def select_card_to_put_down(playable_cards):
    """Allows cycling and choosing which card from the hand to put down."""
    idx = 0
    while True:
        card = playable_cards[idx]
        try:
            brain.screen.set_fill_color(Color.BLACK)
            brain.screen.clear_screen()

            brain.screen.set_pen_color(Color.WHITE)
            brain.screen.set_cursor(1, 1)
            brain.screen.print("PICK TO PLAY")

            brain.screen.set_pen_color(get_text_color(card.color))
            brain.screen.set_cursor(2, 1)
            brain.screen.print(("CARD:" + card.short_text())[:12])

            brain.screen.set_pen_color(Color.WHITE)
            brain.screen.set_cursor(3, 1)
            brain.screen.print(("OPT " + str(idx+1) + "/" + str(len(playable_cards)))[:12])

            brain.screen.set_pen_color(Color.YELLOW)
            brain.screen.set_cursor(4, 1)
            brain.screen.print("TAP=NEXT")
            brain.screen.set_cursor(5, 1)
            brain.screen.print("CHK=PUT DOWN")
        except Exception:
            pass

        while True:
            t_pressed = False
            c_pressed = False
            try:
                if brain.screen.pressing(): t_pressed = True
            except Exception: pass
            try:
                if hasattr(brain, "buttonCheck") and brain.buttonCheck.pressing(): c_pressed = True
            except Exception: pass

            if t_pressed or c_pressed: break
            wait(50, MSEC)

        if c_pressed:
            while hasattr(brain, "buttonCheck") and brain.buttonCheck.pressing(): wait(20, MSEC)
            return card

        if t_pressed:
            while brain.screen.pressing(): wait(20, MSEC)
            idx = (idx + 1) % len(playable_cards)


# ==========================================
# MAIN ROBOT PROGRAM
# ==========================================
def run_robot():
    deck = create_deck()
    
    # 1. Deal 7 random cards to itself
    hand = [deck.pop() for _ in range(7)]

    # ------------------------------------------
    # STEP 1: DISPLAY 7 DRAWN CARDS
    # ------------------------------------------
    try:
        brain.screen.set_fill_color(Color.BLACK)
        brain.screen.clear_screen()

        brain.screen.set_pen_color(Color.WHITE)
        brain.screen.set_cursor(1, 1)
        brain.screen.print("START HAND:")

        row2 = hand[0].short_text() + " " + hand[1].short_text() + " " + hand[2].short_text()
        brain.screen.set_cursor(2, 1)
        brain.screen.print(row2[:12])

        row3 = hand[3].short_text() + " " + hand[4].short_text() + " " + hand[5].short_text()
        brain.screen.set_cursor(3, 1)
        brain.screen.print(row3[:12])

        row4 = "7:" + hand[6].short_text()
        brain.screen.set_cursor(4, 1)
        brain.screen.print(row4[:12])

        brain.screen.set_pen_color(Color.YELLOW)
        brain.screen.set_cursor(5, 1)
        brain.screen.print("PRESS CHECK")
    except Exception:
        pass

    wait_for_check()

    # ------------------------------------------
    # STEP 2: USER SELECTS INITIAL TOP CARD
    # ------------------------------------------
    top_card, active_color, pending_draws = select_initial_top_card()
    last_action = "START"

    # ------------------------------------------
    # STEP 3: MAIN GAME LOOP
    # ------------------------------------------
    while True:
        # Clear screen to black background
        try:
            brain.screen.set_fill_color(Color.BLACK)
            brain.screen.clear_screen()
        except Exception:
            pass

        # Line 1: Hand count (White text)
        try:
            brain.screen.set_pen_color(Color.WHITE)
            brain.screen.set_cursor(1, 1)
            brain.screen.print(("HAND:" + str(len(hand)))[:12])
        except Exception:
            pass

        # Line 2: Top Card (Color matching card)
        try:
            brain.screen.set_pen_color(get_text_color(top_card.color))
            brain.screen.set_cursor(2, 1)
            brain.screen.print(("TOP:" + top_card.short_text())[:12])
        except Exception:
            pass

        # Line 3: Active Color (Color matching active color)
        try:
            brain.screen.set_pen_color(get_text_color(active_color))
            brain.screen.set_cursor(3, 1)
            brain.screen.print(("CLR:" + active_color[:3].upper())[:12])
        except Exception:
            pass

        # Line 4: Action Status / Attack Warning
        try:
            if pending_draws > 0:
                brain.screen.set_pen_color(Color.RED)
                brain.screen.set_cursor(4, 1)
                brain.screen.print(("ATK:+" + str(pending_draws))[:12])
            else:
                brain.screen.set_pen_color(Color.WHITE)
                brain.screen.set_cursor(4, 1)
                brain.screen.print(("ACT:" + last_action[:7])[:12])
        except Exception:
            pass

        # Line 5: Check Button Prompt (Yellow text)
        try:
            brain.screen.set_pen_color(Color.YELLOW)
            brain.screen.set_cursor(5, 1)
            brain.screen.print("PRESS CHECK")
        except Exception:
            pass

        wait_for_check()

        # ==========================================
        # ATTACK HANDLING (+2 / +4 DIRECT DRAW)
        # ==========================================
        if pending_draws > 0:
            take_count = pending_draws
            last_action = "TAKE +" + str(take_count)

            try:
                brain.screen.set_fill_color(Color.BLACK)
                brain.screen.clear_screen()
                brain.screen.set_pen_color(Color.RED)
                brain.screen.set_cursor(1, 1)
                brain.screen.print(("TAKE +" + str(take_count))[:12])
                brain.screen.set_cursor(2, 1)
                brain.screen.print("DRAWING...")
                brain.screen.set_cursor(3, 1)
                brain.screen.print("MOVING WHS")
            except Exception:
                pass

            # Drive wheels to take penalty cards
            drive_wheels()

            for _ in range(take_count):
                if deck:
                    hand.append(deck.pop())

            pending_draws = 0

        else:
            # ==========================================
            # NORMAL TURN: PICK & PUT DOWN CARD
            # ==========================================
            playable = [c for c in hand if can_play(c, top_card, active_color)]

            if playable:
                chosen_card = select_card_to_put_down(playable)
                
                hand.remove(chosen_card)
                top_card = chosen_card

                if str(chosen_card.value) == "Draw Two":
                    pending_draws = 2
                    last_action = "ATK +2"
                elif str(chosen_card.value) == "Draw Four":
                    pending_draws = 4
                    last_action = "ATK +4"
                else:
                    last_action = "PUT " + chosen_card.short_text()

                active_color = random.choice(COLORS) if chosen_card.color == "Wild" else chosen_card.color
            else:
                last_action = "DRAWING"

                try:
                    brain.screen.set_fill_color(Color.BLACK)
                    brain.screen.clear_screen()
                    brain.screen.set_pen_color(Color.WHITE)
                    brain.screen.set_cursor(1, 1)
                    brain.screen.print("NO MATCH")
                    brain.screen.set_cursor(2, 1)
                    brain.screen.print("DRAWING...")
                    brain.screen.set_cursor(3, 1)
                    brain.screen.print("MOVING WHS")
                except Exception:
                    pass

                drive_wheels()

                if deck:
                    drawn = deck.pop()
                    hand.append(drawn)
                    last_action = "DREW " + drawn.short_text()

        # Win Condition
        if len(hand) == 0:
            try:
                brain.screen.set_fill_color(Color.BLACK)
                brain.screen.clear_screen()
                brain.screen.set_pen_color(Color.GREEN)
                brain.screen.set_cursor(2, 1)
                brain.screen.print("ROBOT WINS!")
                brain.screen.set_cursor(3, 1)
                brain.screen.print("UNO!")
            except Exception:
                pass
            break


run_robot()