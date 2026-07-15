# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children. The path must start at the root and end at a leaf node. For example, consider the binary tree with the following structure: 
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      5
The path sum from the root to the leaf node 5 -> 4 -> 11 -> 2 is 5 + 4 + 11 + 2 = 22. If the target sum is 22, the function should return true.

## Approach
The solution uses a recursive depth-first search (DFS) approach to traverse the binary tree, keeping track of the current sum of node values. If a leaf node is reached and the current sum equals the target sum, the function returns true.

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
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == nullptr) return false;
        if (root->left == nullptr && root->right == nullptr) {
            // Check if the current node is a leaf node
            return root->val == targetSum;
        }
        // Recursively search for a path sum in the left and right subtrees
        return hasPathSum(root->left, targetSum - root->val) || hasPathSum(root->right, targetSum - root->val);
    }
};
```

## Test Cases
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: true
```

## Key Takeaways
- Use recursive DFS to traverse the binary tree and keep track of the current sum of node values.
- Check if the current node is a leaf node and if its value equals the remaining target sum.
- Recursively search for a path sum in the left and right subtrees by subtracting the current node's value from the target sum.