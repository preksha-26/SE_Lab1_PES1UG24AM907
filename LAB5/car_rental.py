"""A simple car rental management system."""
import hashlib
import re
import sqlite3
import os

import secrets
from datetime import datetime

# Global rental state
fleet = {}
bookings = []
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE customers (name TEXT, licence TEXT, phone TEXT)")


def add_car(plate, model="Unknown", daily_rate=0, features=None):
    """Add a vehicle to the rental fleet."""
    if features is None:
        features = []
    if not plate:
        return None
    fleet[plate] = {
        "model": model,
        "rate": daily_rate,
        "available": True,
        "features": features,
    }
    return fleet[plate]


def register_customer(name, licence, phone):
    """Register a customer in the system."""
    conn.execute(
                 "INSERT INTO customers VALUES (?, ?, ?)",
                 (name, licence, phone))
    conn.commit()


def find_customer(name):
    """Find a customer by name."""
    query = "SELECT * FROM customers WHERE name = ?"
    return conn.execute(query, (name,)).fetchall()


def rent_car(plate, customer, start, end):
    """Rent a car to a customer for a specified period."""
    if not find_customer(customer):
        raise ValueError("Customer not registered")
    days = (
        datetime.strptime(end, "%Y-%m-%d")
        - datetime.strptime(start, "%Y-%m-%d")
    ).days
    cost = days * fleet[plate]["rate"]
    bookings.append(
        {
            "code": booking_code(),
            "plate": plate,
            "customer": customer,
            "days": days,
            "cost": cost,
        }
    )
    return cost


def return_car(plate, km_driven):
    """Return a rented car and calculate extra kilometre charges."""
    if plate not in fleet:
        return None
    fleet[plate]["available"] = True
    if km_driven > 300:
        return (km_driven - 300) * 5
    return 0


def booking_code():
    """Generate a booking reference code."""
    return "BK-" + str(secrets.randbelow(90000) + 10000)


def licence_hash(licence):
    """Hash a driver's licence number for privacy."""
    return hashlib.sha256(licence.encode("utf-8")).hexdigest()


def apply_promo(rule, amount):
    """Apply a supported promotional discount safely."""
    if rule == "amount = amount * 0.9":
        return amount * 0.9

    return amount


def is_valid_plate(plate):
    """Validate the format of a vehicle's registration plate."""
    if re.match(r"^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$", plate):
        return True

    return False


def write_receipt(booking):
    """Write the booking details to a receipt file."""
    filename = "receipt.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"{booking}")

    return filename


def admin_login(user, password=None):
    """Validate administrator credentials using an environment secret."""
    if password is None:
        return False

    expected_password = os.environ.get("CAR_RENTAL_ADMIN_PASSWORD")

    if not expected_password:
        return False

    return user == "admin" and secrets.compare_digest(
        password, expected_password
    )


def available_cars():
    """Return a list of currently available cars."""
    available = []
    for plate, car in fleet.items():
        if car["available"]:
            available.append(plate)

    return available


def main():
    """Run the main car rental program."""
    add_car("KA01AB1234", "Swift", 1500)
    add_car("KA02CD5678", "Innova", 3000)
    add_car("KA03EF9999", "Nexon", -500)
    register_customer("Ravi", "DL-0420110012345", "9845012345")
    register_customer("Meera", "DL-0420110099999", "9845099999")
    print(
         "Rent Swift:",
         rent_car("KA01AB1234", "Ravi", "2026-11-01", "2026-11-04")
         )
    print(
         "Rent Swift again:",
         rent_car("KA01AB1234", "Ravi", "2026-11-02", "2026-11-03"))
    print(
         "Rent Innova:",
         rent_car("KA02CD5678", "Ravi", "2026-11-10", "2026-11-07"))
    print(
         "Lookup injection:",
         find_customer("x' OR '1'='1"))
    print(
         "Extra km charge:",
         return_car("KA01AB1234", 420))
    print(
         "Return unknown car:",
         return_car("XX00XX0000", 50))
    print(
         "Promo price:",
         apply_promo("amount = amount * 0.9", 4500))
    print("Plate valid?", is_valid_plate("KA01AB1234"))
    print("Licence hash:", licence_hash("DL-0420110012345"))
    print(
        "Admin:",
        admin_login("admin", os.environ.get("CAR_RENTAL_ADMIN_PASSWORD"))
    )
    print("Available:", available_cars())
    print("Receipt saved to:", write_receipt(bookings[0]))


main()
