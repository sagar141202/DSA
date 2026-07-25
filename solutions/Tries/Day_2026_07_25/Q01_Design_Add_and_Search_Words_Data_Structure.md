# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
The `search` function should also return true if the word is a prefix of another word in the data structure. 
However, if the word contains a '.' character, it should be treated as a wildcard character that can be replaced with any letter. 
The data structure should be case-sensitive and support words with uppercase and lowercase letters.

## Approach
We will use a Trie data structure with a nested map to store the words. 
The Trie will allow us to efficiently add and search for words. 
We will also implement a recursive function to handle the '.' wildcard character.

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
        bool isWord;
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
        node->isWord = true;
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
            }
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->isWord;
    }
};
```

## Test Cases
```
Input: WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // returns False
wordDictionary.search("bad"); // returns True
wordDictionary.search(".ad"); // returns True
wordDictionary.search("b.."); // returns True
```

## Key Takeaways
- Use a Trie data structure to efficiently store and search for words.
- Implement a recursive function to handle the '.' wildcard character.
- Use a nested map to store the children of each Trie node.