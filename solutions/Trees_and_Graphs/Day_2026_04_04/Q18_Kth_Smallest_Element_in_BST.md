# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have a total of n nodes, and the nodes are numbered from 1 to n in in-order traversal. You should return the kth smallest element, where k is 1-indexed.

## Approach
The approach is to use in-order traversal of the BST, which visits nodes in ascending order. We can use a recursive or iterative method to perform the traversal and keep track of the current node index.

## Complexity
- Time: O(n)
- Space: O(h), where h is the height of the BST

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
    int kthSmallest(TreeNode* root, int k) {
        // Initialize a stack to store nodes for in-order traversal
        stack<TreeNode*> st;
        TreeNode* current = root;
        
        // Traverse the BST and keep track of the current node index
        while (current || !st.empty()) {
            // Go as far left as possible
            while (current) {
                st.push(current);
                current = current->left;
            }
            
            // Visit the current node
            current = st.top();
            st.pop();
            k--;
            
            // If we've visited k nodes, return the current node's value
            if (k == 0) {
                return current->val;
            }
            
            // Move to the right subtree
            current = current->right;
        }
        
        // If we've reached this point, the kth smallest element does not exist
        return -1;
    }
};
```

## Test Cases
```
Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

## Key Takeaways
- In-order traversal visits nodes in ascending order in a BST.
- We can use a stack to implement in-order traversal iteratively.
- Keep track of the current node index to find the kth smallest element.