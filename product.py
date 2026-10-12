class Product:
    def __init__(self, product_id, name, stock):
        self.__id = product_id
        self.name = name
        self.stock = stock

    @property
    def id(self):
        return self.__id

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            print("Error: Stock cannot be negative.")
        else:
            self.__stock = value

    def show_details(self):
        return f"Product ID: {self.__id}, Name: {self.name}, Stock: {self.__stock}"

    def sell(self, quantity):
        if quantity > self.__stock:
            print("Error: Cannot sell more than available stock!")
        elif quantity <= 0:
            print("Error: Invalid quantity.")
        else:
            self.__stock -= quantity
            print(f"Sold {quantity} successfully. Remaining stock: {self.__stock}")