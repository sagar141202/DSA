# Invert Binary Tree

## Problem Statement
Invert a binary tree, which means swapping the left and right child nodes of each internal node. Given the root of a binary tree, return the root of the inverted binary tree. The number of nodes in the tree is in the range [0, 100]. -100 <= Node.val <= 100.

## Approach
The algorithm involves recursively traversing the binary tree and swapping the left and right child nodes of each internal node. This can be achieved by using a recursive function that takes the root node as an argument. The base case for the recursion is when the root is NULL, in which case the function returns NULL.

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
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return NULL
        if (root == NULL) {
            return NULL;
        }

        // Swap the left and right subtrees
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;

        // Recursively invert the left and right subtrees
        root->left = invertTree(root->left);
        root->right = invertTree(root->right);

        return root;
    }
};
```

## Test Cases
```
Input: [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

## Key Takeaways
- Recursive approach can be used to traverse and modify the binary tree.
- Swapping the left and right child nodes of each internal node inverts the binary tree.
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, since each node is visited exactly once.