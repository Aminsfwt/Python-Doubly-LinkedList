##the basic node of the linked list data structure
class Node:
    def __init__(self, data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

#the linked list data structure
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):                    #print the data from forward of linked list
        if self.head is None:
            print("The List is Empty")
            return
        
        itr = self.head
        itrlst = ""

        while itr:
            itrlst += str(itr.data) + '---->'
            itr = itr.next
        print("Link list in Forward: ", itrlst)    

    def insert_in_begin(self, data):            #insert data in the begining of linked list
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.previous = node
            self.head = node

    def get_last_node(self):                    #Get the last node of linked list 
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def insert_in_end(self, data):              #insert data in the end of linked list
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        last_node = self.get_last_node()

        last_node.next = Node(data, None, last_node)

    def print_backward(self):                   #print the data from backward of linked list
        if self.head is None:
            print("The List is Empty")
            return
        
        last_node = self.get_last_node()
        itr = last_node
        itrlst = ''
        while itr:
            itrlst += itr.data + '---->'
            itr = itr.previous
        print("Link list in Reverse: ", itrlst)

    def get_length(self):                       #get the length of linked list
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        print("Link list Length: ", count)
        return count    

    def insert_values(self, data_list):         #insert several data at th same time in the begin of linked list
        #self.head = None
        for data in data_list:
            self.insert_in_end(data)

    def insert_at(self, index, data):           #insert data in certain place
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_in_begin(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):                 #remove data  after certin index
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.previous = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.previous.next = itr.next
                if itr.next:
                    itr.next.previous = itr.previous
                break

            itr = itr.next
            count+=1

data_lst = ["Ahmed", 'Hassan', 'Eslam']
node_1 = DoublyLinkedList()

node_1.insert_in_end("Mahmoud")

node_1.insert_in_begin("Amin")
node_1.insert_in_begin("Ali")
node_1.insert_in_end("Mohammed")
node_1.print_forward()

node_1.insert_at(1,'Yacine')

node_1.print_forward()
node_1.print_backward()
node_1.get_length()

node_1.remove_at(3)
node_1.print_forward()
