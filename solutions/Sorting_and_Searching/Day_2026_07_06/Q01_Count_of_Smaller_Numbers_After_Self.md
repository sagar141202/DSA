# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to find the count of smaller numbers after self for each element in the array. The count of smaller numbers after self for an element at index `i` is the number of elements in the array to the right of `i` (i.e., `nums[j]` where `j > i`) that are smaller than `nums[i]`. Return an array of the same length as `nums` where each element at index `i` is the count of smaller numbers after self. The input array `nums` has a length of at most 50000 and contains only distinct integers.

## Approach
We can solve this problem using a Binary Indexed Tree (BIT) or a modified merge sort. The idea is to iterate over the array from right to left, maintaining a sorted list of elements seen so far. For each element, we find its rank in the sorted list, which gives us the count of smaller numbers after self.

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
        vector<int> sortedNums;
        
        for (int i = nums.size() - 1; i >= 0; --i) {
            // Find the insertion point for nums[i] in sortedNums to get the count of smaller numbers
            auto it = lower_bound(sortedNums.begin(), sortedNums.end(), nums[i]);
            result[i] = it - sortedNums.begin();
            // Insert nums[i] into sortedNums
            sortedNums.insert(it, nums[i]);
        }
        
        return result;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {5, 2, 6, 1};
    vector<int> result = solution.countSmaller(nums);
    for (int count : result) {
        cout << count << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```

## Key Takeaways
- We use a sorted list to keep track of elements seen so far and find the insertion point for each new element to get the count of smaller numbers after self.
- The `lower_bound` function in C++ returns an iterator pointing to the first element that is not less than the given value, which helps us find the insertion point.
- The time complexity of O(n log n) comes from the iteration over the array and the use of `lower_bound` and `insert` operations on the sorted list.