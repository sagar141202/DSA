# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. For example, given the binary tree `[4,2,5,1,3]`, the inorder traversal is `[1,2,3,4,5]`. The binary tree node has a value and two children: `left` and `right`. The constraints are that the number of nodes in the tree is in the range `[0, 100]`, and `-100 <= Node.val <= 100`.

## Approach
The algorithm uses a recursive or iterative approach to traverse the binary tree, visiting the left subtree, the current node, and then the right subtree. This ensures that nodes are visited in ascending order. The solution utilizes a stack data structure for the iterative approach.

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
        stack<TreeNode*> s;
        TreeNode* current = root;
        
        while (current || !s.empty()) {
            // Traverse to the leftmost node
            while (current) {
                s.push(current);
                current = current->left;
            }
            
            // Backtrack and visit the node
            current = s.top();
            s.pop();
            result.push_back(current->val);
            
            // Move to the right subtree
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
Input: []
Output: []
```

## Key Takeaways
- Inorder traversal visits nodes in ascending order for a binary search tree.
- Recursive and iterative approaches can be used to solve the problem, with the iterative approach using a stack to simulate recursion.
- The time complexity is O(n), where n is the number of nodes, and the space complexity is O(n) due to the recursive call stack or the explicit stack used in the iterative approach.