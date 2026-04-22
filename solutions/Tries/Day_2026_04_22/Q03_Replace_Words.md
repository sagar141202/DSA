# Replace Words
## Problem Statement
In this problem, we are given a sentence and a list of words to replace. We need to replace all occurrences of these words in the sentence with a specified replacement string. The replacement should be case-sensitive and should only replace whole words. For example, given the sentence "the cat and the dog" and the words to replace ["cat", "dog"] with replacement string "animal", the output should be "the animal and the animal".

## Approach
The approach to this problem is to use a Trie data structure to store the words to replace. Then, we iterate over each word in the sentence and check if it exists in the Trie. If it does, we replace it with the replacement string.

## Complexity
- Time: O(n*m) where n is the number of words in the sentence and m is the average length of a word
- Space: O(k) where k is the total number of characters in all words to replace

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    string replacement;

    TrieNode() : isEndOfWord(false) {}
};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        TrieNode* root = new TrieNode();
        for (string word : dictionary) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
            node->replacement = word;
        }

        istringstream iss(sentence);
        string word;
        string result;
        while (iss >> word) {
            TrieNode* node = root;
            string prefix;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    break;
                }
                prefix += c;
                node = node->children[c];
                if (node->isEndOfWord) {
                    result += prefix + " ";
                    break;
                }
            }
            if (!node->isEndOfWord) {
                result += word + " ";
            }
        }
        result.pop_back(); // remove trailing space
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
- Using a Trie data structure can efficiently store and retrieve words to replace
- Iterating over each word in the sentence and checking if it exists in the Trie allows for efficient replacement of words
- The replacement string should be stored in the Trie node to facilitate replacement of words