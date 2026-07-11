# Search Suggestions System

## Problem Statement
Given a list of strings, implement an autocomplete system that returns all strings in the list that start with a given prefix. The system should return a list of lists, where each sublist contains at most three strings that match the prefix. The strings should be ordered lexicographically. For example, if the input list is ["mobile", "mouse", "moneypot", "monitor", "mousepad"] and the prefix is "mo", the output should be ["mobile", "moneypot", "monitor"].

## Approach
The problem can be solved using a Trie data structure, where each node represents a character in the string. We can then traverse the Trie to find all strings that start with a given prefix. The algorithm involves inserting all strings into the Trie, then performing a depth-first search to find all matching strings.

## Complexity
- Time: O(N * M + P * Q), where N is the number of strings, M is the maximum length of a string, P is the number of prefixes, and Q is the maximum number of matching strings for a prefix.
- Space: O(N * M), where N is the number of strings and M is the maximum length of a string.

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
                    node->words.resize(3);
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

int main() {
    Solution solution;
    vector<string> products = {"mobile", "mouse", "moneypot", "monitor", "mousepad"};
    string searchWord = "mo";
    vector<vector<string>> result = solution.suggestedProducts(products, searchWord);
    for (vector<string> suggestion : result) {
        for (string word : suggestion) {
            cout << word << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord = "mo"
Output: [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mobile", "monitor"], ["mouse", "mousepad", "moneypot"], ["mouse", "mousepad", "moneypot"]]
```

## Key Takeaways
- Use a Trie data structure to store the strings and perform a depth-first search to find all matching strings.
- Sort the matching strings lexicographically and return at most three strings for each prefix.
- Handle cases where the prefix does not match any strings by returning an empty list.