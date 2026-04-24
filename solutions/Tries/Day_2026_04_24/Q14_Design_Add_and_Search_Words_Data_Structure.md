# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: Adds a word to the data structure. 
- `bool search(word)`: Returns true if the word is in the data structure. 
The `search` function should return true if the word is in the data structure, and false otherwise. The `search` function also supports a special character `'.'` which can be used as a wildcard to match any single character. 
For example, `addWord("bad")` and `search("pad")` returns false, but `search("bad")` returns true, and `search(".ad")` returns true. 
The data structure should support at least 10^4 operations.

## Approach
The problem can be solved using a Trie data structure, where each node contains a map of characters to its child nodes and a boolean flag to indicate whether a word ends at the current node. 
The `addWord` operation involves traversing the Trie from the root node and creating new nodes if necessary, until the entire word is added. 
The `search` operation also involves traversing the Trie from the root node, but it should handle the special character `'.'` by exploring all possible child nodes.

## Complexity
- Time: O(m) where m is the length of the word
- Space: O(n*m) where n is the number of words

## C++ Solution
```cpp
#include <unordered_map>
using namespace std;

class WordDictionary {
public:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isWord;
    };

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
        return search(word, root);
    }

    bool search(string word, TrieNode* node) {
        for (int i = 0; i < word.size(); i++) {
            char c = word[i];
            if (c == '.') {
                for (auto child : node->children) {
                    if (search(word.substr(i + 1), child.second)) {
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

private:
    TrieNode* root;
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
- The Trie data structure is particularly useful for problems that involve string matching and retrieval.
- The `addWord` operation in a Trie involves traversing the Trie from the root node and creating new nodes if necessary.
- The `search` operation in a Trie should handle the special character `'.'` by exploring all possible child nodes.