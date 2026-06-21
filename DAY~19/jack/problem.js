const arr = [5, 2, 8, 2, 7, 5]
const dists = [];
for(let i =0;i<arr.length;i++){
   
    for(let j =0;j<arr.length;j++){
        console.log("E:"+arr[i]+" CE:"+arr[j]);
        
        if(i===j) continue;
        if(arr[i]===arr[j]){
            
                dists[i]=j-i;
            dists[j]=j-i;
            
            console.log("D:"+(j-i));
            console.log(dists);
        }
        
    }    
}

console.log(dists);
