class Node:
    def __init__(self,data):
        self.data = data
        self.next = None    #.next is an iterator (like i++ in java)

class LinkedList:
    def __init__(self):
        self.head = None    #.head is used for clarification, but can be any variable

    def append(self,data): #adds a new node to the end
        newNode = Node(data)    #creates new node
        if not self.head:       #if the CURRENT HEAD is empty
            self.head = newNode #CURRENT HEAD changed to point to newNode
            return
        current = self.head     #variable created and set to CURRENT HEAD
        while current.next:     #while CURRENT HEAD is not null
            current = current.next #set CURRENT HEAD to the next node
        current.next = newNode  #newNode is now the CURRENT HEAD

    def prepend(self,data): #adds a new node to the beginning
        newNode = Node(data)        #newNode is created and data is set
        newNode.next = self.head    #newNode's head points to previous node
        self.head = newNode         #current head changed to point to newNode

    #def delete(self,data):
        #temp
    def printList(self):
        list = []
        current = self.head
        while current:
            list.append(str(current.data)) #changing int to str for [.join] to work
            current = current.next
        if list:
            print(" --> ".join(list))
        else:
            print("Linked List is empty")

if __name__ ==  "__main__":

    ll = LinkedList()

    ll.append(2)
    ll.append(4)
    ll.append(6)

    ll.printList()

    ll.prepend(0)
    ll.prepend(1)

    ll.printList()

"""
**FIRST NODE**

[CURRENT HEAD]
        |
[data|head]
        |
        -> NULL
"""
#------------------------------------------------
"""
**SECOND NODE**

[CURRENT HEAD]
       |
[data|head] --> [data|head]
                        |
                        -> NULL
"""
#------------------------------------------------
"""
**THIRD NODE**

[CURRENT HEAD]
       |
[data|head] --> [data|head] --> [data|head]
                                        |
                                        -> NULL
"""
