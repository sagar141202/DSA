# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store a collection of strings, and the operations should be performed efficiently. The `insert` operation should add a new string to the Trie, the `search` operation should return whether a given string is in the Trie, and the `startsWith` operation should return whether there is any string in the Trie that starts with a given prefix. The input strings will only contain lowercase letters, and the maximum length of a string is 100. The maximum number of operations is 10^4.

## Approach
The approach is to create a Trie data structure using a nested map to store the children of each node, and a boolean flag to mark the end of a word. The `insert` operation iterates over the characters of the input string, creating new nodes as necessary. The `search` operation checks if a word is in the Trie by traversing the nodes corresponding to the characters of the word. The `startsWith` operation checks if a prefix is in the Trie by traversing the nodes corresponding to the characters of the prefix.

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
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
    }

    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }

    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (!node->children.count(c)) {
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
trie.search("apple") -> true
trie.search("app") -> true
trie.search("banana") -> true
trie.search("ban") -> false
trie.startsWith("app") -> true
trie.startsWith("ban") -> true
trie.startsWith("ora") -> false
```

## Key Takeaways
- The Trie data structure is useful for storing a collection of strings and performing prefix-based operations efficiently.
- The `insert` operation creates new nodes as necessary, while the `search` and `startsWith` operations traverse the existing nodes to find the desired strings or prefixes.
- The time complexity of the operations is O(m), where m is the length of the input string, and the space complexity is O(n*m), where n is the number of strings and m is the average length of the strings.