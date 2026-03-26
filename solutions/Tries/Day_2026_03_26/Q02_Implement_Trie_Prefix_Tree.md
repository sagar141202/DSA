# Implement Trie (Prefix Tree)

## Problem Statement
Implement a trie (prefix tree) with the following methods: `insert`, `search`, and `startsWith`. The `insert` method inserts a word into the trie, the `search` method checks if a word is in the trie, and the `startsWith` method checks if there is any word in the trie that starts with the given prefix. The trie should support storing and retrieving strings of lowercase English letters.

## Approach
The approach is to create a TrieNode class that stores a boolean indicating whether a word ends at the node and a map of characters to child nodes. The `insert`, `search`, and `startsWith` methods will then be implemented using recursive or iterative traversals of the trie.

## Complexity
- Time: O(m) where m is the length of the word or prefix
- Space: O(n*m) where n is the number of words and m is the average length of the words

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
- The TrieNode class is used to represent each node in the trie, which stores a boolean indicating whether a word ends at the node and a map of characters to child nodes.
- The `insert`, `search`, and `startsWith` methods are implemented using recursive or iterative traversals of the trie.
- The time complexity of the `insert`, `search`, and `startsWith` methods is O(m) where m is the length of the word or prefix.