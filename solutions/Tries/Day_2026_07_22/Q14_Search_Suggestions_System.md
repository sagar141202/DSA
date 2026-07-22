# Search Suggestions System

## Problem Statement
Given a list of strings, implement a search suggestions system that, for a given prefix, returns the top 3 most frequent strings that start with the prefix, sorted lexicographically. The system should be case-insensitive and support prefix matching. For example, if the input list is ["mobile", "mouse", "moneypot", "monitor", "mousepad"] and the prefix is "mo", the output should be ["mobile", "moneypot", "monitor"].

## Approach
The solution uses a Trie data structure to store the input strings, and then performs a depth-first search to find all strings that start with the given prefix. The results are then sorted by frequency and lexicographical order.

## Complexity
- Time: O(N + M), where N is the total length of all input strings and M is the number of strings that start with the prefix
- Space: O(N), where N is the total length of all input strings

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    int count;
    string word;

    TrieNode() : count(0) {}
};

class Trie {
public:
    TrieNode* root;

    Trie() : root(new TrieNode()) {}

    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->count++;
        node->word = word;
    }

    vector<string> search(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return {};
            }
            node = node->children[c];
        }
        vector<string> result;
        dfs(node, result);
        sort(result.begin(), result.end(), [](string a, string b) {
            if (a == b) return 0;
            int countA = getCount(a);
            int countB = getCount(b);
            if (countA == countB) return a < b ? -1 : 1;
            return countA > countB ? -1 : 1;
        });
        if (result.size() > 3) result.resize(3);
        return result;
    }

    void dfs(TrieNode* node, vector<string>& result) {
        if (node->word != "") result.push_back(node->word);
        for (auto& child : node->children) {
            dfs(child.second, result);
        }
    }

    int getCount(string word) {
        TrieNode* node = root;
        for (char c : word) {
            node = node->children[c];
        }
        return node->count;
    }
};

vector<string> suggestedProducts(vector<string>& products, string searchWord) {
    Trie trie;
    for (string product : products) {
        trie.insert(product);
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
    vector<vector<string>> result = {{"mobile", "moneypot", "monitor"}, 
                                      {"mobile", "moneypot", "monitor"}, 
                                      {"mouse", "mousepad"}, 
                                      {"mouse", "mousepad"}, 
                                      {"mouse", "mousepad"}};
    vector<vector<string>> output = suggestedProducts(products, searchWord);
    for (int i = 0; i < output.size(); i++) {
        for (int j = 0; j < output[i].size(); j++) {
            cout << output[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord = "mouse"
Output: [["mobile", "moneypot", "monitor"], 
         ["mobile", "moneypot", "monitor"], 
         ["mouse", "mousepad"], 
         ["mouse", "mousepad"], 
         ["mouse", "mousepad"]]
```

## Key Takeaways
- Use a Trie data structure to efficiently store and retrieve strings that start with a given prefix.
- Perform a depth-first search to find all strings that start with the prefix and store them in a vector.
- Sort the results by frequency and lexicographical order to get the top 3 most frequent strings.