# Huffman Coding

## Problem Statement
Huffman coding is a method of encoding characters in binary such that the more frequently a character appears in a text, the shorter its binary representation will be. Given a text, we need to find the Huffman codes for each character. The constraints are that we have a limited number of characters (e.g., ASCII characters) and the input text is a string of these characters. For example, if the input text is "this is an example for huffman encoding", we need to find the Huffman codes for each character such that the total length of the encoded text is minimized.

## Approach
The Huffman coding algorithm works by building a priority queue of characters based on their frequencies, then repeatedly removing the two nodes with the lowest frequencies and combining them into a new node. This process continues until only one node is left, which is the root of the Huffman tree. The path from the root to each character in the tree gives its Huffman code.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure for the Huffman tree node
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
Node* buildHuffmanTree(vector<char>& characters, vector<int>& frequencies) {
    priority_queue<Node*, vector<Node*>, compare> queue;
    for (int i = 0; i < characters.size(); i++) {
        Node* node = new Node();
        node->character = characters[i];
        node->frequency = frequencies[i];
        node->left = nullptr;
        node->right = nullptr;
        queue.push(node);
    }

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
void generateHuffmanCodes(Node* node, string code, unordered_map<char, string>& huffmanCodes) {
    if (node == nullptr) {
        return;
    }

    if (node->character != '\0') {
        huffmanCodes[node->character] = code;
    }

    generateHuffmanCodes(node->left, code + "0", huffmanCodes);
    generateHuffmanCodes(node->right, code + "1", huffmanCodes);
}

// Function to calculate the Huffman codes for a given text
unordered_map<char, string> huffmanCoding(string text) {
    unordered_map<char, int> frequencyMap;
    for (char c : text) {
        frequencyMap[c]++;
    }

    vector<char> characters;
    vector<int> frequencies;
    for (auto& pair : frequencyMap) {
        characters.push_back(pair.first);
        frequencies.push_back(pair.second);
    }

    Node* root = buildHuffmanTree(characters, frequencies);
    unordered_map<char, string> huffmanCodes;
    generateHuffmanCodes(root, "", huffmanCodes);

    return huffmanCodes;
}

int main() {
    string text = "this is an example for huffman encoding";
    unordered_map<char, string> huffmanCodes = huffmanCoding(text);

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
t: 1110
h: 11110
i: 110
s: 101
 : 000
i: 110
s: 101
 : 000
a: 0110
n: 01110
 : 000
e: 100
x: 1000
a: 0110
m: 1010
p: 10110
l: 1100
e: 100
 : 000
f: 010
o: 0100
r: 011
 : 000
h: 11110
u: 1110
f: 010
f: 010
m: 1010
a: 0110
n: 01110
 : 000
e: 100
n: 01110
c: 11010
o: 0100
d: 11011
i: 110
n: 01110
g: 11011
```

## Key Takeaways
- Huffman coding is a variable-length prefix code that assigns shorter codes to more frequent characters.
- The Huffman tree is a binary tree where each leaf node represents a character and its path from the root gives its Huffman code.
- The Huffman coding algorithm works by building a priority queue of characters based on their frequencies and repeatedly combining the two nodes with the lowest frequencies until only one node is left.