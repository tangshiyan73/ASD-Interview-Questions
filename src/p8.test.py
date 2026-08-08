from p8 import are_anagrams

def run_tests():
    print("=== Running Unit Tests for Problem 8 (Anagram Checker) ===\n")

    test_cases = [
        {
            "name": "Example 1: Basic Anagram",
            "str1": "listen",
            "str2": "silent",
            "expected": True
        },
        {
            "name": "Example 2: Whitespace & Case Sensitivity",
            "str1": "debit card",
            "str2": "Bad credit",
            "expected": True
        },
        {
            "name": "Example 3: Completely Different Strings",
            "str1": "hello",
            "str2": "bye",
            "expected": False
        },
        {
            "name": "Example 4: Character Count Check",
            "str1": "restful",
            "str2": "fluster",
            "expected": True
        },
        {
            "name": "Example 5: Extra Character",
            "str1": "listen",
            "str2": "silentt",
            "expected": False
        },
        {
            "name": "Example 6: Punctuation, Whitespace & Mixed Case",
            "str1": "Conversation",
            "str2": "Voices, rant on",
            "expected": True
        }
    ]

    for tc in test_cases:
        actual = are_anagrams(tc["str1"], tc["str2"])
        passed = (actual == tc["expected"])
        status = "PASSED ✓" if passed else "FAILED ✗"

        print(f"[{status}] Test: {tc['name']}")
        print(f"  Input String 1:  \"{tc['str1']}\"")
        print(f"  Input String 2:  \"{tc['str2']}\"")
        print(f"  Expected Output: {tc['expected']}")
        print(f"  Actual Output:   {actual}")
        print("-" * 50)
        assert passed, f"Failed on {tc['name']}"

    print("\nAll Problem 8 tests completed successfully!")


if __name__ == "__main__":
    run_tests()