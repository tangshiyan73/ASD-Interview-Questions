from p3 import generate_fibonacci_sequence, fibonacci_recursive

def run_tests():
    print("--- Running Tests for Problem 3 (Fibonacci) ---")

    # Test Case 1: First 10 elements matching expected assignment output
    expected_10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    actual_10 = generate_fibonacci_sequence(10)
    _assert_test("First 10 Fibonacci elements", actual_10, expected_10)

    # Test Case 2: Edge case - count = 1
    _assert_test("Single element count = 1", generate_fibonacci_sequence(1), [0])

    # Test Case 3: Edge case - count = 2
    _assert_test("Two elements count = 2", generate_fibonacci_sequence(2), [0, 1])

    # Test Case 4: Individual recursive values
    _assert_test("fib(0) base case", fibonacci_recursive(0), 0)
    _assert_test("fib(1) base case", fibonacci_recursive(1), 1)
    _assert_test("fib(7) value check (13)", fibonacci_recursive(7), 13)

    print("\nAll tests completed!")


def _assert_test(test_name: str, actual, expected):
    passed = actual == expected
    status = "PASSED ✓" if passed else "FAILED ✗"
    print(f"\n{test_name}: {status}")
    print(f"  Expected: {expected}")
    print(f"  Actual:   {actual}")
    assert passed, f"Failed on {test_name}"


if __name__ == "__main__":
    run_tests()