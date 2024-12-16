import random
import time

#Rolls the dice
def Dice_Roll():
    """Rolls Single Sided Dice"""
    return random.randint(1, 6)

def player_turn():
    """Plays Single Turn Of Game"""
    #Start the timer for game
    start_time = time.time()

    dice = [Dice_Roll(), Dice_Roll(), Dice_Roll()]
    print(f"Intial roll: {dice}")

    
    #check die for pairs or triples
    counts = {die: dice.count(die) for die in set (dice)}
    fixed = [die for die, count in counts.items() if count > 1]

    if len (fixed) == 1 and counts[fixed[0]] == 3:
       print(f"Cancels out all dice {fixed[0]}s! Nothing gained this round")
       return 0

    #If The players rolls the same number with all three dice he/she tuples out
    if len(fixed) == 1 and counts [fixed[0]] == 3:
       print(f"Tuples out due to same number on each dice{fixed[0]} No Points gained this round.")
       return 0

    #Dice Cannot Be Fixed
    if fixed:
        print(f"Fixed dice(Cannot Be Re-rolled): {fixed}")
    
    for i in range(2):
        rolldices_indices = [i for i, die in enumerate(dice) if die not in fixed]
        if not rolldices_indices:
            break
        
        #See if Players tupled out
        reroll = input(f"Would you like to reroll in the positions {rolldices_indices}? (y/n): ").lower()
        if reroll == 'y':
            for index in rolldices_indices:
                dice[index] = Dice_Roll()
            print(f"Reroll {i+1}: {dice}")
        
            #See if Players tupled out
            counts = {die: dice.count(die) for die in set (dice)}
            if any(count >=3 for count in counts.values()):
                print("Tupled Out! No points gained this round.")
                return 0

    #calculate points
    score = sum(dice)
    print(f"Player stops with dice {dice} for a total score of {score} points.")
    end_time = time.time()
    elasped_time = end_time - start_time
    print(f"Time taken for this turn: {elasped_time:.2f} seconds.")
    return score

#Run A Game
Score_Value = 0
#The game clock starts running
start_gametimer = time.time()

while input("Play The Turn (y/n):").lower() == 'y':
    Score_Value += player_turn()
    print(f"Total score: {Score_Value}")

#The game clock ends
end_gametimer = time.time()
total_gametime = end_gametimer - start_gametimer
print("OVER!!!!!")
print(f"Total game duration: {total_gametime:.2f} seconds.")


