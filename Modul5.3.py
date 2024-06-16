class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

Dom1 = Building(100, "Высокий дом")
Dom2 = Building(5, "Низкий дом")
Dom3 = Building(9, "Девятиэтажка")
Dom4 = Building(9, "Девятиэтажка")
print(Dom1 == Dom2)
print(Dom3 == Dom4)
