# Replace Words

## Problem Statement
In this problem, we are given a sentence and a list of words. We need to replace all the words in the sentence that are prefixes of any word in the list with the shortest word that they are a prefix of. For example, if the sentence is "cat catfish catnap" and the list of words is ["cat", "catfish", "catnap"], we need to replace "cat" with the shortest word that it is a prefix of, which is "cat" itself. The constraints are that the sentence contains only lowercase English letters and spaces, and the list of words contains only unique lowercase English letters.

## Approach
We will use a Trie data structure to store the list of words, and then iterate through each word in the sentence to find the shortest word that it is a prefix of in the Trie. We will use a depth-first search approach to find the shortest word.

## Complexity
- Time: O(N * M) where N is the number of words in the sentence and M is the maximum length of a word
- Space: O(K) where K is the total number of characters in all the words in the list

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
                node = node->children[c];
                prefix += c;
                if (node->isEndOfWord) {
                    result += prefix + " ";
                    break;
                }
            }
            if (!node->isEndOfWord) {
                result += word + " ";
            }
        }

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
Output: "the cat was rat by the bat"
```

## Key Takeaways
- We use a Trie data structure to store the list of words for efficient prefix matching.
- We iterate through each word in the sentence and use a depth-first search approach to find the shortest word that it is a prefix of in the Trie.
- We use a string to store the result and append the replaced word or the original word depending on whether a prefix match is found.