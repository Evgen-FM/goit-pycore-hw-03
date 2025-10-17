import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > max - min:
        return []
    
    ran = range(min, max)
    result = random.sample(ran, quantity)
    result.sort()
    return result

print(get_numbers_ticket(1, 1000, 4))

