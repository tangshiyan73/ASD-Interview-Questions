from p5 import find_symmetric_difference

def run_tests():
    print("=== Running Unit Tests for Problem 5 (Symmetric Difference) ===\n")

    test_cases = [
        {
            "name": "Sample Assignment Input",
            "list1": [4, 5, 2, 3, 1, 6],
            "list2": [8, 7, 6, 9, 4, 5],
            "expected": [1, 2, 3, 7, 8, 9]
        },
        {
            "name": "Disjoint Lists (No Overlap)",
            "list1": [1, 2],
            "list2": [3, 4],
            "expected": [1, 2, 3, 4]
        },
        {
            "name": "Identical Lists (100% Overlap)",
            "list1": [10, 20],
            "list2": [10, 20],
            "expected": []
        },
        {
            "name": "One Empty List Boundary Test",
            "list1": [5, 10, 15],
            "list2": [],
            "expected": [5, 10, 15]
        }
    ]

    for tc in test_cases:
        actual = find_symmetric_difference(tc["list1"], tc["list2"])
        passed = actual == tc["expected"]
        status = "PASSED ✓" if passed else "FAILED ✗"

        print(f"[{status}] Test: {tc['name']}")
        print(f"  Input List 1: {tc['list1']}")
        print(f"  Input List 2: {tc['list2']}")
        print(f"  Expected Output: {tc['expected']}")
        print(f"  Actual Output:   {actual}")
        print("-" * 50)
        assert passed, f"Failed on {tc['name']}"

    print("\nAll Problem 5 tests completed successfully!")


if __name__ == "__main__":
    run_tests()