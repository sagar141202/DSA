# Sort Colors (Dutch Flag)

## Problem Statement
Given an array with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We can use a constant amount of extra memory. The array is represented as a sequence of integers where 0 represents red, 1 represents white, and 2 represents blue. For example, given the array [2,0,2,1,1,0], the function should return [0,0,1,1,2,2].

## Approach
The algorithm uses three pointers to track the position of the next 0, 1, and 2 in the array. It iterates through the array, swapping elements as necessary to maintain the correct order. The pointers are updated accordingly after each swap.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0, mid = 0, high = nums.size() - 1;
    while (mid <= high) {
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        } else if (nums[mid] == 1) {
            mid++;
        } else {
            swap(nums[mid], nums[high]);
            high--;
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
- The Dutch National Flag algorithm is an efficient way to solve this problem, with a time complexity of O(n) and a space complexity of O(1).
- The use of three pointers (low, mid, high) allows us to track the position of the next 0, 1, and 2 in the array, making it easy to swap elements as necessary.