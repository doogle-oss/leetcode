"""
word_justify module

This module provides functionality to wrap words into lines with a specified maximum length. The lines are joined using dashes instead of spaces.

Functions:
- wrapLines(words: List[str], line_length: int) -> List[str]:
    Wraps words into lines with a maximum length using dashes.
- justifyLines(lines: List[str], line_length: int) -> List[str]:
    Justifies lines by filling them with dashes to match the specified length.
- reflowLines(lines: List[str], line_length: int) -> List[str]:
    Reflows lines to distribute spaces evenly between words to match the specified length.
- test_wrapLines():
    Runs test cases to verify the implementation of wrapLines.
- test_justifyLines():
    Runs test cases to verify the implementation of justifyLines.
- test_reflowLines():
    Runs test cases to verify the implementation of reflowLines.
"""

from typing import List


def wrapLines(words: List[str], line_length: int) -> List[str]:
    """
    Wraps words into lines with maximum length, using dashes instead of spaces.

    Time Complexity: O(n) where n is the number of words
    Space Complexity: O(n) for storing the result

    Parameters:
    words (List[str]): Array of words to wrap
    line_length (int): Maximum length for each line

    Returns:
    List[str]: Array of lines where each line length <= line_length
    """

    result: List[str] = []

    if not words:
        return result

    current_line: str = ""
    current_length = 0

    for word in words:
        word_len = len(word)

        # Calculate length if we add this word to current line
        # Need to account for dash separator if not the first word
        needed_length = current_length + word_len + (1 if current_line else 0)

        if needed_length <= line_length:
            # Word fits in current line
            current_line += ("-" if current_line else "") + word
            current_length = needed_length
        else:
            # Word doesn't fit, finalize current line and start new one
            if current_line:
                result.append(current_line)

            # Start new line with current word
            current_line = word
            current_length = word_len

    # Add the last line if it has words
    if current_line:
        result.append(current_line)

    return result


def line_justify(words: List[str], line_length: int) -> str:
    """
    Justifies a single line by distributing dashes evenly between words to match the specified line length.

    Parameters:
    words (List[str]): List of words to justify
    line_length (int): Desired length for the line

    Returns:
    str: A justified line with dashes evenly distributed
    """
    total_word_length = sum(len(word) for word in words)
    total_dashes = line_length - total_word_length

    if len(words) == 1:
        # If there's only one word, pad with dashes at the end
        return words[0] + "-" * total_dashes

    # Distribute dashes evenly between words
    dashes_between_words = total_dashes // (len(words) - 1)
    extra_dashes = total_dashes % (len(words) - 1)

    justified_line = ""
    for i, word in enumerate(words):
        justified_line += word
        if i < len(words) - 1:  # Add dashes between words
            justified_line += "-" * (
                dashes_between_words + (1 if i < extra_dashes else 0)
            )

    return justified_line


def reflow_and_justify(lines: List[str], line_length: int) -> List[str]:
    """
    Reflows and justifies lines by distributing dashes evenly between words to match the specified line length.

    Parameters:
    lines (List[str]): List of lines to reflow and justify
    line_length (int): Desired length for each line

    Returns:
    List[str]: List of reflowed and justified lines
    """
    result = []

    for l in lines:
        words = [(w, len(w)) for w in l.split(" ")]
        word_count = len(words)
        words_length = sum([w[1] for w in words])

        if not words:
            result.append("")
        elif word_count == 1:
            # If there's only one word, pad with dashes at the end
            result.append(words[0][0] + "-" * (line_length - words_length))
        else:
            # Calculate dashes to distribute
            dashes = line_length - words_length
            dash_between = dashes // (word_count - 1)
            extra_dashes = dashes % (word_count - 1)

            justified_line = ""
            for i, (word, _) in enumerate(words):
                justified_line += word
                if i < word_count - 1:  # Add dashes between words
                    justified_line += "-" * (
                        dash_between + (1 if i < extra_dashes else 0)
                    )

            result.append(justified_line)

    return result
