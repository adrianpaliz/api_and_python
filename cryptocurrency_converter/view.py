from cryptocurrency_converter import CURRENCIES

class View:
    def __init__(self):
        self.currency_from = ""
        self.currency_to = ""

    def ask(self):
        currency_from = input("Origin currency: ")
        while currency_from not in CURRENCIES:
            print("Currencies will be one of the following:")
            print(",".join(CURRENCIES))
            currency_from = input("Origin currency: ")
        
        self.currency_from = currency_from
            
        currency_to = input("Destination currency: ")
        while currency_to not in CURRENCIES:
            print("Currencies will be one of the following:")
            print(",".join(CURRENCIES))
            currency_from = input("Origin currency: ")

        self.currency_to = currency_to

    def show(self, rate):
        print("1 {} is {:.2f} {}".format(self.currency_from, rate, self.currency_to))
