# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`. For each element in the array, count the number of smaller elements on its right side. Return the count array. The length of the input array will not exceed 1000. The range of the elements in the input array is between 0 and 10^9. For example, given the array `[5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]`.

## Approach
We can use a modified merge sort algorithm to count the smaller numbers. The idea is to divide the array into two halves, count the smaller numbers in each half, and then merge the results. This approach takes advantage of the fact that the smaller numbers are already counted in the sorted subarrays.

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
        vector<int> result(nums.size(), 0);
        vector<pair<int, int>> sortedNums;
        
        for (int i = 0; i < nums.size(); i++) {
            sortedNums.push_back({nums[i], i});
        }
        
        mergeSort(sortedNums, result);
        
        return result;
    }
    
    void mergeSort(vector<pair<int, int>>& nums, vector<int>& result) {
        if (nums.size() <= 1) return;
        
        int mid = nums.size() / 2;
        vector<pair<int, int>> left(nums.begin(), nums.begin() + mid);
        vector<pair<int, int>> right(nums.begin() + mid, nums.end());
        
        mergeSort(left, result);
        mergeSort(right, result);
        
        merge(left, right, nums, result);
    }
    
    void merge(vector<pair<int, int>>& left, vector<pair<int, int>>& right, vector<pair<int, int>>& nums, vector<int>& result) {
        int i = 0, j = 0, k = 0;
        
        while (i < left.size() && j < right.size()) {
            if (left[i].first <= right[j].first) {
                result[left[i].second] += j;
                nums[k++] = left[i++];
            } else {
                nums[k++] = right[j++];
            }
        }
        
        while (i < left.size()) {
            result[left[i].second] += j;
            nums[k++] = left[i++];
        }
        
        while (j < right.size()) {
            nums[k++] = right[j++];
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
- The problem can be solved using a modified merge sort algorithm.
- The merge sort algorithm is used to divide the array into two halves, count the smaller numbers in each half, and then merge the results.
- The time complexity of the solution is O(n log n) due to the merge sort algorithm.