# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root node and end at any leaf node. The number of nodes in the path represents the depth of the tree. For example, the maximum depth of the binary tree `[3,9,20,null,null,15,7]` is 3, since the longest path from the root node to a leaf node is `3 -> 20 -> 7`.

## Approach
The approach to solve this problem is to use a recursive depth-first search (DFS) algorithm to traverse the binary tree and calculate the maximum depth. We will recursively calculate the maximum depth of the left and right subtrees and return the maximum of the two plus one for the current node.

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
        // base case: if the tree is empty, return 0
        if (root == nullptr) {
            return 0;
        }
        
        // recursively calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // return the maximum of the two plus one for the current node
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
- The time complexity of the algorithm is O(N), where N is the number of nodes in the tree.
- The space complexity of the algorithm is O(H), where H is the height of the tree.