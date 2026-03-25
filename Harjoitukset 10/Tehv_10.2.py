
class Hissi:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f"kerros: {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"kerros: {self.current_floor}")

    def go_to_floor(self, floor):
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()

class Talo:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(number_of_elevators):
            elevator = Hissi(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_floor):
        print("Hissi", elevator_number, "menee kerrokseen", destination_floor)
        self.elevators[elevator_number -1].go_to_floor(destination_floor)


talo= Talo(1,10,3)

talo.run_elevator(1, 6)
talo.run_elevator(2, 3)
talo.run_elevator(3, 8)

print("Kaikkien hissien lähettäminen alimpaan kerrokseen")
talo.run_elevator(1, 1)
talo.run_elevator(2,1)
talo.run_elevator(3, 1)