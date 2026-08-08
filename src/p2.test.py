from p2 import generate_fizzbuzz_range, generate_fizzbuzz_list, fizzbuzz_single

def run_tests():
    print("--- Running Tests for Problem 2 (FizzBuzz) ---")

    # Test Case 1: Custom set matching explicit inputs
    input_list = [1, 2, 3, 4, 5, 15]
    expected_list = ["1", "2", "Fizz", "4", "Buzz", "FizzBuzz"]
    _assert_test("Explicit list evaluation", generate_fizzbuzz_list(input_list), expected_list)

    # Test Case 2: Standard sequence (First 15 elements)
    res_15 = generate_fizzbuzz_range(15)
    expected_15 = [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]
    _assert_test("Range 1 to 15", res_15, expected_15)

    # Test Case 3: Individual functions
    _assert_test("Single check divisible by 3", fizzbuzz_single(9), "Fizz")
    _assert_test("Single check divisible by 5", fizzbuzz_single(20), "Buzz")
    _assert_test("Single check divisible by 3 and 5", fizzbuzz_single(30), "FizzBuzz")

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