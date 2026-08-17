# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store a collection of strings, and the operations should be performed efficiently. The `insert` operation inserts a new string into the Trie, the `search` operation checks if a given string exists in the Trie, and the `startsWith` operation checks if there is any string in the Trie that starts with a given prefix. The Trie should handle a large number of strings and support these operations with minimal time complexity.

## Approach
The algorithm uses a Trie data structure, which is a tree-like structure where each node represents a character in the string. The Trie is implemented using a nested unordered_map to store the child nodes of each node. The `insert` operation iterates through the string and creates new nodes if necessary, the `search` operation checks if the last node of the string exists in the Trie, and the `startsWith` operation checks if the nodes corresponding to the prefix exist in the Trie.

## Complexity
- Time: O(m) where m is the length of the string for `insert`, `search`, and `startsWith` operations
- Space: O(n*m) where n is the number of strings and m is the average length of the strings

## C++ Solution
```cpp
#include <unordered_map>
#include <string>

using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool is_end_of_word;

    TrieNode() : is_end_of_word(false) {}
};

class Trie {
public:
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
        node->is_end_of_word = true;
    }

    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->is_end_of_word;
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

private:
    TrieNode* root;
};
```

## Test Cases
```
Input: insert("apple"), search("apple"), startsWith("app")
Output: true, true
Input: insert("apple"), search("app"), startsWith("app")
Output: false, true
```

## Key Takeaways
- The Trie data structure is suitable for storing a large number of strings and supporting prefix-based operations.
- The use of an unordered_map to store child nodes allows for efficient lookup and insertion of nodes.
- The `is_end_of_word` flag is used to distinguish between complete words and prefixes.