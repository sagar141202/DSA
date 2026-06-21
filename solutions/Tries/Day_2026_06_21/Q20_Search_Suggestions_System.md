# Search Suggestions System

## Problem Statement
Given a list of strings and a search query, design a search suggestions system that returns the top 3 most relevant suggestions for each prefix of the query. The system should return all suggestions that have the same prefix as the query, sorted in descending order of frequency. If there are more than 3 suggestions, return the top 3. The input consists of a list of strings `sentences` and a string `prefix`. The output should be a list of lists, where each inner list contains the top 3 suggestions for each prefix of the query.

## Approach
The approach is to use a Trie data structure to store the sentences and their frequencies. Then, for each prefix of the query, traverse the Trie to find all sentences that have the same prefix and sort them based on their frequencies. Finally, return the top 3 suggestions for each prefix.

## Complexity
- Time: O(N * M * logM)
- Space: O(N * M)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<string> sentences;
};

class SearchSuggestionsSystem {
public:
    TrieNode* root;
    unordered_map<string, int> freq;

    SearchSuggestionsSystem(vector<string>& sentences) {
        root = new TrieNode();
        for (string sentence : sentences) {
            insert(sentence);
            freq[sentence]++;
        }
    }

    void insert(string sentence) {
        TrieNode* node = root;
        for (char c : sentence) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->sentences.push_back(sentence);
        }
    }

    vector<vector<string>> search(string prefix) {
        vector<vector<string>> result;
        TrieNode* node = root;
        for (char c : prefix) {
            if (!node->children.count(c)) {
                break;
            }
            node = node->children[c];
        }
        if (!node) return result;
        vector<string> suggestions = node->sentences;
        sort(suggestions.begin(), suggestions.end(), [this](string a, string b) {
            return freq[a] > freq[b];
        });
        result.push_back(vector<string>(suggestions.begin(), suggestions.begin() + min(3, (int)suggestions.size())));
        return result;
    }
};

vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
    SearchSuggestionsSystem system(products);
    vector<vector<string>> result;
    for (int i = 1; i <= searchWord.size(); i++) {
        string prefix = searchWord.substr(0, i);
        vector<vector<string>> suggestions = system.search(prefix);
        result.push_back(suggestions[0]);
    }
    return result;
}
```

## Test Cases
```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
```

## Key Takeaways
- Use a Trie data structure to efficiently store and retrieve sentences with the same prefix.
- Sort the suggestions based on their frequencies to return the top 3 most relevant suggestions.
- Traverse the Trie for each prefix of the query to find all sentences that have the same prefix.