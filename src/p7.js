// Binary search between 0 and x for the value whose square equals x. No Math.sqrt used.
function sqrt(x) {
  if (x < 0) throw new Error('x must be non-negative');
  if (x === 0 || x === 1) return x; // sqrt(0)=0, sqrt(1)=1, no search needed

  let low = 0, high = x;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    const square = mid * mid;
    if (square === x) return mid;        // found the exact root
    else if (square < x) low = mid + 1;  // root is larger — search upper half
    else high = mid - 1;                 // root is smaller — search lower half
  }
  return -1; // shouldn't be reached given x is guaranteed a perfect square
}

module.exports = { sqrt };
