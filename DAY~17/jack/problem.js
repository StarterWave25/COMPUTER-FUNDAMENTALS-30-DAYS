const arr = [4, 2, 7, 1, 5];
const inf = [];
for (let i = 0; i < arr.length; i++) {
    let le = 0;
    let re = 0;
  for (let j = 0; j < arr.length; j++) {
    console.log("------------");
    
    if (j < i) {
      console.log(arr[i]);
      console.log(arr[j]);

      if (arr[j] < arr[i]) {
        le++;
      }
    }
    if (j > i) {
      console.log(arr[i]);
      console.log(arr[j]);
      if (arr[j] > arr[i]) {
        re++;
      }
    }
    console.log(le);
    console.log(re);
    console.log("------------");
  }
  inf.push(le - re);
}
console.log(inf);
