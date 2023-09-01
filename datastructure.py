import os
from queue import Queue

#function for double linked list
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedlist:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        if self.head is None:
            newnode = Node(data)
            newnode.prev = None
            self.head = newnode
        else:
            newnode = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newnode
            newnode.prev = cur
            newnode.next = None

    def prepend(self,data):
        if self.head is None:
            newnode = Node(data)
            newnode.prev = None
            self.head =newnode
        else:
            newnode = Node(data)
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode
            newnode.prev = None
    
    def printlist(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next

    def deletenode(self, data):
        #not clear
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                break
            current_node = current_node.next

    def search(self, data):
        #not clear
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
        
    def sort(self):
        # bubble sort
        swapped = True
        while swapped:
            swapped = False
            current_node = self.head
            while current_node.next is not None:
                if current_node.data > current_node.next.data:
                    current_node.data, current_node.next.data = current_node.next.data, current_node.data
                    swapped = True
                current_node = current_node.next

#functions for stack menu
class Stack:
    def __init__(self, maxitems):
        self.item = []
        self.maxitems = maxitems
    
    def empty(self):
        return len(self.item) == 0

    def addstack(self, item):
            self.item.append(item)
            print("The updated stacks are the following: ")
            for x in self.item:
                print("|",x,"|",end=' ')       
          
        
    def removelastitem(self):
            item = self.item.pop()
            print("The updated stacks are the following: ")
            for x in self.item:
                print("|",x,"|",end=' ')
        
    def displayrange(self):
        #last code, need ko alisin yung maximuim range para ma display yung range
        maxitems = self.item
        print("The range of the stack: ")
        for i in range(len(maxitems)):
            print("|",i,"|",end=' ')
    
    def removespecifcvalue(self, remove):
        self.item.remove(remove)
        print("The updated stacks are the following: ")
        for x in self.item:
            print("|",x,"|",end=' ')    
        
    def count(self):
        num_elements = len(self.item)
        print("The stack has", num_elements, "elements." )

    def copyintext(self):
        all = self.item
        with open("try.txt", "w") as output:
            output.write(str(all))

#functions for queue menu 
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,qitem):
        self.queue.append(qitem)
    
    def dequeu(self):
        self.queue.pop(0) 
    
    def printqueue(self):
        print("The updated stacks are the following: ")
        for x in self.queue:
            print("|",x,"|",end=' ')  

# all the menu functions
def double_linked_list_menu():
    dlist = DoubleLinkedlist()
    os.system("cls")
    while True:
        print("\nDOUBLY LINKED LIST MENU")
        print("[1] Add new element at the beginng")
        print("[2] Add new element at end ")
        print("[3] Display list")
        print("[4] Exit")
        print("[5] Delete")
        print("[6] Search")
        print("[7] Sort")
        
        choice = input("Enter your choice: ")
        if choice == "1":
           item = input("Enter number: ")
           dlist.prepend(item)
           os.system("cls")
           
        elif choice == "2":
           item = input("Enter number: ")
           dlist.append(item)
           os.system("cls")
           
        elif choice =="3":
            os.system("cls")
            dlist.printlist()

        elif choice =="4":
            os.system("cls")
            main_menu()

        elif choice =="5":
            item = input("Enter node: ")
            os.system("cls")
            dlist.deletenode(item)

        elif choice == "6":
            item = input("Enter the date to search: ")
            os.system("cls")
            if dlist.search(item):
                print(f"{item} Data was found ")
            else:
                print(f"{item} Data was not found ")
        elif choice =="7":
            dlist.sort()
            os.system("cls")

def stack_menu():

    stack = Stack(maxitems =5)
    os.system("cls")
    while True:
        print("\nSTACK MENU")
        print("[A] add an item")
        print("[B] Remove the last item")
        print("[C] Remove the specific value")
        print("[D] Display the range of items")
        print("[E] Count the number of element")
        print("[F] Copy values to text fill ")
        print("[G] Go back to main menu")

        choice = input("What would you like to do? ")

        if choice == "A":
            item = input("Enter item to add: ")
            os.system("cls")     
            stack.addstack(item)
        elif choice =="B":
            os.system("cls")     
            stack.removelastitem()
        elif choice =="C":
            remove = input("Enter item to be removed: ")
            os.system("cls") 
            stack.removespecifcvalue(remove)

        elif choice == "D":
            os.system("cls")
            stack.displayrange()

        elif choice =="E":
            os.system("cls")
            stack.count()
        elif choice == "F":
            os.system("cls")
            stack.copyintext()

        elif choice == "G":
            os.system("cls")
            main_menu()
        
        else:
            os.system("cls")
            print("Try again")
            
        
def  queues_menu():
    q = Queue()
    os.system("cls")
    while True:
        print("\nQueues Menu")
        print("[1] Insert an item")
        print("[2] Delete the item")
        print("[3] Display all lits")
        print("[4] Go back to main menu")

        
        choice = input("Enter choice: ")
        
        if choice == "1":
            qitem = input("Enter the item to be input: ")
            os.system("cls")
            q.enqueue(qitem)
        elif choice =="2":
            os.system("cls")
            q.dequeu()
            
        elif choice == "3":
            os.system("cls")
            q.printqueue()

        elif choice == "4":
            os.system("cls")
            main_menu()
        
        else:
            os.system("cls")
            print("Try again")
            

#Main menu
def main_menu():
    while True:
        print("MAIN MENU")
        print("[D] Double Linked List")
        print("[S] Stacks")
        print("[Q] Queues")
        print("[E] Exit")
        
        choice = input("Enter your choice: ")

        if choice == "D":
            double_linked_list_menu()

        elif (choice == "S" ):
            stack_menu()
        
        elif (choice == "Q"):
            queues_menu()

        elif (choice == "E"):
            print("\nEXIT SuCCESFUL")
            break
        else:
            os.system("cls")
            print("Try again: ")
        
        
        
        
        
        
        
       
main_menu()
