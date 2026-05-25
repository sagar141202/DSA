# Huffman Coding

## Problem Statement
Huffman coding is a method of encoding characters in binary such that the more frequently a character appears in a text, the shorter its binary representation will be. Given a string of characters and their frequencies, design a Huffman coding scheme to encode the characters. The goal is to minimize the total number of bits used to encode the string. For example, if we have a string "this is an example for huffman encoding" and the frequency of each character, we need to create a binary tree where the path from the root to each character represents its binary code.

## Approach
The approach to solve this problem is to use a priority queue to store the characters and their frequencies, and then repeatedly remove the two nodes with the lowest frequencies and combine them into a new node. This process is repeated until only one node is left, which is the root of the Huffman tree. The Huffman codes can then be obtained by traversing the tree.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define the structure for a node in the Huffman tree
struct Node {
    char character;
    int frequency;
    Node* left;
    Node* right;
};

// Define a comparison function for the priority queue
struct compare {
    bool operator()(const Node* a, const Node* b) {
        return a->frequency > b->frequency;
    }
};

// Function to build the Huffman tree
Node* buildHuffmanTree(vector<pair<char, int>>& frequencies) {
    priority_queue<Node*, vector<Node*>, compare> pq;
    for (auto& frequency : frequencies) {
        Node* node = new Node();
        node->character = frequency.first;
        node->frequency = frequency.second;
        node->left = nullptr;
        node->right = nullptr;
        pq.push(node);
    }
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
    if (root->character != '\0') {
        huffmanCodes[root->character] = code;
    }
    generateHuffmanCodes(root->left, code + "0", huffmanCodes);
    generateHuffmanCodes(root->right, code + "1", huffmanCodes);
}

int main() {
    vector<pair<char, int>> frequencies = {{'a', 15}, {'b', 7}, {'c', 6}, {'d', 6}, {'e', 5}};
    Node* root = buildHuffmanTree(frequencies);
    unordered_map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);
    for (auto& code : huffmanCodes) {
        cout << code.first << ": " << code.second << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: frequencies = {{'a', 15}, {'b', 7}, {'c', 6}, {'d', 6}, {'e', 5}}
Output: 
a: 0
b: 100
c: 1010
d: 1011
e: 11
```

## Key Takeaways
- The Huffman coding scheme is a variable-length prefix code that assigns shorter codes to more frequently occurring characters.
- The time complexity of the Huffman coding algorithm is O(n log n) due to the use of a priority queue.
- The space complexity is O(n) as we need to store the characters, their frequencies, and the Huffman codes.