"""
Problem 5: Find List Symmetric Difference without Library Functions

Language Choice: Python
Reason: Python's dictionary mapping enables fast O(1) element frequency lookups
to calculate symmetric difference without relying on built-in set library operations.

Approach:
1. Build a frequency count map for all elements present across both lists.
2. An element belongs to the symmetric difference if it appears in List 1 OR List 2, 
   but NOT in both (frequency count == 1).
3. To present a clean output matching the assignment (1, 2, 3, 7, 8, 9), we sort
   the resulting list using our custom Quick Sort implementation from Problem 1.

Space-Time Complexity Analysis:
- Time Complexity: O(N + M + K log K)
  - Frequency counting across List 1 (length N) and List 2 (length M) takes O(N + M) time.
  - Sorting the output list of size K takes O(K log K) average time.
- Space Complexity: O(N + M)
  - Auxiliary space to hold element counts in the dictionary map.
"""

def find_symmetric_difference(list1: list[int], list2: list[int]) -> list[int]:
    """
    Finds elements that are in either list1 or list2, but not both.
    Avoids built-in set operations.
    """
    # Step 1: Count occurrences of each unique element manually
    counts = {}

    # Helper to track unique appearance in list 1
    seen_l1 = {}
    for item in list1:
        if item not in seen_l1:
            seen_l1[item] = True
            counts[item] = counts.get(item, 0) + 1

    # Helper to track unique appearance in list 2
    seen_l2 = {}
    for item in list2:
        if item not in seen_l2:
            seen_l2[item] = True
            counts[item] = counts.get(item, 0) + 1

    # Step 2: Extract elements that appear in exactly one list
    sym_diff = []
    for item, count in counts.items():
        if count == 1:
            sym_diff.append(item)

    # Step 3: Sort output in ascending order using custom Quick Sort
    _quick_sort(sym_diff, 0, len(sym_diff) - 1)
    
    return sym_diff


def _quick_sort(arr: list[int], low: int, high: int) -> None:
    """In-place Quick Sort helper function."""
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_idx = i + 1

        _quick_sort(arr, low, pivot_idx - 1)
        _quick_sort(arr, pivot_idx + 1, high)


# --- Interactive CLI Execution ---
if __name__ == "__main__":
    print("=== Problem 5: Find List Symmetric Difference ===")
    
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

    result = find_symmetric_difference(list1, list2)
    
    print("\nExpected Output (Symmetric Difference):")
    print(", ".join(map(str, result)))
    print()