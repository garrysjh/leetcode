#remove nth node from lnked list
#given head of linked list, remove nth node from end of list

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
    
#creating nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
#connecting nos
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

def removeNthNode(head: ListNode,n: int):
    totalNodes = count(head)
    for i in range(0,totalNodes-n):
        head=head.next
    head.val = head.next.val
    head.next=head.next.next

def count(head):
    count=1
    while (head.next!=None):
        count+=1
        head = head.next
    return count

print(node1)
removeNthNode(node1, 2)
print(node1)