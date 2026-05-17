# Count of Smaller Numbers After Self

## Problem Statement
Given an array of integers `nums`, return an array of the same length where each element at index `i` represents the number of elements in `nums` that are to the right of `i` and are smaller than `nums[i]`. The input array `nums` will contain at least one element and at most 10000 elements. Each element in `nums` will be between 0 and 10000.

## Approach
We will utilize a Binary Indexed Tree (BIT) to keep track of the cumulative count of elements smaller than each element in the array. The algorithm iterates through the array from right to left, updating the BIT and calculating the count of smaller numbers for each element.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class FenwickTree {
public:
    vector<int> tree;
    int n;

    FenwickTree(int n) {
        this->n = n;
        tree.resize(n + 1, 0);
    }

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
    vector<int> sortedNums = nums;
    sort(sortedNums.begin(), sortedNums.end());
    map<int, int> rank;
    int unique = 0;
    for (int num : sortedNums) {
        if (rank.find(num) == rank.end()) {
            rank[num] = ++unique;
        }
    }

    FenwickTree ft(unique);
    vector<int> result(nums.size());
    for (int i = nums.size() - 1; i >= 0; --i) {
        result[i] = ft.query(rank[nums[i]] - 1);
        ft.update(rank[nums[i]], 1);
    }
    return result;
}
```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```

## Key Takeaways
- Utilize a Binary Indexed Tree (BIT) to efficiently calculate the cumulative count of elements smaller than each element.
- Sort the input array to determine the rank of each element and update the BIT accordingly.
- Iterate through the array from right to left to ensure accurate counts of smaller numbers for each element.