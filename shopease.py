import json

# Define the dictionary containing information about different shops and their products
shops = {
    "Yuvarani foot wears": {
        "Location": "G6G8+4XM, Palace Rd, Keerankulangara, Thrissur, Kerala 680001",
        "Products": {
            "Nike": {
                "stock": 10,
                "Price": 1000,
                "Sizes": [7, 8, 9, 10]
            },
            "New Balance": {
                "stock":8,
                "Price": 2400,
                "Sizes": [6, 7, 8, 9, 10]
            },
            "Puma": {
                "stock":9,
                "Price": 1499,
                "Sizes": [7, 8, 9]
            }
        }
    },
    "Kobbler": {
        "Location": "G6G6+9G3, Machingal Ln, Naikkanal, Thrissur, Kerala 680022",
        "Products": {
            "Adidas": {
                "stock":8,
                "Price": 1500,
                "Sizes": [6, 7, 8, 9, 10]
            },
            "Sneaker": {
                "stock":14,
                "Price": 3000,
                "Sizes": [7, 8, 9]
            },
            "Converse": {
                "stock":20,
                "Price": 1500,
                "Sizes": [6, 7, 8, 9, 10]
            }
        }
    },
    "Woodland": {
        "Location": "Shop No. 25/479, Gokul Building, M.G. Road, Opposite Ramdas Theatre, Thrissur, Kerala 680001",
        "Products": {
            "Reebok": {
                "stock":10,
                "Price": 2000,
                "Sizes": [6, 7, 8, 9, 10]
            },
            "Converse": {
                "stock":16,
                "Price": 1800,
                "Sizes": [7, 8, 9]
            },
            "Skechers": {
                "stock":14,
                "Price": 2500,
                "Sizes": [6, 7, 8, 9, 10]
            }
        }
    },
    "DOC & MARK ": {
        "Location": "SBU03, Woodlands Avenue, Room No :25, 789, MG Road, Naikkanal, Thrissur, Kerala 680001",
        "Products": {
            "Reebok": {
                "Price": 1900,
                "stock":12,
                "Sizes": [6, 7, 9, 10]
            },
            "Vans": {
                "stock":12,
                "Price": 1800,
                "Sizes": [3, 7, 8, 9]
            },
            "Skechers": {
                "stock":10,
                "Price": 2570,
                "Sizes": [4, 7, 8, 9, 10]
            }
        }
    },
    "Bongo": {
        "Location": "G6F6+QQH, Kodungallur - Shornur Rd, Naduvilal, Marar Road Area, Naikkanal, Thrissur, Kerala 680001",
        "Products": {
            "Converse": {
                "stock":12,
                "Price": 2000,
                "Sizes": [6, 7, 8, 9, 10]
            },
            "Nike": {
                "stock":10,
                "Price": 1800,
                "Sizes": [7, 8, 9]
            },
            "Adidas": {
                "stock":12,
                "Price": 2500,
                "Sizes": [6, 7, 8, 9, 10]
            }
        }
    },
    "Flexfootwear": {
        "Location": "G6C7+WPQ, Swaraj Round, Thrissur, Kerala 680001",
        "Products": {
            "Puma": {
                "stock":10,
                "Price": 2000,
                "Sizes": [6, 7, 8, 9, 10]
            },
            "Sneaker": {
                "stock":8,
                "Price": 1800,
                "Sizes": [7, 8, 9]
            },
            "Skechers": {
                "stock":12,
                "Price": 2500,
                "Sizes": [6, 7, 8, 9, 10]
            }
        }
    }
}

# Define the file path for storing credentials
USER_CREDENTIALS_FILE = "user_credentials.json"
ADMIN_CREDENTIALS_FILE = "admin_credentials.json"

# Define the dictionary to store admin credentials
admin_credentials = {
    "username": "admin",
    "password": "admin123",
    "is_signed_up": False,
    "shop_name": "Old Shop"
}

# Define the dictionary to store user credentials
user_credentials = {}

# Function to save admin credentials to a file
def save_admin_credentials():
    with open(ADMIN_CREDENTIALS_FILE, "w") as file:
        json.dump(admin_credentials, file)

# Function to load admin credentials from a file
def load_admin_credentials():
    global admin_credentials
    try:
        with open(ADMIN_CREDENTIALS_FILE, "r") as file:
            admin_credentials = json.load(file)
    except FileNotFoundError:
        save_admin_credentials()

