"""
Problem 4: Find List Intersection without Library Functions

Language Choice: Python
Reason: Python allows clean implementation of hash tables (dictionaries) from scratch,
enabling fast element lookup without relying on built-in set intersection libraries.

Approach:
1. Build a lookup frequency map (dictionary) for the first list to record element presence in O(N) time.
2. Iterate through the second list. For each element present in our lookup map, add it to the intersection list.
3. Remove or mark processed elements in the lookup map to avoid duplicate values in the result.

Space-Time Complexity Analysis:
- Time Complexity: O(N + M)
  - Building lookup map for List 1 takes O(N) time, where N is length of List 1.
  - Scanning List 2 and checking dictionary keys takes O(M) time, where M is length of List 2.
  - Total Time: O(N + M) linear time.
- Space Complexity: O(N)
  - Auxiliary memory used to store elements of List 1 in the dictionary hash map.
"""

def find_list_intersection(list1: list[int], list2: list[int]) -> list[int]:
    """
    Finds common elements between list1 and list2 without using library functions like set.intersection().
    Preserves unique intersecting elements.
    """
    if not list1 or not list2:
        return []

    # Step 1: Create a lookup map for elements in list1 manually
    seen_in_list1 = {}
    for item in list1:
        seen_in_list1[item] = True

    intersection = []

    # Step 2: Iterate list2 and check against lookup map
    for item in list2:
        if item in seen_in_list1 and seen_in_list1[item]:
            intersection.append(item)
            # Mark as False/used so duplicates in list2 aren't added twice
            seen_in_list1[item] = False

    return intersection


# --- Interactive CLI Execution ---
if __name__ == "__main__":
    print("=== Problem 4: Find List Intersection ===")
    
    input1 = input(
        "Enter List 1 elements (comma or space separated)\n"
        "(or press Enter for default '4, 5, 2, 3, 1, 6'): "
    ).strip()
    
    input2 = input(
        "Enter List 2 elements (comma or space separated)\n"
        "(or press Enter for default '8, 7, 6, 9, 4, 5'): "
    ).strip()

    if not input1 or not input2:
        list1 = [4, 5, 2, 3, 1, 6]
        list2 = [8, 7, 6, 9, 4, 5]
        print("\nUsing default assignment lists...")
    else:
        try:
            list1 = [int(x) for x in input1.replace(",", " ").split()]
            list2 = [int(x) for x in input2.replace(",", " ").split()]
        except ValueError:
            print("\nError: Invalid input! Please enter valid integers.")
            exit(1)

    print(f"\nList 1: {list1}")
    print(f"List 2: {list2}")

    result = find_list_intersection(list1, list2)
    
    print("\nExpected Output (Intersection):")
    print(", ".join(map(str, result)))
    print()