# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The Trie should store strings and allow for efficient retrieval of strings that start with a given prefix. The constraints are as follows: 1 <= word.length, prefix.length <= 2000, word and prefix consist only of lowercase English letters, and at most 3 * 10^4 calls will be made to insert, search, and startsWith.

## Approach
The approach is to use a Trie data structure with a nested hashmap to store the children of each node. We will iterate over each character in the input string and create a new node if the character does not exist in the current node's children. The algorithm will have a time complexity of O(m), where m is the length of the input string.

## Complexity
- Time: O(m)
- Space: O(n*m)

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
private:
    TrieNode* root;

public:
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
Input: Trie trie; trie.insert("apple"); trie.insert("app"); trie.insert("banana");
Output: trie.search("apple") -> true, trie.search("app") -> true, trie.search("banana") -> true, trie.search("ban") -> false
trie.startsWith("app") -> true, trie.startsWith("ban") -> true, trie.startsWith("ora") -> false
```

## Key Takeaways
- The Trie data structure is useful for storing and retrieving strings with common prefixes.
- The `insert` operation iterates over each character in the input string and creates a new node if the character does not exist in the current node's children.
- The `search` operation iterates over each character in the input string and returns false if the character does not exist in the current node's children. If the end of the string is reached, it checks if the current node is the end of a word.