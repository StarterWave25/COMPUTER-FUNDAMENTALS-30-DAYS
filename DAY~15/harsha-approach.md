Cost = length of sub array x max of sub array

Total Cost = cost of each operations

1. [1,2,3,4,5]

[1,2] -> 2 * 2 = 4, 
[2,3] -> 2 * 3 = 6, 
[3,4] -> 2 * 4 = 8, 
[4,5] -> 2 * 5 = 10

Total = 28 -> 2 elements for each sub array
---
[1,2,3] -> 3 * 3 = 9,
[3,4,5] -> 3 * 5 = 15

Total = 24 -> Half of the array as sub arrays

N is even then sub array size is N/2.
N is odd then sub array size is (N+1)/2.
---

[1,2,3,4,5] -> 5 * 5 = 25

Total = 25 -> Entire array as sub array

I will select the 2nd approach.
---


2. [5,4,3,2,1]

Half:
[5,4,3] -> 3 * 5 = 15
[5,2,1] -> 3 * 5 = 15

Total = 30
---
Full:
[5,4,3,2,1] -> 5 * 5 = 25

Total = 25
---


3. [7,7,7,7,7]

Half:
[7,7,7] -> 3 * 7 = 21
[7,7,7] -> 3 * 7 = 21

Total = 42
---
Full:
[7,7,7,7,7] -> 5 * 7 = 35


# We need to reduce the no of operations to minimize the total cost. So, the best approach is to choose the entire array as sub array and finding the maximum element in it.