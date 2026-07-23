# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`. For each element in the array, count the number of smaller elements to its right. Return an array where each element at index `i` represents the count of smaller numbers after `nums[i]`. The length of the input array will be between 1 and 20000. Each integer in the input array will be between 0 and 10000. For example, given the array `[5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]`, because to the right of `5`, there are `2` numbers smaller than `5` (i.e., `2` and `1`). To the right of `2`, there is `1` number smaller than `2` (i.e., `1`). To the right of `6`, there is `1` number smaller than `6` (i.e., `1`). To the right of `1`, there are `0` numbers smaller than `1`.

## Approach
We can solve this problem by using a modified merge sort algorithm, where we count the number of smaller elements to the right of each element during the merge process. This approach ensures that we only need to traverse the array once. The key insight is to compare elements from the right half with elements from the left half during merging.

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
        vector<int> result(n);
        vector<int> indexes(n);
        for (int i = 0; i < n; i++) {
            indexes[i] = i;
        }
        mergeSort(nums, indexes, result, 0, n - 1);
        return result;
    }

    void mergeSort(vector<int>& nums, vector<int>& indexes, vector<int>& result, int start, int end) {
        if (start >= end) return;
        int mid = start + (end - start) / 2;
        mergeSort(nums, indexes, result, start, mid);
        mergeSort(nums, indexes, result, mid + 1, end);
        merge(nums, indexes, result, start, mid, end);
    }

    void merge(vector<int>& nums, vector<int>& indexes, vector<int>& result, int start, int mid, int end) {
        vector<int> left(indexes.begin() + start, indexes.begin() + mid + 1);
        vector<int> right(indexes.begin() + mid + 1, indexes.begin() + end + 1);
        int i = 0, j = 0, k = start;
        while (i < left.size() && j < right.size()) {
            if (nums[left[i]] <= nums[right[j]]) {
                result[left[i]] += j;
                indexes[k++] = left[i++];
            } else {
                indexes[k++] = right[j++];
            }
        }
        while (i < left.size()) {
            result[left[i]] += j;
            indexes[k++] = left[i++];
        }
        while (j < right.size()) {
            indexes[k++] = right[j++];
        }
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
- The problem can be solved using a modified merge sort algorithm to count the number of smaller elements to the right of each element.
- The time complexity is O(n log n) due to the merge sort, and the space complexity is O(n) for the auxiliary arrays.
- This approach avoids unnecessary comparisons and ensures an efficient solution.