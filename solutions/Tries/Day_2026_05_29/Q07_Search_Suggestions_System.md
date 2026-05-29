# Search Suggestions System

## Problem Statement
Given a list of strings `products` and a string `searchWord`, return a list of strings representing the search suggestions system. The system should return a list of strings where each string is a suggestion based on the prefix of the `searchWord`. The suggestions should be in lexicographical order and should not exceed the length of the `searchWord`. The `products` list contains a list of product names and the `searchWord` is the word being searched. For example, if `products = ["mobile","mouse","moneypot","monitor","mousepad"]` and `searchWord = "mouse"`, the output should be `[["mobile","mouse","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]`.

## Approach
The approach is to use a Trie data structure to store the products and then traverse the Trie based on the search word to get the suggestions. The Trie is built by inserting each product into the Trie. Then, for each prefix of the search word, the suggestions are retrieved from the Trie.

## Complexity
- Time: O(n*m) where n is the number of products and m is the average length of a product
- Space: O(n*m) where n is the number of products and m is the average length of a product

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
        // Build the Trie
        TrieNode* root = new TrieNode();
        for (string product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
                node->words.push_back(product);
                sort(node->words.begin(), node->words.end());
                if (node->words.size() > 3) {
                    node->words.resize(3);
                }
            }
        }

        // Get the suggestions
        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (node->children.find(c) == node->children.end()) {
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
Output: [["mobile","mouse","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
```

## Key Takeaways
- Use a Trie data structure to store the products for efficient retrieval of suggestions.
- Traverse the Trie based on the search word to get the suggestions.
- Use a vector to store the suggestions for each prefix of the search word.