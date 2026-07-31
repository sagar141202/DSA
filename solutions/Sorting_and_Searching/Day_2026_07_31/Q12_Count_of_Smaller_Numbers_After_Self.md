# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to find the count of smaller numbers after self for each element in the array. This means that for each element at index `i`, you need to count the number of elements at indices `j` where `j > i` and `nums[j] < nums[i]`. Return an array of these counts.

## Approach
We will use a modified merge sort algorithm to solve this problem, utilizing the fact that merge sort can be used to count inversions in an array. The idea is to count the inversions while merging the two sorted halves of the array.

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
                i++;
            } else {
                arr[k++] = right[j];
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
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
```

## Key Takeaways
- The problem can be solved using a modified merge sort algorithm to count inversions.
- The time complexity of the solution is O(n log n) due to the merge sort.
- The space complexity is O(n) for storing the temporary arrays during the merge sort.