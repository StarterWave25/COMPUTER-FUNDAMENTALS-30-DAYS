# **Understanding:** I need to find the distance of each element to its same nearest element in the array.

# **Brute force Approach:**
## ar = [1,2,3]
1. I use nested loops which the outer loop & inner loop.
2. **Outer loop:** To select the each element from the array using i as index.
3. **Inner loop:** To find out the same nearest element in the array using j as index.
- I will check if each element in the array is equal to the selected element **(ar[i] == ar[j])** by the outer loop(i) except the same postion element **(i != j)**.
- If it finds any same element then I will store the distance between them.
- For the first time when a same element is found, then we will store the distance directly. If we found the same element for the second time, then we will compare the previous distance to the new distance, and we will finalize the least one among them.
- After completion of all iterations of the inner loop for an element, we will store the distance in a navier array at the same index i.
- If any element doesn't have the same repeated element in the array, then we will store its distance as -1.
4. Finally, we will print all the distances of the elements of the array.

# **Optimized Approach:**
1. 