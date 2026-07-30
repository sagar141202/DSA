# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store a collection of strings, and the operations should be performed efficiently. The `insert` operation adds a new string to the Trie, the `search` operation checks if a given string is in the Trie, and the `startsWith` operation checks if there is any string in the Trie that starts with the given prefix. The input strings will only contain lowercase letters, and the maximum length of a string is 100.

## Approach
The algorithm uses a Trie data structure to store the strings, where each node represents a character in the string. The `insert` operation iterates through the characters in the string and creates new nodes as necessary. The `search` and `startsWith` operations also iterate through the characters in the string and check if the corresponding nodes exist in the Trie.

## Complexity
- Time: O(m) where m is the length of the string
- Space: O(n*m) where n is the number of strings and m is the maximum length of a string

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

    Trie() : root(new TrieNode()) {}

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
Input: Trie trie; trie.insert("apple"); trie.insert("app"); trie.insert("banana");
Output: trie.search("apple") -> true, trie.search("app") -> true, trie.search("banana") -> true, trie.search("ban") -> false
Output: trie.startsWith("app") -> true, trie.startsWith("ban") -> true, trie.startsWith("ora") -> false
```

## Key Takeaways
- The Trie data structure is useful for storing a collection of strings and performing prefix-based operations efficiently.
- The `insert` operation has a time complexity of O(m) where m is the length of the string.
- The `search` and `startsWith` operations also have a time complexity of O(m) where m is the length of the string.