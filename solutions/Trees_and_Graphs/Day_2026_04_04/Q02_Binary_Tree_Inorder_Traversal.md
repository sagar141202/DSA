# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree node has a value and two children: left and right. The constraints are: the number of nodes in the tree is in the range [0, 100], and -100 <= Node.val <= 100.

## Approach
The algorithm uses a recursive approach to traverse the binary tree in an inorder manner. It first visits the left subtree, then the current node, and finally the right subtree. This can also be achieved using an iterative approach with a stack data structure.

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
        // Recursive approach
        // inorderTraversalHelper(root, result);
        
        // Iterative approach
        stack<TreeNode*> st;
        TreeNode* curr = root;
        while (curr != nullptr || !st.empty()) {
            // Traverse to the leftmost node
            while (curr != nullptr) {
                st.push(curr);
                curr = curr->left;
            }
            // Backtrack and visit the node
            curr = st.top();
            st.pop();
            result.push_back(curr->val);
            // Move to the right subtree
            curr = curr->right;
        }
        return result;
    }
    
    // Recursive helper function
    void inorderTraversalHelper(TreeNode* root, vector<int>& result) {
        if (root == nullptr) return;
        inorderTraversalHelper(root->left, result);
        result.push_back(root->val);
        inorderTraversalHelper(root->right, result);
    }
};
```

## Test Cases
```
Input: root = [4,2,5,1,3]
Output: [1,2,4,5,3]
Input: root = [1]
Output: [1]
```

## Key Takeaways
- Inorder traversal visits the left subtree, the current node, and then the right subtree.
- Recursive and iterative approaches can be used to achieve inorder traversal.
- The time complexity is O(n), where n is the number of nodes in the tree, and the space complexity is O(n) due to the recursive call stack or the explicit stack used in the iterative approach.