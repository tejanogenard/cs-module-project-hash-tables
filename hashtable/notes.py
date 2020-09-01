

# table = [None] * 8

# def hashf(s):
#     b  = s.encode()

#     total = 0 

#     for i in b:
#         total += i 

#     return total

# # print(hashf("ivan"))
# # print(hashf("Goat"))


# def get_index(key):
#     index_value = hashf(key)
#     index_value %= len(table)

#     return index_value

# def put(key, value):
#     # Which slot in the table is the value going? 
#     index = get_index(key)
#     table[index] = value 

#     # Store the value at that slot 



# def get(key):
#     index = get_index(key)

#     return table[index]


# def delete(key):
#     index = get_index(key)

#     table[index] = None 

# # print(table)


# put("Ivan", 3490) 
# print(table)

# delete("navI")
# print(table)


############################

class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 

    def repr(self):
        return f"Node({repr(self.value)})"

class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_head(self,node):
        node.next = self.head 
        self.head = node 

    def find(self, value): 
        """"Return the node with the given value, or None"""
        cur = self.head 
        
        while cur != None: 
            if cur.value  == value: 
                return cur 
            
            cur = cur.next 

    #if value was not found 
        return None 

    def delete(self, value):
    #special case: delete the head         
        if self.head is None: 
            return None 

    #special case: delete the head 
        if value == self.head.value: 
            old_head = self.head 
            self.head = self.head.next 
            return old_head  # delete successful

        prev = self.head 
        cur = prev.next 

        while cur is not None: 
            if cur.value == value: 
                prev.next = cur.next 
                cur.next = None 
                return cur 

            prev = prev.next 
            cur = cur.next 

        # if we didn't find it 
        return None 


ll = LinkedList()

ll.insert_at_head(Node(5))
ll.insert_at_head(Node(98))
ll.insert_at_head(Node(12))
ll.insert_at_head(Node(22))

print(ll.find(98))
print(ll.find(999999)) # None 

# curr = ll.head

# while curr !=None:
#     print(curr.value)
#     curr = curr.next 
