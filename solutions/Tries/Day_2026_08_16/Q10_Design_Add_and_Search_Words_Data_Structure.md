# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: `addWord(word)` and `search(word)`. The `search(word)` method can search a literal word or a regular expression containing only dots `.` as wildcards. The `addWord(word)` method adds a word to the data structure, and the `search(word)` method checks if there is any word in the data structure that matches the given word. The data structure should support up to 2500 operations. A word can contain up to 250 characters, and the total length of all words is up to 10^5.

## Approach
The problem can be solved using a Trie data structure. We will create a Trie node with a boolean flag to mark the end of a word and a map to store the child nodes. We will iterate through each word and add it to the Trie. For the search operation, we will use a depth-first search (DFS) approach to traverse the Trie and check if the word matches.

## Complexity
- Time: O(M) for `addWord` and `search`, where M is the length of the word
- Space: O(N*M) for storing all words, where N is the number of words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class WordDictionary {
private:
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
        return dfs(root, word, 0);
    }

    bool dfs(TrieNode* node, string& word, int index) {
        if (index == word.size()) {
            return node->isEndOfWord;
        }
        if (word[index] == '.') {
            for (auto child : node->children) {
                if (dfs(child.second, word, index + 1)) {
                    return true;
                }
            }
        } else {
            if (node->children.find(word[index]) != node->children.end()) {
                return dfs(node->children[word[index]], word, index + 1);
            }
        }
        return false;
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
- Use a Trie data structure to store the words for efficient search.
- Implement a depth-first search (DFS) approach for the search operation.
- Handle the '.' wildcard character by recursively searching all child nodes.