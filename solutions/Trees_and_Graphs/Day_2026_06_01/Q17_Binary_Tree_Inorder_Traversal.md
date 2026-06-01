# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree node has a value, a left child, and a right child. Constraints: The number of nodes in the tree is in the range [0, 100]. -100 <= Node.val <= 100. Examples: Input: root = [4,2,5,1,3], Output: [1,2,3,4,5]. Input: root = [1], Output: [1].

## Approach
The algorithm uses a recursive or iterative approach to traverse the binary tree in an inorder manner. It first visits the left subtree, then the current node, and finally the right subtree. This process is repeated for all nodes in the tree. The result is a list of node values in ascending order.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <iostream>
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
        // recursive helper function to perform inorder traversal
        helper(root, result);
        return result;
    }
    
    void helper(TreeNode* node, vector<int>& result) {
        if (node == nullptr) {
            return;
        }
        // visit left subtree
        helper(node->left, result);
        // visit current node
        result.push_back(node->val);
        // visit right subtree
        helper(node->right, result);
    }
};

// iterative solution
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> stack;
        TreeNode* current = root;
        
        while (current != nullptr || !stack.empty()) {
            // go as far left as possible, pushing nodes onto stack
            while (current != nullptr) {
                stack.push(current);
                current = current->left;
            }
            // visit node at top of stack
            current = stack.top();
            stack.pop();
            result.push_back(current->val);
            // move to right subtree
            current = current->right;
        }
        return result;
    }
};
```

## Test Cases
```
Input: [4,2,5,1,3]
Output: [1,2,3,4,5]
Input: [1]
Output: [1]
```

## Key Takeaways
- Inorder traversal visits nodes in ascending order for a binary search tree.
- Recursive and iterative solutions can be used to implement inorder traversal.
- The time complexity is O(n) where n is the number of nodes in the tree.