**Finding the Low Operation Cost**
```
1. Here you need take the sub-arrays in array and find the maximum value in it and replace that entire sub-array with maximum value you found in the sub-array.

2. Every operation will cost length of subarray x maximum value in subarray.

3. Goal is to find the Low Operation Cost.. which is optimal solution

4. To divide the sub arrays.., we need to keep the length of the sub array to be 2 for last to Elments of the array.. as we arrange the elements in the ascending array.. and the first elements making the largeat subarray.

5. At last take the whole note of Costs and add them .. to find the low optimal cost.

6. So we will get the operation which is the lowest one.

```

[5,10,8,9,12,30] 

[5,8,9,10,12,30] 

5,8,9 => 27
10,12,30 => 90
9,30 => 60
total = 177



1,2,3,4,5,6,7,8,9,10 

1,2,3,4,5 => 25
5,6,7,8,9,10 => 60
total => 85

1,2,3,4,,5 => 25        
6,7,8,9,10 => 50
5,10 => 20
total = 95


[1, 100, 1] 

```

1,100 = 200
100,1 = 200 => 400

1,100,1 => 300

```

[1, 100, 1, 1]

```

1,100,1 => 300
100,1 => 200 => 500

1,100,1,1 => 400

```

[1, 100, 1, 1, 1]

```

1,100,1 => 300
1,1  => 2

```