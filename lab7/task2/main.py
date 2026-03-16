from models import Product, Smartphone, Laptop

def main():
    phone = Smartphone("iPhone 17", 800, 5, "iOS")
    laptop = Laptop("MacBook Neo", 600, 3, 8)
    simple_item = Product("Case", 20, 50)

    products = [phone, laptop, simple_item]

    print("Product List")
    for p in products:
        print(p)

    print("\nTesting Methods")
    phone.apply_discount(10)
    print(f"New phone price: {phone.price}")
    
    laptop.upgrade_ram(4)

if __name__ == "__main__":
    main()
