user_input_number = ''
number_of_items = 0
while not user_input_number.isnumeric():
    user_input_number = input('Please enter number of items: ')

number_of_items = int(user_input_number)
print(number_of_items)

user_input_cost = ''
cost_per_item = 0

while not user_input_cost.isnumeric():
    user_input_cost = input('Please enter the cost per item in cents: ')

cost_per_item = int(user_input_cost)/100
print(cost_per_item)

if number_of_items < 10:
    pass
elif 10 <= number_of_items < 20:
    cost_per_item = cost_per_item * 0.9
elif 20 <= number_of_items:
    cost_per_item = cost_per_item * 0.8

member = False
is_member = ''

while not is_member == 'yes' and not is_member == 'no':
    is_member = input('Are you a member? Type "yes" or "no": ')

if is_member == 'yes': 
    member = True
else:
    member = False

if member and number_of_items < 10:
    cost_per_item = int(user_input_cost) * 0.85
elif member and number_of_items >= 10:
    cost_per_item = int(user_input_cost) * 0.75
else:
    pass

print('Your cost per item is {}'.format(cost_per_item))