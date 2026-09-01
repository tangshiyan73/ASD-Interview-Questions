// Merge sort: split array in half recursively, then merge two sorted halves.

function mergeSort(arr) {
  if (arr.length <= 1) return arr; // base case: a single element (or empty) is already sorted

  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));   // recursively sort left half
  const right = mergeSort(arr.slice(mid));     // recursively sort right half
  return merge(left, right);                   // combine the two sorted halves
}

function merge(left, right) {
  const result = [];
  let i = 0, j = 0;
  // walk both halves together, always taking the smaller front element
  while (i < left.length && j < right.length) {
    result.push(left[i] <= right[j] ? left[i++] : right[j++]);
  }
  // one half may still have leftover elements — they're already sorted, just append
  while (i < left.length) result.push(left[i++]);
  while (j < right.length) result.push(right[j++]);
  return result;
}

module.exports = { mergeSort };
