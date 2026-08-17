# Count of Smaller Numbers After Self

## Problem Statement
Given an array of integers, return the count of smaller numbers after self for each element in the array. The count of smaller numbers after self for an element at index `i` is the number of elements at indices `j` such that `j > i` and `nums[j] < nums[i]`. For example, given the array `nums = [5, 2, 6, 1]`, the count of smaller numbers after self would be `[2, 1, 1, 0]`.

## Approach
We can solve this problem using a modified merge sort algorithm, which keeps track of the number of smaller elements as we merge the sorted subarrays. The idea is to count the number of smaller elements for each element in the array as we build the sorted array.

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
        for (int i = 0; i < nums.size(); i++) {
            arr.push_back({nums[i], i});
        }
        mergeSort(arr, result);
        return result;
    }

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

    void merge(vector<pair<int, int>>& left, vector<pair<int, int>>& right, vector<pair<int, int>>& arr, vector<int>& result) {
        int i = 0, j = 0, k = 0;
        while (i < left.size() && j < right.size()) {
            if (left[i].first <= right[j].first) {
                arr[k++] = left[i];
                result[left[i].second] += j;
                i++;
            } else {
                arr[k++] = right[j];
                j++;
            }
        }
        while (i < left.size()) {
            arr[k++] = left[i];
            result[left[i].second] += j;
            i++;
        }
        while (j < right.size()) {
            arr[k++] = right[j];
            j++;
        }
    }
};

// Example usage:
// Solution solution;
// vector<int> nums = {5, 2, 6, 1};
// vector<int> result = solution.countSmaller(nums);
// for (int num : result) {
//     cout << num << " ";
// }
```

## Test Cases
```
Input: nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Input: nums = [1, 2, 3, 4, 5]
Output: [0, 0, 0, 0, 0]
```

## Key Takeaways
- The problem can be solved using a modified merge sort algorithm that keeps track of the number of smaller elements.
- The time complexity of the solution is O(n log n) due to the merge sort algorithm.
- The space complexity of the solution is O(n) for storing the result and the temporary arrays used in the merge sort algorithm.