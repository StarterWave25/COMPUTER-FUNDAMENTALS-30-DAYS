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



