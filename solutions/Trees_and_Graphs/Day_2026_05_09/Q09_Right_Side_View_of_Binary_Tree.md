# Right Side View of Binary Tree

## Problem Statement
Given the root of a binary tree, return the rightmost node value at each level, from left to right. The input tree is guaranteed to be non-empty, and each level will have at least one node. For example, given the binary tree `[1,2,3,null,5,null,4]`, the right side view is `[1,3,4]`. The tree is defined as follows: the root node is `1`, the left child of `1` is `2`, the right child of `1` is `3`, the right child of `2` is `5`, and the right child of `3` is `4`. The constraints are: the number of nodes in the tree is in the range `[1, 100]`, and `-100 <= Node.val <= 100`.

## Approach
The algorithm uses a level order traversal (Breadth-First Search, BFS) to visit each level of the tree from left to right, and for each level, it adds the last visited node's value to the result. This way, we can efficiently find the rightmost node at each level.

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
- Use level order traversal to visit each level of the tree from left to right.
- For each level, add the last visited node's value to the result to get the right side view.
- The time complexity is O(N), where N is the number of nodes in the tree, since we visit each node once.