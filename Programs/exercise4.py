# EX : 4: Lists
# sold lemonade for 2 weeks, list shows no. of lemonade sell 
# for 2 weeks.
# - profit for each lemonade is 1.5$
# - Add another day to week 2 list by capturing number from
#   inupt.
# - combine two lists into single list called `sales`
# - print how much you have earned on 
#     - best day 
#     - worse day 
#     - separately and in total
#   Hint: 3 prints in total.

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]

last_Day = int(input("Enter last day sale for 2nd week: "))
sales_w2.append(last_Day)
#print(sales_w2)

sales = sales_w1.copy()
sales.extend(sales_w2)
#print(sales)
set1 = set()

best_day_earn = sales.pop() * 1.5
worse_day_earn = sales[0] * 1.5

print(f"Best day earning: ${best_day_earn}")
print(f"Worse day earning: ${worse_day_earn}")
print(f"Total: ${best_day_earn + worse_day_earn}")

# OP:
# Enter last day sale for 2nd week: 10
# Best day earning: $63.0
# Worse day earning: $4.5
# Total: $67.5
