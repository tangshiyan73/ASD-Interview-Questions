"""
Problem 1: Sorting numbers in ascending order without library functions.

Language Choice: Python
Reason: Python offers clean, readable code and clear syntax for algorithmic tasks,
making custom algorithm implementations direct and concise.

Approach:
- Implemented Quick Sort algorithm using a divide-and-conquer strategy.
- Selects a pivot element and partitions the array into two sub-arrays:
  elements smaller than or equal to pivot go to the left, elements greater go to the right.
- Recursively sorts the sub-arrays in-place.

Space-Time Complexity Analysis:
- Time Complexity:
  - Best & Average Case: O(N log N) — Dividing the array roughly in half at each recursive level.
  - Worst Case: O(N^2) — Occurs when the pivot choice is consistently extreme (e.g., already sorted array).
- Space Complexity:
  - Auxiliary Space: O(log N) — Stack space required for recursive function calls.
"""

def sort_ascending(arr: list[int]) -> list[int]:
    """
    Main entry point for sorting. Sorts the list in-place using Quick Sort.
    """
    if not arr or len(arr) <= 1:
        return arr
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr: list[int], low: int, high: int) -> None:
    """
    Recursive helper function for Quick Sort.
    """
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = _partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        _quick_sort(arr, low, pivot_index - 1)
        _quick_sort(arr, pivot_index + 1, high)


def _partition(arr: list[int], low: int, high: int) -> int:
    """
    Partitions the sub-array around a pivot (uses the last element as pivot).
    """
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# --- Interactive CLI Execution ---
if __name__ == "__main__":
    print("=== Problem 1: Custom Array Sorter ===")
    user_input = input("Enter numbers separated by commas or spaces\n(or press Enter to use default sample): ").strip()

    if not user_input:
        # Default assignment numbers
        numbers = [21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28]
        print("\nUsing default assignment input...")
    else:
        # Parse user-entered numbers
        try:
            # Replaces commas with spaces, then splits by space and converts to integers
            cleaned_input = user_input.replace(",", " ")
            numbers = [int(x) for x in cleaned_input.split()]
        except ValueError:
            print("\nError: Invalid input! Please enter valid integers.")
            exit(1)

    print(f"\nOriginal List: {numbers}")
    
    # Sort a copy so we preserve the original display
    sorted_numbers = sort_ascending(numbers.copy())
    
    print(f"Sorted List:   {sorted_numbers}\n")