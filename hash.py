# list1 = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]


# def smallest(key):

#     total = 0 

#     for arr in list1:
#         smallest_val = min(arr)
#         total += smallest_val
#     return total


# print(smallest(list1))




# 0 1 1 2 3 5 8 13...... fib example 

# cache = {}

# def fib(n):
#     if n < 1: 
#         return n

#     if n not in cache: 
#         cache[n] = fib(n-1) + fib(n-2)

#     return cache[n]

# for i in range(100):
#     print(f"{i:3} {fib(i)}") 


# d = {
#     "foo": 12, 
#     "bar": 17,
#     "qux": 2 
# }

# items = list(d.items())
# items.sort()
# print(items)

# # sort by key 
# # items.sort(reverse = True )
# # we can also sort by value 


# # def fun(e):
# #     return e[1] 
# # items.sort(key = fun) 

# # does the same as the code above 
# items.sort(key=lambda e: e[1])

# print(items)


# def letter_count(s):
#     d = {}

#     for c in s: 
#         if c.isspace():
#             continue

#         c = c.lower() 

#         if c not in d: 
#             d[c] = 0

#         d[c] += 1 
#     return d 
         

# def print_sorted_letter_count(s):
#     d = letter_count(s)
#     items = list(d.items())

#     items.sort(key = lambda e: e[1], reverse = True)

#     for i in items:
#         print(f"{i[0]}: {i[1]}")
# print_sorted_letter_count("hello")
# print_sorted_letter_count("they also thought in the 1980s that there would be flying cars by 2015, from Back to the Future 2")

# """
# GOATS 

# JEHFN
# """
# encode_table = {
#     'A': 'H',
#     'B': 'Z',
#     'C': 'Y',
#     'D': 'W',
#     'E': 'O',
#     'F': 'R',
#     'G': 'J',
#     'H': 'D',
#     'I': 'P',
#     'J': 'T',
#     'K': 'I',
#     'L': 'G',
#     'M': 'L',
#     'N': 'C',
#     'O': 'E',
#     'P': 'X',
#     'Q': 'K',
#     'R': 'U',
#     'S': 'N',
#     'T': 'F',
#     'U': 'A',
#     'V': 'M',
#     'W': 'B',
#     'X': 'Q',
#     'Y': 'V',
#     'Z': 'S'
# }


# decode_table = {}
# # Build the reverse map 

# for k, v in encode_table.items():
#     decode_table[v] = k


# def encode(s):
#     r = ""

#     for c in s: 
#         r += encode_table[c]

#     return r



# print(encode("GOATS"))
# print(encode("ELEPHANTS"))


# import hashlib
# import random 

# def hash_function(key):
#     return int(hashlib.md5(str(key). encode()).hexdigest() [-8:], 16) & 0xffffffff

# def how_many_before_collision(buckets, loops=1):
#     for i in range(loops):
#         tries = 0 
#         tried = set()

#         while True: 
#             random_key = random.random() 
#             index = hash_function(random_key) % buckets

#             if index not in tried: 
#                 tried.add(index)
#                 tries += 1

#             else: 
#                 break 

#             print(f"{buckets} buckets, {tries} hases before collision.({tries / buckets * 100:.1f}) % full")

# how_many_before_collision(4096, 10)


# l = [1,2,4,5,1,2,3,4,7,1,1,3,4,3,8]


# def is_in_list(n):
#     for x in l:
#         if n == x: 
#             return True 

#     return False 

# print(is)

# import math 

# lookup_table = {}

# for n in range(1, 1001):
#     lookup_table[n] = 1 / math.sqrt(n)
# def inv_sqrt(n):
#     # n is an integer between 1 and 1000

#     if n not in lookup_table:
#         lookup_table[n] = 1 / math.sqrt(n)

#     return lookup_table[n]

# print(inv_sqrt(10))
# print(inv_sqrt(100))