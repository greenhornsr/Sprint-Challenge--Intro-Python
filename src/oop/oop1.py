# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

## Base Class
# Vehicle
class Vehicle:
    def __init__(self):
        pass

# Direct Sub Class to Vehicle
class FlightVehicle(Vehicle):
        pass

class GroundVehicle(Vehicle):
        pass

# Sub Class to FlightVehicle
class Starship(FlightVehicle):
        pass

class Airplane(FlightVehicle):
        pass

# Sub Class to GroundVehicle
class Motorcycle(GroundVehicle):
        pass

class Car(GroundVehicle):
        pass





    
