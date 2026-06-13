# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure, which is a tree-like data structure that is often used to store a dynamic set or associative array where the keys are usually strings. The Trie should support the following operations: `insert(word)`, `search(word)`, and `startsWith(prefix)`. The `insert(word)` operation adds a new word to the Trie, the `search(word)` operation checks if a word is already in the Trie, and the `startsWith(prefix)` operation checks if there is any word in the Trie that starts with the given prefix. The Trie should be case-sensitive and should handle words with lowercase and uppercase letters.

## Approach
The algorithm uses a nested hashmap to store the characters of the words, where each character is a key in the hashmap and its corresponding value is another hashmap. The Trie is implemented using a class with methods for insertion, search, and prefix check. The time complexity of the operations is proportional to the length of the word or prefix.

## Complexity
- Time: O(m) where m is the length of the word or prefix
- Space: O(n*m) where n is the number of words and m is the average length of the words

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
- Tries are useful for storing and retrieving strings with common prefixes.
- The time complexity of Trie operations depends on the length of the word or prefix.
- Tries can be implemented using a nested hashmap or a tree-like data structure.