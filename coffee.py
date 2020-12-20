ingredients = [{'water':250, 'milk': 0, 'coffee': 16, 'cost': 4},{'water':350, 'milk': 75, 'coffee': 20, 'cost': 7},{'water':200, 'milk': 100, 'coffee': 12, 'cost': 6}]
class coffee_machine:
    water = None
    milk = None
    coffee = None
    cups = None
    money = None
    def __init__(self, w, m, f, c, n):
        self.water = w
        self.milk = m
        self.coffee = f
        self.cups = c
        self.money = n
        
        
    def operation(self):
        operations = ["buy", "fill", "take","remaining","exit"]
        while True:
            operation = input("Write action (buy, fill, take, remaining, exit): ")
            if operation in operations:
                if operation == "buy":
                    self.buy()
                elif operation == "fill":
                    self.fill()
                elif operation == "take":
                    self.take()
                elif operation == "remaining":
                    self.state()
                else:
                    break
                
    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if choice == "back":
            return
        elif 1 <= int(choice) <= 3:
            choice = int(choice)
            if self.water >= ingredients[choice - 1]["water"] and self.milk >= ingredients[choice - 1]["milk"] and self.coffee >= ingredients[choice - 1]["coffee"] and self.cups > 0:
                self.water -= ingredients[choice - 1]["water"]
                self.milk -= ingredients[choice - 1]["milk"]
                self.coffee -= ingredients[choice - 1]["coffee"]
                self.money += ingredients[choice - 1]["cost"]
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough water!")
    
    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))
        
    def take(self):
        print("I gave you {}".format(self.money))
        self.money = 0
        
    def state(self):
        print("""
The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
{} of money
""".format(self.water, self.milk, self.coffee, self.cups, self.money))

my_machine = coffee_machine(400, 540, 120, 9, 550)
my_machine.operation()
