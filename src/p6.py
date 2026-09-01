# Python's Unicode-native strings + unicodedata.category() make skipping
# whitespace/punctuation and counting non-ASCII scripts correctly straightforward.
import unicodedata

def max_occurring_char(text):
    counts = {}
    for ch in text:
        category = unicodedata.category(ch)
        # 'Z*' categories = separators (space, etc.), 'P*' categories = punctuation
        if category.startswith('Z') or category.startswith('P'):
            continue
        counts[ch] = counts.get(ch, 0) + 1  # case-sensitive: 'H' and 'h' count separately

    if not counts:
        return None, 0  # no countable characters at all

    max_char, max_count = None, 0
    for ch, count in counts.items():
        if count > max_count:  # first character to reach a new max wins ties
            max_char, max_count = ch, count

    return max_char, max_count
