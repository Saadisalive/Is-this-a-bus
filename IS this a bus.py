class Vechicle:

    def __init__(self, name ,max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class Bus(Vechicle):
    pass

School_bus = Bus("School Volvo",180, 12)
print("Vechicle Name :",School_bus.name,"speed",School_bus.max_speed,"Milage", School_bus.milage)