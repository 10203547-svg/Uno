# VEXcode EXP - Uno Lab
# File Name: Uno_LastNames.py[cite: 5]

import random
import time
from vex import *

# Initialize Brain
brain = Brain()

# ==========================================
# EVENT BROADCAST & MOTOR SETUP
# ==========================================

def motor1_move_forward():
    m1 = globals().get('motor_1') or globals().get('motor1')
    if m1 is not None:
        m1.spin_for(FORWARD, 425, DEGREES)
    print("motor1 FWD 425")

def motor5_move_forward():
    m5 = globals().get('motor_5') or globals().get('motor5')
    if m5 is not None:
        m5.spin_for(FORWARD, 425, DEGREES)
    print("motor5 FWD 425")

def motor1_turn_right():
    m1 = globals().get('motor_1') or globals().get('motor1')
    if m1 is not None:
        m1.spin_for(FORWARD, 220, DEGREES)
    print("motor1 FRW 220")

def motor5_turn_right():
    m5 = globals().get('motor_5') or globals().get('motor5')
    if m5 is not None:
        m5.spin_for(REVERSE, 220, DEGREES)
    print("motor5 RAV 220")

def motor1_turn_left():
    m1 = globals().get('motor_1') or globals().get('motor1')
    if m1 is not None:
        m1.spin_for(REVERSE, 220, DEGREES)
    print("motor1 RAV 220")

def motor5_turn_left():
    m5 = globals().get('motor_5') or globals().get('motor5')
    if m5 is not None:
        m5.spin_for(FORWARD, 220, DEGREES)
    print("motor5 FRW 220")

# Define Event objects to fix undefined variable errors[cite: 12]
FWD = Event()
RT = Event()
LT = Event()

# Register callback functions to events[cite: 12]
FWD(motor1_move_forward)
FWD(motor5_move_forward)
RT(motor1_turn_right)
RT(motor5_turn_right)
LT(motor1_turn_left)
LT(motor5_turn_left)
wait(15, MSEC)

# ==========================================
# COLOR & SCREEN HELPER FUNCTIONS
# ==========================================

def clear_screen():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)

def set_card_color(card_text):
    """Sets screen pen color matching card type."""
    card_str = str(card_text)
    if "Red" in card_str:
        brain.screen.set_pen_color(Color.RED)
    elif "Yellow" in card_str:
        brain.screen.set_pen_color(Color.YELLOW)
    elif "Green" in card_str:
        brain.screen.set_pen_color(Color.GREEN)
    elif "Blue" in card_str:
        brain.screen.set_pen_color(Color.BLUE)
    elif "Wild" in card_str:
        brain.screen.set_pen_color(Color.PURPLE)
    else:
        brain.screen.set_pen_color(Color.WHITE)

def wait_for_button_release():
    """Waits for all brain buttons to be released to prevent menu skipping."""
    while brain.buttonLeft.pressing() or brain.buttonRight.pressing() or brain.buttonCheck.pressing():
        time.sleep(0.05)

def display_loading_screen():
    """Displays UNO loading screen while robot moves to pick up cards[cite: 2, 4]."""
    clear_screen()
    brain.screen.set_cursor(2, 3)
    brain.screen.set_pen_color(Color.RED)
    brain.screen.print("== UNO ==")
    brain.screen.set_cursor(4, 1)
    brain.screen.set_pen_color(Color.YELLOW)
    brain.screen.print("Loading Cards...")
    brain.screen.set_pen_color(Color.WHITE)