# Function to save user credentials to a file
def save_user_credentials():
    with open(USER_CREDENTIALS_FILE, "w") as file:
        json.dump(user_credentials, file)

# Function to load user credentials from a file
def load_user_credentials():
    global user_credentials
    try:
        with open(USER_CREDENTIALS_FILE, "r") as file:
            user_credentials = json.load(file)
    except FileNotFoundError:
        save_user_credentials()

# Function to search for a product in all shops
def search_product(product_name):
    locations = [{
        "Shop": shop,
        "Location": shop_data["Location"],
        "stock": brand_data["stock"],
        "Price": brand_data["Price"],
        "Sizes": brand_data["Sizes"]
    } for shop, shop_data in shops.items() for brand, brand_data in shop_data["Products"].items() if product_name.lower() == brand.lower()]

    return locations

# Function to display the available brands
def display_brands():
    brands = set()
    for shop, shop_data in shops.items():
        for brand, _ in shop_data["Products"].items():
            brands.add(brand)
    print("Available Brands:")
    print("-----------------")
    for brand in brands:
        print(brand)

# Function for admin sign-up
def admin_signup():
    if not admin_credentials["is_signed_up"]:
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        shop_name = input("Enter shop name: ")
        admin_credentials["username"] = username
        admin_credentials["password"] = password
        admin_credentials["shop_name"] = shop_name
        admin_credentials["is_signed_up"] = True
        print("---------------------")
        print("|sign-up successful! |")
        print("---------------------")

        save_admin_credentials()  # Save the admin credentials to a file

        return True
    else:
        print("Admin is already signed up.")
        return False

# Function for admin login
def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    if (
        username == admin_credentials["username"]
        and password == admin_credentials["password"]
        and admin_credentials["is_signed_up"]
    ):
        print("----------------------------")
        print("|    login successful!     |")
        print("----------------------------")

        # Check if shop name exists in admin_credentials
        if "shop_name" not in admin_credentials:
            admin_credentials["shop_name"] = "not in change"

        print(f"Current shop name: {admin_credentials['shop_name']}")
        change_shop_name = input("Do you want to change the shop name? (y/n): ")
        if change_shop_name.lower() == "y":
            new_shop_name = input("Enter the new shop name: ")
            admin_credentials["shop_name"] = new_shop_name
            print("Shop name changed successfully!")

        save_admin_credentials()  # Save the admin credentials to a file

        return True
    else:
        print("Invalid admin credentials.")
        return False

# Function for user sign-up
def user_signup():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if username in user_credentials:
        print("Username already exists. Please choose a different username.")
    else:
        user_credentials[username] = password
        save_user_credentials()  # Save the user credentials to a file
        print("---------------------------")
        print("| User sign-up successful! |")
        print("--------------------- ------")

# Function for user login
def user_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_credentials and user_credentials[username] == password:
        print("----------------------------")
        print("| User login successful!   |")
        print("----------------------------")

        return True
    else:
        print("Invalid username or password.")
        return False

# Function to add multiple products to a shop
def add_products():
    shop_name = input("Enter the shop name: ")
    products = []

    product_names = input("Enter the product names (comma-separated): ").split(",")

    for product_name in product_names:
        product_name = product_name.strip()
        product_stock = int(input(f"Enter the stock for {product_name}:"))
        product_price = float(input(f"Enter the price for {product_name}: "))
        product_sizes = input(f"Enter the available sizes for {product_name} (comma-separated): ").split(",")
        product_sizes = [int(size.strip()) for size in product_sizes]

        products.append({
            "Name": product_name,
            "stock": product_stock,
            "Price": product_price,
            "Sizes": product_sizes
        })

    if shop_name in shops:
        for product in products:
            product_name = product["Name"]
            product_price = product["Price"]
            product_sizes = product["Sizes"]

            shops[shop_name]["Products"][product_name] = {
                "Price": product_price,
                "Sizes": product_sizes
            }

        print("Products added successfully!")
    else:
        print("Shop not found!")

# Function to delete a product from a shop
def delete_product():
    shop_name = input("Enter the shop name: ")
    product_name = input("Enter the product name: ")

    if shop_name in shops and product_name in shops[shop_name]["Products"]:
        del shops[shop_name]["Products"][product_name]
        print("Product deleted successfully!")
    else:
        print("Shop or product not found!")

