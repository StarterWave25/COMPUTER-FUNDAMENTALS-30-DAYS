# The goal is to reduce the array into a single number at the last.

# For this process we need to follow the compression rule =>

## ->For every subarray choosen to be compressed, we have to pick the largest element of that subarray and replace it in the place of the original subarray in the main array

## ->This comes with a cost => length of the subarray X max. element of the subarray.

# I have noticed one thing, after compression, there is only one element in the array remaining, that is the max element of the array itself.

# And i have tried with some examples numbers 1 to 5 in ascending order, descending order and same elements in the array as per the problem statement in the md file, and came to a conclusion:-

## -> Largest element of the array lives to the end, if it may be in the first or last, it remains to end.

## -> If the largest element is in the starting of the array, it gets passed on the going turns in turn increasing the sum

## -> for each turn, how smallest the max is, that much cost of compression is going to optimize.

## -> So sorting the array in ascending order is best for reducing cost as it pushes the max to the last

## -> And also how much large the subarray size is, that much cost is going to reduce, upon decreasing the subarray size, cost is going to increase. This condition doesn't apply to the descending sorted array as the max element is at start, but in that case also decreasing subarray size helps for reducing cost, but not much than ascending and doing the same process.

## ->If all the elements are equal, then increasing the subarray size in turn reducing the number of turns is going to help reduce the cost of the array, and sorting doesn't help as all elements are equal.

## ->And also how small the original array size is and how small it's elements are , that much cost is going to reduce.
