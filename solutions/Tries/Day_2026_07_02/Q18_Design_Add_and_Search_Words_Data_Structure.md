# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
A word could contain the dot character '.' to represent any one letter. 
For example, if the data structure contains the word "bad" then it should return true for "bad" and false for "dad" but true for ".ad". 
The data structure should support up to 2500 operations.

## Approach
We will utilize a Trie data structure to efficiently store and retrieve words. 
The Trie will be implemented using a nested unordered_map to represent the tree structure.
We will iterate through each word and character to build the Trie and perform the search operation.

## Complexity
- Time: O(m) where m is the length of the word for both addWord and search operations
- Space: O(n*m) where n is the number of words and m is the average length of a word

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
        return searchFrom(root, word);
    }

    bool searchFrom(TrieNode* node, string word) {
        for (int i = 0; i < word.size(); i++) {
            char c = word[i];
            if (c == '.') {
                for (auto child : node->children) {
                    if (searchFrom(child.second, word.substr(i + 1))) {
                        return true;
                    }
                }
                return false;
            } else {
                if (node->children.find(c) == node->children.end()) {
                    return false;
                }
                node = node->children[c];
            }
        }
        return node->isEndOfWord;
    }
};
```

## Test Cases
```
Input: 
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output: 
[null,null,null,null,false,true,true,true]
```

## Key Takeaways
- Using a Trie data structure is efficient for storing and retrieving words with prefix and suffix matches.
- The search operation can be optimized by utilizing a recursive approach to handle the '.' character.
- Memory management is crucial when using pointers to avoid memory leaks.