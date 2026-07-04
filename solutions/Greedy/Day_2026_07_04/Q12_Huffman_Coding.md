# Huffman Coding

## Problem Statement
Huffman coding is a method of encoding characters in binary such that the more frequently a character appears in a text, the shorter its binary representation will be. Given a text, create a Huffman coding scheme and use it to encode the text. The input is a string of characters and their frequencies. The output should be the encoded string and the dictionary used for encoding. The constraint is that the input string will have at most 100 unique characters and the total length of the string will not exceed 1000 characters.

## Approach
The approach to solve this problem is to use a priority queue to store characters and their frequencies. We keep removing the two nodes with the lowest frequencies, combine them, and insert the new node back into the queue. This process continues until only one node is left, which is the root of the Huffman tree.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure for the Huffman node
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
Node* buildHuffmanTree(vector<char>& characters, vector<int>& frequencies) {
    priority_queue<Node*, vector<Node*>, compare> pq;
    for (int i = 0; i < characters.size(); i++) {
        Node* newNode = new Node();
        newNode->character = characters[i];
        newNode->frequency = frequencies[i];
        newNode->left = newNode->right = NULL;
        pq.push(newNode);
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

// Function to build the Huffman codes
void buildHuffmanCodes(Node* root, string code, unordered_map<char, string>& huffmanCodes) {
    if (root == NULL) return;
    if (root->left == NULL && root->right == NULL) {
        huffmanCodes[root->character] = code;
    }
    buildHuffmanCodes(root->left, code + "0", huffmanCodes);
    buildHuffmanCodes(root->right, code + "1", huffmanCodes);
}

// Function to encode the text using Huffman coding
string encodeText(string text, unordered_map<char, string>& huffmanCodes) {
    string encodedText = "";
    for (char c : text) {
        encodedText += huffmanCodes[c];
    }
    return encodedText;
}

int main() {
    string text = "this is an example for huffman encoding";
    vector<char> characters;
    vector<int> frequencies;
    unordered_map<char, int> frequencyMap;
    for (char c : text) {
        if (frequencyMap.find(c) == frequencyMap.end()) {
            frequencyMap[c] = 1;
        } else {
            frequencyMap[c]++;
        }
    }
    for (auto& pair : frequencyMap) {
        characters.push_back(pair.first);
        frequencies.push_back(pair.second);
    }
    Node* root = buildHuffmanTree(characters, frequencies);
    unordered_map<char, string> huffmanCodes;
    buildHuffmanCodes(root, "", huffmanCodes);
    string encodedText = encodeText(text, huffmanCodes);
    cout << "Encoded Text: " << encodedText << endl;
    cout << "Huffman Codes: " << endl;
    for (auto& pair : huffmanCodes) {
        cout << pair.first << ": " << pair.second << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: "this is an example for huffman encoding"
Output: Encoded Text and Huffman Codes for each character
```

## Key Takeaways
- Huffman coding is a variable-length prefix code that assigns shorter codes to more frequently occurring characters.
- The time complexity of building the Huffman tree is O(n log n) due to the use of a priority queue.
- The space complexity of the Huffman coding scheme is O(n) for storing the Huffman codes and the encoded text.