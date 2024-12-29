def greet_guests(guests):
    for guest in guests:
        print(f"Привет, {guest}!")

guest_list = ["Александр", "Мария", "Дмитрий", "Елена"]
greet_guests(guest_list)