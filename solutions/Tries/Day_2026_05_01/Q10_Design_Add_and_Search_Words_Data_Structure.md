# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(string word)`: Adds a word to the data structure.
- `bool search(string word)`: Returns true if the word is in the data structure. 
A word could contain the dot character '.' to represent any one letter. 
For example, `addWord("bad")` then `search("pad")` -> false, `search("bad")` -> true, `search(".ad")` -> true, `search("b..")` -> true.

## Approach
The approach is to use a Trie data structure to store the words. We will iterate over each word and insert it into the Trie. For the search operation, we will use a depth-first search (DFS) approach to handle the '.' character.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(N*M) where N is the number of words and M is the maximum length of a word

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
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isWord = true;
    }

    bool search(string word) {
        return dfs(root, word, 0);
    }

    bool dfs(TrieNode* node, string word, int index) {
        if (index == word.size()) {
            return node->isWord;
        }
        if (word[index] == '.') {
            for (auto& child : node->children) {
                if (dfs(child.second, word, index + 1)) {
                    return true;
                }
            }
            return false;
        }
        if (node->children.find(word[index]) == node->children.end()) {
            return false;
        }
        return dfs(node->children[word[index]], word, index + 1);
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
wordDictionary.search("pad") -> false
wordDictionary.search("bad") -> true
wordDictionary.search(".ad") -> true
wordDictionary.search("b..") -> true
```

## Key Takeaways
- Use a Trie data structure to store the words for efficient insertion and search.
- Use a depth-first search (DFS) approach to handle the '.' character in the search operation.
- The time complexity is O(N*M) where N is the number of words and M is the maximum length of a word.