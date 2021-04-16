class CoffeeMachine:
    def __init__(self):
        self.supplies = [400, 540, 120, 9, 550]

    # what task to do
    def task(self):
        print("Write action (buy, fill, take, remaining, exit):")
        want = input()
        print()
        if want == "buy":
            self.buy(self.supplies)
        elif want == "fill":
            self.fill(self.supplies)
        elif want == "take":
            self.take(self.supplies)
        elif want == "remaining":
            self.remaining(self.supplies)
        elif want == "exit":
            return "stop"

    # gets what coffee they want to buy
    def buy(self, items):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee = input()
        needed = [0, 0, 0, 0]

        if coffee != "back":
            if coffee == "1":
                needed = [250, 0, 16, 4]
            elif coffee == "2":
                needed = [350, 75, 20, 7]
            elif coffee == "3":
                needed = [200, 100, 12, 6]

            if self.enough(self.supplies, needed):
                items[0] -= needed[0]
                items[1] -= needed[1]
                items[2] -= needed[2]
                items[3] -= 1
                items[4] += needed[3]
                print("I have enough resources, making you a coffee!")
                print()

    # tests if there is enough W M B
    def enough(self, items, wanted):
        if items[0] - wanted[0] < 0:
            print("Sorry, not enough water!")
            print()
        elif items[1] - wanted[1] < 0:
            print("Sorry, not enough milk!")
            print()
        elif items[2] - wanted[2] < 0:
            print("Sorry, not enough beans!")
            print()
        elif items[3] == 0:
            print("Sorry, not enough disposable cups!")
            print()
        else:
            return True

    # gets how much of W M B C they want to add
    def fill(self, items):
        print("Write how many ml of water do you want to add:")
        items[0] += int(input())
        print("Write how many ml of milk do you want to add:")
        items[1] += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        items[2] += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        items[3] += int(input())
        print()

    # takes money out of machine
    def take(self, coins):
        print("I gave you $" + str(coins[4]))
        coins[4] = 0
        print()

    # remaining
    def remaining(self, items):
        print("The coffee machine has:")
        print(items[0], "of water")
        print(items[1], "of milk")
        print(items[2], "of coffee beans")
        print(items[3], "of disposable cups")
        print("$" + str(items[4]) + " of money")
        print()


test = CoffeeMachine()
while test.task() != "stop":
    pass
