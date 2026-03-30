# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The task is to replace all occurrences of the given words in the sentence with a specified replacement string. The replacement should be done in a way that the smallest possible word is replaced first. For example, if we have the words "cat" and "category" in the list, "cat" should be replaced before "category". The input sentence and the list of words are given as strings.

## Approach
The approach to solve this problem is to use a Trie data structure to store the list of words. We then iterate over each word in the sentence and check if it is present in the Trie. If it is, we replace it with the replacement string. We use the Trie to ensure that the smallest possible word is replaced first.

## Complexity
- Time: O(n*m) where n is the number of words in the sentence and m is the maximum length of a word
- Space: O(n) where n is the total number of characters in the list of words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    string word;

    TrieNode() : isEndOfWord(false) {}
};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        TrieNode* root = new TrieNode();
        // Insert all words from the dictionary into the Trie
        for (const auto& word : dictionary) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
            node->word = word;
        }

        // Replace all occurrences of the given words in the sentence
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
        // Remove the trailing space
        if (!result.empty()) {
            result.pop_back();
        }
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
- The Trie data structure is useful for solving problems that involve replacing words in a sentence.
- The Trie allows us to efficiently check if a word is present in the dictionary and replace it with the replacement string.
- The approach ensures that the smallest possible word is replaced first.