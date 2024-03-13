from datetime import datetime
def calculateprice(birth_date):
    current_date = datetime.now()
    current_day = current_date.strftime("%A")
    age = current_date.year - birth_date.year
    if age < 18:
        ticket=1000
    elif age >=18 or age <= 60 :
        ticket=750
    elif age > 60 :
        ticket=500
    if (current_day=="Tuesday") or (current_date=="Thursday") :
        ticket*=0.8
    return ticket

year = int(input("Enter the year of your birth (YYYY): "))
month = int(input("Enter the month of your birth (MM): "))
day = int(input("Enter the day of your birth (DD): "))

birth_date = datetime(year, month, day)
price = calculateprice(birth_date)

print("TICKET PRICE :", price)
