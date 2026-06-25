# Search Suggestions System

## Problem Statement
Given a list of strings and a prefix, return all strings in the list that start with the given prefix, sorted lexicographically. The system should return at most 3 suggestions. For example, if the input list is ["mobile", "mouse", "moneypot", "monitor", "mousepad"] and the prefix is "mouse", the output should be ["mouse", "mousepad"]. If the prefix is "mo", the output should be ["mobile", "moneypot", "monitor"].

## Approach
We can solve this problem using a Trie data structure, where each node stores a list of strings that pass through it. We iterate through the list of strings and insert each string into the Trie. Then, we search for the prefix in the Trie and return all strings that start with the prefix.

## Complexity
- Time: O(n * m + p), where n is the number of strings, m is the average length of a string, and p is the length of the prefix.
- Space: O(n * m), where n is the number of strings and m is the average length of a string.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<string> strings;
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
                node->strings.push_back(product);
            }
        }

        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (node->children.find(c) == node->children.end()) {
                break;
            }
            node = node->children[c];
            sort(node->strings.begin(), node->strings.end());
            vector<string> suggestions;
            for (string str : node->strings) {
                if (str.find(searchWord) == 0) {
                    suggestions.push_back(str);
                }
                if (suggestions.size() == 3) {
                    break;
                }
            }
            result.push_back(suggestions);
        }

        // Fill the remaining result with empty vectors
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
- We can use a Trie to store a list of strings and then search for a prefix in the Trie to return all strings that start with the prefix.
- The time complexity of the solution is O(n * m + p), where n is the number of strings, m is the average length of a string, and p is the length of the prefix.