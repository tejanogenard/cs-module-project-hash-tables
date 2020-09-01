

table = [None] * 8

def hashf(s):
    b  = s.encode()

    total = 0 

    for i in b:
        total += i 

    return total

# print(hashf("ivan"))
# print(hashf("Goat"))


def get_index(key):
    index_value = hashf(key)
    index_value %= len(table)

    return index_value

def put(key, value):
    # Which slot in the table is the value going? 
    index = get_index(key)
    table[index] = value 

    # Store the value at that slot 



def get(key):
    index = get_index(key)

    return table[index]


def delete(key):
    index = get_index(key)

    table[index] = None 

# print(table)


put("Ivan", 3490) 
print(table)

delete("navI")
print(table)
