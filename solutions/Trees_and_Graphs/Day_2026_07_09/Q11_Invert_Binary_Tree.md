# Invert Binary Tree

## Problem Statement
Invert a binary tree, where the left and right child nodes of every node are swapped. The function should take the root of the binary tree as input and return the root of the inverted binary tree. For example, given the binary tree:
     4
   /   \
  2     7
 / \   / \
1   3 6   9
The inverted binary tree would be:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
The binary tree node has an integer value and two children, left and right.

## Approach
The algorithm to invert a binary tree involves recursively traversing the tree and swapping the left and right child nodes of each node. This can be achieved by using a recursive function that takes the root of the binary tree as input. The base case is when the root is null, in which case the function returns null.

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
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return null
        if (root == NULL) return NULL;
        
        // Swap the left and right child nodes
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recursively invert the left and right subtrees
        invertTree(root->left);
        invertTree(root->right);
        
        // Return the root of the inverted binary tree
        return root;
    }
};
```

## Test Cases
```
Input: 
     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output: 
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

## Key Takeaways
- The time complexity of the algorithm is O(n), where n is the number of nodes in the binary tree, because each node is visited once.
- The space complexity of the algorithm is O(h), where h is the height of the binary tree, because of the recursive call stack. In the worst case, the binary tree is skewed and the space complexity is O(n).