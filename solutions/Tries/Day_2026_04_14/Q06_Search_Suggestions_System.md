# Search Suggestions System

## Problem Statement
Given a list of strings and a prefix, design a search suggestions system that returns the top three lexicographically smallest strings that start with the given prefix. The system should handle a large number of queries and strings efficiently.

## Approach
The approach involves using a Trie data structure to store the given list of strings. Then, for each query, we traverse the Trie to find all strings that start with the given prefix and return the top three lexicographically smallest ones.

## Complexity
- Time: O(n + m) where n is the number of strings and m is the length of the prefix
- Space: O(n * m) where n is the number of strings and m is the average length of the strings

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<string> words;

    TrieNode() {}
};

class SearchSuggestionsSystem {
public:
    TrieNode* root;

    SearchSuggestionsSystem(vector<string>& products) {
        root = new TrieNode();
        for (const auto& product : products) {
            TrieNode* node = root;
            for (char c : product) {
                if (!node->children.count(c)) {
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
    }

    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : searchWord) {
            if (!node->children.count(c)) {
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
    vector<string> products = {"mobile", "mouse", "moneypot", "monitor", "mousepad"};
    string searchWord = "mouse";
    SearchSuggestionsSystem system(products);
    vector<vector<string>> result = system.suggestedProducts(products, searchWord);
    for (const auto& suggestions : result) {
        for (const auto& suggestion : suggestions) {
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
["mobile", "moneypot", "monitor"]
["mobile", "moneypot", "monitor"]
["mouse", "mousepad"]
["mouse", "mousepad"]
["mouse", "mousepad"]
```

## Key Takeaways
- Using a Trie to store the given list of strings allows for efficient querying of strings that start with a given prefix.
- Storing the top three lexicographically smallest strings at each node in the Trie reduces the time complexity of the query operation.
- The Trie data structure can be used to solve a variety of string-related problems, including autocomplete and spell-checking.