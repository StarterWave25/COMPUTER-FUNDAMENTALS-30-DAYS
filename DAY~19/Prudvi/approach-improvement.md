```
Input: Accept the array. [5, 3, 2, 8, 5, 4]

Loop: 

1. Will the current element now (5).
2. We already have a object(sol), now update that object.

3. if we found the current element in object, in that key add one more object as a value. which 
ie, {5: {0:2, 3: 2, 6: 3}}


4. If we don't found the current element in object, we will update the object with this value as a key.

i.e, {5:?}
now, for the value of that key,
will store a object in that we have index and distance. But now it is found for that first so will index and value as 1.
i.e, {5: {0:-1}, 3: {1: -1}}
```