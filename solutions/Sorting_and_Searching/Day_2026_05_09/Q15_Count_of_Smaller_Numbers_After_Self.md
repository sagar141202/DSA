# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`. For each element in the array, count the number of smaller elements on its right side and return the count for each element. The length of the array is at most 500. The array elements are in the range [0, 10^9]. For example, given the array `nums = [5, 2, 6, 1]`, the function should return `[2, 1, 1, 0]` because there are 2 numbers smaller than 5 on its right side, 1 number smaller than 2 on its right side, 1 number smaller than 6 on its right side, and 0 numbers smaller than 1 on its right side.

## Approach
The approach is to use the concept of Binary Indexed Tree (BIT) or Fenwick Tree to efficiently count the number of smaller elements. We first create a sorted copy of the input array and then for each element in the original array, we find its index in the sorted array and use the BIT to count the number of smaller elements.

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
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            int index = lower_bound(sortedNums.begin(), sortedNums.end(), nums[i]) - sortedNums.begin();
            result.push_back(index);
            sortedNums.erase(sortedNums.begin() + index);
        }
        return result;
    }
};

class BIT {
public:
    vector<int> tree;
    int n;
    BIT(int n) {
        this->n = n;
        tree.resize(n + 1);
    }
    void update(int i, int val) {
        while (i <= n) {
            tree[i] += val;
            i += (i & -i);
        }
    }
    int query(int i) {
        int sum = 0;
        while (i > 0) {
            sum += tree[i];
            i -= (i & -i);
        }
        return sum;
    }
};

class Solution2 {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> rank = nums;
        sort(rank.begin(), rank.end());
        map<int, int> map;
        for (int i = 0; i < rank.size(); i++) {
            map[rank[i]] = i + 1;
        }
        BIT bit(nums.size() + 1);
        vector<int> result(nums.size());
        for (int i = nums.size() - 1; i >= 0; i--) {
            result[i] = bit.query(map[nums[i]] - 1);
            bit.update(map[nums[i]], 1);
        }
        return result;
    }
};
```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Input: [1, 2, 3, 4]
Output: [0, 0, 0, 0]
```

## Key Takeaways
- Use Binary Indexed Tree (BIT) or Fenwick Tree to efficiently count the number of smaller elements.
- Create a sorted copy of the input array to find the rank of each element.
- Use a map to store the rank of each element for efficient lookup.