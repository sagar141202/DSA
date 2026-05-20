# Sort Colors (Dutch Flag)

## Problem Statement
Given an array with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We are only allowed to use a constant amount of space. For example, with the following input: [2,0,2,1,1,0], the output should be [0,0,1,1,2,2].

## Approach
The algorithm uses three pointers: one for the next red element, one for the next white element, and one for the next blue element. We iterate through the array and swap elements to maintain the correct order. The key insight is to use the Dutch National Flag algorithm to solve this problem efficiently.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    int red = 0, white = 0, blue = nums.size() - 1;
    while (white <= blue) {
        if (nums[white] == 0) {
            swap(nums[red], nums[white]);
            red++;
            white++;
        } else if (nums[white] == 1) {
            white++;
        } else {
            swap(nums[white], nums[blue]);
            blue--;
        }
    }
}

int main() {
    vector<int> nums = {2,0,2,1,1,0};
    sortColors(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Input: [2,2,0,1,2,0]
Output: [0,0,1,2,2,2]
```

## Key Takeaways
- The Dutch National Flag algorithm is a efficient solution for this problem, with a time complexity of O(n) and a space complexity of O(1).
- The algorithm uses three pointers to maintain the correct order of the colors.
- The solution can be implemented using a simple iterative approach with swaps.