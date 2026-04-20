# Huffman Coding

## Problem Statement
Huffman coding is a method of encoding characters in binary such that the more frequently a character appears in a text, the shorter its binary representation will be. Given a text, find the Huffman codes for each character and calculate the total length of the encoded text. The text consists of only lowercase English letters and the frequency of each character is given. The frequency of each character is a positive integer.

## Approach
The Huffman coding algorithm works by building a binary tree where the path from the root to each leaf node represents the binary code for a character. The algorithm starts with a priority queue of characters and their frequencies, and repeatedly removes the two nodes with the lowest frequencies, combining them into a new node with a frequency equal to the sum of the two nodes' frequencies.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a struct to represent a node in the Huffman tree
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
Node* buildHuffmanTree(map<char, int>& frequencies) {
    priority_queue<Node*, vector<Node*>, compare> pq;
    for (auto& pair : frequencies) {
        Node* node = new Node();
        node->character = pair.first;
        node->frequency = pair.second;
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

// Function to generate Huffman codes
void generateHuffmanCodes(Node* root, string code, map<char, string>& huffmanCodes) {
    if (root == nullptr) return;

    if (root->left == nullptr && root->right == nullptr) {
        huffmanCodes[root->character] = code;
    }

    generateHuffmanCodes(root->left, code + "0", huffmanCodes);
    generateHuffmanCodes(root->right, code + "1", huffmanCodes);
}

int main() {
    map<char, int> frequencies = {{'a', 15}, {'b', 7}, {'c', 6}, {'d', 6}, {'e', 5}};
    Node* root = buildHuffmanTree(frequencies);
    map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);

    for (auto& pair : huffmanCodes) {
        cout << pair.first << ": " << pair.second << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
frequencies = {{'a', 15}, {'b', 7}, {'c', 6}, {'d', 6}, {'e', 5}}
Output: 
a: 0
b: 10
c: 110
d: 111
e: 11
```

## Key Takeaways
- The Huffman coding algorithm is a greedy algorithm that builds a binary tree by combining the two nodes with the lowest frequencies at each step.
- The time complexity of the Huffman coding algorithm is O(n log n) due to the use of a priority queue.
- The space complexity of the Huffman coding algorithm is O(n) for storing the Huffman tree and the Huffman codes.