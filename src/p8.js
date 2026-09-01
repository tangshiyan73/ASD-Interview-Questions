// Strip non-alphanumeric chars and lowercase both strings, then compare character counts.
function isAlphaNumeric(ch) {
  return (ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9');
}

function normalize(str) {
  let result = '';
  for (let i = 0; i < str.length; i++) {
    const ch = str[i].toLowerCase();
    if (isAlphaNumeric(ch)) result += ch; // drops whitespace/punctuation, per spec
  }
  return result;
}

function isAnagram(str1, str2) {
  const a = normalize(str1);
  const b = normalize(str2);
  if (a.length !== b.length) return false; // different lengths can never be anagrams

  const counts = {};
  for (let i = 0; i < a.length; i++) counts[a[i]] = (counts[a[i]] || 0) + 1; // tally chars in `a`
  for (let i = 0; i < b.length; i++) {
    const ch = b[i];
    if (!counts[ch]) return false; // `b` has a char `a` doesn't (or used up all of it)
    counts[ch]--;                  // "consume" one occurrence
  }
  return true; // all of `b`'s characters were matched and consumed from `a`'s counts
}

module.exports = { isAnagram };
