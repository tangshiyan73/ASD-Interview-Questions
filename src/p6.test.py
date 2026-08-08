from p6 import find_max_occurrence

def run_tests():
    print("=== Running Unit Tests for Problem 6 (Max Character Occurrence) ===\n")

    test_cases = [
        {
            "name": "Sample Assignment Input",
            "input": "Hello, world!",
            "expected_char": "l",
            "expected_count": 3
        },
        {
            "name": "Case Sensitivity Check",
            "input": "HhHhHhhhh",
            "expected_char": "h",
            "expected_count": 6  # 'h' appears 6 times, 'H' appears 3 times
        },
        {
            "name": "Punctuation & Whitespace Ignored",
            "input": "   ! ? , . -- ... ",
            "expected_char": None,
            "expected_count": 0
        },
        {
            "name": "Unicode Characters (Chinese CJK)",
            "input": "你好，世界！你好 Python！",
            "expected_char": "你",  # '你' appears 2 times, '好' appears 2 times (returns either)
            "expected_count": 2
        },
        {
            "name": "Unicode Accents / Foreign Characters",
            "input": "Café, crêpe, éléphant",
            "expected_char": "é",
            "expected_count": 3
        }
    ]

    for tc in test_cases:
        char, count = find_max_occurrence(tc["input"])
        
        # If multiple characters tie, checking count is primary
        count_passed = (count == tc["expected_count"])
        char_passed = (char == tc["expected_char"]) if tc["expected_char"] is not None else (char is None)
        
        passed = count_passed and (char_passed or tc["name"] == "Unicode Characters (Chinese CJK)")
        status = "PASSED ✓" if passed else "FAILED ✗"

        print(f"[{status}] Test: {tc['name']}")
        print(f"  Input String:    \"{tc['input']}\"")
        print(f"  Expected Output: Character: '{tc['expected_char']}', Occurrence: {tc['expected_count']}")
        print(f"  Actual Output:   Character: '{char}', Occurrence: {count}")
        print("-" * 50)
        assert passed, f"Failed on {tc['name']}"

    print("\nAll Problem 6 tests completed successfully!")


if __name__ == "__main__":
    run_tests()