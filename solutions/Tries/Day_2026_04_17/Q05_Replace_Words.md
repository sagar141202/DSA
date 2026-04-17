# Replace Words

## Problem Statement
In this problem, we are given a list of words in a dictionary and a sentence. The task is to replace all words in the sentence with their corresponding prefixes from the dictionary if they exist. For example, if the dictionary contains the word "cat" and the sentence is "the cat is sleeping", we should replace "cat" with "cat" because it is in the dictionary. However, if the dictionary contains the word "ca" and the sentence is "the cat is sleeping", we should replace "cat" with "ca" because "ca" is a prefix of "cat" and it is in the dictionary. The goal is to find the shortest possible replacement for each word in the sentence.

## Approach
We will use a Trie data structure to store the dictionary words. Then, for each word in the sentence, we will check all prefixes of the word in the Trie and replace the word with the longest prefix that exists in the Trie.

## Complexity
- Time: O(N * M) where N is the number of words in the sentence and M is the maximum length of a word
- Space: O(D) where D is the total number of characters in the dictionary

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    
    TrieNode() {
        isEndOfWord = false;
    }
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
    
    string getLongestPrefix(string word) {
        TrieNode* node = root;
        string prefix = "";
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                break;
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
        result += trie.getLongestPrefix(word) + " ";
    }
    result.pop_back();
    return result;
}
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle is grazing in the field"
Output: "the cat is grazing in the field"
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cbsbb babababab"
Output: "a a b c b a"
```

## Key Takeaways
- Using a Trie data structure allows us to efficiently store and retrieve dictionary words and their prefixes.
- The getLongestPrefix function in the Trie class is used to find the longest prefix of a word that exists in the dictionary.
- The replaceWords function iterates over each word in the sentence, finds the longest prefix that exists in the dictionary, and appends it to the result string.