"""
Problem 8: Anagram Checker

Language Choice: Python
Reason: Python's expressive dictionary manipulation and built-in Unicode string methods
make it easy to clean strings and perform custom frequency checks without relying
on banned library sorting or comparison algorithms.

Approach:
1. Normalize both input strings: convert characters to lowercase and filter out
   whitespaces, punctuation, and control characters using Unicode categories.
2. If the lengths of the cleaned strings differ, they cannot be anagrams -> return False.
3. Build a frequency count map for the first cleaned string in linear time.
4. Decrement the frequency counts using characters from the second cleaned string:
   - If a character in the second string is not in the map, return False.
   - Decrement its count; if the count falls below zero, return False.
5. If all characters match and counts reach zero, return True.

Space-Time Complexity Analysis:
- Time Complexity: O(N + M)
  - Cleaning and normalizing string 1 of length N takes O(N) time.
  - Cleaning and normalizing string 2 of length M takes O(M) time.
  - Frequency counting and verification take O(N) linear time.
  - Total Time: O(N + M) linear time.
- Space Complexity: O(U)
  - Auxiliary memory used for the character frequency dictionary, where U is the
    number of unique characters in the cleaned string.
"""

import unicodedata


def _is_valid_char(char: str) -> bool:
    """
    Checks if a character is a valid letter/digit (not a space, punctuation, or control char).
    Uses Unicode categories:
    - 'Z' = Separator/Whitespace
    - 'P' = Punctuation
    - 'C' = Control/Other
    """
    category = unicodedata.category(char)
    return not (category.startswith('Z') or category.startswith('P') or category.startswith('C'))


def are_anagrams(str1: str, str2: str) -> bool:
    """
    Checks whether two strings are anagrams of each other.
    Ignores case sensitivity, whitespaces, and punctuation.
    Returns True if anagrams, False otherwise.
    """
    # Clean and normalize strings: lowercase + remove punctuation/whitespace
    clean1 = [char.lower() for char in str1 if _is_valid_char(char)]
    clean2 = [char.lower() for char in str2 if _is_valid_char(char)]

    # Quick length check
    if len(clean1) != len(clean2):
        return False

    # Build frequency map for clean1
    counts = {}
    for char in clean1:
        counts[char] = counts.get(char, 0) + 1

    # Verify against clean2
    for char in clean2:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1

    return True


# --- Interactive CLI Execution ---
if __name__ == "__main__":
    print("=== Problem 8: Anagram Checker ===")
    
    input1 = input(
        "Enter first string (e.g., 'Conversation')\n"
        "(or press Enter for default 'Conversation'): "
    )
    input2 = input(
        "Enter second string (e.g., 'Voices, rant on')\n"
        "(or press Enter for default 'Voices, rant on'): "
    )

    # Use defaults if user hits Enter
    if input1 == "" or input2 == "":
        s1 = "Conversation"
        s2 = "Voices, rant on"
        print("\nUsing default assignment inputs...")
    else:
        s1 = input1
        s2 = input2

    result = are_anagrams(s1, s2)

    print(f"\nString 1: \"{s1}\"")
    print(f"String 2: \"{s2}\"")
    print(f"Expected Output: {str(result).lower()}\n")