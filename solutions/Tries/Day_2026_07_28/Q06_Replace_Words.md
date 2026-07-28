# Replace Words
## Problem Statement
In this problem, we are given a list of words and a sentence. The task is to replace words in the sentence with their prefixes if the prefix is present in the list of words. For example, if the list of words contains "cat" and the sentence contains "catch", we should replace "catch" with "cat". The replacement should be done in a way that the resulting sentence has the minimum number of words.

## Approach
We will use a Trie data structure to store the list of words. Then, we will iterate over each word in the sentence and check if it or any of its prefixes is present in the Trie. If a prefix is found, we replace the word with the prefix.

## Complexity
- Time: O(n * m) where n is the number of words in the sentence and m is the maximum length of a word
- Space: O(n) for storing the Trie

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
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

    string getPrefix(string word) {
        TrieNode* node = root;
        string prefix = "";
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return word;
            }
            prefix += c;
            node = node->children[c];
            if (node->isEndOfWord) {
                return prefix;
            }
        }
        return word;
    }
};

string replaceWords(vector<string>& dictionary, string sentence) {
    Trie trie;
    for (string word : dictionary) {
        trie.insert(word);
    }
    istringstream iss(sentence);
    string word;
    string result = "";
    while (iss >> word) {
        string prefix = trie.getPrefix(word);
        result += prefix + " ";
    }
    result.pop_back(); // remove the last space
    return result;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

## Key Takeaways
- Using a Trie data structure allows for efficient prefix matching.
- The getPrefix function in the Trie class returns the shortest prefix of a word that is present in the Trie.
- The replaceWords function constructs a Trie from the given dictionary and then uses it to replace words in the sentence with their prefixes.