# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`. For each element in the array, count the number of smaller elements on its right side. Return the count array. The length of the input array will not exceed 1000. The range of the elements in the input array is [0, 10^4]. For example, given `nums = [5, 2, 6, 1]`, the count array is `[2, 1, 1, 0]`, because there are 2 smaller numbers to the right of 5, 1 smaller number to the right of 2, 1 smaller number to the right of 6, and 0 smaller numbers to the right of 1.

## Approach
We can use a modified merge sort algorithm to count the number of smaller elements on the right side of each element. The idea is to divide the array into two halves, recursively count the smaller elements in each half, and then merge the two halves while counting the smaller elements. We can use a binary indexed tree to store the count of smaller elements.

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
        vector<int> index(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            index[i] = i;
        }
        mergeSort(nums, index, result, 0, nums.size() - 1);
        return result;
    }

    void mergeSort(vector<int>& nums, vector<int>& index, vector<int>& result, int start, int end) {
        if (start >= end) {
            return;
        }
        int mid = start + (end - start) / 2;
        mergeSort(nums, index, result, start, mid);
        mergeSort(nums, index, result, mid + 1, end);
        merge(nums, index, result, start, mid, end);
    }

    void merge(vector<int>& nums, vector<int>& index, vector<int>& result, int start, int mid, int end) {
        int left = start;
        int right = mid + 1;
        vector<int> temp(index.size());
        int k = start;
        while (left <= mid && right <= end) {
            if (nums[index[left]] <= nums[index[right]]) {
                temp[k++] = index[left++];
                result[index[left - 1]] += (right - mid - 1);
            } else {
                temp[k++] = index[right++];
            }
        }
        while (left <= mid) {
            temp[k++] = index[left++];
            result[index[left - 1]] += (right - mid - 1);
        }
        while (right <= end) {
            temp[k++] = index[right++];
        }
        for (int i = start; i <= end; i++) {
            index[i] = temp[i];
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {5, 2, 6, 1};
    vector<int> result = solution.countSmaller(nums);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
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
- Use a modified merge sort algorithm to count the number of smaller elements on the right side of each element.
- Use a binary indexed tree to store the count of smaller elements.
- Divide the array into two halves, recursively count the smaller elements in each half, and then merge the two halves while counting the smaller elements.