# Search Suggestions System

## Problem Statement
Given a list of strings `products` and a string `searchWord`, design a search suggestions system where for each character in the search word, it returns the top 3 products that match the current prefix of the search word. The products should be sorted by their positions in the original list. If there are less than 3 matching products, return all of them. The search word can contain lowercase letters only.

## Approach
The problem can be solved by using a Trie data structure to store the products. We iterate over each character in the search word and find all products that match the current prefix. We then sort the matching products based on their original positions and return the top 3 products.

## Complexity
- Time: O(n * m * log(n)) where n is the number of products and m is the length of the search word
- Space: O(n * m) where n is the number of products and m is the maximum length of a product

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
        // Create a Trie and insert all products into it
        TrieNode* root = new TrieNode();
        for (const string& product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
                node->words.push_back(product);
                sort(node->words.begin(), node->words.end(), [&](const string& a, const string& b) {
                    return products.size() - (lower_bound(products.begin(), products.end(), a) - products.begin()) <
                           products.size() - (lower_bound(products.begin(), products.end(), b) - products.begin());
                });
                if (node->words.size() > 3) {
                    node->words.pop_back();
                }
            }
        }

        // Search for products that match each prefix of the search word
        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (node->children.find(c) == node->children.end()) {
                break;
            }
            node = node->children[c];
            result.push_back(node->words);
        }

        // If the search word is longer than the products in the Trie, add empty vectors to the result
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
- We use a Trie to store the products, which allows us to efficiently find products that match each prefix of the search word.
- We sort the products in each node of the Trie based on their original positions in the list, so that we can return the top 3 products that match each prefix.
- We use a vector to store the result, where each element is a vector of strings representing the top 3 products that match the corresponding prefix of the search word.