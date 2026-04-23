# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The number of nodes at each level of the tree is not limited, and each node has at most two children (i.e., left child and right child). For example, given the binary tree `[3,9,20,null,null,15,7]`, the maximum depth is `3` because the path from the root node `3` to the leaf node `7` has three nodes.

## Approach
The approach is to use a recursive depth-first search (DFS) to traverse the binary tree and find the maximum depth. We start at the root node and recursively call the function for the left and right children. The maximum depth is the maximum of the depths of the left and right subtrees plus one for the current node.

## Complexity
- Time: O(N)
- Space: O(H)

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
        // Base case: if the tree is empty, return 0
        if (root == nullptr) {
            return 0;
        }
        
        // Recursively find the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // Return the maximum depth of the two subtrees plus one for the current node
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
- The maximum depth of a binary tree can be found using a recursive DFS approach.
- The time complexity is O(N), where N is the number of nodes in the tree, because each node is visited once.
- The space complexity is O(H), where H is the height of the tree, because of the recursive call stack.