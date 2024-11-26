"""Module providing a solution to leetcode problem X."""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    """Solution."""

    def addTwoNumbersRest(self, l1: Optional[ListNode], l2: Optional[ListNode], l3: Optional[ListNode], rest: int):
        val1 = 0
        val2 = 0

        if l1 != None:
            val1 = l1.val
        if l2 != None:
            val2 = l2.val

        result = val1 + val2 + rest

        if result < 10:
            pass
            rest = 0
        else:
            rest = 1
            result = result - 10

        
        l3.val = result

        if rest == 0 and (l1 == None or l1.next == None) and (l2 == None or l2.next == None):
            return
        else:
            res = ListNode(result)
            l3.next = res

            if l1 == None:
                self.addTwoNumbersRest(None, l2.next, l3.next,rest)
            elif l2 == None:
                self.addTwoNumbersRest(l1.next, None, l3.next,rest)
            else:
                self.addTwoNumbersRest(l1.next, l2.next, l3.next,rest)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       l3 = ListNode()
       self.addTwoNumbersRest(l1,l2,l3,0)
       return l3

if __name__ == '__main__':
    pass