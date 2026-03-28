# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. For example, the maximum depth of the binary tree in the figure is 3. Constraints: The number of nodes in the tree is in the range [0, 104]. The depth of the tree is in the range [0, 104]. 

## Approach
The algorithm uses a recursive approach to traverse the tree and find the maximum depth. It checks if the root is null, and if so, returns 0. Otherwise, it recursively finds the maximum depth of the left and right subtrees and returns the maximum of these two depths plus 1.

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
        // Recursively find the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        // Return the maximum of these two depths plus 1
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
- Recursion can be used to solve tree problems by breaking down the problem into smaller sub-problems.
- The time complexity of this solution is O(N), where N is the number of nodes in the tree, because each node is visited once.
- The space complexity of this solution is O(H), where H is the height of the tree, because of the recursive call stack.