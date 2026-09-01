// Naive recursive Fibonacci: fib(n) = fib(n-1) + fib(n-2), base cases 0 and 1.
function fibAt(n) {
  if (n === 0) return 0; // base case
  if (n === 1) return 1; // base case
  return fibAt(n - 1) + fibAt(n - 2); // recursive case — each call branches into two more
}

function fibonacci(count) {
  const sequence = [];
  for (let i = 0; i < count; i++) sequence.push(fibAt(i)); // build the sequence one term at a time
  return sequence;
}

module.exports = { fibonacci, fibAt };
