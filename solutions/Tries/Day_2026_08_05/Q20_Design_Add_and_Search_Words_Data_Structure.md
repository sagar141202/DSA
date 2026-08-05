# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
The `search` function should also support searching with a wildcard '.' that can represent any single character. 
For example, `addWord("bad")` and `search("pad")` should return false, but `search("bad")` and `search(".ad")` should return true. 
You may assume that all words are composed of lowercase letters `a-z` and the wildcard character `'.'`.

## Approach
The problem can be solved using a Trie data structure, where each node stores a boolean value indicating whether a word ends at that node. 
The `addWord` operation involves inserting the word into the Trie, and the `search` operation involves traversing the Trie according to the given word.

## Complexity
- Time: O(m) where m is the length of the word
- Space: O(n*m) where n is the number of words and m is the average length of the words

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
        return search(word, root);
    }

    bool search(string word, TrieNode* node) {
        for (int i = 0; i < word.size(); i++) {
            char c = word[i];
            if (c == '.') {
                for (auto child : node->children) {
                    if (search(word.substr(i + 1), child.second)) {
                        return true;
                    }
                }
                return false;
            }
            if (!node->children.count(c)) {
                return false;
            }
            node = node->children[c];
        }
        return node->isWord;
    }
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
- The Trie data structure is suitable for problems involving string matching and prefix matching.
- The use of a wildcard character requires a depth-first search approach to explore all possible matches.
- The time complexity of the `search` operation can be optimized by using a recursive approach with memoization.