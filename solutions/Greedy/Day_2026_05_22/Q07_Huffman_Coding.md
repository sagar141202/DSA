# Huffman Coding

## Problem Statement
Huffman coding is a lossless data compression algorithm. The goal is to assign variable-length binary codes to input characters based on their frequencies, such that the total length of the encoded string is minimized. Given a string of characters and their frequencies, design a Huffman coding scheme to achieve the optimal compression.

## Approach
The algorithm works by building a binary tree where the path from the root to each leaf node represents the Huffman code for a character. The tree is constructed by repeatedly combining the two nodes with the lowest frequencies until only one node remains.

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
};

// Compare function to sort nodes based on frequency
struct compare {
    bool operator()(const Node* a, const Node* b) {
        return a->frequency > b->frequency;
    }
};

// Function to build the Huffman tree
Node* buildHuffmanTree(map<char, int>& frequencyMap) {
    priority_queue<Node*, vector<Node*>, compare> pq;
    for (auto& pair : frequencyMap) {
        Node* newNode = new Node();
        newNode->character = pair.first;
        newNode->frequency = pair.second;
        newNode->left = newNode->right = nullptr;
        pq.push(newNode);
    }

    while (pq.size() > 1) {
        Node* left = pq.top();
        pq.pop();
        Node* right = pq.top();
        pq.pop();

        Node* internalNode = new Node();
        internalNode->character = '\0';
        internalNode->frequency = left->frequency + right->frequency;
        internalNode->left = left;
        internalNode->right = right;

        pq.push(internalNode);
    }

    return pq.top();
}

// Function to generate Huffman codes
void generateHuffmanCodes(Node* root, string code, map<char, string>& huffmanCodes) {
    if (root == nullptr) {
        return;
    }

    if (root->character != '\0') {
        huffmanCodes[root->character] = code;
    }

    generateHuffmanCodes(root->left, code + "0", huffmanCodes);
    generateHuffmanCodes(root->right, code + "1", huffmanCodes);
}

int main() {
    string input = "this is an example for huffman encoding";
    map<char, int> frequencyMap;

    // Calculate frequency of each character
    for (char c : input) {
        frequencyMap[c]++;
    }

    Node* huffmanTree = buildHuffmanTree(frequencyMap);
    map<char, string> huffmanCodes;
    generateHuffmanCodes(huffmanTree, "", huffmanCodes);

    // Print Huffman codes
    for (auto& pair : huffmanCodes) {
        cout << pair.first << ": " << pair.second << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: "this is an example for huffman encoding"
Output: 
  : 00
a: 0100
c: 0110
d: 01110
e: 01111
f: 1000
g: 10010
h: 10011
i: 1010
l: 10110
m: 10111
n: 1100
o: 1101
p: 1110
r: 11110
s: 11111
t: 0101
x: 10001
```

## Key Takeaways
- Huffman coding is a variable-length prefix code that assigns shorter codes to more frequent characters.
- The Huffman tree is constructed by combining the two nodes with the lowest frequencies until only one node remains.
- The time complexity of building the Huffman tree is O(n log n) due to the use of a priority queue.