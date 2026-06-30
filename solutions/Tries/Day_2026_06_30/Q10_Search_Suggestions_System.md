# Search Suggestions System

## Problem Statement
Given a list of strings `products` and a string `searchWord`, return a list of strings representing the search suggestions system. The search suggestions system is designed to return a list of strings that match the prefix of the `searchWord` as the user types it in. The system should return at most three suggestions for each prefix. If there are less than three matching products, return all of them. The `products` list is sorted in lexicographical order, and all strings in `products` are lowercase.

## Approach
The approach is to use a Trie data structure to store the products and then traverse the Trie based on the characters of the searchWord to get the suggestions. We will use a recursive function to build the Trie and another function to get the suggestions.

## Complexity
- Time: O(n + m) where n is the total number of characters in all products and m is the length of the searchWord
- Space: O(n) where n is the total number of characters in all products

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<string> suggestions;
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        TrieNode* root = new TrieNode();
        for (string product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
                if (node->suggestions.size() < 3) {
                    node->suggestions.push_back(product);
                }
            }
        }
        
        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (node->children.find(c) == node->children.end()) {
                break;
            }
            node = node->children[c];
            result.push_back(node->suggestions);
        }
        
        // fill the remaining result with empty vectors
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
- Use a Trie data structure to efficiently store and retrieve the suggestions.
- Use a recursive function to build the Trie and another function to get the suggestions.
- Make sure to handle the case where there are less than three matching products.