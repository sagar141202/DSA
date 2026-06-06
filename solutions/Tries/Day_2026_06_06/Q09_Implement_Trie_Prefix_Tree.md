# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should be able to store a collection of strings. The `insert` operation should add a new string to the Trie if it does not already exist. The `search` operation should return `true` if the given string is in the Trie, and `false` otherwise. The `startsWith` operation should return `true` if there is any string in the Trie that starts with the given prefix, and `false` otherwise. The Trie should be able to handle a large number of strings and should be efficient in terms of time and space complexity. For example, given the strings "apple", "app", and "banana", the Trie should be able to correctly handle the following operations: `insert("apple")`, `insert("app")`, `insert("banana")`, `search("apple")`, `search("app")`, `search("banana")`, `search("bat")`, `startsWith("app")`, `startsWith("ban")`, `startsWith("ora")`.

## Approach
The algorithm uses a Trie data structure to store the strings, where each node in the Trie represents a character in the string. The `insert` operation iterates through the characters in the string and adds new nodes to the Trie as necessary. The `search` and `startsWith` operations iterate through the characters in the string and check if the corresponding nodes exist in the Trie.

## Complexity
- Time: O(m) where m is the length of the string
- Space: O(n*m) where n is the number of strings and m is the average length of the strings

## C++ Solution
```cpp
#include <unordered_map>
#include <string>

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

    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
    }

    bool search(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }

    bool startsWith(const string& prefix) {
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
trie.search("bat") -> false
trie.startsWith("app") -> true
trie.startsWith("ban") -> true
trie.startsWith("ora") -> false
```

## Key Takeaways
- The Trie data structure is suitable for storing a large number of strings and performing prefix-based queries.
- The `insert`, `search`, and `startsWith` operations have a time complexity of O(m) where m is the length of the string.
- The space complexity of the Trie is O(n*m) where n is the number of strings and m is the average length of the strings.