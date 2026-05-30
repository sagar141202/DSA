# Implement Trie (Prefix Tree)

## Problem Statement
Implement a trie (prefix tree) with the following methods: `insert`, `search`, and `startsWith`. The trie should store strings, and the methods should return a boolean indicating whether the string is in the trie or not. The `insert` method should add a new string to the trie, the `search` method should check if a string is in the trie, and the `startsWith` method should check if there is any string in the trie that starts with the given prefix. The trie should be case-sensitive and should store only lowercase English letters.

## Approach
The algorithm uses a trie data structure, which is a tree-like data structure where each node stores a character and has children nodes for each possible next character. The `insert` method iterates through the string and adds new nodes to the trie as necessary. The `search` method checks if a string is in the trie by traversing the trie according to the characters in the string. The `startsWith` method checks if a prefix is in the trie by traversing the trie according to the characters in the prefix.

## Complexity
- Time: O(m) where m is the length of the string
- Space: O(n) where n is the total number of characters in all strings stored in the trie

## C++ Solution
```cpp
#include <unordered_map>
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
trie.search("apple") -> True
trie.search("app") -> True
trie.search("banana") -> True
trie.search("ban") -> False
trie.startsWith("app") -> True
trie.startsWith("ban") -> True
trie.startsWith("ora") -> False
```

## Key Takeaways
- The trie data structure is particularly useful for tasks that involve frequent string matching and prefix matching.
- The `insert`, `search`, and `startsWith` methods have a time complexity of O(m) where m is the length of the string.
- The space complexity of the trie is O(n) where n is the total number of characters in all strings stored in the trie.