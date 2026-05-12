# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The number of nodes at each level of the tree is not limited, and the tree can be empty. For example, the maximum depth of the binary tree in the figure is 3.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the tree and calculate the maximum depth. It starts from the root node and recursively calculates the maximum depth of the left and right subtrees. The maximum depth is then determined by taking the maximum of the left and right subtree depths and adding 1 for the current node.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        // base case: if the tree is empty, return 0
        if (root == NULL) {
            return 0;
        }
        
        // recursively calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // return the maximum of the left and right subtree depths plus 1 for the current node
        return max(leftDepth, rightDepth) + 1;
    }
};
```

## Test Cases
```
Input: 
    3
   / \
  9  20
    /  \
   15   7
Output: 3

Input: 
   1
Output: 1

Input: 
Output: 0
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using a recursive DFS approach.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree.
- The space complexity of the solution is O(h), where h is the height of the tree.