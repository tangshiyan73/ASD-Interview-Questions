// Hash first list into a lookup object, then scan second list for matches. O(n+m), no built-ins.
function intersection(list1, list2) {
  const seen = {};
  for (let i = 0; i < list1.length; i++) seen[list1[i]] = true; // O(1) lookup table for list1

  const result = [];
  const added = {}; // tracks what's already in result, so duplicates in list2 don't repeat
  for (let i = 0; i < list2.length; i++) {
    const val = list2[i];
    if (seen[val] && !added[val]) { // present in both lists, and not already output
      result.push(val);
      added[val] = true;
    }
  }
  return result;
}

module.exports = { intersection };
