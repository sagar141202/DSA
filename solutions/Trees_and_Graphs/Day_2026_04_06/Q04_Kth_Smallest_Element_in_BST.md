# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST contains unique integers and is guaranteed to have at least k nodes. For example, if the input BST is [5,3,6,2,4,null,null,1] and k = 3, the output should be 3, which is the 3rd smallest element in the BST.

## Approach
We can solve this problem by using an in-order traversal of the BST, which visits nodes in ascending order. We keep track of the current node index and return the node's value when the index reaches k. This approach takes advantage of the BST property, where the left subtree of a node contains smaller values and the right subtree contains larger values.

## Complexity
- Time: O(h + k), where h is the height of the tree
- Space: O(h), due to the recursive call stack

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
        while (root || !st.empty()) {
            while (root) {
                st.push(root);
                root = root->left;
            }
            root = st.top();
            st.pop();
            k--;
            if (k == 0) return root->val;
            root = root->right;
        }
        return -1; // not found
    }
};
```

## Test Cases
```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

## Key Takeaways
- Use in-order traversal to visit nodes in ascending order
- Keep track of the current node index to find the kth smallest element
- Utilize a stack to implement iterative in-order traversal and avoid recursion