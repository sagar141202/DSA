# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to return a new array `count` where `count[i]` is the number of smaller elements to the right of `nums[i]`. The length of `nums` is in the range `[1, 100]`, and each integer in `nums` is in the range `[0, 100]`. For example, if `nums = [5, 2, 6, 1]`, then `count = [2, 1, 1, 0]` because there are 2 smaller numbers to the right of `5`, 1 smaller number to the right of `2`, 1 smaller number to the right of `6`, and 0 smaller numbers to the right of `1`.

## Approach
We can use a modified merge sort algorithm to solve this problem. The idea is to divide the array into two halves, recursively count the smaller numbers in each half, and then merge the two halves while counting the smaller numbers. This approach takes advantage of the fact that merge sort is a stable sorting algorithm, which means that the order of equal elements is preserved.

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
        vector<int> count(n);
        vector<pair<int, int>> arr;
        
        // Create a new array with pairs of numbers and their indices
        for (int i = 0; i < n; i++) {
            arr.push_back({nums[i], i});
        }
        
        // Merge sort and count smaller numbers
        mergeSort(arr, count);
        
        return count;
    }
    
    void mergeSort(vector<pair<int, int>>& arr, vector<int>& count) {
        if (arr.size() <= 1) {
            return;
        }
        
        int mid = arr.size() / 2;
        vector<pair<int, int>> left(arr.begin(), arr.begin() + mid);
        vector<pair<int, int>> right(arr.begin() + mid, arr.end());
        
        mergeSort(left, count);
        mergeSort(right, count);
        
        merge(left, right, arr, count);
    }
    
    void merge(vector<pair<int, int>>& left, vector<pair<int, int>>& right, vector<pair<int, int>>& arr, vector<int>& count) {
        int i = 0, j = 0, k = 0;
        
        while (i < left.size() && j < right.size()) {
            if (left[i].first <= right[j].first) {
                // Count smaller numbers
                count[left[i].second] += j;
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }
        
        while (i < left.size()) {
            arr[k++] = left[i++];
        }
        
        while (j < right.size()) {
            arr[k++] = right[j++];
        }
    }
};

```

## Test Cases
```
Input: nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Input: nums = [1, 2, 3, 4]
Output: [0, 0, 0, 0]
```

## Key Takeaways
- The modified merge sort algorithm is used to count smaller numbers to the right of each element in the array.
- The time complexity of the solution is O(n log n) due to the merge sort algorithm.
- The space complexity is O(n) for storing the auxiliary arrays.