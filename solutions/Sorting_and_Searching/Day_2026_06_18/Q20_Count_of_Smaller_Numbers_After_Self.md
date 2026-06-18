# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to find the count of smaller numbers after self for each element in the array. The count of smaller numbers after self for an element at index `i` is the number of elements in the array to the right of `i` (i.e., `nums[i+1:]`) that are smaller than `nums[i]`. The function should return an array of these counts. For example, given the input `nums = [5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]`.

## Approach
The approach is to use a modified merge sort algorithm to count the smaller numbers after self for each element in the array. We iterate over the array from right to left and for each element, we count the number of smaller elements to its right. We use a temporary array to store the counts and then update the original array with the counts.

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
        vector<pair<int, int>> temp;
        
        for (int i = n - 1; i >= 0; i--) {
            int count = 0;
            auto it = lower_bound(temp.begin(), temp.end(), make_pair(nums[i], -1));
            count = it - temp.begin();
            result[i] = count;
            temp.insert(it, make_pair(nums[i], i));
        }
        
        return result;
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
Input: nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Input: nums = [1, 2, 3]
Output: [0, 0, 0]
```

## Key Takeaways
- The problem can be solved using a modified merge sort algorithm.
- The use of a temporary array to store the counts of smaller numbers after self is necessary to achieve the required time complexity.
- The `lower_bound` function in C++ can be used to find the insertion point for a given element in a sorted array.