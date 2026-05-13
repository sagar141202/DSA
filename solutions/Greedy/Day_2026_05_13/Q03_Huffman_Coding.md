# Huffman Coding

## Problem Statement
Huffman coding is a lossless data compression algorithm. The goal is to assign variable-length binary codes to input characters based on their frequencies. Given a string of characters, design a Huffman coding scheme to compress the data. The input string will have at most 100 unique characters, and each character will appear at least once. The output should include the Huffman codes for each character and the compressed string.

## Approach
The Huffman coding algorithm works by building a priority queue of characters based on their frequencies, then iteratively combining the two nodes with the lowest frequencies until only one node remains. This process creates a binary tree where the path from the root to each leaf node represents the Huffman code for the corresponding character.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Structure to represent a node in the Huffman tree
struct Node {
    char character;
    int frequency;
    Node* left;
    Node* right;
};

// Comparison function for the priority queue
struct compare {
    bool operator()(const Node* a, const Node* b) {
        return a->frequency > b->frequency;
    }
};

// Function to build the Huffman tree
Node* buildHuffmanTree(map<char, int>& frequencyMap) {
    priority_queue<Node*, vector<Node*>, compare> queue;
    for (auto& pair : frequencyMap) {
        Node* node = new Node();
        node->character = pair.first;
        node->frequency = pair.second;
        node->left = nullptr;
        node->right = nullptr;
        queue.push(node);
    }

    while (queue.size() > 1) {
        Node* left = queue.top();
        queue.pop();
        Node* right = queue.top();
        queue.pop();

        Node* newNode = new Node();
        newNode->character = '\0';
        newNode->frequency = left->frequency + right->frequency;
        newNode->left = left;
        newNode->right = right;

        queue.push(newNode);
    }

    return queue.top();
}

// Function to generate Huffman codes
void generateHuffmanCodes(Node* root, string code, map<char, string>& huffmanCodes) {
    if (root == nullptr) return;

    if (root->left == nullptr && root->right == nullptr) {
        huffmanCodes[root->character] = code;
    }

    generateHuffmanCodes(root->left, code + "0", huffmanCodes);
    generateHuffmanCodes(root->right, code + "1", huffmanCodes);
}

// Function to compress the input string using Huffman coding
string compressString(string input, map<char, string>& huffmanCodes) {
    string compressed;
    for (char c : input) {
        compressed += huffmanCodes[c];
    }
    return compressed;
}

int main() {
    string input;
    cout << "Enter the input string: ";
    cin >> input;

    map<char, int> frequencyMap;
    for (char c : input) {
        frequencyMap[c]++;
    }

    Node* huffmanTree = buildHuffmanTree(frequencyMap);
    map<char, string> huffmanCodes;
    generateHuffmanCodes(huffmanTree, "", huffmanCodes);

    string compressed = compressString(input, huffmanCodes);

    cout << "Huffman Codes:" << endl;
    for (auto& pair : huffmanCodes) {
        cout << pair.first << ": " << pair.second << endl;
    }

    cout << "Compressed String: " << compressed << endl;

    return 0;
}
```

## Test Cases
```
Input: thisisatest
Output: 
Huffman Codes:
t: 00
h: 010
i: 011
s: 10
a: 110
e: 111
Compressed String: 011011001001110110111
```

## Key Takeaways
- Huffman coding is a variable-length prefix code that assigns shorter codes to more frequent characters.
- The Huffman coding algorithm uses a priority queue to build the Huffman tree, which represents the optimal coding scheme.
- The time complexity of the Huffman coding algorithm is O(n log n), where n is the number of unique characters in the input string.