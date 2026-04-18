# Longest Word in Dictionary

## Problem Statement
Given a dictionary of words, find the longest word that can be formed by other words in the dictionary. A word can be formed by other words if it can be constructed by concatenating other words in the dictionary. The dictionary does not contain duplicates and all words are in lowercase. For example, if the dictionary contains the words "cat", "cats", and "catsdogcats", then "catsdogcats" can be formed by "cat" and "cats" and "dog". The function should return the longest word that can be formed by other words in the dictionary.

## Approach
The approach to solve this problem involves using a Trie data structure to store the dictionary words and then checking each word in the dictionary to see if it can be formed by other words in the Trie. We use depth-first search to check all possible combinations of words.

## Complexity
- Time: O(N * M^2) where N is the number of words in the dictionary and M is the maximum length of a word
- Space: O(N * M) for storing the Trie and the dictionary words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool endOfWord;

    TrieNode() : endOfWord(false) {}
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
        node->endOfWord = true;
    }

    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->endOfWord;
    }
};

string longestWord(vector<string>& words) {
    Trie trie;
    for (string word : words) {
        trie.insert(word);
    }

    string longest;
    for (string word : words) {
        if (canBeFormed(word, trie)) {
            if (word.length() > longest.length()) {
                longest = word;
            }
        }
    }
    return longest;
}

bool canBeFormed(string word, Trie& trie) {
    for (int i = 1; i < word.length(); i++) {
        string prefix = word.substr(0, i);
        if (trie.search(prefix)) {
            if (canBeFormed(word.substr(i), trie)) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    vector<string> words = {"cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatsdogcat"};
    cout << longestWord(words) << endl;
    return 0;
}
```

## Test Cases
```
Input: ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatsdogcat"]
Output: "ratcatsdogcat"
```

## Key Takeaways
- Using a Trie data structure to store the dictionary words allows for efficient searching of words.
- Depth-first search can be used to check all possible combinations of words to form a given word.
- The problem can be solved by checking each word in the dictionary to see if it can be formed by other words in the Trie.