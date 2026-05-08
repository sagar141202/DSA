# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: Adds a word to the data structure.
- `bool search(word)`: Returns `true` if the word is in the data structure. 
A word could contain the dot character('.') to represent any one letter. 
For example, `addWord("bad")` then `search("pad")` returns `false`, but `search("bad")` returns `true` because 'a' is present in the word list and 'b' and 'd' are also present in the word list. Also, `search("b..")` returns `true` because the first two characters do not matter.

## Approach
The problem can be solved by using a Trie data structure. We will create a Trie and add words to it. For the search operation, we will traverse the Trie according to the word. If the word contains '.', we will traverse all possible nodes.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(N*M) for storing the Trie

## C++ Solution
```cpp
class WordDictionary {
private:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isEnd;
        TrieNode() : isEnd(false) {}
    };

    TrieNode* root;

public:
    WordDictionary() : root(new TrieNode()) {}

    void addWord(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        return searchFrom(root, word, 0);
    }

    bool searchFrom(TrieNode* node, string& word, int index) {
        if (index == word.size()) {
            return node->isEnd;
        }
        if (word[index] == '.') {
            for (auto& child : node->children) {
                if (searchFrom(child.second, word, index + 1)) {
                    return true;
                }
            }
            return false;
        }
        if (!node->children.count(word[index])) {
            return false;
        }
        return searchFrom(node->children[word[index]], word, index + 1);
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
Output: wordDictionary.search("bad") -> true
Output: wordDictionary.search(".ad") -> true
Output: wordDictionary.search("b..") -> true
```

## Key Takeaways
- We use a Trie data structure to store the words.
- The search operation is implemented recursively to handle the '.' character.
- We use an unordered_map to store the children of each node in the Trie for efficient lookup.