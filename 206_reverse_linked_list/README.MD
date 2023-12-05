# 206. Reverse Linked List

## Iterative Solution
- We need two pointers: curr and prev
- prev pointer should point to NULL and curr pointer should point to head
- Now we iterate through the list until curr isn't NULL
- To reverse, curr.next should point to prev, which initially is NULL.
- prev pointer should point to curr 
- and curr point should move to the next item in the linked list (curr.next). Here we are updating the rest of the list which should be avoided.
- Thus, we need a new pointer called remainingList. This should point to curr.next, we add this line of code after the while loop. And point curr to remainingList.
- Now we have the entire linked list reversed in prev pointer. Thus, we return it.

Time Complexity: O(n) and Space Complexity: O(1)

## Recursive Solution
- Note: For this solution, the last node is going to be the new head.
- Base case: if our head is null, then we will return null
- Now, we would set our newHead to head
- If our head.next is not null, then
- Set newHead to our function reverseList and pass in head.next as the parameter (recursion)
- In order to reverse head.next, we get the next node of head.next (head.next.next) and set it to our head
- Then we set the reversed head's next pointer to null.

Eg: head -> 1 -> 2 -> 3 -> null

Reverse using recursion:
- head -> 3 -> null 
- head -> 3 -> 2 -> null 
- head -> 3 -> 2 -> 1 -> null

Time Complexity: O(n) and Space Complexity: O(n)
