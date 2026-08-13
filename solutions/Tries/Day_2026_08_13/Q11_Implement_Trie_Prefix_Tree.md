# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store a collection of strings, where each string is composed of lowercase English letters. The `insert` operation adds a new string to the Trie, the `search` operation checks if a given string is present in the Trie, and the `startsWith` operation checks if there is any string in the Trie that starts with a given prefix. The Trie should be case-sensitive and should handle duplicate strings.

## Approach
The algorithm uses a nested unordered map to represent the Trie, where each node stores a boolean value indicating whether a word ends at that node and a map of its child nodes. The `insert` operation iterates over each character in the string and adds a new node to the Trie if the character is not present. The `search` and `startsWith` operations traverse the Trie based on the input string and return the result.

## Complexity
- Time: O(m) where m is the length of the input string
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
trie.startsWith("app") -> true, trie.startsWith("ban") -> true, trie.startsWith("ora") -> false
```

## Key Takeaways
- The Trie data structure is suitable for storing a collection of strings and supporting prefix-based operations.
- The use of a nested unordered map allows for efficient storage and retrieval of the Trie nodes.
- The `insert`, `search`, and `startsWith` operations have a time complexity of O(m), where m is the length of the input string.