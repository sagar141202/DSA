# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The replacement is done by checking if any word in the sentence starts with a word from the list. If a match is found, the word is replaced with the corresponding word from the list. The task is to implement a function that performs this replacement efficiently. The input sentence is a string of words separated by spaces, and the list of words to replace is also a list of strings. The output should be the modified sentence after replacement.

## Approach
The approach to solve this problem is to use a Trie data structure to store the words to replace. This allows for efficient lookup and replacement of words in the sentence. We iterate through each word in the sentence and check if it starts with any word in the Trie.

## Complexity
- Time: O(n * m) where n is the number of words in the sentence and m is the maximum length of a word
- Space: O(k) where k is the total number of characters in the words to replace

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    string word;
};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        TrieNode* root = new TrieNode();
        for (auto word : dictionary) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->word = word;
        }

        istringstream iss(sentence);
        string word, result;
        while (iss >> word) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) break;
                node = node->children[c];
                if (!node->word.empty()) {
                    result += node->word + " ";
                    break;
                }
            }
            if (node->word.empty()) result += word + " ";
        }

        // Remove the trailing space
        if (!result.empty()) result.pop_back();
        return result;
    }
};
```

## Test Cases
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rattled by the bat"
```

## Key Takeaways
- Using a Trie data structure allows for efficient lookup and replacement of words in the sentence.
- The Trie is particularly useful when dealing with prefix matching, as in this problem where we need to find words that start with a certain prefix.