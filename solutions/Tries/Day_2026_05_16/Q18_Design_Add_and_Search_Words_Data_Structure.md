# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports adding new words and searching for words where some letters can be represented by a wildcard character. The data structure should have two methods: `void addWord(string word)` and `bool search(string word)`. The `addWord` method adds a word to the data structure, and the `search` method checks if a word is present in the data structure. The word can contain dots (`.`) which represent any single letter. For example, `addWord("bad")` followed by `search("pad")` should return `false`, while `addWord("pad")` followed by `search("bad")` should also return `false`. However, `addWord("pad")` followed by `search("pad")` should return `true`, and `addWord("bad")` followed by `search(".ad")` should return `true`.

## Approach
The approach is to use a Trie data structure with a recursive search function to handle the wildcard character. Each node in the Trie will store a boolean value indicating whether a word ends at that node, and a map of its child nodes. The search function will recursively traverse the Trie, checking each character in the search word against the corresponding child node.

## Complexity
- Time: O(N * M) for the search operation, where N is the length of the search word and M is the number of nodes in the Trie.
- Space: O(N) for the space used by the Trie, where N is the total number of characters in all words.

## C++ Solution
```cpp
#include <unordered_map>
#include <string>

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
- We use a Trie data structure to efficiently store and search for words.
- The `search` function uses recursion to handle the wildcard character, checking all possible child nodes.
- The time complexity of the `search` operation is O(N * M), where N is the length of the search word and M is the number of nodes in the Trie.