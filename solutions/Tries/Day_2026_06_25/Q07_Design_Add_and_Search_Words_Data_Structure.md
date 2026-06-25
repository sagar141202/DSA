# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports adding words and searching for words where some letters can be represented by a wildcard character ('.'). The data structure should have two methods: `void addWord(string word)` and `bool search(string word)`. The `addWord` method adds a word to the data structure, and the `search` method returns true if the word is in the data structure, and false otherwise. The wildcard character '.' can represent any letter.

## Approach
The problem can be solved using a Trie data structure. We create a Trie node with a boolean flag to mark the end of a word and a map to store the child nodes. We iterate over each character in the word and create a new node if the character is not present in the Trie. For the search method, we check if the current character in the word matches the character in the Trie or if it is a wildcard character.

## Complexity
- Time: O(m) where m is the length of the word
- Space: O(n*m) where n is the number of words and m is the average length of the words

## C++ Solution
```cpp
#include <unordered_map>
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
- The Trie data structure is suitable for solving problems that involve adding and searching for words with wildcard characters.
- The search method in the Trie can be implemented using recursion or iteration.
- The time complexity of the search method is O(m) where m is the length of the word, and the space complexity is O(n*m) where n is the number of words and m is the average length of the words.