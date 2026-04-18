# Search Suggestions System

## Problem Statement
Given a list of strings `products` and a string `searchWord`, return a list of strings that represent the search suggestions system. The search suggestions system is designed to return a list of strings that match the prefix of the `searchWord` as the user types. The list of strings should be sorted in lexicographical order and should not contain any duplicates. The `searchWord` is typed character by character, and the system returns a list of strings that match the prefix of the `searchWord` at each character. The system should return at most 3 strings that match the prefix of the `searchWord` at each character.

## Approach
The solution uses a Trie data structure to store the list of strings. It iterates over the `searchWord` character by character, and at each character, it uses the Trie to find the strings that match the prefix of the `searchWord`. The list of strings is then sorted and duplicates are removed.

## Complexity
- Time: O(n * m * log(m)) where n is the length of the `searchWord` and m is the average length of the strings in the `products` list
- Space: O(n * m) where n is the length of the `searchWord` and m is the average length of the strings in the `products` list

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<string> words;
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        // Create the Trie
        TrieNode* root = new TrieNode();
        for (const auto& product : products) {
            TrieNode* node = root;
            for (const auto& c : product) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
                // Store the words that pass through this node
                node->words.push_back(product);
                // Sort and remove duplicates
                sort(node->words.begin(), node->words.end());
                node->words.erase(unique(node->words.begin(), node->words.end()), node->words.end());
                // Keep at most 3 words
                if (node->words.size() > 3) {
                    node->words.resize(3);
                }
            }
        }

        // Search for the suggestions
        vector<vector<string>> result;
        TrieNode* node = root;
        for (const auto& c : searchWord) {
            if (node->children.find(c) == node->children.end()) {
                // If the character is not in the Trie, break the loop
                break;
            }
            node = node->children[c];
            result.push_back(node->words);
        }

        // Fill the rest of the result with empty vectors
        while (result.size() < searchWord.size()) {
            result.push_back({});
        }

        return result;
    }
};
```

## Test Cases
```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
```

## Key Takeaways
- The Trie data structure is useful for storing and searching strings with common prefixes.
- The system returns at most 3 strings that match the prefix of the `searchWord` at each character.
- The solution uses a TrieNode class to represent each node in the Trie, and a Solution class to implement the search suggestions system.