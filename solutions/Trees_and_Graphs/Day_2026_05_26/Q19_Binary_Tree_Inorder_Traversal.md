# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree node has a value and two children: left and right. The constraints are: the number of nodes in the tree is in the range [0, 100], and -100 <= Node.val <= 100. For example, given the binary tree [1, null, 2, 3], the inorder traversal is [1, 3, 2].

## Approach
The algorithm uses a recursive approach to traverse the binary tree in inorder. It first visits the left subtree, then the current node, and finally the right subtree. This can also be achieved using a stack-based iterative approach.

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
        if (node == nullptr) {
            return;
        }
        traverse(node->left, result);
        result.push_back(node->val);
        traverse(node->right, result);
    }
};
```

## Test Cases
```
Input: [1, null, 2, 3]
Output: [1, 3, 2]
Input: []
Output: []
Input: [1]
Output: [1]
```

## Key Takeaways
- Inorder traversal visits the left subtree, the current node, and then the right subtree.
- The recursive approach can be used to solve this problem by traversing the left subtree, the current node, and then the right subtree.
- The time complexity of this solution is O(n), where n is the number of nodes in the tree, and the space complexity is also O(n) due to the recursive call stack.