// Hash both lists, collect elements present in only one, then sort (small insertion sort, no built-ins).
function symmetricDifference(list1, list2) {
  const in1 = {};
  const in2 = {};
  for (let i = 0; i < list1.length; i++) in1[list1[i]] = true;
  for (let i = 0; i < list2.length; i++) in2[list2[i]] = true;

  const result = [];
  // elements only in list1
  for (const key in in1) if (!in2[key]) result.push(Number(key));
  // elements only in list2
  for (const key in in2) if (!in1[key]) result.push(Number(key));

  return insertionSort(result); // output must be ascending per spec
}

function insertionSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    const current = arr[i];
    let j = i - 1;
    // shift larger elements one position right to make room for `current`
    while (j >= 0 && arr[j] > current) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = current;
  }
  return arr;
}

module.exports = { symmetricDifference };
