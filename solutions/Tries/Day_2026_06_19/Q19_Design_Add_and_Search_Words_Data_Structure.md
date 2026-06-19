# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
The word may contain dots (`.`) which can be used as wildcards to represent any character. 
For example, `addWord("bad")` and `search("pad")` should return false, but `addWord("pad")` and `search("bad")` should return false, while `addWord("pad")` and `search(".ad")` should return true. 
The data structure should support up to 10^4 operations.

## Approach
We can use a Trie data structure to solve this problem. The Trie will store all the words, and for each word, we will traverse the Trie and check if the word matches the pattern. 
We will use a recursive approach to traverse the Trie and match the word with the pattern.

## Complexity
- Time: O(N*M) for addWord, O(26^M) for search where N is the number of words and M is the length of the word
- Space: O(N*M) where N is the number of words and M is the length of the word

## C++ Solution
```cpp
class WordDictionary {
private:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isWord;
    };
    TrieNode* root;
public:
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
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
        } else {
            if (!node->children.count(word[index])) {
                return false;
            }
            return searchHelper(node->children[word[index]], word, index + 1);
        }
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
         wordDictionary.search("b..") -> True
```

## Key Takeaways
- We use a Trie data structure to store the words.
- We use a recursive approach to traverse the Trie and match the word with the pattern.
- We use a `.` character as a wildcard to represent any character in the pattern.