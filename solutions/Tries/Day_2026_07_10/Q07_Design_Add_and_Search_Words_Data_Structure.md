# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
The `search` function should also return true if the word is a prefix of another word in the data structure, and it should also support regex-like '*' character which can represent any sequence of characters, including an empty sequence. 
For example, `addWord("bad")` and `addWord("dad")`, then `search("pad")` returns false, `search("ba")` returns false, `search(".ad")` returns true, `search("b..")` returns true.

## Approach
The problem can be solved by using a Trie data structure, where each node stores a dictionary of its children and a boolean flag to indicate whether it's the end of a word. We iterate through each character in the word and add it to the Trie if it's not already there. For the search function, we use a recursive approach to handle the '*' character.

## Complexity
- Time: O(m) for addWord and search, where m is the length of the word
- Space: O(n*m) for storing all the words, where n is the number of words

## C++ Solution
```cpp
#include <unordered_map>
#include <string>

using namespace std;

class WordDictionary {
public:
    class TrieNode {
    public:
        unordered_map<char, TrieNode*> children;
        bool is_word;
        
        TrieNode() : is_word(false) {}
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
        node->is_word = true;
    }
    
    bool search(string word) {
        return searchHelper(root, word, 0);
    }

private:
    TrieNode* root;

    bool searchHelper(TrieNode* node, string word, int index) {
        if (index == word.size()) {
            return node->is_word;
        }
        char c = word[index];
        if (c == '.') {
            for (auto child : node->children) {
                if (searchHelper(child.second, word, index + 1)) {
                    return true;
                }
            }
            return false;
        } else if (node->children.find(c) != node->children.end()) {
            return searchHelper(node->children[c], word, index + 1);
        } else if (c == '*') {
            if (searchHelper(node, word, index + 1)) {
                return true;
            }
            for (auto child : node->children) {
                if (searchHelper(child.second, word, index)) {
                    return true;
                }
            }
            return false;
        }
        return false;
    }
};
```

## Test Cases
```
Input: WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
Output: wordDictionary.search("pad") -> false
wordDictionary.search("bad") -> true
wordDictionary.search(".ad") -> true
wordDictionary.search("b..") -> true
```

## Key Takeaways
- A Trie data structure is suitable for storing a collection of strings and supporting prefix matching and regex-like searches.
- The `addWord` function iterates through each character in the word and adds it to the Trie if it's not already there.
- The `search` function uses a recursive approach to handle the '*' character, which can represent any sequence of characters.