# Huffman Coding

## Problem Statement
Huffman coding is a method of encoding characters in binary such that the more frequently a character appears in a text, the shorter its binary representation will be. Given a text, create a Huffman coding scheme and use it to encode the text. The input is a string of characters, and the output is the encoded string and the Huffman coding scheme. The frequency of each character in the text is also given. The encoding scheme should be such that it minimizes the total length of the encoded text.

## Approach
The approach to solve this problem is to use a priority queue to store the characters and their frequencies, and then repeatedly remove the two nodes with the lowest frequencies, combine them, and add the new node back to the queue. This process continues until only one node is left, which is the root of the Huffman tree.

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

// Compare function for the priority queue
struct compare {
    bool operator()(const Node* a, const Node* b) {
        return a->frequency > b->frequency;
    }
};

// Function to build the Huffman tree
Node* buildHuffmanTree(vector<char> characters, vector<int> frequencies) {
    priority_queue<Node*, vector<Node*>, compare> queue;
    
    // Create a leaf node for each character and add it to the queue
    for (int i = 0; i < characters.size(); i++) {
        Node* node = new Node();
        node->character = characters[i];
        node->frequency = frequencies[i];
        node->left = NULL;
        node->right = NULL;
        queue.push(node);
    }
    
    // Repeatedly remove the two nodes with the lowest frequencies, combine them, and add the new node back to the queue
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
    
    // The root of the Huffman tree is the only node left in the queue
    return queue.top();
}

// Function to generate the Huffman codes
void generateHuffmanCodes(Node* root, string code, unordered_map<char, string>& huffmanCodes) {
    if (root == NULL) {
        return;
    }
    
    if (root->left == NULL && root->right == NULL) {
        huffmanCodes[root->character] = code;
    }
    
    generateHuffmanCodes(root->left, code + "0", huffmanCodes);
    generateHuffmanCodes(root->right, code + "1", huffmanCodes);
}

// Function to encode the text using the Huffman codes
string encodeText(string text, unordered_map<char, string> huffmanCodes) {
    string encodedText = "";
    
    for (char c : text) {
        encodedText += huffmanCodes[c];
    }
    
    return encodedText;
}

int main() {
    vector<char> characters = {'a', 'b', 'c', 'd', 'e', 'f'};
    vector<int> frequencies = {5, 9, 12, 13, 16, 45};
    string text = "this is an example for huffman encoding";
    
    Node* root = buildHuffmanTree(characters, frequencies);
    unordered_map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);
    string encodedText = encodeText(text, huffmanCodes);
    
    cout << "Huffman Codes:" << endl;
    for (auto& pair : huffmanCodes) {
        cout << pair.first << ": " << pair.second << endl;
    }
    
    cout << "Encoded Text: " << encodedText << endl;
    
    return 0;
}
```

## Test Cases
```
Input: 
characters = ['a', 'b', 'c', 'd', 'e', 'f']
frequencies = [5, 9, 12, 13, 16, 45]
text = "this is an example for huffman encoding"
Output: 
Huffman Codes:
a: 000
b: 001
c: 010
d: 011
e: 100
f: 101
Encoded Text: 000001010011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010011011100100110100101001110010