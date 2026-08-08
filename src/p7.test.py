from p7 import integer_square_root

def run_tests():
    print("=== Running Unit Tests for Problem 7 (Square Root) ===\n")

    test_cases = [
        {"name": "Base Case x = 0", "input": 0, "expected": 0},
        {"name": "Base Case x = 1", "input": 1, "expected": 1},
        {"name": "Sample Case x = 4", "input": 4, "expected": 2},
        {"name": "Sample Case x = 9", "input": 9, "expected": 3},
        {"name": "Sample Case x = 16", "input": 16, "expected": 4},
        {"name": "Sample Case x = 25", "input": 25, "expected": 5},
        {"name": "Sample Case x = 36", "input": 36, "expected": 6},
        {"name": "Larger Perfect Square x = 10000", "input": 10000, "expected": 100},
        {"name": "Very Large Perfect Square x = 123456789^2", "input": 15241578750190521, "expected": 123456789}
    ]

    for tc in test_cases:
        actual = integer_square_root(tc["input"])
        passed = actual == tc["expected"]
        status = "PASSED ✓" if passed else "FAILED ✗"

        print(f"[{status}] Test: {tc['name']}")
        print(f"  Input:           x = {tc['input']}")
        print(f"  Expected Output: {tc['expected']}")
        print(f"  Actual Output:   {actual}")
        print("-" * 50)
        assert passed, f"Failed on {tc['name']}"

    print("\nAll Problem 7 tests completed successfully!")


if __name__ == "__main__":
    run_tests()