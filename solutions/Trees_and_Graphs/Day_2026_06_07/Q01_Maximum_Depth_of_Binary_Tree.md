# Maximum Depth of Binary Tree

## Problem Statement
Given a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root node and end at any leaf node. The depth of a tree is the maximum number of edges between the root and any leaf node. For example, the maximum depth of the binary tree `[3,9,20,null,null,15,7]` is `3`, because the longest path from the root node `3` to the farthest leaf node `7` has `3` edges.

## Approach
The approach to solve this problem is to use a recursive depth-first search (DFS) algorithm to traverse the binary tree and calculate the maximum depth. We will recursively calculate the depth of the left and right subtrees and return the maximum depth plus one for the current node.

## Complexity
- Time: O(n)
- Space: O(h)

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
    int maxDepth(TreeNode* root) {
        // base case: if the tree is empty, return 0
        if (root == nullptr) {
            return 0;
        }
        
        // recursively calculate the depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // return the maximum depth plus one for the current node
        return max(leftDepth, rightDepth) + 1;
    }
};
```

## Test Cases
```
Input: [3,9,20,null,null,15,7]
Output: 3
Input: [1,null,2]
Output: 2
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using a recursive DFS algorithm.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree.
- The space complexity of the solution is O(h), where h is the height of the tree.