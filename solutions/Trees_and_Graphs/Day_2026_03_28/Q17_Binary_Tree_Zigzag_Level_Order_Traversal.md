# Binary Tree Zigzag Level Order Traversal

## Problem Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. The zigzag level order traversal is defined as follows: for each given tree level, the first node from the left is the first node for that level, and then the last node from the left (i.e., the rightmost node for that level), then the second node from the left, and so on, with each level ordered from left to right and right to left alternatingly. The input tree is guaranteed to be non-empty, and each node has a unique value. The number of nodes in the tree is in the range [1, 2000], and the values of the nodes are in the range [-1000, 1000].

## Approach
The algorithm uses a level order traversal (BFS) approach with a queue to traverse the tree level by level. To achieve the zigzag effect, we use a flag to track whether we should traverse the current level from left to right or right to left. We then reverse the level order when the flag is set to reverse.

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;

        queue<TreeNode*> q;
        q.push(root);
        bool reverse = false;

        while (!q.empty()) {
            int size = q.size();
            vector<int> level;

            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();

                if (reverse) {
                    level.insert(level.begin(), node->val);
                } else {
                    level.push_back(node->val);
                }

                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }

            result.push_back(level);
            reverse = !reverse;
        }

        return result;
    }
};
```

## Test Cases
```
Input: [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Input: [1]
Output: [[1]]

Input: []
Output: []
```

## Key Takeaways
- Use a level order traversal (BFS) approach with a queue to traverse the tree level by level.
- Use a flag to track whether we should traverse the current level from left to right or right to left.
- Reverse the level order when the flag is set to reverse.