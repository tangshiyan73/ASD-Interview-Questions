"""
Problem 2: FizzBuzz

Language Choice: Python
Reason: Python's concise list comprehensions and intuitive conditional logic make
it ideal for clear, readable implementation of classic logic problems.

Approach:
- Evaluate each number against divisibility conditions using modulo operator (%):
  - Divisible by both 3 and 5 (i.e. divisible by 15) -> "FizzBuzz"
  - Divisible by 3 -> "Fizz"
  - Divisible by 5 -> "Buzz"
  - Otherwise -> return the number as a string.
- Supports both array/list input and integer upper-bound limit.

Space-Time Complexity Analysis:
- Time Complexity: O(N) — Iterates through N numbers exactly once with O(1) modulo checks per number.
- Space Complexity: O(N) — Stores resulting output values in a list of size N.
"""

def fizzbuzz_single(num: int) -> str:
    """
    Evaluates a single number for FizzBuzz rules.
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


def generate_fizzbuzz_list(numbers: list[int]) -> list[str]:
    """
    Evaluates a list of explicit numbers against FizzBuzz rules.
    """
    return [fizzbuzz_single(n) for n in numbers]


def generate_fizzbuzz_range(n: int = 100) -> list[str]:
    """
    Generates FizzBuzz values for range 1 to n.
    """
    return [fizzbuzz_single(i) for i in range(1, n + 1)]


# --- Interactive CLI Execution ---
if __name__ == "__main__":
    print("=== Problem 2: Flexible FizzBuzz Evaluator ===")
    user_input = input(
        "Enter a single limit integer (e.g., 100)\n"
        "OR a list of numbers separated by space or comma (e.g., 1, 2, 3, 4, 5, 15)\n"
        "(or press Enter for default range 1 to 100): "
    ).strip()

    if not user_input:
        # Default assignment case: range 1 to 100
        print("\nUsing default range (1 to 100)...")
        results = generate_fizzbuzz_range(100)
    else:
        # Clean input by converting commas into spaces
        cleaned = user_input.replace(",", " ")
        parts = cleaned.split()

        try:
            parsed_numbers = [int(p) for p in parts]
            
            # If user provided a single positive integer, generate 1 to N
            if len(parsed_numbers) == 1 and parsed_numbers[0] > 0:
                limit = parsed_numbers[0]
                print(f"\nGenerating FizzBuzz for range 1 to {limit}...")
                results = generate_fizzbuzz_range(limit)
            else:
                # User provided multiple numbers or explicit custom set
                print(f"\nEvaluating custom input set ({len(parsed_numbers)} items)...")
                results = generate_fizzbuzz_list(parsed_numbers)
                
        except ValueError:
            print("\nError: Invalid input! Please enter valid integer numbers.")
            exit(1)

    # Display expected output formatted with commas
    print("\nExpected Output:")
    print(", ".join(results))
    print()