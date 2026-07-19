# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level. The rightmost node at each level is the last node to be visited during a level order traversal of the binary tree. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`. The binary tree node has a value and two children, left and right.

## Approach
We can use a level order traversal (BFS) approach to solve this problem. We start from the root node and traverse each level from left to right. At each level, we store the last visited node's value. This approach ensures that we get the rightmost node at each level.

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
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (i == size - 1) {
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
- Use level order traversal (BFS) to traverse the binary tree.
- At each level, store the last visited node's value to get the rightmost node.
- Use a queue data structure to implement the level order traversal.