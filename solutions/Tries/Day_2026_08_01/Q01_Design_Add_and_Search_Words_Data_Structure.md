# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports adding words and searching for words where some letters can be represented by a wildcard character ('.'). The data structure should have two methods: `void addWord(string word)` and `bool search(string word)`. The `addWord` method adds a word to the data structure, and the `search` method checks if a word is present in the data structure, considering the wildcard character. The word will only consist of lowercase English letters and the wildcard character.

## Approach
The approach to solve this problem is to use a Trie data structure. A Trie is a tree-like data structure where each node represents a character in the word. We will modify the Trie to handle the wildcard character by checking all possible paths from a node when a wildcard character is encountered.

## Complexity
- Time: O(m) for both addWord and search operations, where m is the length of the word
- Space: O(n*m) where n is the number of words and m is the average length of the words

## C++ Solution
```cpp
#include <unordered_map>
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
            } else if (node->children.find(c) == node->children.end()) {
                return false;
            } else {
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
["WordDictionary","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["pad"],["bad"],[".ad"],["b.."]]
Output: 
[null,null,null,false,true,true,true]
```

## Key Takeaways
- Use a Trie data structure to efficiently store and search for words
- Handle the wildcard character by checking all possible paths from a node when a wildcard character is encountered
- Implement recursive search to handle the wildcard character