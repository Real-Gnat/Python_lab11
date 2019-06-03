from woodworkingmachine.manager.Manager import Manager
from woodworkingmachine.models.WoodWorkingMachine import WoodWorkingMachine
from woodworkingmachine.models.ClassificationType import ClassificationType
from woodworkingmachine.models.CirucularMachine import CirucularMachine
from woodworkingmachine.models.MaterialType import MaterialType
from woodworkingmachine.models.ProcessingType import ProcessingType
from woodworkingmachine.models.RamusMachine import RamusMachine


def main():
    cirucularMachine = CirucularMachine("liniyka" , "painting",  70, 10, ClassificationType.PRESS_FORGING, 15, 35)
    ramusMachine = RamusMachine("procesing",  "fills in",  43, 20, ProcessingType.DRILL)

    machines = [cirucularMachine, ramusMachine]
    manager = Manager(machines)

    print(manager.sort_machines_list_by_power(True))
    print(manager.sort_machines_list_by_volume(True))

if __name__ == '__main__':
    main()