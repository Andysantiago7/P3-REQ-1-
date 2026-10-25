def calculate_expenses(transportation_fare,food , academic_supply):
     total = transportation_fare + food + academic_supply
     return total


print("THIS IS YOUR BUDGET FOR MONDAY TO FRIDAY: ")

budget = int(input("ENTER YOUR BUDGET: "))
print()

total_expenses = 0

days = ["MONDAY" , "TUESDAY" ,"WEDNESDAY","THURSDAY", "FRIDAY"]

for expenses in range (1,6):
     print(f"TOTAL EXPENSES ON {days[expenses -1]}: ")
     
     transportation_fare = int(input("TRANSPORTATION: "))
     food = int(input("FOOD: "))
     academic_supply = int(input("ACADEMIC SUPPLY: "))
     total = calculate_expenses( transportation_fare, food , academic_supply)

     total_expenses += total   

     print()
     print("TOTAL:" , total)
     print()
     
print("TOTAL EXPENSES FROM MONDAY TO FRIDAY:" , total_expenses)
print("REMAINING BUDGET:" , budget - total_expenses)