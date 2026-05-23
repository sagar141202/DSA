# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value in each level from left to right. The input tree is a binary tree where each node has a value and at most two children (i.e., left child and right child). The tree has at most 100 nodes and the values are in the range [0, 100]. The output should be a vector of integers representing the rightmost node values in each level. For example, given the binary tree:
```
    1
   / \
  2   3
 / \
4   5
```
The output should be `[1, 3, 5]`.

## Approach
The approach is to use a level-order traversal (BFS) and store the last node value in each level. We can use a queue to store the nodes and their corresponding levels.

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
Input: 
    1
   / \
  2   3
 / \
4   5
Output: [1, 3, 5]
```

## Key Takeaways
- Use level-order traversal (BFS) to traverse the tree level by level.
- Store the last node value in each level to get the rightmost node values.
- Use a queue to store the nodes and their corresponding levels for efficient traversal.