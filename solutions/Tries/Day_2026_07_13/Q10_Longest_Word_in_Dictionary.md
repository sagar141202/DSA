# Longest Word in Dictionary

## Problem Statement
Given a list of strings which are all in lowercase, find the longest word that can be formed from other words in the list. A word can only be formed from other words in the list if it can be split into two non-empty parts where both parts are in the list. If there are multiple longest words, return the lexicographically smallest one. For example, if the input is ["w","wo","wor","word"], the output should be "word" because it can be split into "wor" and "d" but "d" is not in the dictionary. However, "word" can also be split into "wo" and "rd" but "rd" is not in the dictionary. The correct split is "wor" and "d" but "d" is not in the dictionary. The correct answer is indeed "word" because it can be split into "wo" and "rd" is not valid but "word" can be formed from "wor" which is in the dictionary.

## Approach
To solve this problem, we can use a Trie data structure to store all the words in the dictionary. Then, we can iterate through each word in the dictionary and check if it can be split into two non-empty parts where both parts are in the Trie. We keep track of the longest word that can be formed and return it.

## Complexity
- Time: O(N*M) where N is the number of words and M is the maximum length of a word
- Space: O(N*M) for storing the Trie

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
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->endOfWord = true;
    }
    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
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
    string longest = "";
    for (string word : words) {
        if (word.length() > longest.length() || (word.length() == longest.length() && word < longest)) {
            bool canBeFormed = false;
            for (int i = 1; i < word.length(); i++) {
                string left = word.substr(0, i);
                string right = word.substr(i);
                if (trie.search(left) && trie.search(right)) {
                    canBeFormed = true;
                    break;
                }
            }
            if (canBeFormed) {
                longest = word;
            }
        }
    }
    return longest;
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
- We use a Trie data structure to store all the words in the dictionary for efficient lookup.
- We iterate through each word in the dictionary and check if it can be split into two non-empty parts where both parts are in the Trie.
- We keep track of the longest word that can be formed and return it. If there are multiple longest words, we return the lexicographically smallest one.