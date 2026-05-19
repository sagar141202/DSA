# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure
- `bool search(word)`: returns true if the word is in the data structure. 
The search function should also support searching with a '.' character which is a wildcard that can match any single character. 
For example, if you add the word "bad" and then search for "ba.", it should return true because "bad" matches "ba.".
The data structure should be case-sensitive and should support adding and searching words in any order.

## Approach
The problem can be solved using a Trie data structure, where each node stores a map of its children and a boolean flag indicating whether a word ends at that node. 
The search function will recursively traverse the Trie, handling the '.' character as a wildcard. 
This approach allows for efficient addition and searching of words.

## Complexity
- Time: O(m) where m is the length of the word
- Space: O(n*m) where n is the number of words and m is the average length of a word

## C++ Solution
```cpp
#include <unordered_map>
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
        return searchHelper(root, word, 0);
    }

    bool searchHelper(TrieNode* node, string word, int index) {
        if (index == word.size()) {
            return node->isWord;
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
Output: 
wordDictionary.search("pad") -> false
wordDictionary.search("bad") -> true
wordDictionary.search(".ad") -> true
wordDictionary.search("b..") -> true
```

## Key Takeaways
- The Trie data structure is particularly useful for problems involving strings and prefix matching.
- The search function can be optimized by using a recursive approach with memoization to avoid redundant computations.
- Handling the '.' character as a wildcard requires iterating over all children of the current node and recursively searching each subtree.