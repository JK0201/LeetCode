class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spot = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.spot[carType-1] == 0:
            return False

        else:
            self.spot[carType-1] -= 1
            return True