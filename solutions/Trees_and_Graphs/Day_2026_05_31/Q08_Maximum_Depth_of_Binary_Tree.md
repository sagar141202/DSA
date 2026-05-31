# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node, and it must only go through nodes that have a parent-child relationship. The input is the root of the binary tree, and the output is the maximum depth of the tree. For example, the maximum depth of the binary tree with the following structure:
```
    3
   / \
  9  20
    /  \
   15   7
```
is 3.

## Approach
The algorithm uses a recursive approach to traverse the binary tree, calculating the maximum depth of the left and right subtrees and returning the maximum of the two plus one. This approach ensures that all nodes are visited and the maximum depth is calculated correctly. The base case is when the tree is empty, in which case the function returns 0.

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
        
        // Recursively calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // Return the maximum of the two depths plus one
        return max(leftDepth, rightDepth) + 1;
    }
};
```

## Test Cases
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
Input: root = [1,null,2]
Output: 2
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using a recursive approach.
- The base case for the recursion is when the tree is empty, in which case the function returns 0.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree, and the space complexity is O(H), where H is the height of the tree.