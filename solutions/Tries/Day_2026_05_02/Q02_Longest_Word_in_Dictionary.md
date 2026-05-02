# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed using other words in the list. The longest word should have at least one other word as a prefix, and the prefix should be a valid word in the list. If there are multiple words with the same length, return the lexicographically smallest one. For example, given the list `["w","wo","wor","word"]`, the function should return `"word"` because it can be formed by the words `"w"`, `"wo"`, and `"wor"`, which are all in the list.

## Approach
The approach is to use a Trie data structure to store the given list of words and then iterate through each word in the list to check if it can be formed by other words in the list. The word with the maximum length that can be formed is the answer.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(N * M) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
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
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }
};

string longestWord(vector<string>& words) {
    Trie trie;
    for (string word : words) {
        trie.insert(word);
    }
    
    string longest;
    for (string word : words) {
        if (word.length() < longest.length() || (word.length() == longest.length() && word > longest)) {
            continue;
        }
        
        bool valid = true;
        for (int i = 1; i < word.length(); i++) {
            string prefix = word.substr(0, i);
            if (!trie.search(prefix)) {
                valid = false;
                break;
            }
        }
        
        if (valid && (word.length() > longest.length() || (word.length() == longest.length() && word < longest))) {
            longest = word;
        }
    }
    
    return longest;
}
```

## Test Cases
```
Input: ["w","wo","wor","word"]
Output: "word"
Input: ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
```

## Key Takeaways
- Use a Trie data structure to store the given list of words for efficient lookup.
- Iterate through each word in the list to check if it can be formed by other words in the list.
- Keep track of the longest word that can be formed and update it if a longer word is found.