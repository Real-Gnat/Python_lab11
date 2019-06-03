from woodworkingmachine.models.WoodWorkingMachine import WoodWorkingMachine


class CirucularMachine(WoodWorkingMachine):
    def __init__(self, name, appointment, power, volume, classification, radius, sortie):
        super().__init__(name, appointment, power, volume)
        self.classification = classification
        self.radius = radius
        self.sortie = sortie

    def name(self):
        return "CircularMachine"