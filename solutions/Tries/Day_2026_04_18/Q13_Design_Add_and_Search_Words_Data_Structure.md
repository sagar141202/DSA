# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
The word may contain dots (`.`) which can be used as wildcards to represent any single character. 
For example, `addWord("bad")` and `search("pad")` should return false, but `addWord("pad")` and `search("bad")` should return true because the first 'p' can match the first 'b' due to the dot.

## Approach
The problem can be solved using a Trie data structure, where each node stores a boolean value indicating whether a word ends at that node and a map of its children nodes. 
We iterate over each character in the word, creating new nodes as necessary. 
For the search operation, we also iterate over each character in the word, using a recursive approach to handle the wildcard character.

## Complexity
- Time: O(m) where m is the length of the word
- Space: O(n*m) where n is the number of words and m is the average length of the words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class WordDictionary {
private:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isEndOfWord;
    };

    TrieNode* root;

public:
    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {
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
        return searchHelper(root, word, 0);
    }

    bool searchHelper(TrieNode* node, string word, int index) {
        if (index == word.size()) {
            return node->isEndOfWord;
        }

        char c = word[index];
        if (c == '.') {
            for (auto child : node->children) {
                if (searchHelper(child.second, word, index + 1)) {
                    return true;
                }
            }
            return false;
        } else {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            return searchHelper(node->children[c], word, index + 1);
        }
    }
};
```

## Test Cases
```
Input: 
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
Output: 
wordDictionary.search("pad") -> False
wordDictionary.search("bad") -> True
wordDictionary.search(".ad") -> True
wordDictionary.search("b..") -> True
```

## Key Takeaways
- The Trie data structure is particularly useful for problems that involve strings and prefix matching.
- The recursive approach can be used to handle the wildcard character in the search operation.
- The time complexity of the search operation is O(m) where m is the length of the word, because in the worst case we have to iterate over each character in the word.