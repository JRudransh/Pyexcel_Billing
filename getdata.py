def get_products():
    done = False
    sl = 1
    product_list = []
    while not done:
        product = input(f"Enter Product No {sl}: ")
        sl += 1
        if product == "":
            done = True
        else:
            product_list.append(product)
    return product_list


def get_number():
    get = input("Enter Customer's Number: ")
    done = False
    while not done:
        try:
            number_int = int(get)
            if len(str(number_int)) != 10:
                int("aaa")
            done = True
            number = f"+91{number_int}"
        except ValueError:
            print("Invalid input !!")
            get = input("Enter Customer's Number Again: ")
            done = False
    return number


def get_discount():
    get = input("Enter Discount Rs: ")
    done = False
    while not done:
        try:
            number_int = int(get)
            done = True
            discount = number_int
        except ValueError:
            print("Invalid input !!")
            get = input("Enter Discount Rs. Again: ")
            done = False
    return discount


def get_gst():
    get = input("Enter GST Percent(%): ")
    if get == "":
        get = 0
    done = False
    while not done:
        try:
            number_int = int(get)
            done = True
            gst = number_int
        except ValueError:
            print("Invalid input !!")
            print("Use only numbers !!")
            get = input("Enter GST Percent(%) Again: ")
            done = False
    return gst


def get_advance():
    get = input("Advance Amount (If Any): ")
    if get == "":
        get = 0
    done = False
    while not done:
        try:
            number_int = int(get)
            done = True
            advance = number_int
        except ValueError:
            print("Invalid input !!")
            print("Use only numbers !!")
            get = input("Enter GST Percent(%) Again: ")
            done = False
    return advance


def get_note():
    done = False
    sl = 1
    note_list = []
    while not done:
        note = input(f"Enter Note Line {sl}: ")
        sl += 1
        if note == "":
            done = True
        else:
            note_list.append(note)
    return note_list


def get_address():
    get = input("Enter Address: ")
    done = False
    while not done:
        if len(get) > 30:
            print("Too Long Address..")
            print("Can't fit into bill..")
            get = input("Enter Address Again: ")
        else:
            address = get
            done = True
    return address


number = get_number()
add = get_address()
prods = get_products()
adv = get_advance()
discount = get_discount()
notes = get_note()
count = 1
count2 = 1

print(f"The number is: +91{number}")
print(f"The address is: {add}")
for i in prods:
    print(f"The product-{count} is: {i}")
    count += 1

for j in notes:
    print(f"The Note-{count2} is: {j}")
    count2 += 1



