"""
==============================================================================
PRACTICE QUESTION: Vehicle Rental System
==============================================================================

Build a vehicle rental system using OOP.
This question focuses on abstract classes/methods, inheritance, method
overriding, and polymorphism (composition is used too, for the Agency).

------------------------------------------------------------------------------
CLASS: Vehicle (abstract)
------------------------------------------------------------------------------

Vehicle should be an ABSTRACT class — it must never be instantiated directly.

__init__(self, make, model, daily_rate)
    - Stores make and model as private attributes (_make, _model).
    - Stores daily_rate as a private attribute (_daily_rate).
    - Raises a ValueError if daily_rate is not a positive number.

make (property — read only)
    - Returns the vehicle's make.

model (property — read only)
    - Returns the vehicle's model.

daily_rate (property — read only)
    - Returns the daily rental rate.

calculate_rental_cost(self, days)
    - ABSTRACT METHOD — no implementation here.
    - Each subclass must provide its own version.

__str__(self)
    - Returns a string like: "Toyota Corolla"  (i.e. "{make} {model}")

------------------------------------------------------------------------------
CLASS: Car (inherits from Vehicle)
------------------------------------------------------------------------------

__init__(self, make, model, daily_rate, passenger_capacity)
    - Calls the parent constructor using super().
    - Stores passenger_capacity as a private attribute (_passenger_capacity).

passenger_capacity (property — read only)

calculate_rental_cost(self, days)
    - Overrides the abstract method.
    - Simply returns daily_rate * days. No discounts.

------------------------------------------------------------------------------
CLASS: Van (inherits from Vehicle)
------------------------------------------------------------------------------

__init__(self, make, model, daily_rate, cargo_capacity_kg)
    - Calls the parent constructor using super().
    - Stores cargo_capacity_kg as a private attribute (_cargo_capacity_kg).

cargo_capacity_kg (property — read only)

calculate_rental_cost(self, days)
    - Overrides the abstract method.
    - Base cost = daily_rate * days.
    - If days >= 7, apply a 10% discount to the TOTAL (long-term hire).
    - Otherwise, no discount.
    - Return the cost rounded to 2 decimal places.

------------------------------------------------------------------------------
CLASS: RentalAgency
------------------------------------------------------------------------------

__init__(self, name)
    - Stores the agency name.
    - Initialises an empty private list _fleet.

add_vehicle(self, vehicle)
    - Adds a Vehicle (or subclass) instance to the fleet.
    - Raises a TypeError if the argument is not a Vehicle instance.

find_by_make(self, make)
    - Returns a list of all vehicles matching the given make (case-insensitive).

cheapest_vehicle(self)
    - Returns the Vehicle in the fleet with the lowest daily_rate.
    - Returns None if the fleet is empty.

generate_quote(self, vehicle, days)
    - Takes a Vehicle instance and a number of days.
    - Returns a string like:
      "Toyota Corolla: £180.00 for 7 days"
    - IMPORTANT: this method should work for ANY Vehicle subclass without
      needing to know or check which subclass it is (this is the polymorphism
      part of the exercise — think about *why* that works here).

__str__(self)
    - Returns a string like: "Sunshine Rentals — 3 vehicles"

==============================================================================
EXAMPLE USAGE
==============================================================================

car = Car("Toyota", "Corolla", 30, passenger_capacity=5)
van = Van("Ford", "Transit", 45, cargo_capacity_kg=1200)

agency = RentalAgency("Sunshine Rentals")
agency.add_vehicle(car)
agency.add_vehicle(van)

print(agency)
# Expected: Sunshine Rentals — 2 vehicles

print(agency.generate_quote(car, 7))
# Expected: Toyota Corolla: £210.00 for 7 days

print(agency.generate_quote(van, 7))
# Expected: Ford Transit: £283.50 for 7 days   (45*7=315, minus 10% = 283.50)

print(agency.generate_quote(van, 3))
# Expected: Ford Transit: £135.00 for 3 days   (no discount, under 7 days)

cheapest = agency.cheapest_vehicle()
print(str(cheapest))
# Expected: Toyota Corolla

# Trying to instantiate the abstract class directly should fail:
try:
    v = Vehicle("Generic", "Model", 20)
except TypeError as e:
    print(f"Caught: {e}")
# Expected: Caught (message will mention it can't instantiate an abstract class)

"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, daily_rate):
        self._make = make
        self._model = model
        if not isinstance(daily_rate, (int, float)) or daily_rate <= 0:
            raise ValueError("Daily rate must be a positive number.")
        self._daily_rate = daily_rate

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def daily_rate(self):
        return self._daily_rate

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    def __lt__(self, other):
        return self._daily_rate < other.daily_rate

    def __str__(self):
        return f"{self._make}: {self._model}. Daily Rate: {self._daily_rate}"


class Car(Vehicle):
    def __init__(self, make, model, daily_rate, passenger_capacity):
        super().__init__(make, model, daily_rate)
        self._passenger_capacity = passenger_capacity

    @property
    def passenger_capacity(self):
        return self._passenger_capacity

    @passenger_capacity.setter
    def passenger_capacity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Pages must be a positive integer")
        self.passenger_capacity = value

    def calculate_rental_cost(self, days):
        return self.daily_rate * days


class Van(Vehicle):
    def __init__(self, make, model, daily_rate, cargo_capacity_kg):
        super().__init__(make, model, daily_rate)
        self._cargo_capacity_kg = cargo_capacity_kg

    @property
    def cargo_capacity_kg(self):
        return self._cargo_capacity_kg

    def calculate_rental_cost(self, days):
        base_cost = self.daily_rate * days
        if days >= 7:
            discounted_cost = base_cost * 0.9
            return f"{discounted_cost:.2f}"
        else:
            return f"{base_cost:.2f}"


class RentalAgency:
    def __init__(self, name):
        self.name = name
        self._fleet = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Invalid input")
        self._fleet.append(vehicle)

    def find_by_make(self, make):
        vehicles = []
        for vehicle in self._fleet:
            if vehicle.make.lower() == make.lower():
                vehicles.append(vehicle)
        return vehicles

    def cheapest_vehicle(self):
        vehicles = self._fleet
        if not vehicles:
            return None
        else:
            return min(vehicles)

    def generate_quote(self, vehicle, days):
        return f"{vehicle.make} {vehicle.model}: £{vehicle.calculate_rental_cost(days)}"

    def __str__(self):
        return f"{self.name} - {len(self._fleet)} vehicles"


# ==============================================================================
# TEST CASES — run this file to check your solution
# ==============================================================================

car = Car("Toyota", "Corolla", 30, passenger_capacity=5)
van = Van("Ford", "Transit", 45, cargo_capacity_kg=1200)
car2 = Car("Honda", "Civic", 25, passenger_capacity=5)

agency = RentalAgency("Sunshine Rentals")
agency.add_vehicle(car)
agency.add_vehicle(van)
agency.add_vehicle(car2)

print(agency)
# Expected: Sunshine Rentals — 3 vehicles

print(agency.generate_quote(car, 7))
# Expected: Toyota Corolla: £210.00 for 7 days

print(agency.generate_quote(van, 7))
# Expected: Ford Transit: £283.50 for 7 days

print(agency.generate_quote(van, 3))
# Expected: Ford Transit: £135.00 for 3 days

cheapest = agency.cheapest_vehicle()
print(str(cheapest))
# Expected: Honda Civic

toyota_matches = agency.find_by_make("toyota")
print([str(v) for v in toyota_matches])
# Expected: ['Toyota Corolla']

# Instantiating the abstract class directly should fail
try:
    v = Vehicle("Generic", "Model", 20)
except TypeError as e:
    print(f"Caught: {e}")
# Expected: Caught: ... (Python's built-in abstract class error)

# Invalid daily_rate raises ValueError
try:
    bad_car = Car("Bad", "Car", -10, passenger_capacity=4)
except ValueError as e:
    print(f"Caught: {e}")
# Expected: Caught: <your validation message>

# Adding a non-Vehicle raises TypeError
try:
    agency.add_vehicle("not a vehicle")
except TypeError as e:
    print(f"Caught: {e}")
# Expected: Caught: <your validation message>
