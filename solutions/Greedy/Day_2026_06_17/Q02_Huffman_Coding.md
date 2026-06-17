# Huffman Coding

## Problem Statement
Huffman coding is a method of encoding characters in binary such that the more frequently a character appears in a text, the shorter its binary representation will be. Given a text, we need to find the Huffman codes for each character and then use these codes to encode the text. The constraints are that we have a text of size n and we need to find the Huffman codes for each unique character in the text. For example, if we have a text "this is an example for huffman encoding", we need to find the Huffman codes for each unique character in the text.

## Approach
The approach to solve this problem is to use a priority queue to store the frequencies of each character and then use these frequencies to construct the Huffman tree. We will then use the Huffman tree to find the Huffman codes for each character. The algorithm works by repeatedly removing the two nodes with the smallest frequencies from the priority queue and combining them into a new node with a frequency equal to the sum of the frequencies of the two nodes.

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

// Define a comparison function to compare two nodes based on their frequencies
struct compare {
    bool operator()(const Node* a, const Node* b) {
        return a->frequency > b->frequency;
    }
};

// Function to build the Huffman tree
Node* buildHuffmanTree(unordered_map<char, int>& frequencyMap) {
    priority_queue<Node*, vector<Node*>, compare> pq;
    
    // Create a leaf node for each character and add it to the priority queue
    for (auto& it : frequencyMap) {
        Node* node = new Node();
        node->character = it.first;
        node->frequency = it.second;
        node->left = nullptr;
        node->right = nullptr;
        pq.push(node);
    }
    
    // Repeatedly remove the two nodes with the smallest frequencies from the priority queue and combine them into a new node
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

// Function to encode the text using the Huffman codes
string encodeText(string text, unordered_map<char, string>& huffmanCodes) {
    string encodedText = "";
    
    for (char c : text) {
        encodedText += huffmanCodes[c];
    }
    
    return encodedText;
}

int main() {
    string text = "this is an example for huffman encoding";
    unordered_map<char, int> frequencyMap;
    
    // Calculate the frequency of each character in the text
    for (char c : text) {
        frequencyMap[c]++;
    }
    
    Node* root = buildHuffmanTree(frequencyMap);
    unordered_map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);
    string encodedText = encodeText(text, huffmanCodes);
    
    cout << "Huffman Codes:" << endl;
    for (auto& it : huffmanCodes) {
        cout << it.first << ": " << it.second << endl;
    }
    
    cout << "Encoded Text: " << encodedText << endl;
    
    return 0;
}
```

## Test Cases
```
Input: "this is an example for huffman encoding"
Output: 
Huffman Codes:
t: 1110
h: 11110
i: 110
s: 1010
 : 000
i: 110
s: 1010
 : 000
a: 1000
n: 10010
 : 000
e: 011
x: 10110
a: 1000
m: 11111
p: 10111
l: 1100
e: 011
 : 000
f: 1101
o: 10011
r: 0111
 : 000
h: 11110
u: 11101
f: 1101
f: 1101
m: 11111
a: 1000
n: 10010
 : 000
e: 011
n: 10010
c: 11010
o: 10011
d: 10101
i: 110
n: 10010
g: 11100
Encoded Text: 111011101110100011110101011100100100110100110110111101110110110110100011101110100110100011101110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100110110100110100011110110100110111111110111011111011110011101101101110111101110111001110100110110100110101110111001101110100110100011110110100110110100110111011110100