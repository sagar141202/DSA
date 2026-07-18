# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
The word may contain dots (`.`) which can be used as wildcards to represent any letter. 
For example, `addWord("bad")` and `search("pad")` should return false, while `addWord("pad")` and `search("bad")` should return false, and `addWord("pad")` and `search(".ad")` should return true. 
The data structure should support up to 2500 operations.

## Approach
The problem can be solved using a Trie data structure, which is a tree-like data structure where each node stores a string. 
We will iterate over each character in the word and create a new node if the character does not exist in the current node. 
If the character is a dot (`.`), we will create a new node for all possible characters.

## Complexity
- Time: O(m) for addWord and search operations, where m is the length of the word.
- Space: O(n*m) for storing all words, where n is the number of words.

## C++ Solution
```cpp
#include <unordered_map>
using namespace std;

class WordDictionary {
private:
    unordered_map<char, WordDictionary*> children;
    bool isEnd;

public:
    WordDictionary() : isEnd(false) {}

    void addWord(string word) {
        WordDictionary* node = this;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new WordDictionary();
            }
            node = node->children[c];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        return searchHelper(this, word, 0);
    }

    bool searchHelper(WordDictionary* node, string word, int index) {
        for (int i = index; i < word.size(); i++) {
            char c = word[i];
            if (c == '.') {
                for (auto child : node->children) {
                    if (searchHelper(child.second, word, i + 1)) {
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
        return node->isEnd;
    }
};
```

## Test Cases
```
Input: WordDictionary wordDictionary = new WordDictionary();
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
- The Trie data structure is suitable for problems that involve prefix matching or wildcards.
- The `addWord` operation involves iterating over each character in the word and creating a new node if necessary.
- The `search` operation involves recursively checking all possible nodes for a given character or wildcard.