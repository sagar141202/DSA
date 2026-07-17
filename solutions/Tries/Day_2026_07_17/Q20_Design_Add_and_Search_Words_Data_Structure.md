# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: `addWord(word)` and `search(word)`. `addWord(word)` adds a word to the data structure, while `search(word)` checks if a word is in the data structure. The `search(word)` operation may contain a '.' character, which is a wildcard that matches any single character. The data structure should support a maximum of 2500 operations (addWord and search), and each word consists only of lowercase English letters. For example, `addWord("bad")` and `search("pad")` should return False, while `addWord("bad")` and `search("bad")` should return True.

## Approach
The approach to solve this problem is to use a Trie data structure, where each node represents a character in the word. We will iterate through each word and add it to the Trie. When searching for a word, we will also iterate through the Trie and check for matches.

## Complexity
- Time: O(m) for addWord and search operations, where m is the length of the word
- Space: O(n*m) for storing all words, where n is the number of words and m is the average length of the words

## C++ Solution
```cpp
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
        return searchHelper(word, 0, root);
    }

    bool searchHelper(string word, int index, TrieNode* node) {
        if (index == word.size()) {
            return node->isEndOfWord;
        }

        char c = word[index];
        if (c == '.') {
            for (auto& child : node->children) {
                if (searchHelper(word, index + 1, child.second)) {
                    return true;
                }
            }
            return false;
        }

        if (node->children.find(c) == node->children.end()) {
            return false;
        }

        return searchHelper(word, index + 1, node->children[c]);
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
wordDictionary.search("pad"); // returns False
wordDictionary.search("bad"); // returns True
wordDictionary.search(".ad"); // returns True
wordDictionary.search("b.."); // returns True
```

## Key Takeaways
- Use a Trie data structure to store words for efficient search operations
- Handle the '.' character as a wildcard by recursively searching all child nodes
- Use a recursive helper function to simplify the search operation