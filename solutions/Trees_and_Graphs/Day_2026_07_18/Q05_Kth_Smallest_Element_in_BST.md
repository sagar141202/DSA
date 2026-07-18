# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have at least k nodes. The problem can be solved using an in-order traversal of the tree, which visits the nodes in ascending order. For example, given a BST with the following structure:
```
    5
   / \
  3   6
 / \
2   4
```
And k = 3, the output should be 3, which is the 3rd smallest element in the BST.

## Approach
The algorithm uses a stack-based in-order traversal to visit the nodes in ascending order. It keeps track of the current node and the number of nodes visited so far. When the kth node is visited, its value is returned as the result. The traversal is done using a while loop that continues until the kth node is found.

## Complexity
- Time: O(h + k)
- Space: O(h)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> s;
        TreeNode* curr = root;
        while (curr || !s.empty()) {
            // go as left as possible
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // visit the node
            curr = s.top();
            s.pop();
            k--;
            if (k == 0) {
                return curr->val;
            }
            // go to the right subtree
            curr = curr->right;
        }
        return -1; // not found
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
k = 3
Output: 3
```

## Key Takeaways
- In-order traversal visits nodes in ascending order in a BST.
- Using a stack to implement in-order traversal allows for efficient traversal of the tree.
- Keeping track of the number of nodes visited allows us to find the kth smallest element.