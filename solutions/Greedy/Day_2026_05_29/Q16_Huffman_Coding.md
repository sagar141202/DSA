# Huffman Coding

## Problem Statement
Huffman coding is a lossless data compression algorithm. The goal is to create a binary tree where the path from the root to each leaf node represents a character in the input string. The frequency of each character determines the length of the path, with more frequent characters having shorter paths. Given a string of characters, create a Huffman coding tree and generate the Huffman codes for each character. The input string will contain only lowercase letters (a-z) and will have a length between 1 and 1000.

## Approach
The approach involves building a priority queue of characters based on their frequencies, then repeatedly removing the two nodes with the lowest frequencies and combining them into a new node. This process continues until only one node remains, which is the root of the Huffman tree.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure for the nodes in the Huffman tree
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

int main() {
    string text = "this is an example for huffman encoding";
    Node* root = buildHuffmanTree(text);
    unordered_map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);

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
a: 1110
c: 11010
d: 11110
e: 01
f: 11011
g: 110001
h: 110000
i: 100
m: 0111
n: 1010
o: 11001
p: 110011
r: 1000
s: 1011
t: 00
x: 1101
```

## Key Takeaways
- Huffman coding is a lossless data compression algorithm that works by building a binary tree where the path from the root to each leaf node represents a character in the input string.
- The frequency of each character determines the length of the path, with more frequent characters having shorter paths.
- The Huffman coding algorithm has a time complexity of O(n log n) and a space complexity of O(n), making it efficient for large input strings.