def select_option_menu(title, options):
    """Scrollable menu fitted for 16-column by 8-row screens[cite: 4]."""
    cursor = 0
    wait_for_button_release()
    
    while True:
        clear_screen()
        
        # Row 1: Header printed in matching card color
        set_card_color(title)
        brain.screen.print(str(title)[:16])
        brain.screen.next_row()
        
        # Rows 2-7: Windowed slice of options for small screen
        max_visible = 5
        start_idx = max(0, min(cursor - 2, len(options) - max_visible))
        end_idx = min(len(options), start_idx + max_visible)
        
        for idx in range(start_idx, end_idx):
            prefix = ">" if idx == cursor else " "
            brain.screen.set_pen_color(Color.WHITE)
            brain.screen.print(prefix)
            
            set_card_color(options[idx])
            brain.screen.print(str(options[idx])[:15])
            brain.screen.next_row()
            
        # Blocking wait: Screen only refreshes on button press
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
# PHASE 1: SETUP UNO DECK & STARTING HAND
# ==========================================

def custom_shuffle(items):
    """Custom Fisher-Yates shuffle[cite: 8]."""
    for i in range(len(items) - 1, 0, -1):
        j = random.randint(0, i)
        items[i], items[j] = items[j], items[i]

def create_uno_deck():
    """Creates a full 108-card deck[cite: 5]."""
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
    """Deals starting hand of 7 cards[cite: 4]."""
    hand = []
    for i in range(7):
        card = draw_card(deck)
        if card:
            hand.append(card)
    return hand

def view_hand_screen(hand):
    """Interactive scroll screen letting you see all 7 cards in hand before starting[cite: 4]."""
    cursor = 0
    wait_for_button_release()
    
    while True:
        clear_screen()
        brain.screen.set_pen_color(Color.WHITE)
        brain.screen.print("Hand (" + str(len(hand)) + " cards):")
        brain.screen.next_row()
        
        # Display 5 scrollable cards at a time
        max_visible = 5
        start_idx = max(0, min(cursor, max(0, len(hand) - max_visible)))
        end_idx = min(len(hand), start_idx + max_visible)
        
        for idx in range(start_idx, end_idx):
            prefix = "> " if idx == cursor else "  "
            brain.screen.set_pen_color(Color.WHITE)
            brain.screen.print(prefix)
            
            set_card_color(hand[idx])
            brain.screen.print(str(hand[idx])[:14])
            brain.screen.next_row()
            
        brain.screen.set_pen_color(Color.WHITE)
        brain.screen.print("[Check = Start]")
        
        # Wait for button interaction
        while not (brain.buttonLeft.pressing() or brain.buttonRight.pressing() or brain.buttonCheck.pressing()):
            time.sleep(0.05)
            
        if brain.buttonLeft.pressing():
            cursor = (cursor - 1) % len(hand)
        elif brain.buttonRight.pressing():
            cursor = (cursor + 1) % len(hand)
        elif brain.buttonCheck.pressing():
            wait_for_button_release()
            return
            
        wait_for_button_release()

# ==========================================
# PHASE 2: CONTROLLER TOP CARD INPUT
# ==========================================

def input_top_card_from_controller():
    """Allows controller to select top card color and value[cite: 4]."""
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
    legal = []
    for card in hand:
        if is_legal_play(card, top_card):
            legal.append(card)
    return legal

# ==========================================
# PHASE 3 & 4: HARDWARE MOTION & SOUNDS
# ==========================================

def robot_drive_forward(units):
    """Triggers FWD event broadcast for physical motors[cite: 3, 12]."""
    print("Robot driving forward " + str(units) + " units...")
    FWD.broadcast()
    time.sleep(1)

def robot_turn_90(direction):
    """Triggers RT or LT event broadcast for physical turns[cite: 3, 12]."""
    print("Robot turning 90 degrees " + str(direction) + "...")
    if direction == "right":
        RT.broadcast()
    else:
        LT.broadcast()
    time.sleep(1)

def fetch_starting_cards():
    """Displays loading screen and drives to center to pick up 7 cards[cite: 2, 3, 4]."""
    display_loading_screen()
    brain.play_sound(SoundType.FILLUP)
    
    # Drive FRONT to pickup center[cite: 3]
    robot_drive_forward(2)
    time.sleep(0.3)
    
    # TURN, TURN around[cite: 3]
    robot_turn_90("right")
    time.sleep(0.2)
    robot_turn_90("right")
    time.sleep(0.3)
    
    # Drive FRONT back to player position[cite: 3]
    robot_drive_forward(2)
    time.sleep(0.3)
    
    # TURN, TURN back forward[cite: 3]
    robot_turn_90("right")
    time.sleep(0.2)
    robot_turn_90("right")
    time.sleep(0.3)

