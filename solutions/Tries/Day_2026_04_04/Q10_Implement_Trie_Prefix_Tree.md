# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store a collection of strings. The `insert` operation inserts a string into the Trie, the `search` operation checks if a string is in the Trie, and the `startsWith` operation checks if there is any string in the Trie that starts with a given prefix. The Trie should be case-sensitive and should handle duplicate strings.

## Approach
The algorithm uses a Trie data structure with a nested map to store the children of each node. The `insert` operation iterates through each character in the string and creates a new node if the character is not in the current node's children. The `search` and `startsWith` operations also iterate through each character in the string and check if the character is in the current node's children.

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
private:
    TrieNode* root;

public:
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
trie.search("ban") -> false
trie.startsWith("app") -> true
trie.startsWith("ban") -> true
trie.startsWith("ora") -> false
```

## Key Takeaways
- The Trie data structure is useful for storing a collection of strings and supporting operations like `insert`, `search`, and `startsWith`.
- The `insert` operation has a time complexity of O(m) where m is the length of the string.
- The `search` and `startsWith` operations also have a time complexity of O(m) where m is the length of the string.