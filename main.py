from datetime import date


def AgeCalculate(birth_data , birth_month , birth_year):
    today = date.today()
    current_date = today.day
    current_month = today.month
    current_year = today.year

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   
    if birth_date > current_data:
        current_date = current_data + months[birth_month-1]
        current_month = current_month - 1
    if birth_month > current_month:
        current_year = current_year - 1
        current_month = current_month + 12

    calculated_date = current_date - birth_date
    calculated_month = current_month - birth_month
    calculated_year = current_year - birth_year
    print(f"Your Age  Year : {calculated_year}  Month : {calculated_month}  Day : {calculated_date}\n")
print("\n\tWelcome to Age Calculator")
today = date.today()
current_data = today.day
current_month = today.month
current_year = today.year

birth_date = int(input("Enter Your Birth Data    "))
birth_month = int(input("Enter Your Birth Month  "))
birth_year = int(input("Enter Your Birth Year    "))

AgeCalculate(birth_date , birth_month , birth_year)