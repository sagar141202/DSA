# Search Suggestions System

## Problem Statement
Given a list of strings `products` and a string `searchWord`, return a list of strings representing the search suggestions system for the given search word. The search suggestions system is designed to return a list of strings that match the search word as a prefix, and the list should be sorted in lexicographical order. The system should also handle the case when the search word is empty, in which case it should return all the products. The products list can contain up to 1000 strings, and each string can have up to 10 characters.

## Approach
The problem can be solved using a Trie data structure, which allows for efficient prefix matching. We can insert all the products into the Trie and then use the Trie to find all the strings that match the search word as a prefix. We can use a Depth-First Search (DFS) approach to traverse the Trie and find all the matching strings.

## Complexity
- Time: O(N * M), where N is the number of products and M is the maximum length of a product string
- Space: O(N * M), where N is the number of products and M is the maximum length of a product string

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
                    node->words.pop_back();
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
            result.push_back(node->words);
        }
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
- The Trie data structure is useful for solving problems that involve prefix matching.
- The DFS approach can be used to traverse the Trie and find all the matching strings.
- The time and space complexity of the solution depend on the number of products and the maximum length of a product string.