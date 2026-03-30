# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, return the longest word that can be formed from other words in the list. If multiple words can be formed, return the longest word with the highest alphabetical order. If no such word exists, return an empty string. The list of words is provided as an array of strings. For example, given the list ["w","wo","wor","word"], the function should return "word". The input list will contain at least one word and will not contain any duplicates.

## Approach
We will use a Trie data structure to store the given words. Then we will iterate over each word in the list and check if it can be formed from other words in the Trie. We will keep track of the longest word that can be formed.

## Complexity
- Time: O(N * M) where N is the number of words and M is the maximum length of a word
- Space: O(N * M) for storing the Trie

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

class Trie {
public:
    TrieNode* root;
    Trie() : root(new TrieNode()) {}
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
};

string longestWord(vector<string>& words) {
    Trie trie;
    for (string word : words) {
        trie.insert(word);
    }
    string longest;
    for (string word : words) {
        if (canBeFormed(word, trie.root, trie)) {
            if (word.length() > longest.length() || (word.length() == longest.length() && word > longest)) {
                longest = word;
            }
        }
    }
    return longest;
}

bool canBeFormed(string word, TrieNode* node, Trie& trie) {
    if (word.empty()) {
        return node->isEndOfWord;
    }
    if (node->children.find(word[0]) != node->children.end()) {
        return canBeFormed(word.substr(1), node->children[word[0]], trie);
    }
    for (int i = 1; i < word.length(); ++i) {
        string prefix = word.substr(0, i);
        if (trie.root->children.find(prefix[0]) != trie.root->children.end() && canBeFormed(word.substr(i), trie.root->children[prefix[0]], trie)) {
            return true;
        }
    }
    return false;
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
- Use a Trie data structure to efficiently store and check the existence of words.
- Iterate over each word in the list and check if it can be formed from other words in the Trie.
- Keep track of the longest word that can be formed and return it as the result.