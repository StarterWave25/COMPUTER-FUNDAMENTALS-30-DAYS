ar -> [4, 2, 7, 1, 5] -> n elements, inf[]

1. Iterate the entire array from **0 to n-1**.
2. For every element I iterate 2 loops:
Here, i -> current index, ar[i] -> current element.
- Loop 1: Iterate **i-1 to 0** and count the small numbers than ar[i].
- Loop 2: Iterate **i+1 to n-1** and count the large numbers than ar[i].
3. After completion of 2 loops, I will calculate the influence score of that element and **push into inf[] in index i**.
4. Print the influence scores of all elements.