from UI_interactions import loading_animation;

class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self, drink):
        """Returns the total calculated from coins inserted."""
        print(f"Please insert coins for {drink.name}.\n{drink.name} costs [ {self.CURRENCY}{drink.cost} ]")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"\nPayment in {coin} \nNote: [1 {coin} = {self.COIN_VALUES[coin]} ]?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost,drink):
        """Returns True when payment is accepted, or False if insufficient."""

        if self.money_received >= cost:
            loading_animation('verifying transaction ',1.5);
            change = round(self.money_received - cost, 2)
            if change > 0:
                loading_animation('handling change ', 1);
                print(f"Here is {self.CURRENCY}{change} in change.")

            self.profit += cost
            self.money_received = 0
            return True
        else:
            loading_animation('error detected', 2);
            print("Sorry that's not enough money. Money refunded.")
            print(f"Sorry that's not enough money, you spent {self.money_received}, which is less than {cost}.\nInvalid Transaction\nMoney Refunded.");
            self.money_received = 0
            return False
