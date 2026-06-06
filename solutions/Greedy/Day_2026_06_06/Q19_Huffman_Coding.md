# Huffman Coding

## Problem Statement
Huffman coding is a lossless data compression algorithm. The goal is to assign variable-length binary codes to input characters based on their frequencies, such that the total length of the encoded string is minimized. Given a string `s` containing `n` characters, each character `c` has a frequency `f(c)` representing how many times `c` appears in `s`. The task is to find the optimal Huffman coding for the characters in `s`, and return the encoded string. The input string `s` consists of lowercase English letters only, and `1 <= n <= 10^5`. For example, if `s = "abbc"`, the frequencies are `f(a) = 1`, `f(b) = 2`, and `f(c) = 1`, and one possible Huffman coding is `a = 00`, `b = 1`, and `c = 01`, resulting in the encoded string `00 1 1 01`.

## Approach
The Huffman coding algorithm uses a priority queue to store characters and their frequencies. It repeatedly removes the two nodes with the lowest frequencies, combines them into a new node, and adds the new node back into the queue. This process continues until only one node remains, which is the root of the Huffman tree. The algorithm then traverses the tree to generate the Huffman codes for each character.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    char c;
    int f;
    Node* left;
    Node* right;
    Node(char c, int f) : c(c), f(f), left(nullptr), right(nullptr) {}
};

struct compare {
    bool operator()(const Node* a, const Node* b) {
        return a->f > b->f;
    }
};

string huffmanCoding(string s) {
    // Calculate frequencies of characters
    map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }

    // Create priority queue
    priority_queue<Node*, vector<Node*>, compare> pq;
    for (auto& it : freq) {
        Node* node = new Node(it.first, it.second);
        pq.push(node);
    }

    // Build Huffman tree
    while (pq.size() > 1) {
        Node* a = pq.top();
        pq.pop();
        Node* b = pq.top();
        pq.pop();
        Node* node = new Node('\0', a->f + b->f);
        node->left = a;
        node->right = b;
        pq.push(node);
    }

    // Generate Huffman codes
    Node* root = pq.top();
    map<char, string> codes;
    function<void(Node*, string)> traverse = [&](Node* node, string code) {
        if (node->c != '\0') {
            codes[node->c] = code;
        }
        if (node->left) {
            traverse(node->left, code + "0");
        }
        if (node->right) {
            traverse(node->right, code + "1");
        }
    };
    traverse(root, "");

    // Encode string
    string encoded;
    for (char c : s) {
        encoded += codes[c];
    }

    return encoded;
}

int main() {
    string s = "abbc";
    string encoded = huffmanCoding(s);
    cout << encoded << endl;
    return 0;
}
```

## Test Cases
```
Input: abbc
Output: 00110
```

## Key Takeaways
- Huffman coding is a variable-length prefix code, meaning that no code is a prefix of another code.
- The Huffman coding algorithm has a time complexity of O(n log n) due to the use of a priority queue.
- The space complexity is O(n) because in the worst case, the Huffman tree has n nodes.