# Function to update product details
def update_product():
    while True:
        shop_name = input("Enter the current shop name: ")
        product_name = input("Enter the product name: ")
    #ivide
        print("Please select one of the following options to update:")
        print("1. Price")
        print("2. Stock")
        print("3. Size")
        
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            if shop_name in shops and product_name in shops[shop_name]["Products"]:
                
                new_price = float(input("Enter the new price: "))
                
            # Update product details
                shops[shop_name]["Products"][product_name]["Price"] = new_price
            # Update shop name if it has changed
            if shop_name:
                product_data = shops[shop_name]["Products"].pop(product_name)  # Remove product from current shop
                shops[shop_name]["Products"][product_name] = product_data  # Add product to new shop

                print("Product details updated successfully!")
                inner_choice = input("Do you want to continue(Y/N)").upper()
                if inner_choice == "Y":
                    continue
                else:
                    break
            else:
                print("Shop or product not found!")
                continue
        if choice == 2:
            new_stock = int(input("enter the stocks: "))
        # Update product details
            shops[shop_name]["Products"][product_name]["stock"] = new_stock
            # Update shop name if it has changed
            if shop_name:
                product_data = shops[shop_name]["Products"].pop(product_name)  # Remove product from current shop
                shops[shop_name]["Products"][product_name] = product_data  # Add product to new shop

            print("Product details updated successfully!")
        else:
            print("Shop or product not found!")
        if choice == 3:
            new_sizes = input("Enter the new sizes (comma-separated): ").split(",")
            new_sizes = [int(size.strip()) for size in new_sizes]
            
            shops[shop_name]["Products"][product_name]["Sizes"] = new_sizes
            # Update shop name if it has changed
            if shop_name:
                product_data = shops[shop_name]["Products"].pop(product_name)  # Remove product from current shop
                shops[shop_name]["Products"][product_name] = product_data  # Add product to new shop

            print("Product details updated successfully!")
        else:
            print("Shop or product not found!")

        
        
        
    
# Function to search for a specific shop and display its product count and names
def search_shop():
    shop_name = input("Enter the shop name: ")
    if shop_name in shops:
        shop_data = shops[shop_name]
        product_count = len(shop_data["Products"])
        product_names = ", ".join(shop_data["Products"].keys())
        print(f"Shop: {shop_name}, Product Count: {product_count}, Products: {product_names}")
    else:
        print(f"Shop '{shop_name}' not found.")
        
