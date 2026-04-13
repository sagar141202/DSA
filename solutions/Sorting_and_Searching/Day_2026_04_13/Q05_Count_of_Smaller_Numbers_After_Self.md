# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to return a new array where each element at index `i` represents the number of elements to its right that are smaller than `nums[i]`. The length of the input array is between 1 and 10^5, and each element is an integer between 1 and 10^5. For example, if the input array is `[5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]`.

## Approach
The approach is to use a modified merge sort algorithm to count the number of smaller elements for each element in the array. We will recursively divide the array into two halves and then merge them while counting the smaller elements. This approach takes advantage of the fact that the merge sort algorithm has a time complexity of O(n log n).

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
        mergeSort(temp, result);
        return result;
    }

    void mergeSort(vector<pair<int, int>>& temp, vector<int>& result) {
        if (temp.size() <= 1) return;
        int mid = temp.size() / 2;
        vector<pair<int, int>> left(temp.begin(), temp.begin() + mid);
        vector<pair<int, int>> right(temp.begin() + mid, temp.end());
        mergeSort(left, result);
        mergeSort(right, result);
        merge(left, right, temp, result);
    }

    void merge(vector<pair<int, int>>& left, vector<pair<int, int>>& right, vector<pair<int, int>>& temp, vector<int>& result) {
        int i = 0, j = 0, k = 0;
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
Input: [4, 3, 2, 1]
Output: [3, 2, 1, 0]
```

## Key Takeaways
- Use a modified merge sort algorithm to count the number of smaller elements for each element in the array.
- The time complexity of the merge sort algorithm is O(n log n), making it efficient for large inputs.
- The space complexity is O(n), as we need to store the temporary array and the result array.