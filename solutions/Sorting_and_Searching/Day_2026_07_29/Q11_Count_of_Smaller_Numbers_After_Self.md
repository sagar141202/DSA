# Count of Smaller Numbers After Self

## Problem Statement
Given an array of integers `nums`, return an array of the same length where each element at index `i` represents the number of elements in `nums` that are to the right of `i` and are smaller than `nums[i]`. The input array will have a length of at most 10000 and will contain only non-negative integers.

## Approach
We can use a modified merge sort algorithm to count the smaller numbers after self. The idea is to divide the array into two halves, recursively count the smaller numbers in each half, and then merge the two halves while counting the smaller numbers that are to the right of each element.

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
        vector<int> values = nums;
        mergeSort(values, 0, nums.size() - 1, result, nums);
        return result;
    }
    
    void mergeSort(vector<int>& values, int start, int end, vector<int>& result, vector<int>& nums) {
        if (start >= end) return;
        
        int mid = start + (end - start) / 2;
        mergeSort(values, start, mid, result, nums);
        mergeSort(values, mid + 1, end, result, nums);
        
        merge(values, start, mid, end, result, nums);
    }
    
    void merge(vector<int>& values, int start, int mid, int end, vector<int>& result, vector<int>& nums) {
        vector<int> left(values.begin() + start, values.begin() + mid + 1);
        vector<int> right(values.begin() + mid + 1, values.begin() + end + 1);
        
        int i = 0, j = 0, k = start;
        while (i < left.size() && j < right.size()) {
            if (left[i] <= right[j]) {
                values[k++] = left[i];
                result[nums[k - 1]] += j;
                i++;
            } else {
                values[k++] = right[j];
                j++;
            }
        }
        
        while (i < left.size()) {
            values[k++] = left[i];
            result[nums[k - 1]] += j;
            i++;
        }
        
        while (j < right.size()) {
            values[k++] = right[j];
            j++;
        }
    }
};

```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```

## Key Takeaways
- The key to solving this problem is to use a modified merge sort algorithm that counts the smaller numbers after self.
- The time complexity of this solution is O(n log n) due to the merge sort algorithm.
- The space complexity of this solution is O(n) for the auxiliary arrays used in the merge sort algorithm.