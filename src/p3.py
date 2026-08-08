"""
Problem 3: Fibonacci Sequence with Recursion

Language Choice: Python
Reason: Python allows simple, expressive recursive function definitions while
providing built-in memoization (`@lru_cache`) to optimize performance and prevent call stack depth issues.

Approach:
- Recursive definition: fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2).
- Uses memoization (`functools.lru_cache`) to cache recursive calls, turning O(2^N) exponential time into O(N) linear time.

Space-Time Complexity Analysis:
- Time Complexity: O(N) — With memoization, each Fibonacci term from 0 to N is calculated exactly once.
- Space Complexity: O(N) — Required for both the call stack depth and the memoization lookup cache.

Bonus Answer (Preventing Stack Overflow):
1. Memoization (Caching): Storing previously calculated results prevents duplicate recursive branches.
2. Iteration / Dynamic Programming: Replacing recursion with an iterative loop eliminates function call stack overhead completely, running in O(1) space.
3. Tail Call Optimization / Increasing Recursion Limit: Python has a default recursion limit (~1000). For large N, an iterative bottom-up approach or matrix exponentiation is preferred.
"""

from functools import lru_cache
import sys

# Optional: Adjust default recursion depth limit for moderately large inputs if needed
sys.setrecursionlimit(2000)


@lru_cache(maxsize=None)
def fibonacci_recursive(n: int) -> int:
    """
    Computes the nth Fibonacci number recursively with memoization.
    Base cases: fib(0) = 0, fib(1) = 1
    """
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative integers.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def generate_fibonacci_sequence(count: int) -> list[int]:
    """
    Generates the first `count` numbers of the Fibonacci sequence.
    Example: count = 10 -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if count <= 0:
        return []
    return [fibonacci_recursive(i) for i in range(count)]


# --- Interactive CLI Execution ---
if __name__ == "__main__":
    print("=== Problem 3: Recursive Fibonacci Generator ===")
    user_input = input(
        "Enter the number of Fibonacci elements to generate (e.g., 10)\n"
        "(or press Enter for default 10 elements): "
    ).strip()

    if not user_input:
        count = 10
        print("\nUsing default count (10 elements)...")
    else:
        try:
            count = int(user_input)
            if count < 1:
                print("\nError: Count must be a positive integer greater than 0.")
                exit(1)
        except ValueError:
            print("\nError: Invalid input! Please enter a valid positive integer.")
            exit(1)

    sequence = generate_fibonacci_sequence(count)
    
    print(f"\nFibonacci Sequence ({count} elements):")
    print(", ".join(map(str, sequence)))
    print()