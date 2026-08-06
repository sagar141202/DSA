# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`. For each element in the array, count the number of smaller elements on its right side. Return the count array. The length of the input array will not exceed 10^5. For example, if `nums = [5, 2, 6, 1]`, then the output should be `[2, 1, 1, 0]` because for the first element (5), there are 2 smaller elements on its right (2 and 1). For the second element (2), there is 1 smaller element on its right (1). For the third element (6), there is 1 smaller element on its right (1). For the fourth element (1), there are no smaller elements on its right.

## Approach
The approach is to use a modified merge sort algorithm to count the smaller numbers on the right side for each element in the array. This algorithm works by recursively dividing the array into two halves, sorting them, and then merging them while counting the smaller elements. The merge sort algorithm is modified to count the inversions, which represent the number of smaller elements on the right side of each element.

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
        vector<pair<int, int>> temp;
        for (int i = 0; i < nums.size(); i++) {
            temp.push_back({nums[i], i});
        }
        mergeSort(temp, 0, temp.size() - 1, result);
        return result;
    }

    void mergeSort(vector<pair<int, int>>& temp, int start, int end, vector<int>& result) {
        if (start < end) {
            int mid = start + (end - start) / 2;
            mergeSort(temp, start, mid, result);
            mergeSort(temp, mid + 1, end, result);
            merge(temp, start, mid, end, result);
        }
    }

    void merge(vector<pair<int, int>>& temp, int start, int mid, int end, vector<int>& result) {
        vector<pair<int, int>> left(temp.begin() + start, temp.begin() + mid + 1);
        vector<pair<int, int>> right(temp.begin() + mid + 1, temp.begin() + end + 1);
        int i = 0, j = 0, k = start;
        while (i < left.size() && j < right.size()) {
            if (left[i].first <= right[j].first) {
                result[left[i].second] += j;
                temp[k++] = left[i++];
            } else {
                temp[k++] = right[j++];
            }
        }
        while (i < left.size()) {
            result[left[i].second] += j;
            temp[k++] = left[i++];
        }
        while (j < right.size()) {
            temp[k++] = right[j++];
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
- The merge sort algorithm can be modified to solve various problems, such as counting inversions.
- The use of a temporary array to store the elements along with their original indices is helpful in solving problems that require counting smaller elements on the right side.
- The time complexity of the modified merge sort algorithm is O(n log n), which is efficient for large inputs.