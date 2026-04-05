# Design Add and Search Words Data Structure

## Problem Statement
Design a data structure that supports the following two operations: 
- `void addWord(word)`: adds the word to the data structure.
- `bool search(word)`: returns true if the word is in the data structure. 
The `search(word)` operation may contain a '.' character, which is a wildcard that matches any single character.
For example, `addWord("bad")` and `addWord("dad")`, then `search("pad")` returns false, `search("bad")` returns true, and `search(".ad")` returns true.
You may assume that all words are composed of lowercase letters `a-z` and have a length between 1 and 100.
You may also assume that `atMost` one dot (.) exists in the given word.

## Approach
The problem can be solved using a Trie data structure. We will create a TrieNode class with a dictionary to store the children and a boolean to mark the end of the word. 
We will then implement the addWord and search operations using this Trie data structure.
The search operation will be implemented using a depth-first search approach to handle the '.' character.

## Complexity
- Time: O(n * m) where n is the number of words and m is the length of the word
- Space: O(n * m) where n is the number of words and m is the length of the word

## C++ Solution
```cpp
#include <bits/stdc++.h>
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
    WordDictionary() : root(new TrieNode()) {}
    
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
        return dfs(root, word, 0);
    }
    
    bool dfs(TrieNode* node, string word, int index) {
        if (index == word.size()) {
            return node->isEndOfWord;
        }
        char c = word[index];
        if (c == '.') {
            for (auto child : node->children) {
                if (dfs(child.second, word, index + 1)) {
                    return true;
                }
            }
            return false;
        } else {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            return dfs(node->children[c], word, index + 1);
        }
    }
};

int main() {
    WordDictionary wordDictionary;
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    cout << wordDictionary.search("pad") << endl;  // returns False
    cout << wordDictionary.search("bad") << endl;  // returns True
    cout << wordDictionary.search(".ad") << endl;  // returns True
    return 0;
}
```

## Test Cases
```
Input: 
addWord("bad")
addWord("dad")
search("pad")
search("bad")
search(".ad")
Output: 
False
True
True
```

## Key Takeaways
- The Trie data structure is useful for problems that involve string matching and searching.
- The dfs function is used to handle the '.' character in the search operation.
- The addWord operation is used to add words to the Trie data structure.
- The search operation is used to search for words in the Trie data structure.