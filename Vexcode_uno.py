# VEXcode EXP - Uno Lab
# File Name: Uno_LastNames.py

import random
import time
from vex import *

# Initialize Brain
brain = Brain()

# Ensure motor objects exist if not configured in the VEXcode Devices panel
try:
    motor_1
except NameError:
    motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)

try:
    motor_5
except NameError:
    motor_5 = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)


# ==========================================
# TEACHER'S EVENT & MOTOR SETUP
# ==========================================

# Create new events
FWD = Event()
RT = Event()
LT = Event()

# FUNCTIONS -----------------
def available_command_reference():
    FWD.broadcast_and_wait()
    LT.broadcast_and_wait()
    RT.broadcast_and_wait()

def motor1_move_forward():
    motor_1.spin_for(FORWARD, 415, DEGREES, wait=False)
    print("motor1 FWD 415")

def motor5_move_forward():
    motor_5.spin_for(FORWARD, 415, DEGREES, wait=True)
    print("motor5 FWD 415")

def motor1_turn_right():
    motor_1.spin_for(FORWARD, 220, DEGREES, wait=False)
    print("motor1 FWD 220")

def motor5_turn_right():
    motor_5.spin_for(REVERSE, 220, DEGREES, wait=True)
    print("motor5 REV 220")

def motor1_turn_left():
    motor_1.spin_for(REVERSE, 220, DEGREES, wait=False)
    print("motor1 REV 220")

def motor5_turn_left():
    motor_5.spin_for(FORWARD, 220, DEGREES, wait=True)
    print("motor5 FWD 220")

# Register callback functions to the events
FWD(motor1_move_forward)
FWD(motor5_move_forward)
RT(motor1_turn_right)
RT(motor5_turn_right)
LT(motor1_turn_left)
LT(motor5_turn_left)
wait(15, MSEC)   # Wait to allow events to register


# ==========================================
# FULL-SCREEN CARD GRAPHICS
# ==========================================

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
    
    card = card_str[1:] if len(card_str) > 1 else card_str
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
            brain.screen.draw_line(72, 139, 72, 139)
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
            brain.screen.draw_circle(60+i, int(42+(i/2)), 30)
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
            brain.screen.draw_circle(80, 52, int(30-(i/5)))
        brain.screen.set_pen_color(Color.BLACK)
        for i in range(65):
            brain.screen.draw_circle(80, 52, int(31+(i/5)))
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
            brain.screen.draw_circle(60+i, int(42+(i/2)), 30)
        brain.screen.set_pen_color(Color.YELLOW)
        for i in range(5):
            brain.screen.draw_line(75, 50+i-5, 85, 50+i-5)
            brain.screen.draw_line(75, 50+i+5, 85, 50+i+5)
            brain.screen.draw_line(75, 50+i+5, 85, 50+i-5)

            brain.screen.draw_line(75, 50+i-15, 85, 50+i-15)
            brain.screen.draw_line(int(75+(i/2)), 50-15, int(75+(i/2)), 50-25)
            brain.screen.draw_line(int(83+(i/2)), 50-15, int(83+(i/2)), 50-25)
            brain.screen.draw_line(75, 50+i-25, 85, 50+i-25)

            brain.screen.draw_line(75, 50+i+15, 85, 50+i+15)
            brain.screen.draw_line(int(83+(i/2)), 50+15, int(83+(i/2)), 50+25)
            brain.screen.draw_line(75, 50+i+25, 85, 50+i+25)
            
    brain.screen.set_fill_color(Color.TRANSPARENT)

def render_card_by_name(card_name):
    """Maps text card names to the full screen renderer."""
    c_str = str(card_name)
    color_code = 'W'
    
    if "Red" in c_str: color_code = 'R'
    elif "Green" in c_str: color_code = 'G'
    elif "Blue" in c_str: color_code = 'B'
    elif "Yellow" in c_str: color_code = 'Y'
    
    if "Wild Draw 4" in c_str or c_str == "D4":
        draw_card_full_screen("D4", 'W')
    elif "Wild" in c_str or c_str == "W":
        draw_card_full_screen("W", 'W')
    elif "Draw 2" in c_str:
        draw_card_full_screen(color_code + "D2", color_code)
    elif "Skip" in c_str:
        draw_card_full_screen(color_code + "S", color_code)
    elif "Reverse" in c_str:
        draw_card_full_screen(color_code + "Rv", color_code)
    else:
        parts = c_str.split()
        val = parts[-1] if len(parts) > 1 else c_str
        draw_card_full_screen(color_code + val, color_code)

# ==========================================
# SCREEN & MENU HELPER FUNCTIONS
# ==========================================

def clear_screen():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

