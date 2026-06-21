```
Problem Understanding:

We need to take an as the input,

and for every element we need to find the nearest of that value.
```

```
My Approach:

Input:
Accept the array as input.

Outer Loop:
Iterate sequentially through each element of array.

Inner Loops:
For the current element, execute two separate inner loops.

- Left Scan: From the element immediately preceding of current element to 0 index.
- Right Scan: From the element following the current index to end of the array.

Comparision:
During these inner loops,
I will check the surrounding numbers are equal or not,
And i will store left & right found indices.

Calculation:
After completing both inner loops for the current element, i will check which one is near based on that i will store the nearest occurence in new array.
```