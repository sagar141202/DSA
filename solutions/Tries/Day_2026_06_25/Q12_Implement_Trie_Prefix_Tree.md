# Implement Trie (Prefix Tree)

## Problem Statement
Implement a trie (prefix tree) data structure that supports the following operations: `insert`, `search`, and `startsWith`. The `insert` operation inserts a word into the trie, the `search` operation checks if a word is in the trie, and the `startsWith` operation checks if there is any word in the trie that starts with a given prefix. The trie should be case-sensitive and should handle words with duplicate characters. For example, given the words "apple", "app", and "banana", the `search` operation should return `true` for "apple" and `false` for "ban", and the `startsWith` operation should return `true` for "app" and `false` for "ban".

## Approach
The approach to solving this problem is to create a Trie class with a nested Node class. Each Node represents a character in the word and has a boolean flag to indicate if it's the end of a word. The Trie class has methods to insert a word, search for a word, and check if a prefix exists. The algorithm uses a recursive or iterative approach to traverse the trie and perform the required operations.

## Complexity
- Time: O(m) where m is the length of the word
- Space: O(n) where n is the total number of characters in all words

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
trie.search("ban") -> false
trie.startsWith("app") -> true
trie.startsWith("ban") -> false
```

## Key Takeaways
- The Trie data structure is useful for tasks that involve frequent prefix matching, such as autocomplete and spell-checking.
- The `insert` operation has a time complexity of O(m), where m is the length of the word.
- The `search` and `startsWith` operations also have a time complexity of O(m), where m is the length of the word or prefix.