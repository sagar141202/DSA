# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, sort the array in a way that all elements at even indices are in increasing order, and all elements at odd indices are in decreasing order. The first element should be the smallest, and the second element should be the largest, then the third element should be the second smallest, and the fourth element should be the second largest, and so on.

## Approach
We can solve this problem by first sorting the array in ascending order, then iterating over the sorted array to construct the wiggle sorted array. The idea is to place the smallest element at the first index, the largest element at the second index, the second smallest element at the third index, and the second largest element at the fourth index, and so on.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        // Create a copy of the input array
        vector<int> sortedNums = nums;
        
        // Sort the copied array in ascending order
        sort(sortedNums.begin(), sortedNums.end());
        
        int small = 0, large = nums.size() - 1;
        
        // Iterate over the input array
        for (int i = 0; i < nums.size(); i++) {
            // If the index is even, place the smallest element at this index
            if (i % 2 == 0) {
                nums[i] = sortedNums[small++];
            }
            // If the index is odd, place the largest element at this index
            else {
                nums[i] = sortedNums[large--];
            }
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 5, 1, 1, 6, 4};
    solution.wiggleSort(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
```

## Key Takeaways
- First, we sort the input array in ascending order to get the smallest and largest elements.
- Then, we iterate over the input array and place the smallest element at the even index and the largest element at the odd index.
- We use two pointers, one starting from the beginning of the sorted array and one starting from the end, to keep track of the smallest and largest elements.