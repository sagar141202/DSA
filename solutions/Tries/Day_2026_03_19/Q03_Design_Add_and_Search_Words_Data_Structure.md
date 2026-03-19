# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
The data structure should also support searching with a '.' character, which can represent any letter. 
For example, `addWord("bad")` and `search("pad")` should return false, but `addWord("bad")` and `search(".ad")` should return true.

## Approach
We can use a Trie data structure to store the words, where each node in the Trie represents a character in the word. 
To support searching with '.', we can recursively search all possible branches of the Trie. 
This allows us to efficiently search for words with '.' characters.

## Complexity
- Time: O(N * M), where N is the number of words and M is the maximum length of a word
- Space: O(N * M), where N is the number of words and M is the maximum length of a word

## C++ Solution
```cpp
class WordDictionary {
private:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isWord;
        TrieNode() : isWord(false) {}
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
Input: WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
Output: wordDictionary.search("pad") -> False
wordDictionary.search("bad") -> True
wordDictionary.search(".ad") -> True
```

## Key Takeaways
- Use a Trie data structure to store words for efficient search.
- Recursively search all possible branches of the Trie to support searching with '.' characters.
- Use a helper function to simplify the search logic and avoid code duplication.