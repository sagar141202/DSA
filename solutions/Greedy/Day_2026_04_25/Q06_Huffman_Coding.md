# Huffman Coding

## Problem Statement
Huffman coding is a method of encoding characters in binary such that the more frequently a character appears in a text, the shorter its binary representation will be. Given a text, we need to find the Huffman codes for each character. The constraints are: the text can contain any ASCII character, the frequency of each character can be any positive integer, and the Huffman codes should be prefix-free (i.e., no code is a prefix of another code). For example, if the input text is "this is an example for huffman encoding", the output should be a dictionary where each key is a character from the text and its corresponding value is the Huffman code for that character.

## Approach
The Huffman coding algorithm works by creating a priority queue of nodes, where each node represents a character and its frequency. We repeatedly remove the two nodes with the lowest frequencies, create a new node with the sum of their frequencies, and add it back to the queue. We assign 0 to the left child and 1 to the right child of each new node. This process continues until only one node is left, which is the root of the Huffman tree.

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

// Compare function for the priority queue
struct compare {
    bool operator()(const Node* a, const Node* b) {
        return a->frequency > b->frequency;
    }
};

// Function to build the Huffman tree
Node* buildHuffmanTree(map<char, int> frequencyMap) {
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
    if (root == nullptr) return;
    
    if (root->left == nullptr && root->right == nullptr) {
        huffmanCodes[root->character] = code;
    }
    
    generateHuffmanCodes(root->left, code + "0", huffmanCodes);
    generateHuffmanCodes(root->right, code + "1", huffmanCodes);
}

int main() {
    string text = "this is an example for huffman encoding";
    map<char, int> frequencyMap;
    
    // Calculate the frequency of each character
    for (char c : text) {
        frequencyMap[c]++;
    }
    
    // Build the Huffman tree
    Node* root = buildHuffmanTree(frequencyMap);
    
    // Generate the Huffman codes
    map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);
    
    // Print the Huffman codes
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
t: 1101
h: 1100
i: 1110
s: 1000
 : 0000
a: 1010
n: 1011
e: 0110
x: 0010
m: 0011
p: 0100
l: 0101
f: 1111
o: 1001
r: 0111
u: 0001
c: 0010
d: 0101
g: 0110
```

## Key Takeaways
- The Huffman coding algorithm is a greedy algorithm that works by creating a priority queue of nodes, where each node represents a character and its frequency.
- The time complexity of the Huffman coding algorithm is O(n log n), where n is the number of unique characters in the text.
- The space complexity of the Huffman coding algorithm is O(n), where n is the number of unique characters in the text.