class Manager:
    def __init__(self, machines_list):
        self.machines_list = machines_list

    def sort_machines_list_by_volume(self, reverse):
        return sorted(self.machines_list, key=lambda machines: machines.volume, reverse=reverse)

    def sort_machines_list_by_power(self, reverse):
        return sorted(self.machines_list, key=lambda machines: machines.power, reverse=reverse)
    