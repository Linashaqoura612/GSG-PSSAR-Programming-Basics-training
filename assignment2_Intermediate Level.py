points = 40
total_bill = 160

points += 20 #earned 20 points
points -= 10 #used 10 points
points *= 2 #doubled their points

vip = points >= 100
free_delivery = (total_bill > 150) or vip

print(points)
print(vip)
print(free_delivery)