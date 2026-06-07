# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children. The path must start at the root and end at a leaf node. For example, given the binary tree `root = [5,4,8,11,null,13,4,7,2,null,null,5,1]` and `targetSum = 22`, the function should return `true` because the path `5 -> 4 -> 11 -> 2` has a sum of 22.

## Approach
The solution involves using a recursive depth-first search (DFS) to traverse the tree and keep track of the current path sum. If the current node is a leaf and the path sum equals the target sum, return true. Otherwise, recursively search the left and right subtrees.

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
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == nullptr) return false;
        if (root->left == nullptr && root->right == nullptr) {
            // if the current node is a leaf
            return root->val == targetSum;
        }
        // recursively search the left and right subtrees
        return hasPathSum(root->left, targetSum - root->val) || hasPathSum(root->right, targetSum - root->val);
    }
};
```

## Test Cases
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: true
Input: root = [1,2,3], targetSum = 5
Output: false
```

## Key Takeaways
- Use recursive DFS to traverse the tree and keep track of the current path sum.
- Check if the current node is a leaf and the path sum equals the target sum.
- Handle the base case where the tree is empty.