import random

class ParkingLot:
    def __init__(self, size, spot_size=(8, 12)):
        self.size = size
        self.spot_size = spot_size
        self.num_spots = self.size // (spot_size[0] * spot_size[1])
        self.spots = [None] * self.num_spots
        
    def find_empty_spot(self):
        empty_spots = [i for i, spot in enumerate(self.spots) if spot is None]
        if empty_spots:
            return random.choice(empty_spots)
        else:
            return None
        
class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
        
    def __str__(self):
        return f"Car with license plate {self.license_plate}"
        
    def park(self, parking_lot, spot_num):
        if parking_lot.spots[spot_num] is None:
            parking_lot.spots[spot_num] = self
            print(f"{self} parked successfully in spot {spot_num}.")
            return True
        else:
            print(f"Spot {spot_num} is occupied. Trying another spot...")
            empty_spot = parking_lot.find_empty_spot()
            if empty_spot is not None:
                return self.park(parking_lot, empty_spot)
            else:
                print("Parking lot is full.")
                return False
            
def main(cars, parking_lot):
    random.shuffle(cars)
    for car in cars:
        empty_spot = parking_lot.find_empty_spot()
        if empty_spot is not None:
            car.park(parking_lot, empty_spot)
        else:
            print("Parking lot is full.")
            break

# Taking user input for parking lot size
parking_lot_size = int(input("Enter the size of the parking lot: "))

# Taking user input for car license plates
num_cars = int(input("Enter the number of cars: "))
car_license_plates = []
for i in range(num_cars):
    plate = input(f"Enter license plate for car {i + 1}: ")
    car_license_plates.append(plate)

cars = [Car(plate) for plate in car_license_plates]
parking_lot = ParkingLot(parking_lot_size, spot_size=(10, 12))
main(cars, parking_lot)

#sample input
#Enter the size of the parking lot: 2000
#Enter the number of cars: 4
#Enter license plate for car 1: ACE234
#3000Enter license plate for car 2: NMR546
#Enter license plate for car 3: KLE765
#Enter license plate for car 4: RIO632

#sample output
#Car with license plate RIO632 parked successfully in spot 3.
#Car with license plate KLE765 parked successfully in spot 8.
#Car with license plate NMR546 parked successfully in spot 13.
#Car with license plate ACE234 parked successfully in spot 2.