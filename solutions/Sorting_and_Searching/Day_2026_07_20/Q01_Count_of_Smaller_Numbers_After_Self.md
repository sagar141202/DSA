# Count of Smaller Numbers After Self

## Problem Statement
Given an array of integers, return an array where each element at index `i` represents the number of elements to its right that are smaller than the element at index `i`. The input array will contain between 1 and 10^5 elements, each between 0 and 10^9. For example, given the input `[5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]`, because there are 2 elements smaller than 5 to its right, 1 element smaller than 2, 1 element smaller than 6, and no elements smaller than 1.

## Approach
We can use a Binary Indexed Tree (BIT) to efficiently count the smaller numbers. The idea is to iterate through the array from right to left, and for each element, use the BIT to count the number of smaller elements to its right. We can also use a modified merge sort to achieve the same result.

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
        int n = nums.size();
        vector<int> res(n);
        vector<int> indexedNums(n);
        for (int i = 0; i < n; i++) {
            indexedNums[i] = nums[i];
        }
        sort(indexedNums.begin(), indexedNums.end());
        for (int i = 0; i < n; i++) {
            nums[i] = lower_bound(indexedNums.begin(), indexedNums.end(), nums[i]) - indexedNums.begin() + 1;
        }
        vector<int> bit(n + 1);
        for (int i = n - 1; i >= 0; i--) {
            res[i] = query(bit, nums[i] - 1);
            update(bit, nums[i]);
        }
        return res;
    }

    void update(vector<int>& bit, int i) {
        while (i < bit.size()) {
            bit[i]++;
            i += i & -i;
        }
    }

    int query(vector<int>& bit, int i) {
        int sum = 0;
        while (i > 0) {
            sum += bit[i];
            i -= i & -i;
        }
        return sum;
    }
};

```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Input: [1, 2, 3, 4, 5]
Output: [0, 0, 0, 0, 0]
```

## Key Takeaways
- The Binary Indexed Tree (BIT) is a useful data structure for range sum queries and updates.
- The `lower_bound` function can be used to find the index of the first occurrence of a value in a sorted array.
- The `update` and `query` operations in the BIT have a time complexity of O(log n).