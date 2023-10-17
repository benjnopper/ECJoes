#define customer class
class Customer:
    def __init__(self, name, address, phone):
        self .__name = name
        self. __address = address
        self.__phone = phone

    #define set methods for customer attributes
    def set_name(self, name):
       self.__name = name
    
    def set_address(self, address):
        self.__address = address
    
    def set_phone(self, phone):
        self.__phone = phone
    
    #define get methods for customer attributes
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone

#define car class    
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    #define set methods for car attributes
    def set_make(self, make):
        self.__make = make
    
    def set_model(self, model):
        self.__model = model
    
    def set_year(self, year):
        self.__year = year
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
class ServiceQuote:
    def __init__(self, part_charges, labor_charges):
       self.__parts_charges = part_charges
       self.__labor_charges = labor_charges

    def set_parts_charges(self, parts_charges):
        self.__parts_charges = parts_charges

    def set_labor_charges(self, labor_charges):
        self.__labor_charges = labor_charges

    def get_parts_charges(self):
        return self.__parts_charges
    
    def get_labor_charges(self):
        return self.__labor_charges
    
    def get_sales_tax(self):
        return 0.08 * self.__parts_charges
    
    def get_total_charges(self):
        return self.__parts_charges + self.__labor_charges + self.get_sales_tax