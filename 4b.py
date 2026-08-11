class Car:
    def __init__(self, car_number):
        self.car_number = car_number
        self.next = None


class ParkingQueue:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, car_number):
        new_car = Car(car_number)

        if self.rear is None:
            self.front = self.rear = new_car
            return

        self.rear.next = new_car
        self.rear = new_car

  
    def dequeue(self):
        if self.front is None:
            return None

        car_number = self.front.car_number
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return car_number

   
    def peek(self):
        if self.front is None:
            return None

        return self.front.car_number


    def is_empty(self):
        return self.front is None


    def display(self):
        if self.is_empty():
            print("Parking area is empty.")
            return

        current = self.front
        print("Cars in parking queue:")

        while current:
            print(current.car_number, end=" -> ")
            current = current.next

        print("None")


parking = ParkingQueue()

while True:
    print("\n===== CAR PARKING MANAGEMENT =====")
    print("1. Park a car")
    print("2. Remove a car")
    print("3. Show next car")
    print("4. Display all cars")
    print("5. Check if parking is empty")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        car_number = input("Enter car number: ")
        parking.enqueue(car_number)
        print("Car", car_number, "parked successfully.")

    elif choice == 2:
        car_number = parking.dequeue()

        if car_number is None:
            print("No cars in the parking area.")
        else:
            print("Car", car_number, "removed from parking.")

    elif choice == 3:
        car_number = parking.peek()

        if car_number is None:
            print("No cars in the parking area.")
        else:
            print("Next car to leave:", car_number)

    elif choice == 4:
        parking.display()

    elif choice == 5:
        if parking.is_empty():
            print("Parking area is empty.")
        else:
            print("Cars are present in the parking area.")

    elif choice == 6:
        print("Exiting parking management system...")
        break

    else:
        print("Invalid choice. Please try again.")

