import re

def normalize_phone(phone_number):
    del_sym = re.sub(r"[^\d]" , "" , phone_number)
    if phone_number.strip()[0] == "+":
        return "+" + del_sym 
    elif del_sym[0:2] == "38":
        return "+" + del_sym
    else:
        return "+38" + del_sym
    

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ", 
    " +42150 122 43 22"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", *sanitized_numbers, sep="\n")
