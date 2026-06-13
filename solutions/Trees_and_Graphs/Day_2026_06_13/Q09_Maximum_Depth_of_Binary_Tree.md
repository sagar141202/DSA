# Maximum Depth of Binary Tree

## Problem Statement
Given a binary tree, find its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The number of nodes at each level of the tree (from top to bottom) is as follows: root (1 node), next level (2 nodes), next level after that (4 nodes), and so on. For example, given the binary tree `[3,9,20,null,null,15,7]`, the maximum depth is 3.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the tree and find the maximum depth. It checks if the current node is null, and if so, returns 0. Otherwise, it recursively calculates the maximum depth of the left and right subtrees and returns the maximum of the two plus one.

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
        // Base case: if the tree is empty, return 0
        if (root == NULL) {
            return 0;
        }
        // Recursively calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        // Return the maximum of the two depths plus one (for the current node)
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
- The time complexity is O(n), where n is the number of nodes in the tree, because each node is visited once.
- The space complexity is O(h), where h is the height of the tree, because of the recursive call stack.