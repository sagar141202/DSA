# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to find the count of smaller numbers after self for each element in the array. The count of smaller numbers after self for an element at index `i` is the number of elements in the array to the right of `i` that are smaller than `nums[i]`. Return an array of these counts. The input array will have a length between 1 and 200, and the elements will be between 0 and 10^4. For example, given the input `[5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]`, because to the right of 5, there are 2 numbers smaller than 5, to the right of 2, there is 1 number smaller than 2, and so on.

## Approach
The approach to solve this problem is to use a binary indexed tree (also known as a Fenwick tree) to keep track of the cumulative count of smaller numbers. We can iterate over the array from right to left, for each element, we can query the binary indexed tree to get the count of smaller numbers.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> res(nums.size());
        vector<int> rank = nums;
        sort(rank.begin(), rank.end());
        for (int i = 0; i < nums.size(); i++) {
            auto it = lower_bound(rank.begin(), rank.end(), nums[i]);
            res[i] = it - rank.begin();
        }
        vector<int> ans(nums.size());
        for (int i = nums.size() - 1; i >= 0; i--) {
            ans[i] = query(res[i] - 1);
            update(res[i]);
        }
        return ans;
    }
    
    int query(int i) {
        int sum = 0;
        while (i >= 0) {
            sum += tree[i];
            i = (i & (i + 1)) - 1;
        }
        return sum;
    }
    
    void update(int i) {
        while (i < tree.size()) {
            tree[i]++;
            i = i | (i + 1);
        }
    }
    
    vector<int> tree;
    Solution() {
        tree.resize(20001, 0);
    }
};
```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Input: [1, 2, 3]
Output: [0, 0, 0]
```

## Key Takeaways
- We can use a binary indexed tree to efficiently query the count of smaller numbers.
- The `lower_bound` function can be used to find the rank of each element in the sorted array.
- The `query` and `update` functions are used to query and update the binary indexed tree respectively.