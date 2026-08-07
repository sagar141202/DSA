# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have k nodes. The problem can be solved using an in-order traversal of the BST, which visits nodes in ascending order. For example, if the BST is:
       5
      / \
     3   6
    / \
   2   4
  /
 1
And k = 3, the kth smallest element is 3.

## Approach
The algorithm uses a stack to perform an in-order traversal of the BST. It starts by pushing the root node onto the stack and then enters a loop where it pops nodes from the stack, visits them, and pushes their children onto the stack. The kth smallest element is the kth node visited.

## Complexity
- Time: O(h + k), where h is the height of the tree
- Space: O(h), where h is the height of the tree

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
        stack<TreeNode*> st;
        TreeNode* curr = root;
        while (curr || !st.empty()) {
            // go as left as possible
            while (curr) {
                st.push(curr);
                curr = curr->left;
            }
            // visit the top node
            curr = st.top();
            st.pop();
            k--;
            // if this is the kth node, return its value
            if (k == 0) return curr->val;
            // go to the right subtree
            curr = curr->right;
        }
        // if k is not found, return -1
        return -1;
    }
};
```

## Test Cases
```
Input: 
   5
  / \
 3   6
/ \
2   4
/
1
k = 3
Output: 3

Input: 
 2
/ \
1   3
k = 1
Output: 1
```

## Key Takeaways
- Use a stack to perform an in-order traversal of the BST.
- Keep track of the current node and the number of nodes visited.
- The kth smallest element is the kth node visited during the traversal.
- The time complexity is O(h + k), where h is the height of the tree.