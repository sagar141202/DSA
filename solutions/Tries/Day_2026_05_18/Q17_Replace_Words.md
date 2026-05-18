# Replace Words
## Problem Statement
In this problem, we are given a sentence and a list of words to replace. The task is to replace all occurrences of the words in the sentence with a specified replacement string. The replacement should be done in a way that the longest matching word is replaced first. For example, if we have the sentence "the cat sat on the mat" and the words to replace are "cat" and "mat", the output should be "the xxx sat on the xxx". The constraints are that the sentence and the words to replace are non-empty and contain only lowercase letters.

## Approach
The approach to solve this problem is to use a Trie data structure to store the words to replace. Then, we iterate over the sentence and check if the current substring matches any word in the Trie. If a match is found, we replace the word with the replacement string.

## Complexity
- Time: O(n * m) where n is the length of the sentence and m is the average length of the words to replace
- Space: O(n + m) where n is the number of nodes in the Trie and m is the number of words to replace

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

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        // Create a Trie and insert all words from the dictionary
        TrieNode* root = new TrieNode();
        for (const string& word : dictionary) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
        }

        // Split the sentence into words
        istringstream iss(sentence);
        string word;
        string result;

        // Iterate over each word in the sentence
        while (iss >> word) {
            // Check if the word can be replaced with a shorter word from the dictionary
            TrieNode* node = root;
            string replacement;
            for (int i = 0; i < word.size(); i++) {
                if (node->children.find(word[i]) == node->children.end()) {
                    break;
                }
                replacement += word[i];
                node = node->children[word[i]];
                if (node->isEndOfWord) {
                    result += replacement + " ";
                    break;
                }
            }
            if (node->isEndOfWord) {
                continue;
            }
            result += word + " ";
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
Output: "the cat was rat by the bat"
```

## Key Takeaways
- Using a Trie data structure can efficiently store and retrieve words with common prefixes.
- The replacement should be done in a way that the longest matching word is replaced first to avoid incorrect replacements.
- The solution should handle cases where the sentence contains words that are not in the dictionary.