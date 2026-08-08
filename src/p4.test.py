from p4 import find_list_intersection

def run_tests():
    print("=== Running Unit Tests for Problem 4 (List Intersection) ===\n")

    test_cases = [
        {
            "name": "Sample Assignment Input",
            "list1": [4, 5, 2, 3, 1, 6],
            "list2": [8, 7, 6, 9, 4, 5],
            "expected": [4, 5, 6]  # Sorted order check
        },
        {
            "name": "No Common Elements (Disjoint)",
            "list1": [1, 2, 3],
            "list2": [4, 5, 6],
            "expected": []
        },
        {
            "name": "Identical Lists (Complete Overlap)",
            "list1": [10, 20],
            "list2": [10, 20],
            "expected": [10, 20]
        },
        {
            "name": "Lists with Duplicates",
            "list1": [1, 2, 2, 3],
            "list2": [2, 2, 4],
            "expected": [2]
        }
    ]

    for tc in test_cases:
        actual = find_list_intersection(tc["list1"], tc["list2"])
        # Compare sorted to ignore order variations
        passed = sorted(actual) == tc["expected"]
        status = "PASSED ✓" if passed else "FAILED ✗"

        print(f"[{status}] Test: {tc['name']}")
        print(f"  Input List 1: {tc['list1']}")
        print(f"  Input List 2: {tc['list2']}")
        print(f"  Expected Output: {tc['expected']}")
        print(f"  Actual Output:   {actual}")
        print("-" * 50)
        assert passed, f"Failed on {tc['name']}"

    print("\nAll Problem 4 tests completed successfully!")


if __name__ == "__main__":
    run_tests()