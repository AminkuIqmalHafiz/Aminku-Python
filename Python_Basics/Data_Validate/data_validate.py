import re

order_data = [
    {
        'order_id': 'ORD1234',
        'email': 'customer1@test.com',
        'price': 45.99,
        'status': 'Shipped',
        'items': ['Laptop Stand', 'Wireless Mouse']
    },
    {
        'order_id': 'ord999', 
        'email': 'customer2_at_test.com', 
        'price': -10.50, 
        'status': 'PENDING',
        'items': ['Keyboard']
    },
    {
        'order_id': 'ORD5678',
        'email': 'customer3@test.com',
        'price': 120,
        'status': 'Processing', 
        'items': [] 
    },
    {
        'order_id': 'ORD4321',
        'email': 'customer4@test.com',
        'price': 15.00,
        'status': 'delivered',
        'items': [123, 456] 
    }
]

def validation_rule(order_id,email,price,status,items):
    constraints = {
        'order_id' : isinstance(order_id,str) and re.fullmatch(r'ORD\d+',order_id,re.IGNORECASE),
        'email': isinstance(email,str) and "@" in email,
        'price': isinstance(price,(float,int)) and price >= 0,
        'status' : isinstance(status,(str)) and status.lower() in ('pending','shipped','delivered'),
        'items' : isinstance(items,(list)) and len(items) >= 1
    }
    
    return [key for key,value in constraints.items()if not value]

def validate(data):
    is_sequence = isinstance(data,(list,tuple))
    is_invalid = False
    key_set = set(
        ['order_id','email','price','status','items']
    )   
    ## First filter : not a sequence
    if not is_sequence:
        print("Invalid format : expected a list or a tuple. ")
        return False
    
    ## A loop
    for index, dictionary in enumerate(data):
        #First criteria : a dictionary
        if not isinstance(dictionary,dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        #Second criteria : aligned with key sets
        if set(dictionary.keys()) != key_set:
            print (f"Invalid format: {dictionary} at position {index} has missing and/or invalid key.")
            is_invalid = True
            continue
        
        #Third criteria : specific,granular criteria (validation_rule func)
        invalid_records = validation_rule(**dictionary)
        #This use for unpacking list
        for key in invalid_records:
            value = dictionary[key]
            print(f"Unexpected Format '{key}:{value}'at position {index}.")
            is_invalid = True

    
    if is_invalid:
        return False
    print("Valid Format")
    return True

validate(order_data)
