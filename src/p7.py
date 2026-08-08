"""
Problem 7: Perfect Square Root Calculation

Language Choice: Python
Reason: Python's support for arbitrary-precision integers allows finding exact
square roots for arbitrarily large perfect squares without floating-point precision overflow.

Approach:
- Use Binary Search over the integer range [0, x].
- For a mid value `m`, if `m * m == x`, `m` is the exact square root.
- If `m * m < x`, search the upper half `[m + 1, right]`.
- If `m * m > x`, search the lower half `[left, m - 1]`.

Space-Time Complexity Analysis:
- Time Complexity: O(log x) — Binary search halves the search space at each iteration.
- Space Complexity: O(1) — Uses constant auxiliary memory (only a few integer pointers).
"""

def integer_square_root(x: int) -> int:
    """
    Calculates the exact square root of a non-negative perfect square integer x.
    Does not use math.sqrt() or external libraries.
    """
    if x < 0:
        raise ValueError("Input must be a non-negative integer.")
    if x == 0 or x == 1:
        return x

    left = 1
    right = x

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1

    raise ValueError(f"Input {x} is not a perfect square.")


# --- Interactive CLI Execution ---
if __name__ == "__main__":
    print("=== Problem 7: Perfect Square Root Calculator ===")
    user_input = input(
        "Enter a non-negative perfect square integer (e.g., 4, 9, 16, 25, 36, 100)\n"
        "(or press Enter for default 25): "
    ).strip()

    if not user_input:
        x = 25
        print("\nUsing default assignment input (x = 25)...")
    else:
        try:
            x = int(user_input)
            if x < 0:
                print("\nError: Input must be a non-negative integer.")
                exit(1)
        except ValueError:
            print("\nError: Invalid input! Please enter a valid integer.")
            exit(1)

    try:
        result = integer_square_root(x)
        print(f"\nInput: x = {x}")
        print(f"Expected Output: {result}")
        print(f"Verification: {result} * {result} = {result * result}\n")
    except ValueError as e:
        print(f"\nError: {e}\n")