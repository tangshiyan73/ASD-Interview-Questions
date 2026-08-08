from p1 import sort_ascending

def run_tests():
    print("--- Running Tests for Problem 1 ---")

    # Test Case 1: Provided Input
    input1 = [21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28]
    expected1 = [-36, -16, -3, 8, 21, 28, 55, 77, 99, 111, 400]
    _assert_test("Test Case 1 (Sample Input)", input1, expected1)

    # Test Case 2: Already Sorted List
    input2 = [1, 2, 3, 4, 5]
    expected2 = [1, 2, 3, 4, 5]
    _assert_test("Test Case 2 (Already Sorted)", input2, expected2)

    # Test Case 3: Reverse Sorted List
    input3 = [10, 5, 0, -5, -10]
    expected3 = [-10, -5, 0, 5, 10]
    _assert_test("Test Case 3 (Reverse Sorted)", input3, expected3)

    # Test Case 4: List with Duplicate Values
    input4 = [5, 1, 5, -2, 1, 0]
    expected4 = [-2, 0, 1, 1, 5, 5]
    _assert_test("Test Case 4 (Duplicates)", input4, expected4)

    print("\nAll tests completed!")


def _assert_test(test_name: str, input_data: list[int], expected: list[int]):
    result = sort_ascending(input_data.copy())
    passed = result == expected
    status = "PASSED ✓" if passed else "FAILED ✗"
    
    print(f"\n{test_name}: {status}")
    print(f"  Expected Output: {expected}")
    print(f"  Actual Output:   {result}")
    assert passed, f"Failed on {test_name}"


if __name__ == "__main__":
    run_tests()