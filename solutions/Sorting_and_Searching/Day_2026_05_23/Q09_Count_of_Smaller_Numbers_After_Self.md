# Count of Smaller Numbers After Self

## Problem Statement
Given an array of integers, return an array where each element at index i represents the number of smaller elements to its right. The given array will have a length between 1 and 10^5, and the elements will be between 0 and 10^4. For example, if the input is [5, 2, 6, 1], the output should be [2, 1, 1, 0], because to the right of 5, there are 2 smaller numbers (2 and 1), to the right of 2, there is 1 smaller number (1), to the right of 6, there is 1 smaller number (1), and to the right of 1, there are no smaller numbers.

## Approach
We can use a Binary Indexed Tree (BIT) to efficiently count the number of smaller elements to the right of each element. The algorithm involves iterating over the array from right to left and using the BIT to query the number of smaller elements.

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
    int size;

    BIT(int n) {
        size = n;
        tree.resize(n + 1);
    }

    void update(int i, int val) {
        while (i <= size) {
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
    vector<int> rank(nums.begin(), nums.end());
    sort(rank.begin(), rank.end());
    rank.erase(unique(rank.begin(), rank.end()), rank.end());

    int n = nums.size();
    vector<int> res(n);
    BIT bit(rank.size() + 1);

    for (int i = n - 1; i >= 0; --i) {
        int r = lower_bound(rank.begin(), rank.end(), nums[i]) - rank.begin() + 1;
        res[i] = bit.query(r - 1);
        bit.update(r, 1);
    }

    return res;
}
```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Input: [1, 2, 3, 4]
Output: [0, 0, 0, 0]
```

## Key Takeaways
- The Binary Indexed Tree data structure can be used for efficient range queries and updates.
- The `lower_bound` function can be used to find the insertion point for a target value in a sorted array.
- The `unique` function can be used to remove duplicates from a sorted array.