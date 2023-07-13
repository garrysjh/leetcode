#Delete Node in a Linked List
#There is a singly-linked list head and we want to delete a node node in it
#You are given the node to be accessed

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    def __str__(self):
        output = [self.val]
        while self.next!=None:
            self = self.next
            output.append(self.val)
        return str(output)
    
def deleteNode(node: ListNode):
    node.val = node.next.val
    node.next=node.next.next


node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(8)
node1.next = node2
node2.next = node3
node3.next = node4

print(node1)
deleteNode(node2)
print(node1)

