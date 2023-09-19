import sys
import math

def add_tax(costs_list,tax_val):
    cost_w_tax=[]
    for cost in costs_list:
        cost_w_tax.append(cost*(1+tax_val))
    return cost_w_tax

num_of_purchases=int(input("Number of purchases: "))
sales_tax=float(input("Sales tax: "))
names=[]
costs=[]
i=1
while i<=num_of_purchases:
    names.append(input("Customer: "))
    costs.append(float(input("Cost: ")))
    i+=1
new_costs=add_tax(costs,sales_tax)
customer_cost={}
for i,name in enumerate(names):
    if name in customer_cost:
        customer_cost[name]+=(new_costs[i])
    else:
        customer_cost[name]=(new_costs[i])
print(customer_cost)
