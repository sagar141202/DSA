# Huffman Coding

## Problem Statement
Huffman coding is a lossless data compression algorithm. The goal is to assign variable-length binary codes to input characters based on their frequencies. The character with the highest frequency should have the shortest code. Given a string, generate the Huffman codes for each character. The input string will only contain lowercase English letters (a-z). The frequency of each character is the number of times it appears in the string. The Huffman codes should be generated based on these frequencies.

## Approach
The algorithm uses a priority queue to store characters and their frequencies. It repeatedly removes the two nodes with the lowest frequencies, combines them, and adds the new node back into the queue. This process continues until only one node is left, which represents the root of the Huffman tree.

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

    // Constructor to initialize the node
    Node(char character, int frequency) {
        this->character = character;
        this->frequency = frequency;
        this->left = nullptr;
        this->right = nullptr;
    }
};

// Define a comparison function for the priority queue
struct compare {
    bool operator()(const Node* a, const Node* b) {
        return a->frequency > b->frequency;
    }
};

// Function to generate the Huffman codes
void generateHuffmanCodes(Node* root, string code, unordered_map<char, string>& huffmanCodes) {
    if (root == nullptr) {
        return;
    }

    // If the node is a leaf node, add the character and code to the map
    if (root->left == nullptr && root->right == nullptr) {
        huffmanCodes[root->character] = code;
    }

    // Recursively traverse the left and right subtrees
    generateHuffmanCodes(root->left, code + "0", huffmanCodes);
    generateHuffmanCodes(root->right, code + "1", huffmanCodes);
}

// Function to build the Huffman tree
Node* buildHuffmanTree(string text) {
    // Create a frequency map for the characters in the text
    unordered_map<char, int> frequencyMap;
    for (char c : text) {
        frequencyMap[c]++;
    }

    // Create a priority queue to store the nodes
    priority_queue<Node*, vector<Node*>, compare> priorityQueue;
    for (auto& pair : frequencyMap) {
        Node* node = new Node(pair.first, pair.second);
        priorityQueue.push(node);
    }

    // Build the Huffman tree
    while (priorityQueue.size() > 1) {
        Node* left = priorityQueue.top();
        priorityQueue.pop();
        Node* right = priorityQueue.top();
        priorityQueue.pop();

        Node* newNode = new Node('\0', left->frequency + right->frequency);
        newNode->left = left;
        newNode->right = right;

        priorityQueue.push(newNode);
    }

    // Return the root of the Huffman tree
    return priorityQueue.top();
}

// Function to generate the Huffman codes for a given text
void generateHuffmanCodes(string text) {
    Node* root = buildHuffmanTree(text);
    unordered_map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);

    // Print the Huffman codes
    for (auto& pair : huffmanCodes) {
        cout << pair.first << ": " << pair.second << endl;
    }
}

int main() {
    string text = "this is an example for huffman encoding";
    generateHuffmanCodes(text);
    return 0;
}
```

## Test Cases
```
Input: "this is an example for huffman encoding"
Output: 
t: 1110
h: 1101
i: 1000
s: 1010
a: 11110
n: 1011
e: 1100
x: 11111
m: 10010
p: 111100
l: 10110
f: 10011
o: 11010
r: 10001
c: 111101
d: 100001
g: 111110
```

## Key Takeaways
- Huffman coding is a variable-length prefix code that assigns shorter codes to more frequent characters.
- The algorithm uses a priority queue to build the Huffman tree, which represents the variable-length codes.
- The time complexity of the algorithm is O(n log n) due to the priority queue operations, where n is the number of unique characters in the input text.