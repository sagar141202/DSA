# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree node has a value and two children: left and right. The input tree is guaranteed to be non-empty, and each node has a unique value. For example, given the following binary tree: 
       4
     /   \
    2     6
   / \   / \
  1   3 5   7
The inorder traversal is [1, 2, 3, 4, 5, 6, 7]. 

## Approach
The algorithm uses a recursive or iterative approach to traverse the binary tree in inorder. It starts by visiting the left subtree, then the current node, and finally the right subtree. This can be achieved using a stack to store nodes or by using recursive function calls.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        traverse(root, result);
        return result;
    }

    void traverse(TreeNode* node, vector<int>& result) {
        if (node == nullptr) return;
        traverse(node->left, result);
        result.push_back(node->val);
        traverse(node->right, result);
    }
};
```

## Test Cases
```
Input: [4,2,6,1,3,5,7]
Output: [1,2,3,4,5,6,7]
```

## Key Takeaways
- Inorder traversal visits nodes in ascending order for a binary search tree.
- Recursive and iterative solutions have the same time complexity but differ in space complexity due to the system call stack.
- The choice between recursive and iterative solutions depends on the specific problem constraints and personal preference.