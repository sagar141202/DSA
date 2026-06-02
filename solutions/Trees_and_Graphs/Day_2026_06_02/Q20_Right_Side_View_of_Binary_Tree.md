# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level, from top to bottom. The input tree is a binary tree where each node has a unique value and at most two children (i.e., left child and right child). The number of nodes in the tree is in the range [0, 100]. The input tree is not guaranteed to be balanced. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`.

## Approach
We will use a level order traversal (BFS) approach to solve this problem. This involves traversing the tree level by level, from left to right, and keeping track of the last node at each level. We will use a queue data structure to store nodes at each level.

## Complexity
- Time: O(n)
- Space: O(n)

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
Input: [1,null,3]
Output: [1,3]
```

## Key Takeaways
- Use level order traversal to solve this problem.
- Keep track of the last node at each level.
- Use a queue data structure to store nodes at each level.
- The time complexity is O(n), where n is the number of nodes in the tree.
- The space complexity is O(n), where n is the number of nodes in the tree.