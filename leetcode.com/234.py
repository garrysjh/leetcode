#palindrome linked list
#given teh head of a singly linked list, return true if palindrome or false otherwise

def isPalindrome(self, head) -> bool:
    vals = []
    current_node = head
    while current_node is not None:
        vals.append(current_node.val)
        current_node = current_node.next
    return vals == vals[::-1]

print(isPalindrome([1,2,3,2,1]))
        
