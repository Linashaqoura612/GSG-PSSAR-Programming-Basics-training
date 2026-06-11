#Part A — Math Priority
result = 10 + 5 * 2
print(result)
'''
5 * 2 = 10 first (multiplication before addition)
10 + 10 = 20
'''
result = (10 + 5) * 2
print(result)
'''
Parentheses first: 10 + 5 = 15
15 * 2 = 30
'''
#=======================================
#Part B — Logical Priority
print(True or False and False)
'''
and runs before or
So:
False and False = False
True or False = True
'''
print((True or False) and False)
'''
Parentheses first: True or False = True
Then: True and False = False
'''
#=======================================
#Part C — Real Life Trap
total_bill = 120
points = 20
premium_member = True
print(total_bill > 150 and points > 50 or premium_member)
'''
total_bill > 150 → False
points > 50 → False
So:
False and False = False
Then:
False or premium_member
premium_member = True
'''
print(total_bill > 150 and (points > 50 or premium_member))
'''
total_bill > 150 → False
Inside brackets:
points > 50 → False
premium_member → True
(False or True) = True
Now:
False and True = False
'''