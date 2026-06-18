const arr = [4, 2, 7, 1];
const scores = [];
for (let i = 0; i < arr.length; i++) {
    const currentElement = arr[i];
    let smallerOnLeft = 0; // Count elements smaller than arr[i] on left
    let largerOnRight = 0; // Count elements larger than arr[i] on right
  for (let j = 0; j < arr.length; j++) {
     const compareElement = arr[j];
    if(j===i) continue; // Skip current element itself

        // Count smaller elements on the left
    if(j<i && compareElement < currentElement) {
      smallerOnLeft++;
    }

      // Count larger elements on the right
    if(j>i && compareElement > currentElement) {
      largerOnRight++;
    }
   
  }
  // calulate infScore
  const infScore = smallerOnLeft - largerOnRight;
   // Calculate final scores
 scores[i] = {
    infScore:infScore,
    powScore:infScore * currentElement
 }
};
console.log(scores );
//option 1:
// const maxPowScore = scores.reduce((max,scoreObj)=>{
//     return scoreObj.powScore > max ?scoreObj.powScore : max;
// },scores[0].powScore);

//option 2:
const maxPowScore = Math.max(...scores.map(obj => obj.powScore));
console.log(...scores.map(obj => obj.powScore));

console.log(maxPowScore); //display maxpowScore

//finds highest powScore element
let highestPowScoreElement = scores.find(scoreObj => scoreObj.powScore === maxPowScore);
console.log(highestPowScoreElement);
