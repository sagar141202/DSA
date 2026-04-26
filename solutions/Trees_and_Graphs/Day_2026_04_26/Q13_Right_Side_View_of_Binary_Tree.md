# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level. The rightmost node at each level is the last node to be visited during a level order traversal of the tree. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`. The tree is defined as follows: the root node is `1`, the left child of the root is `2`, the right child of the root is `3`, the right child of `2` is `5`, and the right child of `3` is `4`. The constraints are that the number of nodes in the tree will be in the range `[0, 100]` and `-100 <= Node.val <= 100`.

## Approach
We use a level order traversal (BFS) to visit all nodes at each level from left to right, and update the result with the last node value at each level. This ensures that we capture the rightmost node at each level.

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
Input: []
Output: []
```

## Key Takeaways
- Level order traversal (BFS) is suitable for problems that require visiting nodes level by level.
- Using a queue to store nodes at each level simplifies the traversal process.
- Updating the result with the last node value at each level ensures that we capture the rightmost node.