# Problem: The Influence Array

You are given an integer array.

Each element has an "influence score".

The influence score of an element is:

> Number of elements to its left that are smaller than it
>
> minus
>
> Number of elements to its right that are larger than it

For every element, calculate its influence score.

# my Aproach :i will use a single loop for each element with clean and neat code styles with comment documentation
1. i will take an outer loop to iterate each element 
2. in inner loop i will take every element and i will iterate through and i will check tha it is right to the elemnt or left and also less value or large value for current element also 
3. then i will caluclate theinf score and i will place that in arr directly with the outer loop i index
## updated..
4. then i will caluclate the powscore for each now i will store them in a object and i will push objects into array
5. at last find the max power score and i will display the highest power score element!! 