# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
The `search` method supports the "." wildcard character, where "." can match any single character. For example, `addWord("bad")` and `addWord("dad")`, then `search("pad")` returns false, while `search("bad")` returns true. Also, `search(".ad")` returns true, and `search("b..")` returns true.

## Approach
The problem can be solved using a Trie data structure with a recursive search function. The Trie allows for efficient storage and retrieval of words, while the recursive search function handles the "." wildcard character.

## Complexity
- Time: O(N*M) for search operation where N is the number of words and M is the maximum length of a word
- Space: O(N*M) for storing the Trie

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
        return searchWord(word, root);
    }

    bool searchWord(string word, TrieNode* node) {
        for (int i = 0; i < word.size(); i++) {
            char c = word[i];
            if (c == '.') {
                for (auto child : node->children) {
                    if (searchWord(word.substr(i + 1), child.second)) {
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
Output: wordDictionary.search("pad") -> false
wordDictionary.search("bad") -> true
wordDictionary.search(".ad") -> true
wordDictionary.search("b..") -> true
```

## Key Takeaways
- The Trie data structure is particularly useful for storing and retrieving strings.
- The recursive search function allows for efficient handling of the "." wildcard character.
- The `addWord` and `search` operations have a time complexity of O(M) and O(N*M) respectively, where N is the number of words and M is the maximum length of a word.