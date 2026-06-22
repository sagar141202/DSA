# Maximum Depth of Binary Tree

## Problem Statement
Given a binary tree, find its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any node, and it can go as far left or right as possible. For example, the maximum depth of the binary tree `[3,9,20,null,null,15,7]` is `3` because the path `3 -> 20 -> 7` has the maximum length of `3`. The input binary tree is represented as a tree where each node is an object with an integer value and two pointers, `left` and `right`, representing the left and right child nodes, respectively.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the binary tree and calculate the maximum depth. It starts at the root node and recursively explores the left and right subtrees, keeping track of the maximum depth encountered. The maximum depth is updated whenever a longer path is found.

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
    int maxDepth(TreeNode* root) {
        // Base case: if the tree is empty, return 0
        if (root == nullptr) {
            return 0;
        }

        // Recursively calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);

        // Return the maximum depth of the current node and its subtrees
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
Input: []
Output: 0
```

## Key Takeaways
- The maximum depth of a binary tree can be calculated using a recursive DFS approach.
- The time complexity of the algorithm is O(n), where n is the number of nodes in the tree, because each node is visited once.
- The space complexity of the algorithm is O(h), where h is the height of the tree, because of the recursive call stack.