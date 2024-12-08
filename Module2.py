import os
import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power, attack_bonus=0):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.attack_bonus = attack_bonus
        

    def attack(self, opponent):
        def get_random_value_in_range(number):
            lower_bound = 0.8 * number  # 80% of the number
            upper_bound = 0.9 * number  # 90% of the number
            return random.randint(int(lower_bound), int(upper_bound))

    # Calculate damage as a random value between 80% and 90% of the attack power
        random_value = get_random_value_in_range(self.attack_power)
    
    # Add attack_bonus to the final damage
        trueattack = random_value + self.attack_bonus
    
    # Deal damage to the opponent
        opponent.health -= trueattack
    
        print(f"{self.name} attacks {opponent.name} for {trueattack} damage!")  # Display the damage dealt
        self.attack_bonus = 0  # Reset the attack bonus after the attack
    
    # Check if the opponent is defeated
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    # Add your heal method here
    def regenerate(self):
        self.health += 15  # Increase health by 15
    
    # Ensure health doesn't exceed max health
        if self.health > self.max_health:
            self.health = self.max_health  # Reset to max health if it exceeds
    
        print(f"{self.name} has been healed... Health at {self.health}/{self.max_health}")
        if self.health == self.max_health:
            print(f"{self.name} has been healed to full health!")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, attack_bonus=0)  # Boost health and attack power

    # Add your power attack method here
    def Warrior_Cry(self, opponent):
        if self.attack_bonus >= 15:
            print("Nice try, cant stack buffs, try again")
        else:
            self.attack_bonus = 15
            print("Your Warrior cry channels the power of your ancestors!")
            
    def Lions_Claw(self, opponent):
        opponent.health -= self.attack_bonus + 50
        print("You jump forward bringing your sword down infront of you in an arcing slice")
            


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    def Meteorite_of_Astel(self, opponent):
        opponent.health -= self.attack_bonus + 50
        print("With the gifted power of the Naturalborn of Stars \nYou bring down: Meteorite of Astel")
        
    def Siphon(self, opponent):
        opponent.health -= 15
        self.health += 15
        print("With the cursed Knowledge of the Hemomancers \n You siphon 15 health from your enemy")
    
    
    
    # Add your cast spell method here
    
class Shadow_Monarch(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=40, attack_bonus=0)  # Boost health and attack power
        
    def Bloodlust(self, opponent):
        opponent.health -= 25
        self.health += 25
        print("Ability Activated BloodLust: \nYour Attack Deals 25 Damage and Heals You") 
        
    def Monarchs_Domain(self, opponent):
        self.attack_bonus += 20
        print("Monarch's Domain: Your Strength is permanently increased by 50%")      
        

    # Add your power attack method here

class Berserker(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=50, attack_bonus=0)
    
    def Indominable_Will(self, opponent):
        self.attack_bonus += 20
        print("The Strugglers Will: Boost your attack by 20")
        
    def Quick_Slash(self, opponent):
        opponent.health -= self.attack_bonus + 70
        print("With Haste You Bring Your Mighty Heap of Iron Down on Your Foes!")
    
        
        

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Shadow Monarch")  # Add Archer
    print("4. Berserker")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Shadow_Monarch(name)
    elif class_choice == '4':
        return Berserker(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def main():
    # Character creation phase
    global player
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)
    

def speciallist(wizard):
    os.system('cls')  # Clears the screen
    
    # Handle special abilities for the Warrior
    if isinstance(player, Warrior):
        print("Choose your special ability: \n1: Warrior Cry \n2: Lion's Claw")
        choice = input("--> ")
        if choice == '1':
            player.Warrior_Cry(wizard)  # Activate Warrior Cry
        elif choice == '2':
            player.Lions_Claw(wizard)  # Use Lion's Claw
        else:
            print("Invalid choice! Please select 1 or 2.")
    elif isinstance(player, Mage):
        print("Choose your special ability: \n1: Meteorite of Astel \n2: Siphon")
        choice = input("--> ")
        if choice == '1':
            player.Meteorite_of_Astel(wizard)  
        elif choice == '2':
            player.Siphon(wizard)  
        else:
            print("Invalid choice! Please select 1 or 2.")
    elif isinstance(player, Shadow_Monarch):
        print("Choose your special ability: \n1: BloodLust \n2: Monarch's Domain")
        choice = input("--> ")
        if choice == '1':
            player.Bloodlust(wizard)  
        elif choice == '2':
            player.Monarchs_Domain(wizard)  
        else:
            print("Invalid choice! Please select 1 or 2.")
    elif isinstance(player, Berserker):
        print("Choose your special ability: \n1: Indominable Will \n2: Quickslash")
        choice = input("--> ")
        if choice == '1':
            player.Indominable_Will(wizard) 
        elif choice == '2':
            player.Quick_Slash(wizard)  
        else:
            print("Invalid choice! Please select 1 or 2.")
# Battle function with user menu for actions

def displaygamestats(player, wizard):
    print(f"{player.name}'s Stats".ljust(20) + f"{wizard.name}'s Stats")
    print(f"Health: {player.health}/{player.max_health}".ljust(20) + f"Health: {wizard.health}/{wizard.max_health}")
    print(f"Attack Power: {player.attack_power}".ljust(20) + f"Attack Power: {wizard.attack_power}")
    print(f"Attack Bonus: {player.attack_bonus}".ljust(20) + f"Attack Bonus: {wizard.attack_bonus}")

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        os.system("cls")
        displaygamestats(player, wizard)
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")

        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
            input("press any key to continue")
        elif choice == '2':
            speciallist(wizard)
            pass
        elif choice == '3':
            player.regenerate()
            pass  # Implement this
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)
            input("press any key to continue")

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game

if __name__ == "__main__":
    main()