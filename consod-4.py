import random
import time

# Rolls the dice
def Dice_Roll():
    """Rolls a single six-sided dice"""
    return random.randint(1, 6)

def player_turn():
    """Plays a single turn of the game"""
    # Start the timer for the game
    start_time = time.time()

    # Roll three dice
    dice = [Dice_Roll(), Dice_Roll(), Dice_Roll()]
    print(f"Initial roll: {dice}")

    # Check dice for pairs or triples
    counts = {die: dice.count(die) for die in set(dice)}
    fixed = [die for die, count in counts.items() if count > 1]

    # If the player rolled three of the same number, cancel out the roll
    if len(fixed) == 1 and counts[fixed[0]] == 3:
        print(f"Tupled out due to three {fixed[0]}s! No points gained this round.")
        return 0

    # Dice that cannot be rerolled (fixed dice)
    if fixed:
        print(f"Fixed dice (cannot be re-rolled): {fixed}")
    
    for i in range(2):  # Allow rerolling twice
        rolldices_indices = [i for i, die in enumerate(dice) if die not in fixed]
        if not rolldices_indices:  # If no dice can be rerolled, break
            break
        
        # Ask player if they want to reroll the dice in certain positions
        reroll = input(f"Would you like to reroll the dice in the positions {rolldices_indices}? (y/n): ").lower()
        if reroll == 'y':
            for index in rolldices_indices:
                dice[index] = Dice_Roll()  # Reroll the dice
            print(f"Reroll {i+1}: {dice}")

            # Check if the player tupled out (three of the same number)
            counts = {die: dice.count(die) for die in set(dice)}
            if any(count >= 3 for count in counts.values()):
                print("Tupled out! No points gained this round.")
                return 0

    # Calculate the points
    score = sum(dice)
    print(f"Player stops with dice {dice} for a total score of {score} points.")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken for this turn: {elapsed_time:.2f} seconds.")
    return score

# Run the game
Score_Value = 0
# The game clock starts running
start_gametimer = time.time()

# Loop for player turns
while input("Play the turn (y/n): ").lower() == 'y':
    Score_Value += player_turn()
    print(f"Total score: {Score_Value}")

# The game clock ends
end_gametimer = time.time()
total_gametime = end_gametimer - start_gametimer
print("GAME OVER!!!!!")
print(f"Total game duration: {total_gametime:.2f} seconds.")

