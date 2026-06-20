# Count of Smaller Numbers After Self

## Problem Statement
Given an array of integers, find the count of smaller numbers after self for each element in the array. This means that for each element at index `i`, we need to find the number of elements in the subarray from index `i+1` to the end that are smaller than the element at index `i`. The input array will contain at most 10000 elements, and each element will be between 0 and 10000.

## Approach
The approach to solve this problem is to use a modified merge sort algorithm, where we count the number of smaller elements while merging the sorted subarrays. We will use a recursive function to divide the array into smaller subarrays and then merge them while counting the smaller elements.

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
        vector<pair<int, int>> temp(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            temp[i] = {nums[i], i};
        }
        mergeSort(temp, 0, temp.size() - 1, result);
        return result;
    }

    void mergeSort(vector<pair<int, int>>& temp, int start, int end, vector<int>& result) {
        if (start >= end) return;
        int mid = start + (end - start) / 2;
        mergeSort(temp, start, mid, result);
        mergeSort(temp, mid + 1, end, result);
        merge(temp, start, mid, end, result);
    }

    void merge(vector<pair<int, int>>& temp, int start, int mid, int end, vector<int>& result) {
        vector<pair<int, int>> left(temp.begin() + start, temp.begin() + mid + 1);
        vector<pair<int, int>> right(temp.begin() + mid + 1, temp.begin() + end + 1);
        int i = 0, j = 0, k = start;
        while (i < left.size() && j < right.size()) {
            if (left[i].first <= right[j].first) {
                temp[k++] = left[i];
                result[left[i].second] += j;
                i++;
            } else {
                temp[k++] = right[j];
                j++;
            }
        }
        while (i < left.size()) {
            temp[k++] = left[i];
            result[left[i].second] += j;
            i++;
        }
        while (j < right.size()) {
            temp[k++] = right[j];
            j++;
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
- The modified merge sort algorithm is used to count the number of smaller elements while merging the sorted subarrays.
- The time complexity of the solution is O(n log n) due to the merge sort algorithm.
- The space complexity of the solution is O(n) for storing the temporary array and the result array.