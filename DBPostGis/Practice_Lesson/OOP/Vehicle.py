from abc import abstractmethod,ABCMeta

class Vehicle:
    """A vehicle for sale by Jeffco Car Dealership.


        Attributes:
            wheels: An integer representing the number of wheels the vehicle has.
            miles: The integral number of miles driven on the vehicle.
            make: The make of the vehicle as a string.
            model: The model of the vehicle as a string.
            year: The integral year the vehicle was built.
            sold_on: The date the vehicle was sold.
    """
    __metaclass__ = ABCMeta

    base_sale_price=0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):

        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0
        return self.wheels *5000.0

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0
        return self.base_sale_price-(.10*self.miles)


    @abstractmethod
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        pass


class Car(Vehicle):
    base_sale_price = 4000
    wheels = 4
    def vehicle_type(self):
        return "car"

class Truck(Vehicle):
    base_sale_price = 6000
    wheels = 8

    def vehicle_type(self):
        return 'Truck'
class Moto(Vehicle):
    base_sale_price = 5000
    wheels = 2

    def vehicle_type(self):
        return 'Moto'

Honda=Car(500,'Honda','2017','2017',1000)
print Honda.vehicle_type()
print Honda.purchase_price()

print Honda.sale_price()


