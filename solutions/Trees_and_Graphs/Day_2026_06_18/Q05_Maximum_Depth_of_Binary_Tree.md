# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The number of nodes in the path is the depth of the tree. For example, the maximum depth of the binary tree `[3,9,20,null,null,15,7]` is `3` because the longest path from the root to a leaf node is `3 -> 20 -> 7`. The constraints are that the number of nodes in the tree is in the range `[0, 10^4]`, and the values of the nodes are in the range `[-2^31, 2^31 - 1]`.

## Approach
The algorithm to solve this problem is a recursive depth-first search (DFS) that traverses the tree and keeps track of the maximum depth encountered. The base case is when the tree is empty (i.e., the root is null), in which case the depth is 0. For non-empty trees, the depth is 1 plus the maximum depth of the left and right subtrees.

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
        // Base case: if the tree is empty, the depth is 0
        if (root == nullptr) {
            return 0;
        }
        // Recursive case: the depth is 1 plus the maximum depth of the left and right subtrees
        else {
            return 1 + max(maxDepth(root->left), maxDepth(root->right));
        }
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
- The maximum depth of a binary tree can be found using a recursive DFS approach.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree, because each node is visited once.
- The space complexity of the solution is O(H), where H is the height of the tree, because of the recursive call stack.