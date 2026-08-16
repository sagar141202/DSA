# Huffman Coding

## Problem Statement
Huffman coding is a lossless data compression algorithm. The goal is to assign variable-length binary codes to input characters based on their frequencies. The character with the highest frequency should have the shortest code. Given a string, generate a Huffman code for each character and return the encoded string. The input string consists of ASCII characters, and the frequency of each character is greater than 0. The length of the input string is up to 1000 characters.

## Approach
The algorithm uses a priority queue to store characters and their frequencies. It repeatedly removes the two nodes with the lowest frequencies, combines them, and inserts the new node back into the queue. This process continues until only one node is left, which is the root of the Huffman tree.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure for the Huffman tree node
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
Node* buildHuffmanTree(string text) {
    // Create a frequency map
    unordered_map<char, int> frequencyMap;
    for (char c : text) {
        frequencyMap[c]++;
    }

    // Create a priority queue
    priority_queue<Node*, vector<Node*>, compare> pq;
    for (auto& pair : frequencyMap) {
        Node* node = new Node();
        node->character = pair.first;
        node->frequency = pair.second;
        node->left = nullptr;
        node->right = nullptr;
        pq.push(node);
    }

    // Build the Huffman tree
    while (pq.size() > 1) {
        Node* left = pq.top();
        pq.pop();
        Node* right = pq.top();
        pq.pop();

        Node* newNode = new Node();
        newNode->character = '\0';
        newNode->frequency = left->frequency + right->frequency;
        newNode->left = left;
        newNode->right = right;

        pq.push(newNode);
    }

    return pq.top();
}

// Function to generate the Huffman codes
void generateHuffmanCodes(Node* root, string code, unordered_map<char, string>& huffmanCodes) {
    if (root == nullptr) {
        return;
    }

    if (root->left == nullptr && root->right == nullptr) {
        huffmanCodes[root->character] = code;
    }

    generateHuffmanCodes(root->left, code + "0", huffmanCodes);
    generateHuffmanCodes(root->right, code + "1", huffmanCodes);
}

// Function to encode the input string using Huffman codes
string huffmanEncoding(string text) {
    Node* root = buildHuffmanTree(text);
    unordered_map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);

    string encodedText;
    for (char c : text) {
        encodedText += huffmanCodes[c];
    }

    return encodedText;
}

int main() {
    string text = "this is an example for huffman encoding";
    string encodedText = huffmanEncoding(text);
    cout << encodedText << endl;
    return 0;
}
```

## Test Cases
```
Input: "this is an example for huffman encoding"
Output: encoded string using Huffman codes
```

## Key Takeaways
- Huffman coding is a variable-length prefix code that assigns shorter codes to more frequent characters.
- The Huffman tree is a binary tree where each leaf node represents a character and its frequency.
- The time complexity of building the Huffman tree is O(n log n) due to the priority queue operations.