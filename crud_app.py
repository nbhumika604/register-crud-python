# crud_app.py

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = {"name": name, "email": email}
    users.append(user)
    print("User added successfully!")

def read_users():
    if not users:
        print("No users to display.")
    else:
        for i, user in enumerate(users):
            print(f"{i + 1}. Name: {user['name']}, Email: {user['email']}")

def update_user():
    read_users()
    index = int(input("Enter the user number to update: ")) - 1
    if 0 <= index < len(users):
        users[index]['name'] = input("Enter new name: ")
        users[index]['email'] = input("Enter new email: ")
        print("User updated successfully!")
    else:
        print("Invalid user number.")

def delete_user():
    read_users()
    index = int(input("Enter the user number to delete: ")) - 1
    if 0 <= index < len(users):
        users.pop(index)
        print("User deleted successfully!")
    else:
        print("Invalid user number.")

def menu():
    while True:
        print("\n--- User Register Table ---")
        print("1. Create User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_user()
        elif choice == '2':
            read_users()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

menu()