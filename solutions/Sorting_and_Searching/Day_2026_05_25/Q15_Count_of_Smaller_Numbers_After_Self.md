# Count of Smaller Numbers After Self

## Problem Statement
Given an array of integers, return an array where each element at index `i` represents the number of smaller elements to the right of `i` in the original array. For example, given the array `[5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]` because there are 2 elements smaller than 5 to its right, 1 element smaller than 2 to its right, 1 element smaller than 6 to its right, and 0 elements smaller than 1 to its right. The array can contain duplicate elements and the length of the array is in the range `[1, 10^5]`.

## Approach
The approach is to use a modified merge sort algorithm that keeps track of the number of smaller elements to the right of each element. We can achieve this by counting the number of elements that are smaller than the current element as we merge the two sorted halves. The merge sort algorithm ensures that the elements to the right of the current element are always sorted, allowing us to count the smaller elements efficiently.

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
        vector<pair<int, int>> arr;
        
        // Store the elements along with their indices
        for (int i = 0; i < nums.size(); i++) {
            arr.push_back({nums[i], i});
        }
        
        // Perform merge sort and count the smaller elements
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
                // If the current element in the left half is smaller, increment the count of smaller elements for the current element
                result[left[i].second] += j;
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }
        
        while (i < left.size()) {
            result[left[i].second] += j;
            arr[k++] = left[i++];
        }
        
        while (j < right.size()) {
            arr[k++] = right[j++];
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {5, 2, 6, 1};
    vector<int> result = solution.countSmaller(nums);
    
    for (int num : result) {
        cout << num << " ";
    }
    
    return 0;
}
```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```

## Key Takeaways
- The problem can be solved using a modified merge sort algorithm that keeps track of the number of smaller elements to the right of each element.
- The time complexity is O(n log n) due to the merge sort algorithm.
- The space complexity is O(n) for storing the elements and their indices.