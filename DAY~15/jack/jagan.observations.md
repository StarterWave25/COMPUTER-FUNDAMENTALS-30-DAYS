## option 1:we will take 2 2 elements and find cost 
## option 2:we take entire array and finds cost

const arr = [1,2,3,4,100]
let cost = 0

for(let i = 0;i<arr.length-1;i++){
    let m = (arr[i]>arr[i+1])?arr[i]:arr[i+1]
    console.log(arr[i]);
    console.log(arr[i+1]);
    console.log(m);
    cost +=m*2
    console.log(cost);
    console.log("====\n");
}





output:
1
2
2
4
====

2
3
3
10
====

3
4
4
18
====

4
100
100
218
====