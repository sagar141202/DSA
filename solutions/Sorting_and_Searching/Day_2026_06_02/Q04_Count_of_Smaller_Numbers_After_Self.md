# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to find the count of smaller numbers after self for each element in the array. For an element at index `i`, the count of smaller numbers after self is the number of elements in the array to the right of `i` (i.e., `nums[j]` where `j > i`) that are smaller than `nums[i]`. The function should return an array of integers where the `i-th` integer represents the count of smaller numbers after self for `nums[i]`. The input array `nums` contains only distinct integers and has a length between 1 and 20000. For example, given the input `nums = [5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]`.

## Approach
The approach is to use a Binary Indexed Tree (BIT) to keep track of the count of smaller numbers. We iterate through the array from right to left, maintaining a sorted array of the elements we have seen so far. For each element, we use the BIT to count the number of smaller elements to its right.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class BinaryIndexedTree {
public:
    vector<int> tree;
    int size;

    BinaryIndexedTree(int n) {
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
    vector<int> ranks(nums.begin(), nums.end());
    sort(ranks.begin(), ranks.end());
    unordered_map<int, int> rankMap;
    for (int i = 0; i < ranks.size(); i++) {
        rankMap[ranks[i]] = i + 1;
    }

    BinaryIndexedTree bit(nums.size());
    vector<int> result(nums.size());
    for (int i = nums.size() - 1; i >= 0; i--) {
        result[i] = bit.query(rankMap[nums[i]] - 1);
        bit.update(rankMap[nums[i]], 1);
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
- Use of Binary Indexed Tree to efficiently count the number of smaller elements.
- Utilize an unordered map to store the rank of each element in the sorted array.
- The solution has a time complexity of O(n log n) due to the sorting and BIT operations.