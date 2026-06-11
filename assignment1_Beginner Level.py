coffee_price = 25
cake_price = 40
water_price = 10

coffee_count = 2
cake_count = 1
water_count = 3

total_bill = coffee_price * coffee_count
total_bill += cake_price * cake_count
total_bill += water_price * water_count

print(total_bill) #total bill
print(total_bill > 100) #whether total is greater than 100
print(total_bill == 120) #whether total equals 120

coffee_price = 25
coffee_price += 5 #Increase coffee price by 5
print(coffee_price)