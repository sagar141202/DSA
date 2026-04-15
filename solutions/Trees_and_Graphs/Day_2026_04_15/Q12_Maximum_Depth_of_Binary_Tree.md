# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, find the maximum depth of the tree. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node, and it must only go through nodes one step at a time. The depth of an empty tree is 0, and the depth of a tree with one node is 1. For example, the maximum depth of the binary tree with the following structure:
       3
      / \
     9  20
       /  \
      15   7
is 3.

## Approach
We can use a recursive approach to solve this problem by calculating the maximum depth of the left and right subtrees and returning the maximum of the two plus one. This approach takes advantage of the recursive nature of trees. We will also handle the base case where the tree is empty.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        // base case: if the tree is empty, return 0
        if (root == NULL) {
            return 0;
        }
        
        // recursive case: calculate the maximum depth of the left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // return the maximum of the two plus one
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
- The maximum depth of a binary tree can be calculated using a recursive approach.
- The time complexity of this solution is O(N), where N is the number of nodes in the tree, because we visit each node once.
- The space complexity of this solution is O(H), where H is the height of the tree, because that's the maximum depth of the recursive call stack.