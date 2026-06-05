# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where adjacent cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The input is a 2D array of characters `board` and a list of strings `words`. The output should be a list of strings, which are the words found in the `board`. For example, if the input is `board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]` and `words = ["oath","pea","eat","rain"]`, the output should be `["eat","oath"]`.

## Approach
The solution uses a Trie data structure to store the dictionary words and then performs a depth-first search on the board to find all words. The Trie allows for efficient lookup and the DFS explores all possible word paths.

## Complexity
- Time: O(N * M * 4^L), where N and M are the dimensions of the board and L is the maximum length of a word
- Space: O(N * M + W), where W is the total number of characters in all words

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    string word;
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (string word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->word = word;
        }

        set<string> result;
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                dfs(board, i, j, root, result);
            }
        }
        return vector<string>(result.begin(), result.end());
    }

    void dfs(vector<vector<char>>& board, int i, int j, TrieNode* node, set<string>& result) {
        char c = board[i][j];
        if (node->children.find(c) == node->children.end()) return;
        node = node->children[c];
        if (!node->word.empty()) {
            result.insert(node->word);
        }

        board[i][j] = '#';
        if (i > 0) dfs(board, i - 1, j, node, result);
        if (j > 0) dfs(board, i, j - 1, node, result);
        if (i < board.size() - 1) dfs(board, i + 1, j, node, result);
        if (j < board[0].size() - 1) dfs(board, i, j + 1, node, result);
        board[i][j] = c;
    }
};

```

## Test Cases
```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

## Key Takeaways
- Using a Trie to store the dictionary words allows for efficient lookup and reduces the search space.
- The DFS approach explores all possible word paths in the board.
- Marking visited cells with a special character (#) avoids revisiting the same cell in a word path.