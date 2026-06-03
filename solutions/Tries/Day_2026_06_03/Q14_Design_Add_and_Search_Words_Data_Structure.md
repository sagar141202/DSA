# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure, where word may contain dots (`.`) as wildcards. 
The `word` will only contain lowercase English letters or dots. The maximum length of a word is 500 characters. The maximum number of `addWord` and `search` operations is 10,000.

## Approach
We use a Trie data structure to store the words. Each node in the Trie contains a boolean flag to indicate whether a word ends at that node and a map to store the child nodes. We iterate through each character in the word and create a new node if the character does not exist in the current node's children.

## Complexity
- Time: O(m) for both addWord and search operations, where m is the length of the word.
- Space: O(n*m) where n is the number of words and m is the maximum length of a word.

## C++ Solution
```cpp
#include <unordered_map>
#include <string>

using namespace std;

class WordDictionary {
public:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isEndOfWord;
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
            }
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
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
- Use a Trie data structure to efficiently store and search for words with wildcards.
- Implement a recursive search function to handle the wildcard character (`.`).
- Use an unordered_map to store the child nodes of each Trie node for efficient lookup.