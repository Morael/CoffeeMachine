class CoffeeMachine:
    def __init__(self):
        self.machine_has = {"water": 400, "milk": 540, "coffee beans": 120, "disposable cups": 9, "money": 550}
        self.espresso_needs = {"water": 250, "milk": 0, "coffee beans": 16, "disposable cup": 1, "cost": 4}
        self.latte_needs = {"water": 350, "milk": 75, "coffee beans": 20, "disposable cup": 1, "cost": 7}
        self.cappuccino_needs = {"water": 200, "milk": 100, "coffee beans": 12, "disposable cup": 1, "cost": 6}
        self.action_choice()

    def user_input(self):
        user_input = input()
        return user_input

    def display_machine_content(self):
        print(f"The coffee machine has: \n"
               f"{str(self.machine_has['water'])} of water\n"
               f"{str(self.machine_has['milk'])} of milk\n"
               f"{str(self.machine_has['coffee beans'])} of coffee beans\n"
               f"{str(self.machine_has['disposable cups'])} of disposable cups\n"
               f"${str(self.machine_has['money'])} of money")
        self.action_choice()

    def action_choice(self):
        print("\nWrite action (buy, fill, take, remaining, exit):")
        action = str(input())
        print("")
        if action == "buy":
            self.buy_menu()
        elif action == "fill":
            self.fill_machine()
        elif action == "take":
            self.take_money()
        elif action == "remaining":
            self.display_machine_content()
        elif action == "exit":
            global TURN_ON
            TURN_ON = False
        else:
            print("Unrecognized command. Try again.")
            self.action_choice()

    def buy_menu(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = self.user_input()
        if choice == "1":
            if self.check_availability(choice):
                self.machine_has["water"] -= self.espresso_needs["water"]
                self.machine_has["milk"] -= self.espresso_needs["milk"]
                self.machine_has["coffee beans"] -= self.espresso_needs["coffee beans"]
                self.machine_has["disposable cups"] -= self.espresso_needs["disposable cup"]
                self.machine_has["money"] += self.espresso_needs["cost"]
                print("I have enough resources, making you a coffee!")
                self.action_choice()
            else:
                print("Sorry, not enough water!\n")
        elif choice == "2":
            if self.check_availability(choice):
                self.machine_has["water"] -= self.latte_needs["water"]
                self.machine_has["milk"] -= self.latte_needs["milk"]
                self.machine_has["coffee beans"] -= self.latte_needs["coffee beans"]
                self.machine_has["disposable cups"] -= self.latte_needs["disposable cup"]
                self.machine_has["money"] += self.latte_needs["cost"]
                print("I have enough resources, making you a coffee!")
                self.action_choice()
            else:
                print("Sorry, not enough water!\n")
                self.action_choice()
        elif choice == "3":
            if self.check_availability(choice):
                self.machine_has["water"] -= self.cappuccino_needs["water"]
                self.machine_has["milk"] -= self.cappuccino_needs["milk"]
                self.machine_has["coffee beans"] -= self.cappuccino_needs["coffee beans"]
                self.machine_has["disposable cups"] -= self.cappuccino_needs["disposable cup"]
                self.machine_has["money"] += self.cappuccino_needs["cost"]
                print("I have enough resources, making you a coffee!")
                self.action_choice()
            else:
                print("Sorry, not enough water!")
                self.action_choice()
        else:
            print("Unrecognized command. Try again.")
            self.action_choice()

    def check_availability(self, choice):
        if choice == "1":
            for i in self.machine_has:
                if self.machine_has[i] >= self.espresso_needs[i]:
                    return True
                else:
                    return False
        if choice == "2":
            for i in self.machine_has:
                if self.machine_has[i] >= self.latte_needs[i]:
                    return True
                else:
                    return False
        if choice == "3":
            for i in self.machine_has:
                if self.machine_has[i] >= self.latte_needs[i]:
                    return True
                else:
                    return False

    def fill_machine(self):
        print("Write how many ml of water do you want to add:")
        add_water = abs(int(self.user_input()))
        self.machine_has["water"] += add_water
        print("Write how many ml of milk do you want to add:")
        add_milk = abs(int(self.user_input()))
        self.machine_has["milk"] += add_milk
        print("Write how many grams of coffee beans do you want to add:")
        add_coffee_bns = abs(int(self.user_input()))
        self.machine_has["coffee beans"] += add_coffee_bns
        print("Write how many disposable cups do you want to add:")
        add_cups = abs(int(self.user_input()))
        self.machine_has["disposable cups"] += add_cups
        self.action_choice()

    def take_money(self):
        print("I gave you $" + str(self.machine_has["money"]))
        self.machine_has["money"] = 0
        self.action_choice()


TURN_ON = True

while TURN_ON:
    take = CoffeeMachine()
