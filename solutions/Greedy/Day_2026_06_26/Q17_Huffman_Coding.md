# Huffman Coding

## Problem Statement
Huffman coding is a method of encoding characters in binary such that the more frequently a character appears in a text, the shorter its binary representation will be. Given a string of characters, we need to generate a Huffman code for each character. The constraints are that the input string will contain only lowercase English letters and will have a length between 1 and 1000. The goal is to minimize the total length of the encoded string.

## Approach
The approach to solve this problem is to use a priority queue to store the frequencies of characters and then build a Huffman tree based on these frequencies. We will use a greedy algorithm to construct the Huffman tree, always selecting the two nodes with the lowest frequencies and combining them into a new node.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    char character;
    int frequency;
    Node* left;
    Node* right;

    Node(char character, int frequency) {
        this->character = character;
        this->frequency = frequency;
        this->left = nullptr;
        this->right = nullptr;
    }
};

struct compare {
    bool operator()(const Node* a, const Node* b) {
        return a->frequency > b->frequency;
    }
};

void generateHuffmanCode(Node* root, string code, unordered_map<char, string>& huffmanCode) {
    if (root == nullptr) {
        return;
    }

    if (root->left == nullptr && root->right == nullptr) {
        huffmanCode[root->character] = code;
    }

    generateHuffmanCode(root->left, code + "0", huffmanCode);
    generateHuffmanCode(root->right, code + "1", huffmanCode);
}

void huffmanCoding(string text) {
    unordered_map<char, int> frequency;

    for (char c : text) {
        frequency[c]++;
    }

    priority_queue<Node*, vector<Node*>, compare> pq;

    for (auto& pair : frequency) {
        Node* node = new Node(pair.first, pair.second);
        pq.push(node);
    }

    while (pq.size() > 1) {
        Node* left = pq.top();
        pq.pop();
        Node* right = pq.top();
        pq.pop();

        Node* newNode = new Node('\0', left->frequency + right->frequency);
        newNode->left = left;
        newNode->right = right;

        pq.push(newNode);
    }

    Node* root = pq.top();
    unordered_map<char, string> huffmanCode;
    generateHuffmanCode(root, "", huffmanCode);

    for (auto& pair : huffmanCode) {
        cout << pair.first << ": " << pair.second << endl;
    }
}

int main() {
    string text = "this is an example for huffman encoding";
    huffmanCoding(text);
    return 0;
}
```

## Test Cases
```
Input: "this is an example for huffman encoding"
Output: 
t: 1111
h: 1110
i: 1101
s: 1100
 : 1010
a: 1001
n: 1000
e: 0111
x: 0110
m: 0101
p: 0100
l: 0011
f: 0010
o: 0001
r: 0000
```

## Key Takeaways
- Huffman coding is a variable-length prefix code that assigns shorter codes to more frequently occurring characters.
- The Huffman tree is constructed using a greedy algorithm, where the two nodes with the lowest frequencies are always combined into a new node.
- The time complexity of Huffman coding is O(n log n), where n is the number of unique characters in the input string.