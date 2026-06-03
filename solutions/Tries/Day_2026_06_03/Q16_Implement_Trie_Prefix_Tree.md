# Implement Trie (Prefix Tree)

## Problem Statement
Implement a trie (prefix tree) with the following methods: `insert`, `search`, and `startsWith`. The `insert` method inserts a word into the trie, the `search` method checks if a word is in the trie, and the `startsWith` method checks if there is any word in the trie that starts with the given prefix. The trie should be case-sensitive and should not contain any duplicate words.

## Approach
The approach is to create a TrieNode class that contains a boolean flag to mark the end of a word and a map to store the child nodes. The `insert` method iterates over each character in the word and creates a new node if the character is not in the map. The `search` and `startsWith` methods also iterate over each character in the word and return false if the character is not in the map.

## Complexity
- Time: O(m) where m is the length of the word
- Space: O(n) where n is the total number of characters in all words

## C++ Solution
```cpp
#include <unordered_map>
using namespace std;

class TrieNode {
public:
    bool isEndOfWord;
    unordered_map<char, TrieNode*> children;
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
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output: 
[null, null, true, false, true, null, true]
```

## Key Takeaways
- The Trie data structure is useful for tasks that involve frequent prefix matching.
- The `insert`, `search`, and `startsWith` methods in the Trie class have a time complexity of O(m) where m is the length of the word.
- The space complexity of the Trie class is O(n) where n is the total number of characters in all words.