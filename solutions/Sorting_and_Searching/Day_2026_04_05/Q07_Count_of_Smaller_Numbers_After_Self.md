# Count of Smaller Numbers After Self

## Problem Statement
Given an array of integers, return the count of smaller numbers after self for each element in the array. The count of smaller numbers after self for an element at index `i` is the number of elements at indices `j` such that `j > i` and `nums[j] < nums[i]`. The array contains distinct integers, and the length of the array is between 1 and 10^5.

## Approach
The approach involves using a Binary Indexed Tree (BIT) to keep track of the count of smaller numbers. We iterate over the array from right to left, and for each element, we query the BIT to get the count of smaller numbers. We then update the BIT with the current element.

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
        vector<int> result(nums.size());
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        for (int i = nums.size() - 1; i >= 0; i--) {
            int index = lower_bound(sortedNums.begin(), sortedNums.end(), nums[i]) - sortedNums.begin();
            result[i] = index;
            sortedNums.erase(sortedNums.begin() + index);
        }
        return result;
    }
};

class Solution2 {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> result(nums.size());
        vector<int> index(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            index[i] = i;
        }
        mergeSort(index, 0, nums.size() - 1, nums, result);
        return result;
    }

    void mergeSort(vector<int>& index, int start, int end, vector<int>& nums, vector<int>& result) {
        if (start >= end) return;
        int mid = start + (end - start) / 2;
        mergeSort(index, start, mid, nums, result);
        mergeSort(index, mid + 1, end, nums, result);
        merge(index, start, mid, end, nums, result);
    }

    void merge(vector<int>& index, int start, int mid, int end, vector<int>& nums, vector<int>& result) {
        vector<int> left(index.begin() + start, index.begin() + mid + 1);
        vector<int> right(index.begin() + mid + 1, index.begin() + end + 1);
        int i = 0, j = 0, k = start;
        while (i < left.size() && j < right.size()) {
            if (nums[left[i]] <= nums[right[j]]) {
                index[k++] = left[i++];
                result[left[i - 1]] += j;
            } else {
                index[k++] = right[j++];
            }
        }
        while (i < left.size()) {
            index[k++] = left[i++];
            result[left[i - 1]] += j;
        }
        while (j < right.size()) {
            index[k++] = right[j++];
        }
    }
};
```

## Test Cases
```
Input: [5,2,6,1]
Output: [2,1,1,0]
```

## Key Takeaways
- We can use a modified merge sort to solve this problem efficiently.
- The Binary Indexed Tree (BIT) can be used to keep track of the count of smaller numbers.
- The time complexity of the solution is O(n log n) due to the merge sort operation.