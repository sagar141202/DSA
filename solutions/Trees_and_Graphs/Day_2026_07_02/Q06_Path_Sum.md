# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children. The path must start at the root and end at a leaf. For example, given the binary tree with root [5,4,8,11,null,13,4,7,2,null,null,5,1] and target sum 22, the function should return true because the path 5 -> 4 -> 11 -> 2 sums up to 22.

## Approach
The algorithm uses a recursive depth-first search approach to traverse the tree, keeping track of the current sum of node values. If a leaf node is reached and the current sum equals the target sum, the function returns true.

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
        // Base case: if the tree is empty, return false
        if (!root) return false;
        
        // Recursive case: if the current node is a leaf and its value equals the target sum, return true
        if (!root->left && !root->right) return root->val == targetSum;
        
        // Recursive case: subtract the current node's value from the target sum and continue the search
        targetSum -= root->val;
        
        // Recursively search for a path sum in the left and right subtrees
        return hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum);
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
- The problem can be solved using a recursive depth-first search approach.
- The time complexity is O(N), where N is the number of nodes in the tree, because each node is visited once.
- The space complexity is O(H), where H is the height of the tree, because that's the maximum depth of the recursive call stack.