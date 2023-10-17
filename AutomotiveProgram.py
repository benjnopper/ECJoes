import AutomotiveClass as ac

customer = ac.Customer("John Doe", "123 Main St", "555-123-4567")

car = ac.Car("Mercedes", "C-Class", 2023)

service_quote = ac.ServiceQuote(500, 300)

print("Customer Name:", customer.get_name())
print("Customer Address:", customer.get_address())
print("Customer Phone:", customer.get_phone())
print("Car Make:", car.get_make())
print("Car Model:", car.get_model())
print("Car Year:", car.get_year())

print("Parts Charges:", service_quote.get_parts_charges())
print("Labor Charges:", service_quote.get_labor_charges())
print("Sales Tax:", service_quote.get_sales_tax())
print("Total Charges:", service_quote.get_total_charges())