const ar = [4, 2, 7, 1, 5];
const SIZE = ar.length;
const inf = [];

for (let i = 0; i < SIZE; i++) {
    
    let leftCount = 0, rightCount = 0;

    for (let left = i - 1; left >= 0; left--) {
        if (ar[i] > ar[left]) leftCount++;
    }

    for (let right = i + 1; right < SIZE; right++) {
        if (ar[i] < ar[right]) rightCount++;
    }

    inf[i] = leftCount - rightCount;
}

console.log(inf);