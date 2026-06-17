# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
The `search` method supports the '.' character as a wildcard, meaning it can match any single character. 
For example, `addWord("bad")` and `search(".ad")` should return true. 
The data structure should be case-sensitive and support up to 2500 operations. 
The input word will only contain lowercase letters 'a' to 'z' and the '.' character.

## Approach
We can use a trie data structure to store the words and then perform a depth-first search to find matches for the search word. 
The trie will allow us to efficiently store and retrieve words, while the depth-first search will handle the '.' wildcard character.

## Complexity
- Time: O(N*M) where N is the number of words and M is the length of a word
- Space: O(N*M) where N is the number of words and M is the length of a word

## C++ Solution
```cpp
class WordDictionary {
public:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isEndOfWord;
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
        node->isEndOfWord = true;
    }

    bool search(string word) {
        return searchHelper(root, word, 0);
    }

    bool searchHelper(TrieNode* node, string word, int index) {
        for (int i = index; i < word.size(); i++) {
            char c = word[i];
            if (c == '.') {
                for (auto child : node->children) {
                    if (searchHelper(child.second, word, i + 1)) {
                        return true;
                    }
                }
                return false;
            } else {
                if (node->children.find(c) == node->children.end()) {
                    return false;
                }
                node = node->children[c];
            }
        }
        return node->isEndOfWord;
    }

private:
    TrieNode* root;
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
- Use a trie data structure to efficiently store and retrieve words
- Perform a depth-first search to handle the '.' wildcard character in the search word
- Use recursion to simplify the search function and improve code readability