# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level. The rightmost node value at each level is the last node value when traversing the level from left to right. The input tree is a valid binary tree, and the number of nodes in the tree is in the range [1, 100]. The value of each node is unique. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`.

## Approach
We can solve this problem using a level order traversal (BFS) approach, where we traverse the tree level by level and keep track of the last node value at each level. We use a queue to store the nodes at each level and update the result with the last node value at each level.

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
                
                // if this is the last node at the current level, add it to the result
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
- Use a level order traversal (BFS) approach to traverse the tree level by level.
- Keep track of the last node value at each level using the queue size.
- Update the result with the last node value at each level.