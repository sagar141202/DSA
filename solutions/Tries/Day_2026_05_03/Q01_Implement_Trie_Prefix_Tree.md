# Implement Trie (Prefix Tree)

## Problem Statement
Implement a trie (prefix tree) with the following methods: `insert`, `search`, and `startsWith`. The `insert` method inserts a word into the trie, the `search` method checks if a word is in the trie, and the `startsWith` method checks if there is any word in the trie that starts with the given prefix. The trie should be case-sensitive and should not contain any duplicate words.

## Approach
The algorithm uses a nested unordered map to represent the trie, where each key is a character and each value is another unordered map. The `insert` method iterates over each character in the word and adds it to the trie if it does not exist. The `search` method checks if the word is in the trie by iterating over each character and checking if it exists in the trie. The `startsWith` method checks if the prefix is in the trie by iterating over each character and checking if it exists in the trie.

## Complexity
- Time: O(m) where m is the length of the word
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
trie.search("ap") -> false
trie.startsWith("app") -> true
trie.startsWith("ban") -> true
trie.startsWith("ora") -> false
```

## Key Takeaways
- The trie data structure is useful for tasks that involve frequent prefix matching, such as autocomplete and spell-checking.
- The time complexity of the `insert`, `search`, and `startsWith` methods is O(m) where m is the length of the word.
- The space complexity of the trie is O(n*m) where n is the number of words and m is the average length of the words.