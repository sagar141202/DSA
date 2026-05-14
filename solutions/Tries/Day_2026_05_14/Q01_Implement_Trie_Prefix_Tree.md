# Implement Trie (Prefix Tree)

## Problem Statement
Implement a Trie (Prefix Tree) data structure, which is a tree-like data structure that is often used to store a dynamic set or associative array where the keys are usually strings. The Trie should support the following operations: `insert(word)`, `search(word)`, and `startsWith(prefix)`. The `insert(word)` operation adds a new word to the Trie, the `search(word)` operation checks if a word is already in the Trie, and the `startsWith(prefix)` operation checks if there is any word in the Trie that starts with the given prefix. The Trie should be case-sensitive and should handle duplicate words by only storing each word once.

## Approach
The algorithm uses a nested unordered map to represent the Trie, where each node in the Trie is a map of characters to child nodes. The `insert` operation iterates through each character in the word and adds a new node to the Trie if the character is not already present. The `search` and `startsWith` operations also iterate through each character in the word or prefix and check if the corresponding node exists in the Trie.

## Complexity
- Time: O(m) where m is the length of the word or prefix
- Space: O(n*m) where n is the number of words in the Trie and m is the average length of the words

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
Input: Trie trie; trie.insert("apple"); trie.insert("app"); trie.insert("banana");
Output: trie.search("apple") -> true, trie.search("app") -> true, trie.search("banana") -> true, trie.search("ban") -> false
trie.startsWith("app") -> true, trie.startsWith("ban") -> true, trie.startsWith("ora") -> false
```

## Key Takeaways
- The Trie data structure is particularly useful for tasks that involve frequent prefix matching, such as autocomplete and spell-checking.
- The use of an unordered map to represent each node in the Trie allows for efficient lookup and insertion of characters.
- The `isEndOfWord` flag is used to distinguish between words that are prefixes of other words and words that are not.