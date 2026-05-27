# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The number of nodes that the path passes through is the depth of the tree. For example, the maximum depth of the binary tree in the figure is 3. The constraints are that the number of nodes in the tree is in the range [0, 10^4], and the values of the nodes are in the range [-2^31, 2^31 - 1].

## Approach
The algorithm used to solve this problem is a recursive depth-first search (DFS) approach. We start at the root node and recursively traverse the left and right subtrees, keeping track of the maximum depth encountered. The base case is when the current node is null, in which case the depth is 0.

## Complexity
- Time: O(N)
- Space: O(H), where N is the number of nodes in the tree and H is the height of the tree.

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
        // Recursively find the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        // Return the maximum depth of the two subtrees plus 1 (for the current node)
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
- The maximum depth of a binary tree can be found using a recursive DFS approach.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree.
- The space complexity of the solution is O(H), where H is the height of the tree.