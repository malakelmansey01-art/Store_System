from product import Product
from customer import Customer
from admin import Admin

def main():
    p1 = Product(1, "Laptop", 10)
    p2 = Product(2, "Phone", 25)
    
    cust = Customer(101, "Malak", 50)
    adm = Admin(201, "Ahmed")

    products = [p1, p2]
    users = [cust, adm]

    print("--- 1. Show all products ---")
    for p in products:
        print(p.show_details())

    print("\n--- 2. Search for a product by ID ---")
    search_id = 1
    for p in products:
        if p.id == search_id:
            print(f"Found: {p.show_details()}")

    print("\n--- 3. Sell a product and show remaining stock ---")
    p1.sell(3)

    print("\n--- 4. Try to set a negative stock value ---`")
    p1.stock = -5

    print("\n--- 5. Show all users ---")
    for u in users:
        print(u.show_details())

    print("\n--- 6. Show every user's role using show_role() ---")
    for u in users:
        u.show_role()

if __name__ == "__main__":
    main()