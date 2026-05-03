# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have at least k nodes. For example, if the input BST is: 
       5
      / \
     3   6
    / \
   2   4
  /
 1
and k = 3, the output should be 3, which is the 3rd smallest element in the BST.

## Approach
We can solve this problem using an in-order traversal of the BST, which visits nodes in ascending order. We will keep track of the number of nodes visited and return the kth node. The algorithm will use a stack to perform the in-order traversal efficiently.

## Complexity
- Time: O(h + k), where h is the height of the BST
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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
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
            // backtracking
            curr = st.top();
            st.pop();
            k--;
            if (k == 0) {
                return curr->val;
            }
            curr = curr->right;
        }
        return -1; // this line will never be reached
    }
};
```

## Test Cases
```
Input: root = [5,3,6,2,4,1], k = 3
Output: 3
Input: root = [5,3,6,2,4,1], k = 1
Output: 1
```

## Key Takeaways
- The in-order traversal of a BST visits nodes in ascending order.
- Using a stack to perform the in-order traversal allows us to efficiently traverse the tree without using recursion.
- The time complexity is O(h + k) because we may need to traverse up to the height of the tree (h) before finding the kth smallest element.