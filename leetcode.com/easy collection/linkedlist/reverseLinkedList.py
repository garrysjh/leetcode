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

def count(head):
    count=1
    while (head.next!=None):
        count+=1
        head = head.next
    return count

def linkedListToArr(head):
    llArr = []
    while (head.next!=None):
        llArr.append(head.val)
        head=head.next
    llArr.append(head.val)
    return llArr

def reverseArray(arr: list):
    reversed = []
    for i in range(len(arr)-1,-1,-1):
        reversed.append(arr[i])
    return reversed

def reverseLinkedList(head):
  reversedArr = reverseArray(linkedListToArr(node1))
  for element in reversedArr:
          head.val=element
          head=head.next
    

print(node1)
reverseLinkedList(node1)
print(node1)
