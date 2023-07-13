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
node3 = ListNode(4)
#connecting nos
node1.next=node2
node2.next=node3

#creating second group of nodss
nud1 = ListNode(1)
nud2 = ListNode(3)
nud3 = ListNode(5)
nud4 = ListNode(6)
#connecting nods
nud1.next=nud2
nud2.next=nud3
nud3.next=nud4



print(node1)
print(nud1)

def merge2Lists(firstHead, secondHead):
    arr = []
    while(firstHead.next!=None):
        arr.append(firstHead.val)
        firstHead = firstHead.next
    arr.append(firstHead.val)
    firstHead.next = secondHead
    while(secondHead.next!=None):
        arr.append(secondHead.val)
        secondHead = secondHead.next
    arr.append(secondHead.val)
    for element in arr:
        firstHead.val = element
        firstHead = firstHead.next


merge2Lists(node1,nud1)
print(node1)

