#Parking-Lot program 
import random
import json

class ParkingLot:
    def __init__(self, square_footage, spot_size=(8, 12)):
        self.square_footage = square_footage
        self.spot_size = spot_size
        self.total_spots = self.calculate_total_spots()
        self.parking_lot = [None] * self.total_spots
        self.parked_cars = {}

    def calculate_total_spots(self):
        spot_area = self.spot_size[0] * self.spot_size[1]
        return self.square_footage // spot_area

    def park_car(self, car, spot):
        if self.parking_lot[spot] is None:
            self.parking_lot[spot] = car
            self.parked_cars[car.license_plate] = spot
            return f"Car with license plate {car} parked successfully in spot {spot + 1}."
        else:
            return f"Car with license plate {car} cannot be parked in spot {spot + 1}. Spot already occupied."

    def map_to_json(self):
        mapping = {str(spot + 1): str(car) for spot, car in enumerate(self.parking_lot) if car is not None}
        return json.dumps(mapping, indent=2)

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return str(self.license_plate)

    def park(self, parking_lot):
        while True:
            spot = random.randint(0, parking_lot.total_spots - 1)
            status = parking_lot.park_car(self, spot)
            print(status)
            if "successfully" in status:
                break

def main():
    # Taking input from the user for parking lot size
    parking_lot_size = int(input("Enter the size of the parking lot (in square footage): "))

    # Taking input from the user for car license plates
    num_cars = int(input("Enter the number of cars: "))
    car_license_plates = []
    for i in range(num_cars):
        plate = input(f"Enter license plate for car {i + 1}: ")
        car_license_plates.append(plate)

    parking_lot = ParkingLot(square_footage=parking_lot_size)
    cars = [Car(plate) for plate in car_license_plates]

    while cars:
        car = cars.pop(0)
        car.park(parking_lot)

    print("\nParking Lot Mapping:")
    print(parking_lot.map_to_json())

if __name__ == "__main__":
    main()


#sample input:
#Enter the size of the parking lot (in square footage): 2000
#Enter the number of cars: 4
#Enter license plate for car 1: ACE234
#Enter license plate for car 2: NMR546
#Enter license plate for car 3: KLE765
#Enter license plate for car 4: RI0632

#sample output:
#Car with license plate ACE234 parked successfully in spot 19.
#Car with license plate NMR546 parked successfully in spot 10.
#Car with license plate KLE765 parked successfully in spot 12.
#Car with license plate RI0632 parked successfully in spot 20.

#Parking Lot Mapping:
#{
 # "10": "NMR546",
 # "12": "KLE765",
 # "19": "ACE234",
 # "20": "RI0632"
#}
