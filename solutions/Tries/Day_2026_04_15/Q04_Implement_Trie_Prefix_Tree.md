# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should be able to store a collection of strings and provide efficient lookup, insertion, and prefix matching capabilities. The `insert` operation inserts a new string into the Trie, the `search` operation checks if a given string is present in the Trie, and the `startsWith` operation checks if there is any string in the Trie that starts with a given prefix. The Trie should handle a large number of strings and provide fast lookup times.

## Approach
The approach involves using a nested unordered map to represent the Trie, where each node in the Trie is a map that stores its child nodes. The `insert` operation iterates through each character in the string and creates new nodes as necessary. The `search` and `startsWith` operations traverse the Trie based on the input string or prefix.

## Complexity
- Time: O(m) where m is the length of the string or prefix
- Space: O(n*m) where n is the number of strings and m is the average length of the strings

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;

    TrieNode() : isEndOfWord(false) {}
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
    }

    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }

    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return true;
    }
};
```

## Test Cases
```
Input: 
Trie trie;
trie.insert("apple");
trie.insert("app");
trie.insert("banana");
Output: 
trie.search("apple") = true
trie.search("app") = true
trie.search("ap") = false
trie.startsWith("app") = true
trie.startsWith("ban") = true
trie.startsWith("ora") = false
```

## Key Takeaways
- The Trie data structure is useful for efficient string matching and prefix lookup.
- The use of an unordered map to represent the Trie nodes allows for fast lookup and insertion times.
- The `insert`, `search`, and `startsWith` operations have a time complexity of O(m) where m is the length of the string or prefix.