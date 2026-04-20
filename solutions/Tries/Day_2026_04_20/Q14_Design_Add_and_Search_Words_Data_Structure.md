# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: `void addWord(word)` and `bool search(word)`. `search(word)` can search a literal word or a regular expression containing only dots `.` as wildcards. You may assume that all words added and searched will only consist of lowercase letters `a-z`. The maximum length of a word to be added or searched is 500. The `addWord` and `search` operations will be called at most 10,000 times.

## Approach
The problem can be solved using a Trie data structure, where each node contains a boolean indicating whether a word ends at that node and an unordered map to store the children of the node. The `addWord` operation involves inserting the word into the Trie, while the `search` operation involves traversing the Trie based on the given word, handling the dot `.` wildcard by recursively searching all possible paths.

## Complexity
- Time: O(N*M) for addWord and search, where N is the number of words and M is the maximum length of a word
- Space: O(N*M) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class WordDictionary {
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

        if (word[index] == '.') {
            for (auto& child : node->children) {
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
wordDictionary.search("pad"); // returns False
wordDictionary.search("bad"); // returns True
wordDictionary.search(".ad"); // returns True
wordDictionary.search("b.."); // returns True
```

## Key Takeaways
- Tries are suitable for problems involving string matching and prefix matching.
- Using a recursive approach can simplify the implementation of the `search` operation.
- Handling the dot `.` wildcard requires exploring all possible paths in the Trie.