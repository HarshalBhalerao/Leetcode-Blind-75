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
