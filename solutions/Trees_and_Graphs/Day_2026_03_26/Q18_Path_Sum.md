# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children. The path does not need to go through the root. For example, given the binary tree with root [5,4,8,11,null,13,4,7,2,null,null,5,1] and targetSum 22, the function should return true because the path 5 -> 4 -> 11 -> 2 sums up to 22.

## Approach
The approach is to use depth-first search (DFS) to traverse the tree, keeping track of the current sum of node values. If a leaf node is reached and the current sum equals the target sum, return true. Otherwise, continue exploring other paths.

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
        if (root == nullptr) {
            return false;
        }
        
        // recursive case: if current node is a leaf and sum equals target, return true
        if (root->left == nullptr && root->right == nullptr) {
            return root->val == targetSum;
        }
        
        // recursive case: explore left and right subtrees
        targetSum -= root->val;
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
- Use DFS to traverse the tree and keep track of the current sum of node values.
- If a leaf node is reached, check if the current sum equals the target sum.
- The time complexity is O(N), where N is the number of nodes in the tree, since we visit each node once.
- The space complexity is O(H), where H is the height of the tree, due to the recursive call stack.