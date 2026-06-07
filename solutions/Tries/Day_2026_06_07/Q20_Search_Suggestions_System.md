# Search Suggestions System

## Problem Statement
Given a list of strings `sentences` and a string `prefix`, design a search suggestions system that returns a list of at most 3 suggestions for the given prefix. The suggestions should be in the order of most frequent to least frequent. If there are ties in frequency, the suggestions should be in lexicographical order. The system should be case-insensitive and should ignore non-alphanumeric characters.

## Approach
We will use a Trie data structure to store the sentences and then traverse the Trie to find the suggestions for the given prefix. We will also use a hashmap to store the frequency of each sentence.

## Complexity
- Time: O(n + m), where n is the total number of characters in all sentences and m is the number of characters in the prefix.
- Space: O(n), where n is the total number of characters in all sentences.

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
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }

    void insert(string word, int frequency) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
        node->word = word;
        node->frequency = frequency;
    }

    vector<string> search(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (!node->children.count(c)) {
                return {};
            }
            node = node->children[c];
        }
        return bfs(node, prefix);
    }

    vector<string> bfs(TrieNode* node, string prefix) {
        queue<TrieNode*> q;
        q.push(node);
        vector<pair<string, int>> result;
        while (!q.empty()) {
            TrieNode* curr = q.front();
            q.pop();
            if (curr->isEndOfWord) {
                result.push_back({curr->word, curr->frequency});
            }
            for (auto& child : curr->children) {
                q.push(child.second);
            }
        }
        sort(result.begin(), result.end(), [](const auto& a, const auto& b) {
            if (a.second == b.second) {
                return a.first < b.first;
            }
            return a.second > b.second;
        });
        vector<string> suggestions;
        for (int i = 0; i < min(3, (int)result.size()); i++) {
            suggestions.push_back(result[i].first);
        }
        return suggestions;
    }
};

vector<string> suggestedProducts(vector<string>& products, string searchWord) {
    Trie trie;
    unordered_map<string, int> frequency;
    for (string product : products) {
        frequency[product]++;
    }
    for (auto& pair : frequency) {
        trie.insert(pair.first, pair.second);
    }
    vector<string> result;
    string prefix = "";
    for (char c : searchWord) {
        prefix += c;
        vector<string> suggestions = trie.search(prefix);
        result.push_back(suggestions);
    }
    return result;
}

int main() {
    vector<string> products = {"mobile", "mouse", "moneypot", "monitor", "mousepad"};
    string searchWord = "mouse";
    vector<string> result = suggestedProducts(products, searchWord);
    for (vector<string> suggestions : result) {
        for (string suggestion : suggestions) {
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
- Use a Trie data structure to store the sentences and then traverse the Trie to find the suggestions for the given prefix.
- Use a hashmap to store the frequency of each sentence.
- Use a breadth-first search (BFS) to traverse the Trie and find all the suggestions for the given prefix.