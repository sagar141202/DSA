# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree node has a value, a left child, and a right child. For example, given the following binary tree: 
       4
     /   \
    2     6
   / \   / \
  1   3 5   7
The inorder traversal is [1, 2, 3, 4, 5, 6, 7]. The input is the root of the binary tree and the output is a vector of integers representing the inorder traversal. The tree has at most 100 nodes and the values of the nodes are between 1 and 100.

## Approach
The algorithm uses a recursive or iterative approach to traverse the binary tree in inorder. It first visits the left subtree, then the current node, and finally the right subtree. The base case for recursion is when the current node is null. For iteration, a stack is used to store nodes to be visited.

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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> st;
        TreeNode* curr = root;
        while (curr != NULL || !st.empty()) {
            // Reach the leftmost node
            while (curr != NULL) {
                st.push(curr);
                curr = curr->left;
            }
            // Backtrack and visit the node
            curr = st.top();
            st.pop();
            res.push_back(curr->val);
            // Move to the right subtree
            curr = curr->right;
        }
        return res;
    }
};
```

## Test Cases
```
Input: 
   4
 /   \
2     6
/ \   / \
1   3 5   7
Output: [1, 2, 3, 4, 5, 6, 7]
Input: 
  1
   \
    2
     \
      3
Output: [1, 2, 3]
```

## Key Takeaways
- Use a stack to store nodes to be visited for iterative inorder traversal.
- The time complexity is O(n) where n is the number of nodes in the binary tree.
- The space complexity is O(n) due to the recursive call stack or the explicit stack used for iteration.