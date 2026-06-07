# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to find the count of smaller numbers after self for each element in the array. The count of smaller numbers after self for an element at index `i` is the number of elements in the array to the right of `i` (i.e., `nums[j]` where `j > i`) that are smaller than `nums[i]`. The problem requires you to return an array of counts, where the count at index `i` is the count of smaller numbers after self for the element at index `i` in the input array. The input array contains distinct integers, and its length is between 1 and 200.

## Approach
The approach involves using a modified merge sort algorithm to count the inversions in the array, which represent the count of smaller numbers after self. The merge sort algorithm is modified to count the inversions while merging the two halves of the array. The time complexity of this approach is O(n log n) due to the merge sort.

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
        vector<pair<int, int>> arr;
        
        // Create an array of pairs where each pair contains the value and its original index
        for (int i = 0; i < nums.size(); i++) {
            arr.push_back({nums[i], i});
        }
        
        // Call the modified merge sort function to count the inversions
        mergeSort(arr, result);
        
        return result;
    }
    
    // Modified merge sort function to count the inversions
    void mergeSort(vector<pair<int, int>>& arr, vector<int>& result) {
        if (arr.size() <= 1) {
            return;
        }
        
        int mid = arr.size() / 2;
        vector<pair<int, int>> left(arr.begin(), arr.begin() + mid);
        vector<pair<int, int>> right(arr.begin() + mid, arr.end());
        
        mergeSort(left, result);
        mergeSort(right, result);
        
        merge(left, right, arr, result);
    }
    
    // Merge two sorted arrays and count the inversions
    void merge(vector<pair<int, int>>& left, vector<pair<int, int>>& right, vector<pair<int, int>>& arr, vector<int>& result) {
        int i = 0, j = 0, k = 0;
        
        while (i < left.size() && j < right.size()) {
            if (left[i].first <= right[j].first) {
                arr[k++] = left[i];
                i++;
            } else {
                arr[k++] = right[j];
                // Count the inversions
                for (int x = i; x < left.size(); x++) {
                    result[left[x].second]++;
                }
                j++;
            }
        }
        
        while (i < left.size()) {
            arr[k++] = left[i];
            i++;
        }
        
        while (j < right.size()) {
            arr[k++] = right[j];
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
- The problem can be solved using a modified merge sort algorithm to count the inversions in the array.
- The time complexity of the approach is O(n log n) due to the merge sort.
- The space complexity is O(n) for storing the input array and the result array.