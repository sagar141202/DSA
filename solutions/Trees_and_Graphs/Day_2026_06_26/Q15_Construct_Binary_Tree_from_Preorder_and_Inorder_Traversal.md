# Construct Binary Tree from Preorder and Inorder Traversal

## Problem Statement
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree. The length of both preorder and inorder arrays is equal to the number of nodes in the binary tree. The nodes of the binary tree are numbered from 1 to n, where n is the number of nodes. The root of the binary tree is the first element in the preorder array, and the left and right child nodes of a node are the first and last elements in the inorder array that are less than the node's value. The input arrays are guaranteed to be valid, and it is possible to reconstruct the binary tree from the given preorder and inorder traversals. For example, given preorder = [3,9,20,15,7] and inorder = [9,3,15,20,7], the output should be a binary tree where 3 is the root, 9 is the left child of 3, and 20 is the right child of 3, with 15 and 7 as the left and right children of 20 respectively.

## Approach
We can solve this problem by recursively constructing the binary tree. The base case is when the preorder or inorder array is empty. We find the root of the tree from the preorder array and then find its position in the inorder array to determine the left and right subtrees.

## Complexity
- Time: O(n)
- Space: O(n)

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty() || inorder.empty()) {
            return NULL;
        }
        
        // The first element in the preorder array is the root of the tree
        int rootVal = preorder[0];
        TreeNode* root = new TreeNode(rootVal);
        
        // Find the position of the root in the inorder array
        int pos = 0;
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] == rootVal) {
                pos = i;
                break;
            }
        }
        
        // Construct the left subtree
        vector<int> leftPreorder(preorder.begin() + 1, preorder.begin() + pos + 1);
        vector<int> leftInorder(inorder.begin(), inorder.begin() + pos);
        root->left = buildTree(leftPreorder, leftInorder);
        
        // Construct the right subtree
        vector<int> rightPreorder(preorder.begin() + pos + 1, preorder.end());
        vector<int> rightInorder(inorder.begin() + pos + 1, inorder.end());
        root->right = buildTree(rightPreorder, rightInorder);
        
        return root;
    }
};
```

## Test Cases
```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: 
    3
   / \
  9  20
    /  \
   15   7
```

## Key Takeaways
- The preorder traversal visits the root node first, then the left subtree, and finally the right subtree.
- The inorder traversal visits the left subtree, then the root node, and finally the right subtree.
- We can use the position of the root in the inorder array to determine the left and right subtrees.