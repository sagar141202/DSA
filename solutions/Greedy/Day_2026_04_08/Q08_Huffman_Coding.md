# Huffman Coding

## Problem Statement
Huffman coding is a variable-length prefix code that assigns shorter codes to more frequently occurring characters in a dataset. The problem requires us to create a Huffman coding scheme for a given set of characters and their frequencies. The goal is to minimize the total length of the encoded data. We are given a set of characters and their corresponding frequencies, and we need to generate the Huffman codes for each character.

## Approach
The Huffman coding algorithm works by creating a binary tree where each leaf node represents a character and its frequency. The algorithm starts by creating a priority queue of nodes, where the priority of each node is its frequency. The algorithm then repeatedly removes the two nodes with the lowest frequencies from the queue, creates a new internal node with a frequency equal to the sum of the frequencies of the two removed nodes, and adds the new node back to the queue. This process continues until only one node is left in the queue, which is the root of the Huffman tree.

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

    // Create a leaf node for each character and add it to the queue
    for (auto& frequency : frequencies) {
        Node* node = new Node();
        node->character = frequency.first;
        node->frequency = frequency.second;
        node->left = nullptr;
        node->right = nullptr;
        queue.push(node);
    }

    // Build the Huffman tree
    while (queue.size() > 1) {
        Node* left = queue.top();
        queue.pop();
        Node* right = queue.top();
        queue.pop();

        Node* internalNode = new Node();
        internalNode->character = '\0';
        internalNode->frequency = left->frequency + right->frequency;
        internalNode->left = left;
        internalNode->right = right;

        queue.push(internalNode);
    }

    // Return the root of the Huffman tree
    return queue.top();
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

// Function to encode the data using the Huffman codes
string encodeData(const string& data, const unordered_map<char, string>& huffmanCodes) {
    string encodedData;
    for (char c : data) {
        encodedData += huffmanCodes.at(c);
    }
    return encodedData;
}

// Function to decode the data using the Huffman tree
string decodeData(const string& encodedData, Node* root) {
    string decodedData;
    Node* currentNode = root;

    for (char c : encodedData) {
        if (c == '0') {
            currentNode = currentNode->left;
        } else {
            currentNode = currentNode->right;
        }

        if (currentNode->left == nullptr && currentNode->right == nullptr) {
            decodedData += currentNode->character;
            currentNode = root;
        }
    }

    return decodedData;
}

int main() {
    // Example usage
    vector<pair<char, int>> frequencies = {{'A', 15}, {'B', 7}, {'C', 6}, {'D', 6}, {'E', 5}};
    Node* root = buildHuffmanTree(frequencies);

    unordered_map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);

    string data = "ABCDE";
    string encodedData = encodeData(data, huffmanCodes);
    string decodedData = decodeData(encodedData, root);

    cout << "Huffman Codes:" << endl;
    for (auto& code : huffmanCodes) {
        cout << code.first << ": " << code.second << endl;
    }

    cout << "Encoded Data: " << encodedData << endl;
    cout << "Decoded Data: " << decodedData << endl;

    return 0;
}

```

## Test Cases
```
Input: 
  Characters: A, B, C, D, E
  Frequencies: 15, 7, 6, 6, 5
Output: 
  Huffman Codes:
    A: 0
    B: 10
    C: 110
    D: 111
    E: 100
  Encoded Data: 010110110100
  Decoded Data: ABCDE
```

## Key Takeaways
- Huffman coding is a variable-length prefix code that assigns shorter codes to more frequently occurring characters in a dataset.
- The Huffman coding algorithm works by creating a binary tree where each leaf node represents a character and its frequency.
- The algorithm uses a priority queue to efficiently build the Huffman tree and generate the Huffman codes.