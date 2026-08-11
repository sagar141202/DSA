# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
The search operation can use the dot `.` as a wildcard character, which can be substituted with any single letter. 
For example, `addWord("bad")` and `search(".ad")` should return true, while `search("b..")` should return false because the wildcard character can only be substituted with a single letter.

## Approach
We will use a Trie data structure to store the words. The Trie will have a root node, and each node will have 26 children (one for each letter of the alphabet) and a boolean value to indicate whether a word ends at that node. We will iterate through each word and add it to the Trie, and when searching for a word, we will use a recursive function to handle the wildcard character.

## Complexity
- Time: O(m) for addWord and O(26^m) for search, where m is the length of the word
- Space: O(n*m) for storing n words of maximum length m

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class WordDictionary {
private:
    struct TrieNode {
        TrieNode* children[26];
        bool isEndOfWord;
    };

    TrieNode* root;

    void addWordUtil(TrieNode* node, string word, int index) {
        if (index == word.size()) {
            node->isEndOfWord = true;
            return;
        }
        int charIndex = word[index] - 'a';
        if (node->children[charIndex] == nullptr) {
            node->children[charIndex] = new TrieNode();
        }
        addWordUtil(node->children[charIndex], word, index + 1);
    }

    bool searchUtil(TrieNode* node, string word, int index) {
        if (index == word.size()) {
            return node->isEndOfWord;
        }
        if (word[index] != '.') {
            int charIndex = word[index] - 'a';
            if (node->children[charIndex] == nullptr) {
                return false;
            }
            return searchUtil(node->children[charIndex], word, index + 1);
        } else {
            for (int i = 0; i < 26; i++) {
                if (node->children[i] != nullptr && searchUtil(node->children[i], word, index + 1)) {
                    return true;
                }
            }
            return false;
        }
    }

public:
    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {
        addWordUtil(root, word, 0);
    }

    bool search(string word) {
        return searchUtil(root, word, 0);
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
print(wordDictionary.search("pad")) // It returns False
print(wordDictionary.search("bad")) // It returns True
print(wordDictionary.search(".ad")) // It returns True
print(wordDictionary.search("b..")) // It returns True
```

## Key Takeaways
- We use a Trie data structure to store the words, which allows for efficient addition and search operations.
- The search operation uses a recursive function to handle the wildcard character, which can be substituted with any single letter.
- The time complexity of the addWord operation is O(m), where m is the length of the word, and the time complexity of the search operation is O(26^m) in the worst case.