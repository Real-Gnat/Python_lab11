from woodworkingmachine.models.WoodWorkingMachine import WoodWorkingMachine


class RamusMachine(WoodWorkingMachine):
    def __init__(self, name, appointment, power, volume, processing):
        super().__init__(name, appointment, power, volume)
        self.processing = processing

    def name(self):
        return "RamusMachine"