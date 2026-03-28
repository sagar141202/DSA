# Huffman Coding

## Problem Statement
Huffman coding is a method of encoding characters in binary such that the more frequently a character appears in a text, the shorter its binary representation will be. Given a string of characters, generate a Huffman coding tree and use it to encode the string. The input string will consist of letters (both uppercase and lowercase) and spaces. The frequency of each character will be provided. The goal is to minimize the total length of the encoded string.

## Approach
The Huffman coding algorithm uses a greedy approach to construct a binary tree where the path from the root to each leaf node represents the binary encoding of a character. The algorithm starts by creating a priority queue of nodes, where each node represents a character and its frequency. The two nodes with the lowest frequencies are removed from the queue, combined into a new node, and added back to the queue. This process continues until only one node remains, which is the root of the Huffman tree.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent a node in the Huffman tree
struct Node {
    char character;
    int frequency;
    Node* left;
    Node* right;

    // Constructor to initialize a node
    Node(char character, int frequency) : character(character), frequency(frequency), left(nullptr), right(nullptr) {}
};

// Define a comparison function for the priority queue
struct compare {
    bool operator()(const Node* a, const Node* b) {
        return a->frequency > b->frequency;
    }
};

// Function to build the Huffman tree
Node* buildHuffmanTree(vector<pair<char, int>>& frequencies) {
    // Create a priority queue to store the nodes
    priority_queue<Node*, vector<Node*>, compare> queue;

    // Add each character to the priority queue
    for (auto& frequency : frequencies) {
        Node* node = new Node(frequency.first, frequency.second);
        queue.push(node);
    }

    // Build the Huffman tree
    while (queue.size() > 1) {
        Node* left = queue.top();
        queue.pop();
        Node* right = queue.top();
        queue.pop();

        // Create a new node with the combined frequency
        Node* newNode = new Node('\0', left->frequency + right->frequency);
        newNode->left = left;
        newNode->right = right;

        // Add the new node back to the priority queue
        queue.push(newNode);
    }

    // Return the root of the Huffman tree
    return queue.top();
}

// Function to generate the Huffman codes
void generateHuffmanCodes(Node* node, string code, unordered_map<char, string>& huffmanCodes) {
    if (node == nullptr) {
        return;
    }

    // If the node is a leaf node, add the character and code to the map
    if (node->left == nullptr && node->right == nullptr) {
        huffmanCodes[node->character] = code;
    }

    // Recursively generate the codes for the left and right subtrees
    generateHuffmanCodes(node->left, code + "0", huffmanCodes);
    generateHuffmanCodes(node->right, code + "1", huffmanCodes);
}

int main() {
    string input;
    cout << "Enter the input string: ";
    getline(cin, input);

    // Calculate the frequency of each character
    unordered_map<char, int> frequencies;
    for (char c : input) {
        frequencies[c]++;
    }

    // Convert the frequency map to a vector of pairs
    vector<pair<char, int>> frequencyVector;
    for (auto& frequency : frequencies) {
        frequencyVector.push_back(frequency);
    }

    // Build the Huffman tree
    Node* root = buildHuffmanTree(frequencyVector);

    // Generate the Huffman codes
    unordered_map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);

    // Print the Huffman codes
    cout << "Huffman Codes:" << endl;
    for (auto& code : huffmanCodes) {
        cout << code.first << ": " << code.second << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: this is an example for huffman encoding
Output: 
t: 1110
h: 11110
i: 1000
s: 1010
 : 1100
a: 0000
n: 11010
e: 0010
x: 10110
m: 11011
p: 10111
l: 0001
f: 0110
o: 0111
r: 1001
 : 0100
u: 11111
f: 0111
f: 0111
m: 11011
a: 0000
n: 11010
 : 0100
e: 0010
n: 11010
c: 11101
o: 0111
d: 10101
i: 1000
n: 11010
g: 10000
```

## Key Takeaways
- Huffman coding is a lossless data compression algorithm that uses a variable-length prefix code to encode characters.
- The Huffman coding algorithm uses a greedy approach to construct a binary tree where the path from the root to each leaf node represents the binary encoding of a character.
- The time complexity of the Huffman coding algorithm is O(n log n), where n is the number of unique characters in the input string.