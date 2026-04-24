# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to find the count of smaller numbers after self for each element in the array. This means that for each element at index `i`, you need to find the count of elements at indices `j` where `j > i` and `nums[j] < nums[i]`. The function should return an array of the same length as `nums`, where each element at index `i` is the count of smaller numbers after self for the corresponding element in `nums`. The array `nums` contains only distinct integers, and its length is in the range `[1, 10^5]`.

## Approach
The approach is to use a modified merge sort algorithm to count the smaller numbers after self. We will recursively divide the array into two halves until we reach the base case, and then merge the halves while counting the smaller numbers.

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
        vector<pair<int, int>> temp(n);
        
        for (int i = 0; i < n; i++) {
            temp[i] = {nums[i], i};
        }
        
        mergeSort(temp, 0, n - 1, result);
        
        return result;
    }
    
    void mergeSort(vector<pair<int, int>>& nums, int start, int end, vector<int>& result) {
        if (start >= end) return;
        
        int mid = start + (end - start) / 2;
        
        mergeSort(nums, start, mid, result);
        mergeSort(nums, mid + 1, end, result);
        
        merge(nums, start, mid, end, result);
    }
    
    void merge(vector<pair<int, int>>& nums, int start, int mid, int end, vector<int>& result) {
        vector<pair<int, int>> left(nums.begin() + start, nums.begin() + mid + 1);
        vector<pair<int, int>> right(nums.begin() + mid + 1, nums.begin() + end + 1);
        
        int i = 0, j = 0, k = start;
        
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
Input: nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```

## Key Takeaways
- We use a modified merge sort algorithm to count the smaller numbers after self.
- The time complexity of the solution is O(n log n), where n is the length of the input array.
- The space complexity of the solution is O(n), where n is the length of the input array.