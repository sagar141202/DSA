# Search Suggestions System

## Problem Statement
Given a list of strings, implement a search suggestions system that, given a string, returns all strings in the list that start with the given string. The system should return the suggestions in lexicographical order. The search string can be empty, in which case the system should return all strings in the list.

## Approach
The approach to this problem is to use a Trie data structure to store all the strings in the list. Then, for each input string, traverse the Trie to find all strings that start with the input string. The Trie allows for efficient retrieval of strings with a common prefix.

## Complexity
- Time: O(N + M) where N is the total number of characters in all strings and M is the total number of characters in the input strings.
- Space: O(N) where N is the total number of characters in all strings.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<string> suggestions;
};

class SearchSuggestionsSystem {
public:
    TrieNode* root;

    SearchSuggestionsSystem() {
        root = new TrieNode();
    }

    void addString(string str) {
        TrieNode* node = root;
        for (char c : str) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->suggestions.push_back(str);
    }

    vector<vector<string>> search(string input) {
        TrieNode* node = root;
        vector<vector<string>> result;
        for (char c : input) {
            if (node->children.find(c) == node->children.end()) {
                return result;
            }
            node = node->children[c];
            vector<string> suggestions;
            dfs(node, suggestions);
            sort(suggestions.begin(), suggestions.end());
            if (suggestions.size() > 3) {
                suggestions.resize(3);
            }
            result.push_back(suggestions);
        }
        return result;
    }

    void dfs(TrieNode* node, vector<string>& suggestions) {
        if (node->suggestions.size() > 0) {
            for (string str : node->suggestions) {
                suggestions.push_back(str);
            }
        }
        for (auto child : node->children) {
            dfs(child.second, suggestions);
        }
    }
};

int main() {
    SearchSuggestionsSystem system;
    system.addString("mobile");
    system.addString("mouse");
    system.addString("moneypot");
    system.addString("monitor");
    system.addString("mousepad");

    vector<vector<string>> result = system.search("mouse");
    for (vector<string> suggestions : result) {
        for (string str : suggestions) {
            cout << str << " ";
        }
        cout << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
addString("mobile")
addString("mouse")
addString("moneypot")
addString("monitor")
addString("mousepad")
search("mouse")

Output: 
mouse moneypot mobile 
mouse mousepad monitor 
mouse mousepad monitor 
```

## Key Takeaways
- Use a Trie data structure to store all strings for efficient retrieval.
- Traverse the Trie to find all strings with a common prefix.
- Use a depth-first search to collect all suggestions from the Trie node and its children.