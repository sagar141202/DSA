# Maximum Depth of Binary Tree

## Problem Statement
Given a binary tree, find its maximum depth. The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node. The path must start at the root and end at any leaf node. For example, the maximum depth of the binary tree in the figure below is 3. Constraints: The number of nodes in the tree is in the range [0, 104]. The depth of the tree is in the range [0, 104]. 

## Approach
To find the maximum depth, we can use recursion to traverse the tree. We start at the root node and recursively find the maximum depth of the left and right subtrees. The maximum depth of the tree is the maximum depth of the left and right subtrees plus one. 

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
        if (root == nullptr) return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};
```

## Test Cases
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

## Key Takeaways
- The maximum depth of a binary tree can be found using recursion.
- We need to handle the base case where the tree is empty (i.e., the root is nullptr).
- The time complexity is O(n) where n is the number of nodes in the tree, and the space complexity is O(h) where h is the height of the tree.