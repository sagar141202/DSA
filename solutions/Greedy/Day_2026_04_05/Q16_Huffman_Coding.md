# Huffman Coding

## Problem Statement
Huffman coding is a method of encoding characters in binary such that the more frequently a character appears in a text, the shorter its binary representation will be. Given a string of characters, generate a Huffman code for each character and return the encoded string. The input string will only contain lowercase letters and will have a length between 1 and 1000.

## Approach
The Huffman coding algorithm works by building a priority queue of characters based on their frequency, then repeatedly combining the two least frequent characters into a new node until only one node remains. This node represents the root of the Huffman tree, and the path from the root to each leaf node gives the binary encoding for the corresponding character.

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

// Comparison function for the priority queue
struct compare {
    bool operator()(const Node* a, const Node* b) {
        return a->frequency > b->frequency;
    }
};

// Function to build the Huffman tree
Node* buildHuffmanTree(string text) {
    // Create a frequency map for the characters in the text
    unordered_map<char, int> frequencyMap;
    for (char c : text) {
        frequencyMap[c]++;
    }

    // Create a priority queue of nodes
    priority_queue<Node*, vector<Node*>, compare> queue;
    for (auto& pair : frequencyMap) {
        Node* node = new Node();
        node->character = pair.first;
        node->frequency = pair.second;
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

        Node* newNode = new Node();
        newNode->character = '\0';
        newNode->frequency = left->frequency + right->frequency;
        newNode->left = left;
        newNode->right = right;

        queue.push(newNode);
    }

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

// Function to encode the text using the Huffman codes
string encodeText(string text, unordered_map<char, string>& huffmanCodes) {
    string encodedText;
    for (char c : text) {
        encodedText += huffmanCodes[c];
    }
    return encodedText;
}

int main() {
    string text = "this is an example for huffman encoding";
    Node* root = buildHuffmanTree(text);
    unordered_map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);
    string encodedText = encodeText(text, huffmanCodes);
    cout << encodedText << endl;
    return 0;
}
```

## Test Cases
```
Input: "this is an example for huffman encoding"
Output: (encoded string)
```

## Key Takeaways
- The Huffman coding algorithm is a greedy algorithm that works by building a priority queue of characters based on their frequency.
- The time complexity of the Huffman coding algorithm is O(n log n), where n is the number of unique characters in the text.
- The space complexity of the Huffman coding algorithm is O(n), where n is the number of unique characters in the text.