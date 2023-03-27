from utils import clear_terminal


class coffeeMachine():
    def __init__(self) -> None:
        self.water = 300
        self.milk = 300
        self.coffee = 300
        self.money = 20

        self.coffee_resources = {
            "Espresso": {"water": 50, "coffee": 18, "milk": 0, "price": 1.50},
            "Latte": {"water": 200, "coffee": 24, "milk": 150, "price": 2.50},
            "Cappuccino": {"water": 250, "coffee": 24, "milk": 100, "price": 3.00}
        }

    def options(self):
        print("Select your option:")
        print("1. Order Coffee")
        print("2. Report")
        print("3. Fill-Up Water")
        print("4. Fill-Up Milk")
        print("5. Fill-Up Coffee")
        print("6. Turn Off")
        choice = input("> ")

        if choice == '1':
            self.order_coffee()
        if choice == '2':
            self.report()
        elif choice == '3':
            self.fill_up_water()
        elif choice == '4':
            self.fill_up_milk()
        elif choice == '5':
            self.fill_up_coffee()
        elif choice == '6':
            return False

        return True

    def report(self):
        clear_terminal()
        print("REPORT")
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: {self.water}€\n")

    def fill_up_water(self):
        self.water = 200
        clear_terminal()
        print("Water was filled up\n")

    def fill_up_milk(self):
        self.milk = 200
        clear_terminal()
        print("Milk was filled up\n")

    def fill_up_coffee(self):
        self.coffee = 200
        clear_terminal()
        print("Coffee was filled up\n")

    def order_coffee(self):
        clear_terminal()
        print("Choose your coffee")
        print("1. Espresso  1.50€")
        print("2. Latte  2.50€")
        print("3. Cappuccino  3.00€")
        coffee_type = input("> ")

        if coffee_type == '1':
            coffee_type = "Espresso"
        elif coffee_type == '2':
            coffee_type = "Latte" 
        elif coffee_type == '3':
            coffee_type = "Cappuccino"

        valid_coffee_resources = self.check_coffee_resources(coffee_type)
        if not valid_coffee_resources:
            clear_terminal()
            print("Not enough resources\n")
            return
        
        print("Enter your money")
        money = float(input("> "))

        if money < self.coffee_resources[coffee_type]["price"]:
            clear_terminal()
            print("Not enough money\n")
            return

        clear_terminal()
        print(f"Here is your {coffee_type}\n")
        self.deduct_coffee_resources(coffee_type)

    def check_coffee_resources(self, coffee_type: str) -> bool:
        if (self.water >= self.coffee_resources[coffee_type]["water"] 
            and self.milk >= self.coffee_resources[coffee_type]["milk"] 
            and self.coffee >= self.coffee_resources[coffee_type]["coffee"]):
            return True
        
        return False

    def deduct_coffee_resources(self, coffee_type):
        self.water -= self.coffee_resources[coffee_type]["water"]
        self.milk -= self.coffee_resources[coffee_type]["milk"]
        self.coffee -= self.coffee_resources[coffee_type]["coffee"]

    

