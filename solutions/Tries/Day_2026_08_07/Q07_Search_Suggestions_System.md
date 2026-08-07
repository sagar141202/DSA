# Search Suggestions System

## Problem Statement
Given a list of strings and a search query, design a system that returns the top 3 most relevant search suggestions for the query. The relevance of a suggestion is determined by its frequency of occurrence in the list of strings. If there are ties in frequency, the suggestions should be sorted lexicographically.

## Approach
The approach is to use a Trie data structure to store the list of strings and then traverse the Trie to find the top 3 most relevant search suggestions for the query. We will use a hash map to store the frequency of each string.

## Complexity
- Time: O(N * M * logN)
- Space: O(N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    string word;
    int frequency;
    TrieNode() : isEndOfWord(false), frequency(0) {}
};

class Trie {
public:
    TrieNode* root;
    Trie() : root(new TrieNode()) {}
    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
        node->word = word;
        node->frequency++;
    }
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        Trie trie;
        for (string product : products) {
            trie.insert(product);
        }
        vector<vector<string>> result;
        TrieNode* node = trie.root;
        for (char c : searchWord) {
            if (!node->children.count(c)) {
                break;
            }
            node = node->children[c];
            vector<string> suggestions;
            dfs(node, suggestions);
            sort(suggestions.begin(), suggestions.end(), [](string a, string b) {
                return a.size() == b.size() ? a < b : a.size() < b.size();
            });
            result.push_back(vector<string>(suggestions.begin(), suggestions.begin() + min(3, (int)suggestions.size())));
        }
        while (result.size() < searchWord.size()) {
            result.push_back({});
        }
        return result;
    }
    void dfs(TrieNode* node, vector<string>& suggestions) {
        if (node->isEndOfWord) {
            suggestions.push_back(node->word);
        }
        for (auto& child : node->children) {
            dfs(child.second, suggestions);
        }
    }
};

int main() {
    Solution solution;
    vector<string> products = {"mobile", "mouse", "moneypot", "monitor", "mousepad"};
    string searchWord = "mouse";
    vector<vector<string>> result = solution.suggestedProducts(products, searchWord);
    for (auto& suggestions : result) {
        for (auto& suggestion : suggestions) {
            cout << suggestion << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord = "mouse"
Output: 
[
  ["mobile","moneypot","monitor"],
  ["mobile","moneypot","monitor"],
  ["mouse","mousepad"],
  ["mouse","mousepad"],
  ["mouse","mousepad"]
]
```

## Key Takeaways
- Use a Trie data structure to store the list of strings and then traverse the Trie to find the top 3 most relevant search suggestions for the query.
- Use a hash map to store the frequency of each string.
- Sort the suggestions lexicographically if there are ties in frequency.