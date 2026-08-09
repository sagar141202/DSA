# Replace Words

## Problem Statement
In this problem, we are given a list of words and a sentence. The task is to replace all occurrences of words in the sentence with their corresponding abbreviations. We can abbreviate a word by taking the first letter and appending a dot. For example, "hello" can be abbreviated as "h.". However, if a word cannot be abbreviated, we should leave it as it is. The goal is to minimize the length of the resulting sentence after replacing all possible words with their abbreviations.

## Approach
We will use a Trie data structure to store the given list of words. Then, we will iterate over the sentence and check if each word is present in the Trie. If a word is found in the Trie, we will replace it with its abbreviation.

## Complexity
- Time: O(n * m) where n is the number of words in the sentence and m is the maximum length of a word
- Space: O(n) where n is the total number of characters in all words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isWord;
    TrieNode() : isWord(false) {}
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
        node->isWord = true;
    }
    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                return false;
            }
            node = node->children[c];
        }
        return node->isWord;
    }
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word);
    }
    stringstream ss(sentence);
    string word, result;
    while (ss >> word) {
        string abbrev = word[0] + ".";
        TrieNode* node = trie.root;
        for (char c : word) {
            if (!node->children.count(c)) {
                result += word + " ";
                goto next_word;
            }
            node = node->children[c];
            if (node->isWord) {
                result += abbrev + " ";
                goto next_word;
            }
        }
        result += word + " ";
        next_word:;
    }
    result.pop_back(); // remove trailing space
    return result;
}

int main() {
    vector<string> dictionary = {"cat","bat","rat"};
    string sentence = "the cattle was rattled by the battery";
    cout << replaceWords(dictionary, sentence) << endl;
    return 0;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rattled by the bat"
```

## Key Takeaways
- We use a Trie data structure to efficiently store and search for words in the dictionary.
- We iterate over the sentence and check each word against the Trie to determine if it can be abbreviated.
- We use a stringstream to split the sentence into individual words and process each word separately.