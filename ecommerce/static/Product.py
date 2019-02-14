class Product:

    name = ""
    price = 0
    quantity = 0
    location = ""



    def __init__(self, Name, Price, Quantity, Location):
        self.name = Name
        self.price = Price
        self.quantity = Quantity
        self.location = Location



    def __repr__(self):
        return "{}, ${}, {}pcs, at {}".format(self.name, self.price, self.quantity, self.location)



def validate_price(value):
    # get number from string   
    try:
        # check if number
        float(value)
    except ValueError:
        print("That's not a valid number")
        # string in not valid
        return False
    
    # string is valid
    return True



def validate_quantity(value):
    # get number from string   
    try:
        # check if number
        int(value)
    except ValueError:
        print("That's not a valid number")
        # string in not valid
        return False
    
    # string is valid
    return True