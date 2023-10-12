class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"<Node|{self.value}>"

class LinkedList:
    def __init__(self, head_node=None):
        self.head = head_node
        
    def push_on(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
        
    def traverse_list(self): #print_list
        node = self.head
        while node is not None:
            print(node)
            node = node.next
            
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node
            
    def get_node(self, value_to_get):
        node_to_check = self.head
        while node_to_check is not None:
            if node_to_check.value == value_to_get:
                return node_to_check
            node_to_check = node_to_check.next
        return None
    
    def insert_after(self, prev_value, new_value):
        prev_node = self.get_node(prev_value)
        if prev_node is None:
            print(f"{prev_value} is not in the linked list.")
        else:
            new_node = Node(new_value)
            new_node.next = prev_node.next
            prev_node.next = new_node
            
#     def find_before(self, value_to_get):
#         node = self.head
#         while node.next is not None:
#             if node.next.value == value_to_get:
#                 return node
#             node = node.next
#         return None
            
    def remove(self, value_to_remove):
        if self.head is None:
            print(f"{value_to_remove} is not in the linked list.")
        
        elif self.head.value == value_to_remove:
            self.head = self.head.next
            return
        
        prev_node = self.head
        for node in self:
            if node.value == value_to_remove:
                prev_node.next = node.next
                return
            prev_node = node
        
        
        
        #so you'll have to point the preceeding (or skip over day to be removed) list to the after list
        #get the node that points to the node with the value to remove
        #set the previous node's next to the node to remove's next
        
        
    

weekdays = LinkedList()
list_of_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for day in list_of_days:
    weekdays.append(day)

weekdays.remove('Tuesday')

weekdays.traverse_list()
