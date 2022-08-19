'''
Imagine that you are a thief breaking into a house. There are so 
many valuables to steal, but you’re just one person who can only 
carry so much. Each item has a weight and value, and your goal is 
to maximize the total value of items while remaining within the weight 
limit of your knapsack. Create a knapsack() function that takes in:

- the total amount of weight you can carry
- an array of the weights of all of the items
- an array of the values of all of the items
and returns the maximum value that you will be able to carry.

For example, let’s say your knapsack can carry 10 units of weight. 
The item weights are [3, 6, 8] and their values are [50, 60, 100]. Your 
knapsack function should return 110 since you can carry the first and second 
items, whose values total 110. If you tried to carry the third item, which has 
the value of 100, you wouldn’t be able to fit anything else in the knapsack.
'''
class Item:
    def __init__(self, weight, value):
        self._weight = weight
        self._value = value
        self._value_per_weight = value / weight
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def value(self):
        return self._value
    
    @property
    def value_per_weight(self):
        return self._value_per_weight

def knapsack(weight_cap, weights, values):
    available_items = zip(weights, values)
    available_items = [Item(w, v) for (w, v) in available_items]
    available_items.sort(key=lambda i: i.value_per_weight, reverse=True)
    
    chosen_items = []
    for item in available_items:
        if item.weight <= weight_cap:
            print(f'The thief got the item with weight {item.weight} and value {item.value}')
            weight_cap -= item.weight
            chosen_items.append(item.value)

    return sum(chosen_items)

weight_cap = 10
weights = [3, 6, 8]
values = [50, 60, 100]
print()
print('Maximum amount:', knapsack(weight_cap, weights, values))