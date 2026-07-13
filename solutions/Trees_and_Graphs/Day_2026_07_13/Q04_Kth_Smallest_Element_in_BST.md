# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have k nodes. If there are multiple kth smallest elements, return any of them. The input tree is non-empty and the value of k is between 1 and the number of nodes in the tree.

## Approach
We can solve this problem using an in-order traversal of the BST, which visits nodes in ascending order. We will use a stack to perform the in-order traversal iteratively. When we visit the kth node, we return its value as the kth smallest element.

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
        while (root || !st.empty()) {
            // Go as left as possible
            while (root) {
                st.push(root);
                root = root->left;
            }
            // Backtrack and visit the node
            root = st.top();
            st.pop();
            k--;
            if (k == 0) return root->val;
            // Move to the right subtree
            root = root->right;
        }
        return -1; // Not found
    }
};

int main() {
    // Example usage
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(3);
    root->right = new TreeNode(6);
    root->left->left = new TreeNode(2);
    root->left->right = new TreeNode(4);
    root->left->left->left = new TreeNode(1);
    Solution solution;
    cout << solution.kthSmallest(root, 3) << endl;  // Output: 3
    return 0;
}
```

## Test Cases
```
Input: root = [5,3,6,2,4,1], k = 3
Output: 3
Input: root = [5,3,6,2,4,1], k = 1
Output: 1
```

## Key Takeaways
- Use in-order traversal to visit nodes in ascending order.
- Use a stack to perform the in-order traversal iteratively.
- Keep track of the number of visited nodes to find the kth smallest element.