def display_card_back():
    """Shows card back graphic when drawing cards[cite: 2]."""
    clear_screen()
    brain.screen.set_cursor(3, 1)
    brain.screen.set_pen_color(Color.CYAN)
    brain.screen.print("[CARD BACK]")
    brain.screen.set_pen_color(Color.WHITE)

def deliver_card_to_center():
    """Drives forward to middle, turns 90 twice, and drives forward back to start[cite: 2, 3]."""
    clear_screen()  # Hide player hand while driving[cite: 2]
    brain.screen.set_pen_color(Color.WHITE)
    brain.screen.print("Delivering Card")
    
    # 1. Play delivery sound effect[cite: 2, 10]
    brain.play_sound(SoundType.FILLUP)
    
    # 2. Drive FRONT to middle[cite: 3]
    robot_drive_forward(2)
    time.sleep(0.3)
    
    # 3. TURN, TURN (180 degree turn around)[cite: 3]
    robot_turn_90("right")
    time.sleep(0.2)
    robot_turn_90("right")
    time.sleep(0.3)
    
    # 4. Drive FRONT back to player position[cite: 3]
    robot_drive_forward(2)
    time.sleep(0.3)
    
    # 5. TURN, TURN back to face forward again[cite: 3]
    robot_turn_90("right")
    time.sleep(0.2)
    robot_turn_90("right")
    time.sleep(0.3)

def play_uno_sound():
    brain.play_sound(SoundType.SIREN)

def play_win_sound():
    brain.play_sound(SoundType.TADA)

def perform_victory_dance():
    clear_screen()
    brain.screen.set_pen_color(Color.RED)
    brain.screen.set_cursor(3, 2)
    brain.screen.print("*** WINNER! ***")
    play_win_sound()
    
    # Physical victory dance motion[cite: 2]
    for _ in range(2):
        robot_turn_90("right")
        robot_turn_90("left")

# ==========================================
# MAIN GAME LOOP
# ==========================================

def main():
    # --- PHASE 1: SETUP, PICKUP & SCROLLABLE 7-CARD VIEW ---
    deck = create_uno_deck()
    hand = start_game(deck)
    
    # 1. Show UNO Loading Screen and drive to center to pick up 7 cards[cite: 2, 3, 4]
    fetch_starting_cards()
    
    # 2. Print hand to console and open interactive 7-card scroll view on brain screen[cite: 4]
    print("Starting Hand (7 cards):", hand)
    view_hand_screen(hand)

    # --- PHASE 2: TURN LOOP ---
    while len(hand) > 0:
        # Step 1: Input top card from controller[cite: 4]
        top_card = input_top_card_from_controller()
        
        # Step 2: Show legal play options[cite: 3]
        legal_cards = get_legal_cards(hand, top_card)
        options = legal_cards + ["Draw Card"]
        
        title_text = "Top: " + str(top_card)
        selected = select_option_menu(title_text, options)
        
        if selected == "Draw Card":
            display_card_back()
            time.sleep(1)
            drawn = draw_card(deck)
            if drawn:
                hand.append(drawn)
        else:
            hand.remove(selected)
            
            # Phase 4: UNO alert on 1 card remaining[cite: 2]
            if len(hand) == 1:
                play_uno_sound()
                clear_screen()
                brain.screen.set_pen_color(Color.RED)
                brain.screen.set_cursor(3, 3)
                brain.screen.print("*** UNO! ***")
                time.sleep(1.2)
                
            # Phase 3 & 4: Physical motor driving (Front -> Turn -> Turn -> Front)[cite: 2, 3]
            deliver_card_to_center()

    # Phase 4: Physical victory dance celebration[cite: 1, 2]
    perform_victory_dance()

main()