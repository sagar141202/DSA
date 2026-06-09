# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have at least k nodes. The problem can be solved using an in-order traversal of the tree, which visits nodes in ascending order. The input tree is a binary tree where each node has a unique value, and for each node, all elements in its left subtree are less than the node, and all elements in its right subtree are greater than the node. Examples include finding the 3rd smallest element in a tree with values {5, 3, 7, 2, 4, 6, 8}.

## Approach
The algorithm uses a stack-based in-order traversal to visit nodes in ascending order. It iterates through the tree, pushing left child nodes onto the stack until it reaches a leaf node, then pops nodes off the stack and visits them. This process continues until the kth smallest element is found. The traversal ensures that nodes are visited in ascending order, allowing for efficient identification of the kth smallest element.

## Complexity
- Time: O(h + k)
- Space: O(h)

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
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> st;
        TreeNode* curr = root;
        while (curr || !st.empty()) {
            // Traverse to the leftmost node
            while (curr) {
                st.push(curr);
                curr = curr->left;
            }
            // Visit the node and decrement k
            curr = st.top();
            st.pop();
            k--;
            if (k == 0) return curr->val;
            // Move to the right subtree
            curr = curr->right;
        }
        return -1; // If k is larger than the number of nodes
    }
};
```

## Test Cases
```
Input: root = [5,3,7,2,4,6,8], k = 3
Output: 3
```

## Key Takeaways
- In-order traversal visits nodes in ascending order, making it suitable for finding the kth smallest element.
- Using a stack to store nodes allows for efficient traversal and avoids recursion.
- The time complexity is O(h + k) because in the worst case, we might need to traverse the height of the tree (h) and then visit k nodes.