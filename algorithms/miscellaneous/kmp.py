def kmp_search(pattern, text):
    def compute_lps_array(pattern):
        """
        Computes the Longest Prefix Suffix (LPS) array for the pattern.
        The LPS array is used to skip characters in the pattern to avoid redundant comparisons.
        """
        length = 0  # Length of the previous longest prefix suffix
        lps = [0] * len(pattern)  # Initialize LPS array with 0s
        i = 1  # Start from the second character of the pattern

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1  # Increment the length of the current prefix suffix
                lps[i] = (
                    length  # Update LPS array with the length of the current prefix suffix
                )
                i += 1
            else:
                if length != 0:
                    length = lps[
                        length - 1
                    ]  # Use the previously computed LPS value to avoid redundant comparisons
                else:
                    lps[i] = 0  # No proper prefix which is also a suffix
                    i += 1
        return lps

    # Compute the LPS array for the pattern
    lps = compute_lps_array(pattern)
    i = j = 0  # Initialize pointers for the text and pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            # Pattern found at index i - j
            return i - j

        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                # Use the LPS array to skip unnecessary comparisons
                j = lps[j - 1]
            else:
                i += 1

    # Pattern not found in the text
    return -1


def main():
    pattern = "abc"
    text = "abcpqrabcxyz"

    # Run KMP search
    result = kmp_search(pattern, text)

    # Print the result
    print("Pattern found at index:", result)


if __name__ == "__main__":
    main()
