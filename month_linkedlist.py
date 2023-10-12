#Complete implemenation of linked list
# - add new node to the front of the linked list
# - add new node to the end of the linked list
# - Get a node by it's value
# - Insert new node after a particular node
#Traverse through the linked list and print values

# 2 classes - Node class and Linked List class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
        
    def __repr(self):
        return f"<node | {self.value}>"
    
class LinkedList:
    def __init__(self, head_node=None):
        #Head attribute will point to the first node of the Linked List
        self.head = head_node
        
    # Method to add a new node to the front of our linked list
    def push_on(self, new_value): # O(1) - Constant time operation
        # Create a new node with the value passed in
        new_node = Node(new_value)
        #set the new node's .next attribute to be the current head
        new_node.next = self.head
        # Set the new node to be the front of the linked list (AKA the head attribute)
        self.head = new_node
        
    # Method to print out all of the nodes in the LinkedList in order
    def print_list(self):
        #start at the beginning of list
        node = self.head
        #While the node is a node and not None, continue to loop
        while node is not None:
            #print the node (which will call the Node __str__ method)
            print(node)
            #go to the next node in the list
            node = node.next
    #Method to add a new node to the end of the linked list
    def append(self, new_value): # O(n) -Linear time
        #create a new node with the value passed in
        new_node = Node(new_value)
        #check if the linked list is empty
        if self.head is None:
            #set the head to be the new node
            self.head = new_node
        #if not
        else:
            #traverse to the lase node in the Linked list (aka the node.next is None)
            node = self.head
            while node.next is not None:
                #move to the next node
                node = node.next
            #once node.next is None
            #once node.next is None, set the node's next attribute to be the new node
            node.next = new_node
    
    # Method to get a node by value or return None if not in the LinkedList
    def get_node(self,value_to_get): # O(n) - Linear time
        # Start with the first node
        node_to_check = self.head
        #while the node_to_check is still a node
        while node_to_check is not None:
            #if the value of the node to check is equal to the value to get
            if node_to_check.value == value_to_get:
                #return that node
                return node_to_check
            #if not, move on to the next node
            node_to_check = node_to_check.next
        #once the node to check is None, we know that the value is not in the linked list
        return None
    # Method to insert a new node in the Linked list aftr a certain node (by value)
    def insert_after(self, prev_value, new_value):
        #get the previous node by value
        prev_node = self.get_node(prev_value)
        #make sure the prev_node exists
        if prev_node is None:
            print(f"{prev_value} is not in linked list")
        else:
            # Create a new node with the new value
            new_node = Node(new_value)
            # point the new_node's next attribute at the previous node's next
            new_node.next = prev_node.next
            #point the previousnode's next attribute to the new node
            prev_node.next = new_node
            
        
        
months = LinkedList()

months.append('July')
months.push_on('June')
months.push_on('May')
months.push_on('March')
months.push_on('January')
months.append('August')
months.insert_after('March', 'April')
months.insert_after('January', 'February')
months.append('September')
months.insert_after('September', 'October')
months.append('November')
months.append('Deceber')
may = months.get_node('May')
months.print_list()