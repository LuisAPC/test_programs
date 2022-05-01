class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class MyLinkedList:

    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            return self.head_node.value
        elif index == self.size - 1:
            return self.tail_node.value
        else:
            node_at_idx = self.head_node
            for _ in range(index):
                node_at_idx = node_at_idx.next_node
            return node_at_idx.value
            

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next_node = self.head_node
        self.head_node = new_node
        if self.size == 0:
            self.tail_node = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head_node = new_node
        else:
            self.tail_node.next_node = new_node
        self.tail_node = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        #If index equals the length of the linked list, the node will be appended to the end of the linked list. f index is greater than the length, the node will not be inserted.
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            node_at_idx = self.head_node
            for _ in range(index):
                prev_node = node_at_idx
                node_at_idx = node_at_idx.next_node
            new_node.next_node = node_at_idx
            prev_node.next_node = new_node
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        #Delete the indexth node in the linked list, if the index is valid.
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            self.head_node = self.head_node.next_node
            if self.size == 1:
                self.tail_node == None
        else:
            node_at_idx = self.head_node
            for _ in range(index):
                prev_node = node_at_idx
                node_at_idx = node_at_idx.next_node
            if index == self.size - 1:
                prev_node.next_node = None
                self.tail_node = prev_node
            else:
                prev_node.next_node = node_at_idx.next_node  
        self.size -= 1

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.value != None:
                string_list += str(current_node.value) + "\n"
            current_node = current_node.next_node
        return string_list


# Your MyLinkedList object will be instantiated and called as such:
# myLinkedList = MyLinkedList();
# print(myLinkedList.addAtHead(7))
# print(myLinkedList.addAtHead(2))
# print(myLinkedList.addAtHead(1))
# print(myLinkedList.addAtIndex(3, 0))
# print(myLinkedList.deleteAtIndex(2))  
# print(myLinkedList.addAtHead(6))
# print(myLinkedList.addAtTail(4))
# print(myLinkedList.get(4)) 
# print(myLinkedList.addAtHead(4))
# print(myLinkedList.addAtIndex(5, 0))
# print(myLinkedList.addAtHead(6))

# myLinkedList = MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    #// linked list becomes 1->2->3
# myLinkedList.get(1);              #// return 2
# myLinkedList.deleteAtIndex(1);    #// now the linked list is 1->3
# myLinkedList.get(1);              #// return 3

myLinkedList = MyLinkedList();
print(myLinkedList.addAtTail(1))
print(myLinkedList.get(0))

print('init')
print(myLinkedList.stringify_list()) 