```
Problem Understanding:

We need to take an array as the input,

and for every element we need to calculate the influence score.

so what is it:
For every element - It is the subtraction of,

count of numbers smaller than the current number and presented in the left side of it.

and 

count of numbers larger than the current number and presented in the right of it.
```

```
My Approach:

Input:
Accept the array as input.


Outer Loop:
Iterate sequentially through each element of array.


Inner Loops:
For the current element, execute two separate inner loops.

 - Left Scan: From index 0 to immediately preceding of current element.

 - Right Scan: From the element immediately following the current element to end of the array.

Comparison:
During these inner loops,
check whether the surrounding numbers are larger or smaller than the current element,
and increment the respective counts.

Calculation:
After completing both inner loops for the current element, calculate it's "influence score" based on those counts and store the result in new array.

```