print("---------------------------------------")
# Main program
def main():
    print("        WELCOME TO SHOPEASE")
    print("---------------------------------------")

    # Load admin credentials from file
    load_admin_credentials()

    # Load user credentials from file
    load_user_credentials()
    
    while True:
        print("Please select an option:")
        print("1. shopkeeper")
        print("2. User")
        print("3. Contact") 
        print("4. Send Mail to developer")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            print("-----------------------------")
            print(     "Welcome, shopkeeper!      ")
            print("-----------------------------")
            print("Please select an option:")
            print("1. Sign-up")
            print("2. Login")
            admin_choice = input("Enter your choice (1-2): ")
            if admin_choice == "1":
                print("Sign-up option selected.")
                if admin_signup():
                    print("signup successful!")
                else:
                    print("signup failed. Please try again.")
            elif admin_choice == "2":
                print("Login option selected.")
                if admin_login():
                    while True:
                        print("Please select an option:")
                        print("=========================================")
                        print("1. Add Product")
                        print("_________________________________________")
                        print("2. Delete Product")
                        print("_________________________________________")
                        print("3. Update Product Details")
                        print("_________________________________________")
                        print("4. Display Available Brands")
                        print("_________________________________________")
                        print("5. Display how many product in their shop")
                        print("_________________________________________")
                        print("6. Logout")
                        print("_________________________________________")
                        admin_action = input("Enter your choice (1-5): ")
                        if admin_action == "1":
                            add_products()
                        elif admin_action == "2":
                            delete_product()
                        elif admin_action == "3":
                            update_product()
                        elif admin_action == "4":
                            display_brands()
                        elif admin_action == "5":
                            search_shop()
                        elif admin_action == "6":
                            print("logout successfully")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                else:
                    print("login failed. Please try again.")

        elif choice == "2":
            print("-----------------------------")
            print("Welcome, User!")
            print("-----------------------------")
            print("Please select an option:")
            print("1. User Sign-up")
            print("2. User Login")
            user_choice = input("Enter your choice (1-2): ")
            if user_choice == "1":
                print("User Sign-up option selected.")
                user_signup()
            elif user_choice == "2":
                print("User Login option selected.")
                if user_login():
                    while True:
                        print("Please select an option:")
                        print("1. Search for a Product")
                        print("2. Search for Products under a Price")
                        print("3. Display Available Brands")
                        print("4. display how many products in a shop")
                        print("5. logout")

                        user_action = input("Enter your choice (1-4): ")

                        if user_action == "1":
                            product_name = input("Enter the product name: ")
                            search_result = search_product(product_name)

                            if len(search_result) > 0:
                                print("Matching products found in the following shops:")
                                for location in search_result:
                                    print("_____________________________________")
                                    print("-------------------------------------------------------------------------------------------------------------")
                                    print("Shop:     |", location["Shop"])
                                    print("-------------------------------------------------------------------------------------------------------------")
                                    print("Location: |", location["Location"])
                                    print("-------------------------------------------------------------------------------------------------------------")
                                    print("stock:    |", location["stock"])
                                    print("-------------------------------------------------------------------------------------------------------------")
                                    print("Price:    |", location["Price"])
                                    print("-------------------------------------------------------------------------------------------------------------")
                                    print("Sizes:    |", location["Sizes"])
                                    print("-------------------------------------------------------------------------------------------------------------")
                                    print("_______________________________________________________SHOPEASE______________________________________________")
                            else:
                                print("No matching products found.")
                        elif user_action == "2":
                            max_price = float(input("Enter the maximum price: "))

                            matching_products = []
                            for shop, shop_data in shops.items():
                                for brand, brand_data in shop_data["Products"].items():
                                    if brand_data["Price"] <= max_price:
                                        matching_products.append({
                                            "Shop": shop,
                                            "Location": shop_data["Location"],
                                            "Brand": brand,
                                            "stock":brand_data["stock"],
                                            "Price": brand_data["Price"],
                                            "Sizes": brand_data["Sizes"]
                                        })

                            if len(matching_products) > 0:
                                print("Products under the specified price found in the following shops:")
                                for product in matching_products:
                                    print("___________________________________")
                                    print("---------------------------------------------------------------------------------------------------------")
                                    print("Shop:       |", product["Shop"])
                                    print("---------------------------------------------------------------------------------------------------------")
                                    print("Location:   |", product["Location"])
                                    print("---------------------------------------------------------------------------------------------------------")
                                    print("Brand:      |", product["Brand"])
                                    print("---------------------------------------------------------------------------------------------------------")
                                    print("stock:      |", location["stock"])
                                    print("---------------------------------------------------------------------------------------------------------")
                                    print("Price:      |", product["Price"])
                                    print("---------------------------------------------------------------------------------------------------------")
                                    print("Sizes:      |", product["Sizes"])
                                    print("---------------------------------------------------------------------------------------------------------")
                                    print("___________________________________________________SHOPEASE______________________________________________")
                            else:
                                print("No products found under the specified price.")
                        elif user_action == "3":
                            display_brands()
                        elif user_action =="4":
                            search_shop()
                        elif user_action == "5":
                            print("Logged out successfully!")
                            break
                        else:
                            print("Invalid choice. Please try again.")
                else:
                    print("User login failed. Please try again.")

        elif choice == "3":
            print("-----------------------------")
            print("Contact Information")
            print("-----------------------------")
            print("Please contact us at:")
            print("website   :https://en.wikipedia.org/wiki/Shoe")
            print("instagram :https://www.instagram.com/shope_ease/?igshid=ZGUzMzM3NWJiOQ%3D%3D")
            print("telegram  :http://t.me/ShopEase")
            print("Email     :shopease@gmail.com")
            print("Phone     :+918129690147 , +918157843684")
            print("developers:edwin,abhirami,sreesh")

        elif choice == "4":
            print("-----------------------------")
            print("Send Mail to Programmer")
            print("-----------------------------")
            recipient = input("Enter recipient's email address: ")
            subject = input("Enter email subject: ")
            message = input("Enter email message: ")
            print("Sending mail...")
            # Code to send the email goes here
            print("Mail sent successfully!")

        elif choice == "5":  
            print("Exiting the program....")
            print("THANK FOR USING SHOPEASE")
            break
        else:
            print("Invalid choice. Please try again.")

main()
