# Search Suggestions System

## Problem Statement
Given a list of strings `sentences` and a string `prefix`, design a search suggestions system that returns the top 3 most frequent sentences that start with `prefix`. The frequency of a sentence is the number of times it appears in the `sentences` list. If there are less than 3 sentences that start with `prefix`, return all of them. The search suggestions system should be case-insensitive and should ignore any punctuation.

## Approach
The approach is to use a Trie data structure to store the sentences and their frequencies. Then, perform a depth-first search on the Trie to find all sentences that start with the given prefix. Finally, sort the sentences based on their frequencies and return the top 3.

## Complexity
- Time: O(N + M log M)
- Space: O(N)

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
    unordered_map<string, int> frequency;

    SearchSuggestionsSystem(vector<string>& sentences) {
        root = new TrieNode();
        for (const auto& sentence : sentences) {
            addSentence(sentence);
        }
    }

    void addSentence(const string& sentence) {
        TrieNode* node = root;
        for (char c : sentence) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->sentences.push_back(sentence);
        frequency[sentence]++;
    }

    vector<string> search(const string& prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return {};
            }
            node = node->children[c];
        }
        vector<string> result;
        dfs(node, result);
        sort(result.begin(), result.end(), [this](const string& a, const string& b) {
            return frequency[a] > frequency[b] || (frequency[a] == frequency[b] && a < b);
        });
        if (result.size() > 3) {
            result.resize(3);
        }
        return result;
    }

    void dfs(TrieNode* node, vector<string>& result) {
        for (const auto& sentence : node->sentences) {
            result.push_back(sentence);
        }
        for (const auto& child : node->children) {
            dfs(child.second, result);
        }
    }
};

int main() {
    vector<string> sentences = {"The quick brown fox jumps over the lazy dog", "The sun is shining", "The quick brown fox is very quick"};
    SearchSuggestionsSystem system(sentences);
    vector<string> result = system.search("The");
    for (const auto& sentence : result) {
        cout << sentence << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: sentences = ["The quick brown fox jumps over the lazy dog", "The sun is shining", "The quick brown fox is very quick"], prefix = "The"
Output: ["The quick brown fox jumps over the lazy dog", "The quick brown fox is very quick", "The sun is shining"]
```

## Key Takeaways
- Use a Trie data structure to store the sentences and their frequencies.
- Perform a depth-first search on the Trie to find all sentences that start with the given prefix.
- Sort the sentences based on their frequencies and return the top 3.