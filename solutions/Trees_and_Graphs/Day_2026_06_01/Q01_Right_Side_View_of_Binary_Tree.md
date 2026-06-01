# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level, from top to bottom. The input tree is a binary tree where each node has a value and at most two children (i.e., left child and right child). The number of nodes in the tree is in the range [0, 100]. The input tree is not guaranteed to be balanced. For example, given the binary tree `[1,2,3,null,5,null,4]`, return `[1,3,4]`.

## Approach
The algorithm uses a level-order traversal (BFS) approach to iterate over the tree level by level, storing the last node value at each level. This is done by using a queue to store nodes and their corresponding levels. The rightmost node at each level is the last node processed.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (i == levelSize - 1) {
                    result.push_back(node->val);
                }
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [1,2,3,null,5,null,4]
Output: [1,3,4]
Input: [1]
Output: [1]
Input: []
Output: []
```

## Key Takeaways
- Use level-order traversal (BFS) to solve this problem efficiently.
- Store the last node value at each level to get the rightmost node.
- Use a queue to store nodes and their corresponding levels for efficient traversal.