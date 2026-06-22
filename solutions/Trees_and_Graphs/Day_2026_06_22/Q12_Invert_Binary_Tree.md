# Invert Binary Tree

## Problem Statement
Invert a binary tree, which means swapping the left and right child nodes of each internal node. Given the root of a binary tree, return the root of the inverted binary tree. The binary tree node has a value and two children: left and right. The number of nodes in the tree is in the range [0, 100]. The input tree is guaranteed to be a valid binary tree. For example, given the binary tree:
       4
     /   \
    2     7
   / \   / \
  1   3 6   9
The inverted binary tree will be:
       4
     /   \
    7     2
   / \   / \
  9   6 3   1

## Approach
The algorithm involves recursively traversing the binary tree and swapping the left and right child nodes of each internal node. This can be achieved by using a depth-first search (DFS) approach, where we recursively visit each node and swap its children. The base case for the recursion is when the node is null, in which case we return null.

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
        // Base case: if the tree is empty, return null
        if (root == nullptr) {
            return nullptr;
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
- The time complexity of the solution is O(n), where n is the number of nodes in the tree, since we visit each node exactly once.
- The space complexity of the solution is O(h), where h is the height of the tree, due to the recursive call stack. In the worst case, the tree is completely unbalanced, e.g., each node has only left child node, the recursion call would occur N times (the height of the tree), therefore storage to store the call stack would be O(N). In the best case, the tree is completely balanced, the height of the tree would be log(N). Therefore, the space complexity in this case would be O(log(N)).