class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def size(self):
        count = 0

        if self.head is None:
            print('Stack is empty')
            return

        temp = self.head

        while temp:

            temp = temp.next
            count += 1

        print(count)
            

    def isEmpty(self):
        if self.head is None:
            print(True)
        else:
            print(False)

    def push(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):

        if self.head is None:
            print("Stack is empty")
            return
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return ("Data popped: {}", temp.data)

    def peek(self):
        if self.isEmpty():
            print('Stack is empty')
            return

        else:
            print(self.head.data)
            return

    def printStack(self):
        temp = self.head
        if temp is None:
            return ('Stack is empty')

        else:
            while temp:
                print(temp.data, "->", end = " ")
                temp = temp.next
            return
        

if __name__ == '__main__':

    stack = Stack() 

    stack.size()
    stack.isEmpty()
    stack.push(1)
    stack.push(2)
    stack.peek()
    stack.printStack()

        


        