# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns `true` if the word is in the data structure, otherwise returns `false`.
The `search` function also supports searching with a dot `.` which is a wildcard that can be replaced with any single letter.
For example, `addWord("bad")` and `search("pad")` returns `false`, but `search("b.d")` returns `true`.
Constraints: 
- Only lowercase English letters will be used.
- The maximum length of a word is 500.
- The maximum number of `addWord` and `search` operations is 10,000.

## Approach
We will use a Trie data structure, which is a tree-like data structure where each node stores a string.
We will iterate through each character in the word and create a new node if the character does not exist in the Trie.
For the `search` function, we will also use a depth-first search approach to handle the wildcard character.

## Complexity
- Time: O(m) where m is the length of the word
- Space: O(n*m) where n is the number of words and m is the average length of a word

## C++ Solution
```cpp
#include <unordered_map>
#include <string>

using namespace std;

class WordDictionary {
public:
    **struct TrieNode {
        bool isWord;
        unordered_map<char, TrieNode*> children;
        TrieNode() : isWord(false) {}
    };**

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
        return search(root, word, 0);
    }

    bool search(TrieNode* node, string word, int index) {
        if (index == word.size()) {
            return node->isWord;
        }
        char c = word[index];
        if (c == '.') {
            for (auto& child : node->children) {
                if (search(child.second, word, index + 1)) {
                    return true;
                }
            }
            return false;
        }
        if (!node->children.count(c)) {
            return false;
        }
        return search(node->children[c], word, index + 1);
    }

private:
    TrieNode* root;
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
- Use a Trie data structure to store words for efficient search and add operations.
- Implement a depth-first search approach to handle the wildcard character in the `search` function.
- Use an unordered map to store the children of each node in the Trie for efficient lookup.