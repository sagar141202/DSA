# Search Suggestions System

## Problem Statement
Given a string array `products` and a string `searchWord`, return a list of strings representing the products that match the search word. The search results should be sorted in lexicographical order, and the results for each character in the search word should be returned separately. For example, if the search word is "mobile", the results for "m", "mo", "mob", "mobi", "mobie", and "mobile" should be returned separately.

## Approach
The problem can be solved using a Trie data structure, where each node stores a list of words that pass through it. We can iterate over the `products` array and insert each word into the Trie. Then, for each prefix of the `searchWord`, we can traverse the Trie and return the words that match the prefix.

## Complexity
- Time: O(n * m + k * m), where n is the number of products, m is the maximum length of a product, and k is the length of the search word.
- Space: O(n * m), where n is the number of products and m is the maximum length of a product.

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
        // Create the Trie and insert all products
        TrieNode* root = new TrieNode();
        for (string product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
                node->words.push_back(product);
            }
        }

        // Search for each prefix of the search word
        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (node->children.find(c) == node->children.end()) {
                break;
            }
            node = node->children[c];
            // Sort the words and take the top 3
            sort(node->words.begin(), node->words.end());
            vector<string> top3;
            for (int i = 0; i < min(3, (int)node->words.size()); i++) {
                top3.push_back(node->words[i]);
            }
            result.push_back(top3);
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
- Use a Trie data structure to store the products and search for prefixes of the search word.
- Sort the words at each node and take the top 3 to include in the result.
- Fill the rest of the result with empty vectors if the search word is longer than the number of prefixes found.