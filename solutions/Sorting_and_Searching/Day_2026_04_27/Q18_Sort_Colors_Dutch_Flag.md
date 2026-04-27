# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0, 1, and 2, sort the array in-place such that all 0s are first, followed by all 1s, and then all 2s. The array is also known as the Dutch Flag array. The constraint is that we should only use a constant amount of space and the time complexity should be linear. For example, if the input array is [2, 0, 2, 1, 1, 0], the output should be [0, 0, 1, 1, 2, 2].

## Approach
We can use the Dutch National Flag algorithm, a variation of the quicksort algorithm, to solve this problem. The algorithm uses three pointers to keep track of the positions of the 0s, 1s, and 2s. We iterate through the array and swap elements based on their values.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    // Initialize pointers for 0s and 2s
    int low = 0, high = nums.size() - 1;
    // Initialize pointer for current element
    int mid = 0;
    
    // Continue until mid pointer crosses high pointer
    while (mid <= high) {
        // If current element is 0, swap with low and move both low and mid
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        }
        // If current element is 1, just move mid
        else if (nums[mid] == 1) {
            mid++;
        }
        // If current element is 2, swap with high and move high
        else {
            swap(nums[mid], nums[high]);
            high--;
        }
    }
}

int main() {
    vector<int> nums = {2, 0, 2, 1, 1, 0};
    sortColors(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
Input: [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2]
```

## Key Takeaways
- The Dutch National Flag algorithm is used to sort an array of 0s, 1s, and 2s in linear time complexity.
- We use three pointers (low, mid, high) to keep track of the positions of the 0s, 1s, and 2s.
- The algorithm only uses a constant amount of space, making it space-efficient.