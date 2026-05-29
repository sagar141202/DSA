# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
A word could contain the dot character '.' to represent any one letter. 
For example, `addWord("bad")` and `search("pad")` returns `false`, while `addWord("pad")` and `search("pad")` returns `true`. 
Also, `addWord("bad")` and `search(".ad")` returns `true`, while `addWord(".ad")` and `search("bad")` returns `true`. 
You may assume that all words are composed of lowercase letters `a-z` and have maximum length of 500.

## Approach
The problem can be solved by using a Trie data structure. 
We will create a Trie node with a boolean flag to mark the end of a word and an unordered map to store the child nodes. 
The `addWord` operation will create a new path in the Trie if the word is not already present, and the `search` operation will traverse the Trie to find the word.

## Complexity
- Time: O(m) where m is the length of the word
- Space: O(n*m) where n is the number of words and m is the average length of the words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class WordDictionary {
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isEndOfWord;
        TrieNode() : isEndOfWord(false) {}
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
        if (word[index] == '.') {
            for (auto child : node->children) {
                if (searchHelper(child.second, word, index + 1)) {
                    return true;
                }
            }
            return false;
        }
        if (node->children.find(word[index]) == node->children.end()) {
            return false;
        }
        return searchHelper(node->children[word[index]], word, index + 1);
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
wordDictionary.search("pad"); // It returns False
wordDictionary.search("bad"); // It returns True
wordDictionary.search(".ad"); // It returns True
wordDictionary.search("b.."); // It returns True
```

## Key Takeaways
- Use a Trie data structure to store the words.
- The `addWord` operation creates a new path in the Trie if the word is not already present.
- The `search` operation traverses the Trie to find the word, using a recursive helper function to handle the '.' character.