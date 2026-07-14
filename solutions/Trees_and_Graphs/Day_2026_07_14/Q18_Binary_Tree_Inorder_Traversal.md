# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, then the current node, and finally the right subtree. The binary tree node has a value, a left child node, and a right child node. Constraints: The number of nodes in the tree is in the range [0, 100]. -100 <= Node.val <= 100.

## Approach
The algorithm uses a recursive or iterative approach to traverse the binary tree, visiting the left subtree, the current node, and the right subtree in order. This can be achieved by using a stack to store nodes or by recursive function calls.

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
            
            // Visit the node and move to its right subtree
            current = s.top();
            s.pop();
            result.push_back(current->val);
            current = current->right;
        }
        
        return result;
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
- Inorder traversal visits nodes in ascending order for a binary search tree.
- Recursive and iterative approaches can be used, with the iterative approach using a stack to store nodes.
- The time complexity is linear with respect to the number of nodes, and the space complexity is also linear in the worst case due to the use of the stack or recursive call stack.