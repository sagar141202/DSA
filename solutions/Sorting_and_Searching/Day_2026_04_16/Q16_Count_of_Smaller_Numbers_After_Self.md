# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`. For each element in the array, count the number of smaller elements on its right side and return the counts in an array. The length of the input array will be in the range [1, 20000]. The range of the integers in the array will be in the range [0, 10^9]. For example, given the array `[5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]` because for the first element `5`, there are `2` elements smaller than it on its right side (`2` and `1`). For the second element `2`, there is `1` element smaller than it on its right side (`1`). For the third element `6`, there is `1` element smaller than it on its right side (`1`). For the fourth element `1`, there are `0` elements smaller than it on its right side.

## Approach
We can use a modified merge sort to solve this problem. The idea is to count the number of smaller elements on the right side of each element during the merge process. We will use a helper function to merge two sorted arrays and count the number of smaller elements.

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
        vector<pair<int, int>> arr;
        for (int i = 0; i < n; i++) {
            arr.push_back({nums[i], i});
        }
        mergeSort(arr, result);
        return result;
    }

    void mergeSort(vector<pair<int, int>>& arr, vector<int>& result) {
        if (arr.size() <= 1) return;
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
Input: [1, 2, 3, 4]
Output: [0, 0, 0, 0]
```

## Key Takeaways
- Use a modified merge sort to solve the problem.
- Count the number of smaller elements on the right side of each element during the merge process.
- Use a helper function to merge two sorted arrays and count the number of smaller elements.