def set_card_color(card_text):
    card_str = str(card_text)
    if "Red" in card_str: brain.screen.set_pen_color(Color.RED)
    elif "Yellow" in card_str: brain.screen.set_pen_color(Color.YELLOW)
    elif "Green" in card_str: brain.screen.set_pen_color(Color.GREEN)
    elif "Blue" in card_str: brain.screen.set_pen_color(Color.BLUE)
    elif "Wild" in card_str: brain.screen.set_pen_color(Color.PURPLE)
    else: brain.screen.set_pen_color(Color.WHITE)

def wait_for_button_release():
    while brain.buttonLeft.pressing() or brain.buttonRight.pressing() or brain.buttonCheck.pressing():
        time.sleep(0.05)

def display_loading_screen():
    clear_screen()
    brain.screen.set_cursor(2, 3)
    brain.screen.set_pen_color(Color.RED)
    brain.screen.print("== UNO ==")
    brain.screen.set_cursor(4, 1)
    brain.screen.set_pen_color(Color.YELLOW)
    brain.screen.print("Loading Cards...")
    brain.screen.set_pen_color(Color.WHITE)

def select_option_menu(title, options):
    cursor = 0
    wait_for_button_release()
    
    while True:
        clear_screen()
        set_card_color(title)
        brain.screen.print(str(title)[:16])
        brain.screen.next_row()
        
        max_visible = 4
        start_idx = max(0, min(cursor - 1, len(options) - max_visible))
        end_idx = min(len(options), start_idx + max_visible)
        
        for idx in range(start_idx, end_idx):
            prefix = ">" if idx == cursor else " "
            brain.screen.set_pen_color(Color.WHITE)
            brain.screen.print(prefix)
            
            set_card_color(options[idx])
            brain.screen.print(str(options[idx])[:15])
            brain.screen.next_row()
            
        while not (brain.buttonLeft.pressing() or brain.buttonRight.pressing() or brain.buttonCheck.pressing()):
            time.sleep(0.05)
            
        if brain.buttonLeft.pressing():
            cursor = (cursor - 1) % len(options)
        elif brain.buttonRight.pressing():
            cursor = (cursor + 1) % len(options)
        elif brain.buttonCheck.pressing():
            wait_for_button_release()
            return options[cursor]
            
        wait_for_button_release()

# ==========================================
# DECK & GAME LOGIC
# ==========================================

def custom_shuffle(items):
    for i in range(len(items) - 1, 0, -1):
        j = random.randint(0, i)
        items[i], items[j] = items[j], items[i]

def create_uno_deck():
    colors = ['Red', 'Yellow', 'Green', 'Blue']
    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw 2']
    deck = []
    for color in colors:
        for val in values:
            deck.append(color + " " + str(val))
            if val != '0':
                deck.append(color + " " + str(val))
    for i in range(4):
        deck.append("Wild")
        deck.append("Wild Draw 4")
    custom_shuffle(deck)
    return deck

def draw_card(deck):
    if len(deck) > 0:
        return deck.pop(0)
    return None

def start_game(deck):
    hand = []
    for i in range(7):
        card = draw_card(deck)
        if card:
            hand.append(card)
    return hand

def handle_attack_menu(hand, deck):
    attacks = ["Draw 2", "Draw 4", "Skip", "Cancel"]
    chosen_attack = select_option_menu("Under Attack?", attacks)
    
    if chosen_attack == "Cancel":
        return
        
    if chosen_attack == "Skip":
        clear_screen()
        brain.screen.set_pen_color(Color.YELLOW)
        brain.screen.print("Turn Skipped!")
        time.sleep(1.5)
        return
        
    cards_to_draw = 2 if chosen_attack == "Draw 2" else 4
    defensive_cards = [c for c in hand if chosen_attack in c or "Wild Draw 4" in c]
    
    options = []
    if len(defensive_cards) > 0:
        options.append("Defend Card")
    options.append("Draw " + str(cards_to_draw) + " Cards")
    
    choice = select_option_menu("Attack Action:", options)
    
    if choice == "Defend Card":
        def_card = select_option_menu("Defend With:", defensive_cards)
        hand.remove(def_card)
        deliver_card_to_center(def_card)
    else:
        fetch_starting_cards()
        for _ in range(cards_to_draw):
            drawn = draw_card(deck)
            if drawn:
                hand.append(drawn)

def view_hand_screen(hand, deck):
    cursor = 0
    wait_for_button_release()
    
    while True:
        clear_screen()
        brain.screen.set_pen_color(Color.WHITE)
        brain.screen.print("Hand (" + str(len(hand)) + " cards):")
        brain.screen.next_row()
        
        items = ["Menu / Attack", "[ Ready / Play ]"] + hand
        max_visible = 3
        start_idx = max(0, min(cursor - 1, len(items) - max_visible))
        end_idx = min(len(items), start_idx + max_visible)
        
        for idx in range(start_idx, end_idx):
            prefix = "> " if idx == cursor else "  "
            brain.screen.set_pen_color(Color.WHITE)
            brain.screen.print(prefix)
            
            set_card_color(items[idx])
            brain.screen.print(str(items[idx])[:14])
            brain.screen.next_row()
            
        while not (brain.buttonLeft.pressing() or brain.buttonRight.pressing() or brain.buttonCheck.pressing()):
            time.sleep(0.05)
            
        if brain.buttonLeft.pressing():
            cursor = (cursor - 1) % len(items)
        elif brain.buttonRight.pressing():
            cursor = (cursor + 1) % len(items)
        elif brain.buttonCheck.pressing():
            wait_for_button_release()
            selected = items[cursor]
            if selected == "Menu / Attack":
                handle_attack_menu(hand, deck)
            elif selected == "[ Ready / Play ]":
                return
            
        wait_for_button_release()

