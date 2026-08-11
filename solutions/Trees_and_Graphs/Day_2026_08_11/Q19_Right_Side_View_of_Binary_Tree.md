# Right Side View of Binary Tree

## Problem Statement
Given a binary tree, return a list of values representing the rightmost node at each level. The input tree is represented as a binary tree where each node has a value and two child nodes (left and right). The output should be a list of integers representing the rightmost node value at each level, from top to bottom. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`. The binary tree is defined as follows: the root node is `1`, the left child of the root is `2`, the right child of the root is `3`, the right child of `2` is `5`, and the right child of `3` is `4`. The constraints are that the number of nodes in the tree is between `0` and `100`, and the value of each node is between `0` and `100`.

## Approach
The algorithm uses a level-order traversal (BFS) approach to traverse the binary tree level by level, and at each level, it adds the last node's value to the result list. This ensures that only the rightmost node at each level is included in the output.

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
```

## Key Takeaways
- Use level-order traversal (BFS) to solve this problem efficiently.
- Keep track of the last node at each level to get the right side view.
- Use a queue to implement the level-order traversal.