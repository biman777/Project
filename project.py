FILE_NAME = "geologists.txt"

def load_data():
    """Load geologist data from the file."""
    data = {}
    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                geologist_id, name, age, specialization, salary, home_district, ideology = line.strip().split(',')
                data[geologist_id] = {
                    "name": name,
                    "age": age,
                    "specialization": specialization,
                    "salary": salary,
                    "home_district": home_district,
                    "ideology": ideology
                }
    except FileNotFoundError:
        pass
    return data

def save_data(data):
    """Save geologist data to the file."""
    with open(FILE_NAME, 'w') as file:
        for geologist_id, details in data.items():
            file.write(f"{geologist_id},{details['name']},{details['age']},{details['specialization']},{details['salary']},{details['home_district']},{details['ideology']}\n")

def add_geologist():
    """Add a new geologist."""
    data = load_data()
    geologist_id = input("Enter geologist ID: ")
    if geologist_id in data:
        print("Geologist ID already exists.")
        return
    name = input("Enter geologist name: ")
    age = input("Enter geologist age: ")
    specialization = input("Enter geologist specialization (e.g., Petrologist, Geophysicist, Geochemist): ")
    salary = input("Enter geologist salary: ")
    home_district = input("Enter geologist home district: ")
    ideology = input("Enter geologist ideology: ")
    data[geologist_id] = {
        "name": name,
        "age": age,
        "specialization": specialization,
        "salary": salary,
        "home_district": home_district,
        "ideology": ideology
    }
    save_data(data)
    print("Geologist added successfully.")

def edit_geologist():
    """Edit an existing geologist's information."""
    data = load_data()
    geologist_id = input("Enter geologist ID to edit: ")
    if geologist_id not in data:
        print("Geologist ID not found.")
        return
    print(f"Current data: {data[geologist_id]}")
    name = input("Enter new name (leave blank to keep current): ") or data[geologist_id]['name']
    age = input("Enter new age (leave blank to keep current): ") or data[geologist_id]['age']
    specialization = input("Enter new specialization (leave blank to keep current): ") or data[geologist_id]['specialization']
    salary = input("Enter new salary (leave blank to keep current): ") or data[geologist_id]['salary']
    home_district = input("Enter new home district (leave blank to keep current): ") or data[geologist_id]['home_district']
    ideology = input("Enter new ideology (leave blank to keep current): ") or data[geologist_id]['ideology']
    data[geologist_id] = {
        "name": name,
        "age": age,
        "specialization": specialization,
        "salary": salary,
        "home_district": home_district,
        "ideology": ideology
    }
    save_data(data)
    print("Geologist information updated.")

def search_geologist():
    """Search for a geologist by ID."""
    data = load_data()
    geologist_id = input("Enter geologist ID to search: ")
    if geologist_id in data:
        print(f"Geologist found: {data[geologist_id]}")
    else:
        print("Geologist ID not found.")

def delete_geologist():
    """Delete a geologist by ID."""
    data = load_data()
    geologist_id = input("Enter geologist ID to delete: ")
    if geologist_id in data:
        del data[geologist_id]
        save_data(data)
        print("Geologist deleted successfully.")
    else:
        print("Geologist ID not found.")

def main():
    """Main menu for the geologist information system."""
    while True:
        print("\nGeologist Information System")
        print("1. Add Geologist")
        print("2. Edit Geologist")
        print("3. Search Geologist")
        print("4. Delete Geologist")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_geologist()
        elif choice == '2':
            edit_geologist()
        elif choice == '3':
            search_geologist()
        elif choice == '4':
            delete_geologist()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Adding initial data
    initial_data = {
        "100": {
            "name": "Biman",
            "age": "25",
            "specialization": "Petrologist",
            "salary": "700000",
            "home_district": "Jashore",
            "ideology": "Sree Sree Thakur Anukul Chandra"
        },
        "200": {
            "name": "Dhiman",
            "age": "26",
            "specialization": "Geophysicist",
            "salary": "550000",
            "home_district": "Rajshahi",
            "ideology": "Lord Krishna"
        },
        "300": {
            "name": "Bowman",
            "age": "27",
            "specialization": "Geochemist",
            "salary": "600000",
            "home_district": "Dhaka",
            "ideology": "Thakure Ramkrishna"
        }
    }
    save_data(initial_data)
    main()
