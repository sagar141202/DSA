# Longest Word in Dictionary

## Problem Statement
Given a list of strings which contains a list of dictionary words, find the longest word in the dictionary that can be formed by other words in the list. A word can be formed by other words if it can be constructed by concatenating other words in the list. For example, "cat" can be formed by "ca" and "t" if both "ca" and "t" are in the list. The function should return the longest word that can be formed by other words.

## Approach
We will use a Trie data structure to store all the words in the dictionary, and then check for each word if it can be formed by other words. We will iterate through the word and check if any prefix of the word is in the Trie.

## Complexity
- Time: O(N * M^2) where N is the number of words and M is the maximum length of a word
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
        if (canBeFormed(word, trie.root)) {
            if (word.length() > longest.length()) {
                longest = word;
            }
        }
    }
    return longest;
}

bool canBeFormed(string word, TrieNode* node) {
    for (int i = 0; i < word.length(); i++) {
        if (node->children.find(word[i]) == node->children.end()) {
            return false;
        }
        node = node->children[word[i]];
        if (node->isEndOfWord && i < word.length() - 1) {
            if (canBeFormed(word.substr(i + 1), node)) {
                return true;
            }
        }
    }
    return node->isEndOfWord;
}

int main() {
    vector<string> words = {"w","wo","wor","word"};
    cout << longestWord(words) << endl;
    return 0;
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
- We use a Trie data structure to efficiently store and retrieve words.
- We iterate through each word and check if it can be formed by other words using the Trie.
- The time complexity is O(N * M^2) due to the recursive function call in the canBeFormed function.