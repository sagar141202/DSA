# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. The number of nodes in the path is the depth of the tree. For example, the maximum depth of the binary tree in the figure below is 3. The constraints are that the number of nodes in the tree is in the range [0, 10^4], and the values of the nodes are not relevant to the problem.

## Approach
The algorithm uses a recursive depth-first search (DFS) approach to traverse the tree and calculate the maximum depth. It checks if the current node is null, and if so, returns 0. Otherwise, it recursively calculates the maximum depth of the left and right subtrees and returns the maximum of the two plus 1.

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
        // recursive case: calculate the maximum depth of the left and right subtrees
        int left_depth = maxDepth(root->left);
        int right_depth = maxDepth(root->right);
        // return the maximum of the two depths plus 1
        return max(left_depth, right_depth) + 1;
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
- The maximum depth of a binary tree can be calculated using a recursive DFS approach.
- The time complexity of the solution is O(N), where N is the number of nodes in the tree.
- The space complexity of the solution is O(H), where H is the height of the tree.