# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: `void addWord(word)` and `bool search(word)`. The `search` function should return `true` if the `word` is in the data structure and `false` otherwise. The `word` may contain dots (`.`) which is a wildcard that can represent any letter. The `word` is a string of lowercase letters and dots. The `addWord` function should add the `word` to the data structure if it is not already present, and the `search` function should return `true` if the `word` is in the data structure and `false` otherwise.

## Approach
We can solve this problem using a Trie data structure, where each node represents a character in the word. We can use a recursive approach to search for the word in the Trie, handling the wildcard character (`.`) by recursively searching all possible paths.

## Complexity
- Time: O(N*M) where N is the number of words and M is the average length of a word
- Space: O(N*M) where N is the number of words and M is the average length of a word

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class WordDictionary {
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
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isWord = true;
    }

    bool search(string word) {
        return searchHelper(root, word, 0);
    }

    bool searchHelper(TrieNode* node, string word, int index) {
        if (index == word.size()) {
            return node->isWord;
        }
        char c = word[index];
        if (c == '.') {
            for (auto child : node->children) {
                if (searchHelper(child.second, word, index + 1)) {
                    return true;
                }
            }
            return false;
        }
        if (!node->children.count(c)) {
            return false;
        }
        return searchHelper(node->children[c], word, index + 1);
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
- Use a Trie data structure to store the words
- Handle the wildcard character (`.`) by recursively searching all possible paths
- Use a recursive approach to search for the word in the Trie