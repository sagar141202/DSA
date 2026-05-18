# Huffman Coding

## Problem Statement
Huffman coding is a method of encoding characters in binary such that the more frequently a character appears in a text, the shorter its binary representation will be. Given a string of characters, design a Huffman coding scheme to encode the string. The input string will contain only lowercase letters and will have a length between 1 and 1000. The frequency of each character in the string will be between 1 and 1000.

## Approach
The approach to solve this problem is to use a priority queue to store the frequencies of the characters and then construct the Huffman tree. We will use a greedy algorithm to always choose the two nodes with the smallest frequencies and combine them into a new node.

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
    priority_queue<Node*, vector<Node*>, compare> pq;
    for (auto& pair : frequencyMap) {
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
        newNode->frequency = left->frequency + right->frequency;
        newNode->left = left;
        newNode->right = right;

        pq.push(newNode);
    }

    return pq.top();
}

// Function to generate the Huffman codes
void generateHuffmanCodes(Node* root, string code, map<char, string>& huffmanCodes) {
    if (root == nullptr) {
        return;
    }

    if (root->left == nullptr && root->right == nullptr) {
        huffmanCodes[root->character] = code;
    }

    generateHuffmanCodes(root->left, code + "0", huffmanCodes);
    generateHuffmanCodes(root->right, code + "1", huffmanCodes);
}

// Function to encode the string using Huffman coding
string encodeString(string input, map<char, string>& huffmanCodes) {
    string encodedString = "";
    for (char c : input) {
        encodedString += huffmanCodes[c];
    }
    return encodedString;
}

int main() {
    string input = "this is an example for huffman encoding";
    map<char, int> frequencyMap;

    // Calculate the frequency of each character
    for (char c : input) {
        frequencyMap[c]++;
    }

    Node* root = buildHuffmanTree(frequencyMap);
    map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);

    string encodedString = encodeString(input, huffmanCodes);
    cout << "Encoded String: " << encodedString << endl;

    return 0;
}
```

## Test Cases
```
Input: "this is an example for huffman encoding"
Output: (The encoded string will be displayed)
```

## Key Takeaways
- Huffman coding is a variable-length prefix code that assigns shorter codes to more frequently occurring characters.
- The time complexity of building the Huffman tree is O(n log n) due to the use of a priority queue.
- The space complexity is O(n) as we need to store the frequency of each character and the Huffman codes.