# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store a collection of strings, where each string is a sequence of characters. The `insert` operation adds a new string to the Trie, the `search` operation checks if a given string is in the Trie, and the `startsWith` operation checks if there is any string in the Trie that starts with a given prefix. The constraints are that the Trie will contain at most 10^4 strings, each string will contain only lowercase English letters, and the length of each string will not exceed 10^2 characters.

## Approach
The approach to solving this problem is to create a Trie data structure using a nested map to store the characters and their corresponding child nodes. We will implement the `insert`, `search`, and `startsWith` operations using recursive functions that traverse the Trie.

## Complexity
- Time: O(m) where m is the length of the string for insert, search, and startsWith operations
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
trie.search("apple") -> True
trie.search("app") -> True
trie.search("banana") -> True
trie.search("ban") -> False
trie.startsWith("app") -> True
trie.startsWith("ban") -> True
trie.startsWith("ora") -> False
```

## Key Takeaways
- The Trie data structure is useful for storing and retrieving strings with common prefixes.
- The `insert`, `search`, and `startsWith` operations can be implemented using recursive functions that traverse the Trie.
- The time complexity of these operations is O(m) where m is the length of the string, and the space complexity is O(n*m) where n is the number of strings and m is the average length of the strings.