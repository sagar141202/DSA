# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should be able to store strings and check if a given string is present in the Trie or if there is any string that starts with a given prefix. The Trie should be case-sensitive and should handle only lowercase English letters. For example, given the following operations: `insert("apple")`, `search("apple")`, `search("app")`, `startsWith("app")`, the output should be `true`, `false`, `true` respectively.

## Approach
The approach is to create a Trie data structure using a nested map to store the child nodes of each node. We will use a boolean flag to mark the end of each word. The `insert` operation will iterate through each character of the word and create a new node if the character is not present in the current node. The `search` operation will also iterate through each character of the word and return false if the character is not present in the current node. The `startsWith` operation will return true if the prefix is present in the Trie.

## Complexity
- Time: O(m) where m is the length of the string
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
- A Trie is a data structure used to store a dynamic set or associative array where the keys are usually strings.
- The Trie data structure is particularly useful for tasks that involve frequent prefix matching, such as autocomplete and spell-checking.
- The time complexity of the Trie operations is O(m) where m is the length of the string, making it efficient for large datasets.