#given the head of a singly linked list, return the middle node of the linked list
#if there are 2 middle nods, return the second linked list

def linkedMiddle(head) -> int:
    vals = []
    current_node = head
    while current_node is not None:
        vals.append(current_node.val)
        current_node = current_node.next
    if len(vals)%2 == 0:
        return vals[((len(vals)/2)+1)]
    else:
        return vals[(len(vals)/2)]
head = [1,2,3]
print(linkedMiddle(head))