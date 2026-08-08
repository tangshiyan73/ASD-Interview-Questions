"""
Problem 6: Find Character with Maximum Occurrence

Language Choice: Python
Reason: Python 3 natively supports full Unicode (UTF-8) character strings out of the box.
Its built-in unicode categories (`unicodedata.category`) allow seamless filtering of punctuation
and whitespace across all world scripts.

Approach:
1. Iterate through each character in the string.
2. Filter out whitespaces and punctuation using Unicode category flags ('P' for Punctuation, 'Z' for Separator/Whitespace, etc.).
3. Maintain a frequency map (dictionary) counting occurrences of each valid character.
4. Keep track of the character with the maximum count using a single linear pass.

Unicode Handling:
- Python 3 strings treat code points natively.
- `unicodedata.category(char)` checks Unicode category classes:
  - Categories starting with 'Z' -> Separators / Whitespaces
  - Categories starting with 'P' -> Punctuation marks (e.g. !, ?, commas, foreign punctuation)
  - Categories starting with 'C' -> Control codes (newlines, tabs)

Space-Time Complexity Analysis:
- Time Complexity: O(N) — We scan the string of length N once to build frequencies and track max occurrence.
- Space Complexity: O(U) — Auxiliary space for the frequency map, where U is the number of unique characters in the string (U <= N).
"""

import unicodedata


def _is_whitespace_or_punctuation(char: str) -> bool:
    """
    Checks if a character is whitespace, punctuation, or a control character using Unicode category codes.
    - 'Z' = Separator (spaces, unicode spaces)
    - 'P' = Punctuation (all languages)
    - 'C' = Other / Control characters (\n, \t, etc.)
    """
    category = unicodedata.category(char)
    return category.startswith('Z') or category.startswith('P') or category.startswith('C')


def find_max_occurrence(text: str) -> tuple[str, int]:
    """
    Finds the character with maximum occurrence in `text`, ignoring whitespaces and punctuation.
    Returns a tuple: (max_char, count)
    Returns (None, 0) if no valid characters exist.
    """
    if not text:
        return (None, 0)

    counts = {}
    max_char = None
    max_count = 0

    for char in text:
        # Ignore whitespace and punctuation
        if _is_whitespace_or_punctuation(char):
            continue

        # Count character occurrences manually
        counts[char] = counts.get(char, 0) + 1

        # Track max occurrence dynamically
        if counts[char] > max_count:
            max_count = counts[char]
            max_char = char

    return (max_char, max_count)


# --- Interactive CLI Execution ---
if __name__ == "__main__":
    print("=== Problem 6: Character Frequency Counter ===")
    user_input = input(
        "Enter a string (e.g., 'Hello, world!' or Unicode like '你好世界哈哈哈')\n"
        "(or press Enter for default 'Hello, world!'): "
    )  # Keep raw whitespace to test filtering

    if user_input == "":
        text = "Hello, world!"
        print("\nUsing default assignment input...")
    else:
        text = user_input

    char, count = find_max_occurrence(text)

    print(f"\nInput String: \"{text}\"")
    if char is not None:
        print(f"Expected Output: Character: '{char}', Occurrence: {count}\n")
    else:
        print("Expected Output: No valid characters found (only spaces/punctuation).\n")