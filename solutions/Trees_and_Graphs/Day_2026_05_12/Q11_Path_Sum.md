# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children. The path must start at the root and end at a leaf node, and all nodes in the path must be included in the sum. For example, given the binary tree with root [5,4,8,11,null,13,4,7,2,null,null,5,1] and target sum 22, return true because the path 5 -> 4 -> 11 -> 2 sums up to 22.

## Approach
The algorithm uses a recursive depth-first search approach to traverse the binary tree, checking if the sum of the current path equals the target sum when a leaf node is reached. If such a path is found, the function returns true. The approach ensures that all possible paths are explored.

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
        // base case: if tree is empty, return false
        if (!root) return false;
        
        // if current node is a leaf and its value equals the target sum, return true
        if (!root->left && !root->right && root->val == targetSum) return true;
        
        // recursively explore left and right subtrees with updated target sum
        targetSum -= root->val;
        return hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum);
    }
};
```

## Test Cases
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: true
```

## Key Takeaways
- Use recursive depth-first search to explore all possible paths in the binary tree.
- Keep track of the current path sum by subtracting the current node's value from the target sum.
- Base cases include an empty tree (return false) and a leaf node with a matching sum (return true).