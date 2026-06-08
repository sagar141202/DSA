# Right Side View of Binary Tree

## Problem Statement
Given a binary tree, return a list of values of the rightmost node at each level. The input tree is represented as a binary tree where each node has a value and two children (left and right). The right side view is the set of nodes you will see when the tree is viewed from the right side. For example, given the binary tree `[1,2,3,null,5,null,4]` which is:
```
    1
   / \
  2   3
   \   \
    5   4
```
The right side view is `[1,3,4]`.

## Approach
The approach is to use a level order traversal (BFS) to visit each node at each level from left to right and store the last node's value at each level. We use a queue to keep track of the nodes to be visited.

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
Input: [1,null,3]
Output: [1,3]
```

## Key Takeaways
- Use level order traversal (BFS) to visit each node at each level.
- Store the last node's value at each level to get the right side view.
- Use a queue to keep track of the nodes to be visited.