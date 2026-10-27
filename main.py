"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    semester_cost = cost_per_semester(annual_cost)
    return semester_cost / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    credit_cost = cost_per_credit(annual_cost, credits)
    class_cost = credit_cost * CS1430_CREDITS
    return class_cost / CS1430_MEETINGS_PER_SEMESTER


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost  = float(input("Enter your total cost for one year of college: $"))
    credits = int(input("Enter the number of credits you are taking this semester: "))



    while True:
        # Show your menu here.
        print("\n--- The Cost of College ---")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per CS1430 class meeting")
        print("6. Worth It? (compare cost to hourly pay)")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            print("Goodbye!")
            break
        elif choice == "1":
            result = cost_per_semester(annual_cost)
            print(f"Cost per semester: ${result:.2f}")
        elif choice == "2":
            result = cost_per_month(annual_cost)
            print(f"Cost per month: ${result:.2f}")
        elif choice == "3":
            result = cost_per_day(annual_cost)
            print(f"Cost per class day: ${result:.2f}")
        elif choice == "4":
            result = cost_per_credit(annual_cost, credits)
            print(f"Cost per credit: ${result:.2f}")
        elif choice == "5":
            result = cost_per_class(annual_cost, credits)
            print(f"Cost per CS1430 class meeting: ${result:.2f}")
        elif choice == "6":
            hourly_pay = float(input("Enter an hourly pay rate to compare: $"))
            if hourly_pay > 0:
                meeting_cost = cost_per_class(annual_cost, credits)
                hours_needed = meeting_cost / hourly_pay
                print(f"One CS1430 meeting costs ${meeting_cost:.2f}.")
                print(f"At ${hourly_pay:.2f} per hour, that costs {hours_needed:.2f} hours of work.")
            else:
                print("Hourly pay must be greater than 0.")
        else:
            print("Invalid choice. Choose 1 through 6 or Q to quit.")


        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
