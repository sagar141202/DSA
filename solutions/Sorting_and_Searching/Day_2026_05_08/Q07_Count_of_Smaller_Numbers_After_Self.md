# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to find the count of smaller numbers after self for each element in the array. This means that for each element at index `i`, you need to count the number of elements at indices `j > i` that are smaller than `nums[i]`. The function should return an array of these counts. For example, given the input `[5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]`. The constraints are that the length of the input array is between 1 and 10^5, and each element in the array is between 0 and 10^9.

## Approach
The approach is to use a Binary Indexed Tree (BIT) to keep track of the count of smaller numbers. We first sort the input array and assign ranks to each number. Then, we iterate through the array from right to left, using the BIT to count the number of smaller elements.

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
    vector<int> sorted = nums;
    sort(sorted.begin(), sorted.end());
    unordered_map<int, int> ranks;
    int rank = 1;
    for (int i = 0; i < sorted.size(); i++) {
        if (i > 0 && sorted[i] != sorted[i - 1]) {
            rank++;
        }
        ranks[sorted[i]] = rank;
    }

    BIT bit(sorted.size() + 1);
    vector<int> result(nums.size());
    for (int i = nums.size() - 1; i >= 0; i--) {
        result[i] = bit.query(ranks[nums[i]] - 1);
        bit.update(ranks[nums[i]], 1);
    }
    return result;
}
```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Input: [1, 2, 3, 4, 5]
Output: [0, 0, 0, 0, 0]
```

## Key Takeaways
- The Binary Indexed Tree (BIT) data structure is useful for range sum queries and updates.
- The rank assignment step is crucial to ensure that the BIT works correctly with duplicate elements.
- The time complexity is O(n log n) due to the sorting step, while the space complexity is O(n) for the BIT and the output array.