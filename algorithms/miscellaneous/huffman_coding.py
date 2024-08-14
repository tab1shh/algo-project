import heapq
from collections import defaultdict


class HuffmanNode:
    """
    A class representing a node in the Huffman Tree.
    """

    def __init__(self, char, freq):
        self.char = char  # The character stored in the node (None for internal nodes)
        self.freq = freq  # The frequency of the character (or the combined frequency of children)
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node

    def __lt__(self, other):
        """
        Comparator function for priority queue (min-heap) based on frequency.
        """
        return self.freq < other.freq


def huffman_encoding(data):
    """
    Encodes the input data using Huffman coding.

    Parameters:
    data (str): The input string to encode.

    Returns:
    tuple: A tuple containing:
        - encoded_data (str): The encoded string.
        - huffman_tree (HuffmanNode): The root of the Huffman Tree.
    """
    if not data:
        return "", None

    # Compute frequency of each character in the input data
    freq = defaultdict(int)
    for char in data:
        freq[char] += 1

    # Create a priority queue (min-heap) of HuffmanNodes based on frequencies
    priority_queue = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(priority_queue)

    # Build the Huffman Tree
    while len(priority_queue) > 1:
        # Remove the two nodes with the lowest frequency
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # Create a new internal node with the sum of the frequencies
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the new node to the priority queue
        heapq.heappush(priority_queue, merged)

    # The remaining node is the root of the Huffman Tree
    huffman_tree = heapq.heappop(priority_queue)

    def build_codes(node, prefix="", codebook={}):
        """
        Recursively builds the Huffman codes from the Huffman Tree.

        Parameters:
        node (HuffmanNode): The current node in the Huffman Tree.
        prefix (str): The current prefix (binary code) being built.
        codebook (dict): A dictionary to store the Huffman codes.

        Returns:
        dict: A dictionary mapping characters to their Huffman codes.
        """
        if node.char is not None:
            codebook[node.char] = prefix
        else:
            if node.left:
                build_codes(node.left, prefix + "0", codebook)
            if node.right:
                build_codes(node.right, prefix + "1", codebook)
        return codebook

    # Generate the Huffman codes
    huffman_codes = build_codes(huffman_tree)

    # Encode the input data using the Huffman codes
    encoded_data = "".join(huffman_codes[char] for char in data)
    return encoded_data, huffman_tree


def huffman_decoding(data, tree):
    """
    Decodes the encoded data using the Huffman Tree.

    Parameters:
    data (str): The encoded binary string.
    tree (HuffmanNode): The root of the Huffman Tree.

    Returns:
    str: The decoded string.
    """
    if not tree:
        return ""

    decoded_data = []
    node = tree

    # Decode the encoded data bit by bit
    for bit in data:
        # Traverse the tree based on the bit (0 for left, 1 for right)
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded_data.append(node.char)
            node = tree  # Return to the root of the Huffman Tree

    return "".join(decoded_data)
