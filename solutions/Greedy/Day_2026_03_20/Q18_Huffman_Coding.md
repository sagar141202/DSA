# Huffman Coding

## Problem Statement
Huffman coding is a method of encoding characters in binary such that the more frequently a character appears in a text, the shorter its binary representation will be. Given a string of characters, create a Huffman coding scheme to compress the string. The string will contain only lowercase letters (a-z) and will have a maximum length of 1000 characters. The frequency of each character in the string will be used to determine the Huffman coding scheme.

## Approach
The approach to solve this problem is to use a priority queue to store characters and their frequencies, then repeatedly remove the two nodes with the lowest frequencies and combine them into a new node. This process continues until only one node remains, which is the root of the Huffman tree.

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

// Compare function for the priority queue
struct compare {
    bool operator()(const Node* a, const Node* b) {
        return a->frequency > b->frequency;
    }
};

// Function to build the Huffman tree
Node* buildHuffmanTree(map<char, int> frequencyMap) {
    priority_queue<Node*, vector<Node*>, compare> pq;
    
    // Create a leaf node for each character and add it to the priority queue
    for (auto& pair : frequencyMap) {
        Node* node = new Node();
        node->character = pair.first;
        node->frequency = pair.second;
        node->left = NULL;
        node->right = NULL;
        pq.push(node);
    }
    
    // Repeat the process until only one node remains
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
void generateHuffmanCodes(Node* root, string code, map<char, string>& huffmanCodes) {
    if (root == NULL) {
        return;
    }
    
    if (root->left == NULL && root->right == NULL) {
        huffmanCodes[root->character] = code;
    }
    
    generateHuffmanCodes(root->left, code + "0", huffmanCodes);
    generateHuffmanCodes(root->right, code + "1", huffmanCodes);
}

// Function to compress the string using Huffman coding
string compressString(string input) {
    map<char, int> frequencyMap;
    
    // Calculate the frequency of each character in the input string
    for (char c : input) {
        frequencyMap[c]++;
    }
    
    Node* root = buildHuffmanTree(frequencyMap);
    
    map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);
    
    string compressedString = "";
    
    // Replace each character in the input string with its Huffman code
    for (char c : input) {
        compressedString += huffmanCodes[c];
    }
    
    return compressedString;
}

int main() {
    string input = "this is an example for huffman encoding";
    string compressed = compressString(input);
    cout << "Compressed string: " << compressed << endl;
    return 0;
}
```

## Test Cases
```
Input: "this is an example for huffman encoding"
Output: Compressed string using Huffman coding
```

## Key Takeaways
- The Huffman coding scheme is a variable-length prefix code, meaning that the codes for different characters can have different lengths, but no code is a prefix of another code.
- The time complexity of the Huffman coding algorithm is O(n log n), where n is the number of unique characters in the input string.
- The space complexity of the Huffman coding algorithm is O(n), where n is the number of unique characters in the input string.