from cryptocurrency_converter.model import Model
from cryptocurrency_converter.view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def run(self):
        self.view.ask()
        self.model.currency_from = self.view.currency_from
        self.model.currency_to = self.view.currency_to
        self.model.get_rate()
        self.view.show(self.model.rate)