# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree node has a value and two children: left and right. The inorder traversal of a binary tree is a list of node values in ascending order if the tree is a binary search tree. For example, given the following binary tree:
       4
     /   \
    2     6
   / \   / \
  1   3 5   7
The inorder traversal is [1, 2, 3, 4, 5, 6, 7]. The constraints are: the number of nodes in the tree is in the range [0, 100], and -100 <= Node.val <= 100.

## Approach
The approach is to use recursion or iteration to traverse the binary tree in an inorder manner. We can use a stack to store nodes that need to be visited. The algorithm starts by pushing the root node onto the stack and then enters a loop where it pops a node, visits it, and pushes its right child onto the stack. If the current node has a left child, the algorithm pushes the left child onto the stack and repeats the process until all nodes have been visited.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <stack>

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
Input: [4, 2, 6, 1, 3, 5, 7]
Output: [1, 2, 3, 4, 5, 6, 7]
```

## Key Takeaways
- Inorder traversal visits the left subtree, the current node, and then the right subtree.
- We can use recursion or iteration to traverse the binary tree in an inorder manner.
- Using a stack to store nodes that need to be visited can simplify the iteration process.