# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: `void addWord(word)` and `bool search(word)`. The `search` function checks if a word is in the data structure. A word could contain the dot character '.' to represent any one letter. For example, `"."` could be any letter in the alphabet. The data structure is not case sensitive, and all words are lowercase. The data structure should be able to handle a large number of words. The constraints are: 1 <= word.length <= 500, and the total number of calls to `addWord` and `search` is at most 10^4.

## Approach
The problem can be solved using a Trie data structure. We can create a Trie node class with a boolean flag to mark the end of a word and a hashmap to store the child nodes. The `addWord` function inserts a word into the Trie, and the `search` function checks if a word is in the Trie by traversing the Trie nodes.

## Complexity
- Time: O(m) where m is the length of the word
- Space: O(n*m) where n is the number of words and m is the average length of the words

## C++ Solution
```cpp
#include <unordered_map>
#include <string>

using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;

    TrieNode() : isEndOfWord(false) {}
};

class WordDictionary {
private:
    TrieNode* root;

public:
    WordDictionary() : root(new TrieNode()) {}

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
- Use a Trie data structure to store the words for efficient lookup and insertion.
- Handle the '.' character by recursively searching all child nodes.
- Mark the end of each word in the Trie to distinguish between words.