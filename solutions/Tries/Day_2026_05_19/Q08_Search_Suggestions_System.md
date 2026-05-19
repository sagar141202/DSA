# Search Suggestions System

## Problem Statement
Given a list of strings `products` and a string `searchWord`, return a list of strings that match the given `searchWord` with the following conditions: 
- For each character in `searchWord`, suggest all `products` that have the same character in the same position.
- For each position, return at most three matching `products`.
- The result should be sorted lexicographically within each position.
- If there are no matching `products`, return an empty list.

## Approach
The problem can be solved using a Trie data structure to store the products, and then iterating through the search word to find matching products. We will also use a set to store unique suggestions at each position.

## Complexity
- Time: O(n * m * log(m)) where n is the length of the search word and m is the average length of the products
- Space: O(n * m) for storing the Trie and suggestions

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
        // Create a Trie and insert all products
        TrieNode* root = new TrieNode();
        for (string& product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
                // Add product to suggestions if not already present
                if (node->suggestions.size() < 3 && find(node->suggestions.begin(), node->suggestions.end(), product) == node->suggestions.end()) {
                    node->suggestions.push_back(product);
                    // Sort suggestions
                    sort(node->suggestions.begin(), node->suggestions.end());
                }
            }
        }

        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (node->children.find(c) == node->children.end()) {
                // If character not found, return empty vectors for remaining positions
                for (int i = result.size(); i < searchWord.size(); i++) {
                    result.push_back({});
                }
                break;
            }
            node = node->children[c];
            result.push_back(node->suggestions);
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
- Using a Trie data structure allows for efficient retrieval of matching products.
- Sorting suggestions at each position ensures lexicographical order.
- Limiting suggestions to three at each position ensures the result is not too large.