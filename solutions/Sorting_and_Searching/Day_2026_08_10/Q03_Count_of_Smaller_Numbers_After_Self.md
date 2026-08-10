# Count of Smaller Numbers After Self

## Problem Statement
Given an integer array `nums`, return an array of the same length where each element at index `i` represents the number of elements in `nums` to the right of `i` that are smaller than `nums[i]`. The input array will contain between 1 and 10^5 elements, and each element will be between 0 and 10^9. For example, if `nums = [5,2,6,1]`, the output should be `[2,1,1,0]`, because to the right of `5` there are 2 elements smaller, to the right of `2` there is 1 element smaller, to the right of `6` there is 1 element smaller, and to the right of `1` there are no elements smaller.

## Approach
The approach involves using a Binary Indexed Tree (BIT) to keep track of the count of smaller elements as we iterate through the array from right to left. We will use the BIT to query the count of elements smaller than the current element and update the BIT after each query.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class BIT {
public:
    vector<int> tree;
    int n;

    BIT(int n) : n(n), tree(n + 1, 0) {}

    void update(int i, int val) {
        while (i <= n) {
            tree[i] += val;
            i += i & -i;
        }
    }

    int query(int i) {
        int sum = 0;
        while (i > 0) {
            sum += tree[i];
            i -= i & -i;
        }
        return sum;
    }
};

vector<int> countSmaller(vector<int>& nums) {
    vector<int> rank;
    for (int num : nums) rank.push_back(num);
    sort(rank.begin(), rank.end());
    rank.erase(unique(rank.begin(), rank.end()), rank.end());

    int n = nums.size();
    vector<int> res(n);
    BIT bit(rank.size());
    for (int i = n - 1; i >= 0; --i) {
        int idx = lower_bound(rank.begin(), rank.end(), nums[i]) - rank.begin() + 1;
        res[i] = bit.query(idx - 1);
        bit.update(idx, 1);
    }
    return res;
}
```

## Test Cases
```
Input: [5,2,6,1]
Output: [2,1,1,0]
Input: [1,2,3,4,5]
Output: [0,0,0,0,0]
```

## Key Takeaways
- We use a Binary Indexed Tree to efficiently query and update the count of smaller elements.
- The time complexity is O(n log n) due to the BIT operations and sorting.
- The space complexity is O(n) for storing the BIT and the output array.