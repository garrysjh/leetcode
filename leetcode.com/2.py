#Add two numbers
#given 2 non-empty linked lists representing two non negative integers
# the digits are stored in reverse order and eahc node contains a single dii
# add 2 numbers and return sum as linked list

#singly linked list head l1 and l2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SLinkedList:
    def __init__(self):
        self.head = None

l1 = Node(9)
l1.next = Node(9)
l1.next.next = Node(9)
l1.next.next.next = Node(9)
l1.next.next.next.next = Node(9)
l1.next.next.next.next.next = Node(9)
l1.next.next.next.next.next.next = Node(9)

l2 = Node(9)
l2.next = Node(9)
l2.next.next = Node(9)
l2.next.next.next = Node(9)

def addTwoNumbers(l1, l2):
    num1 = []
    num2 = []
    while (l1!=None):
        num1.append(l1.data)
        l1=l1.next
    while (l2!=None):
        num2.append(l2.data)
        l2=l2.next
    result = str(combineArr(reverseArray(num1)) + combineArr(reverseArray(num2)))
    returnable = [x for x in result]
    return reverseArray(list(map(int, returnable)))

def reverseArray(arr: list):
    newArr = []
    for i in range(len(arr)-1, -1, -1):
        newArr.append(arr[i])
    return newArr

def combineArr(arr: list) -> int:
    str = ""
    for element in arr:
        str += element.__str__()
    return int(str)

print(addTwoNumbers(l1, l2))