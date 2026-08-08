from p9 import find_node_path, SAMPLE_GRAPH

def run_tests():
    print("=== Running Unit Tests for Problem 9 (Node Path Existence) ===\n")

    test_cases = [
        {
            "name": "Example 1: No Path (D to B)",
            "start": "D",
            "end": "B",
            "expected": "False"
        },
        {
            "name": "Example 2: Valid Path (F to A)",
            "start": "F",
            "end": "A",
            "expected": "True (F --> B --> A)"
        },
        {
            "name": "Example 3: Dead End Node (G to C)",
            "start": "G",
            "end": "C",
            "expected": "False"
        },
        {
            "name": "Example 4: Multi-hop Path (E to D)",
            "start": "E",
            "end": "D",
            "expected": "True (E --> F --> B --> D)"
        },
        {
            "name": "Disconnected Isolated Node (H to A)",
            "start": "H",
            "end": "A",
            "expected": "False"
        }
    ]

    for tc in test_cases:
        actual = find_node_path(SAMPLE_GRAPH, tc["start"], tc["end"])
        passed = (actual == tc["expected"])
        status = "PASSED ✓" if passed else "FAILED ✗"

        print(f"[{status}] Test: {tc['name']}")
        print(f"  Input:           Start = {tc['start']}, End = {tc['end']}")
        print(f"  Expected Output: {tc['expected']}")
        print(f"  Actual Output:   {actual}")
        print("-" * 50)
        assert passed, f"Failed on {tc['name']}"

    print("\nAll Problem 9 tests completed successfully!")


if __name__ == "__main__":
    run_tests()