class WoodWorkingMachine:
    def __init__(self, name, appointment, power, volume):
        self.name = name
        self.appointment = appointment
        self.power = power
        self.volume = volume

    def __del__(self):
        print("Destructor")