// Standard FizzBuzz: check divisibility by 15 first (both 3 and 5), then 3, then 5.
function fizzBuzz(n = 100) {
  const output = [];
  for (let i = 1; i <= n; i++) {
    // order matters: 15 must be checked before 3 or 5, otherwise multiples
    // of 15 would incorrectly get caught by the 3 or 5 branch first
    if (i % 15 === 0) output.push('FizzBuzz');
    else if (i % 3 === 0) output.push('Fizz');
    else if (i % 5 === 0) output.push('Buzz');
    else output.push(String(i));
  }
  return output;
}

module.exports = { fizzBuzz };
