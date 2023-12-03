# Two Sum
We use hashmap for the optimal solution. Lets consider we have the array [2, 1, 5, 3] and target = 4.

First we would visit 2 from the array, and then perform subtraction -> target - 2
- Does the result from the subtraction exist in the hashmap, if it does then we get the index of that element from the hashmap.
- Else, if we don't find the result we add this element to our hashmap. So, our hashmap would contain the element and its respective index.
- We keep doing this until we reach the end of the array. If we find the result we just return the indices of those elements.

Time complexity is O(n) as we are iterating through the array. Space complexity if O(n) as we are storing those elements in the hashmap.