def input_top_card_from_controller():
    colors = ['Red', 'Yellow', 'Green', 'Blue', 'Wild']
    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw 2']
    chosen_color = select_option_menu("Top Color:", colors)
    if chosen_color == "Wild":
        return "Wild"
    chosen_value = select_option_menu("Top Value:", values)
    return chosen_color + " " + chosen_value

def is_legal_play(card, top_card):
    if "Wild" in card or "Wild" in top_card:
        return True
    card_parts = card.split()
    top_parts = top_card.split()
    if card_parts[0] == top_parts[0]:
        return True
    if len(card_parts) > 1 and len(top_parts) > 1 and card_parts[1] == top_parts[1]:
        return True
    return False

def get_legal_cards(hand, top_card):
    return [card for card in hand if is_legal_play(card, top_card)]

# ==========================================
# ROBOT PHYSICAL MOTION SEQUENCES
# ==========================================

def robot_drive_blocks(blocks):
    """Drives forward by exact block/hand length count (1 block = 415 degrees)."""
    full_steps = int(blocks)
    for _ in range(full_steps):
        FWD.broadcast_and_wait()
    
    remainder = blocks - full_steps
    if remainder > 0:
        deg = int(415 * remainder)
        motor_1.spin_for(FORWARD, deg, DEGREES, wait=False)
        motor_5.spin_for(FORWARD, deg, DEGREES, wait=True)

def robot_turn_90(direction):
    if direction == "right":
        RT.broadcast_and_wait()
    else:
        LT.broadcast_and_wait()
    time.sleep(0.2)

def fetch_starting_cards():
    display_loading_screen()
    brain.play_sound(SoundType.FILLUP)
    
    # Move forward exactly 2.5 hand lengths
    robot_drive_blocks(2.5)
    
    # Turn 180 degrees
    robot_turn_90("right")
    robot_turn_90("right")
    
    # Drive back exactly 2.5 hand lengths
    robot_drive_blocks(2.5)

def deliver_card_to_center(card_played):
    render_card_by_name(card_played)
    brain.play_sound(SoundType.FILLUP)
    
    # Move forward exactly 2.5 hand lengths
    robot_drive_blocks(2.5)
        
    clear_screen()
    brain.screen.set_pen_color(Color.WHITE)
    brain.screen.print("Dropping Card...")
    
    # Turn 180 degrees
    robot_turn_90("right")
    robot_turn_90("right")
    
    # Drive back exactly 2.5 hand lengths
    robot_drive_blocks(2.5)

def perform_victory_dance():
    clear_screen()
    brain.screen.set_pen_color(Color.GREEN)
    brain.screen.set_cursor(2, 2)
    brain.screen.print("*** WINNER! ***")
    
    brain.play_sound(SoundType.TADA)
    time.sleep(0.4)
    brain.play_sound(SoundType.SIREN)
    time.sleep(0.4)
    
    colors = [Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE, Color.PURPLE]
    for step in range(4):
        brain.screen.set_pen_color(colors[step % len(colors)])
        clear_screen()
        brain.screen.set_cursor(2, 2)
        brain.screen.print("* VICTORY DANCE *")
        
        if step % 2 == 0:
            robot_turn_90("right")
        else:
            robot_turn_90("left")

# ==========================================
# MAIN EXECUTION
# ==========================================

def main():
    deck = create_uno_deck()
    hand = start_game(deck)
    
    fetch_starting_cards()

    while len(hand) > 0:
        view_hand_screen(hand, deck)
        top_card = input_top_card_from_controller()
        
        legal_cards = get_legal_cards(hand, top_card)
        options = legal_cards + ["Draw Card"]
        
        title_text = "Top: " + str(top_card)
        selected = select_option_menu(title_text, options)
        
        if selected == "Draw Card":
            clear_screen()
            brain.screen.print("[CARD BACK]")
            time.sleep(1)
            drawn = draw_card(deck)
            if drawn:
                hand.append(drawn)
        else:
            hand.remove(selected)
            if len(hand) == 1:
                brain.play_sound(SoundType.SIREN)
                clear_screen()
                brain.screen.set_pen_color(Color.RED)
                brain.screen.print("*** UNO! ***")
                time.sleep(1.2)
            deliver_card_to_center(selected)

    perform_victory_dance()

main()