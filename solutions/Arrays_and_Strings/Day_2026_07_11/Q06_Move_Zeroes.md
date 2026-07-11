# Move Zeroes

## Problem Statement
Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of non-zero elements. The function should modify the input array in-place. The array can contain duplicate elements, and the size of the array can be up to 10^4. For example, if the input array is [0, 1, 0, 3, 12], the output should be [1, 3, 12, 0, 0]. If the input array is [4, 2, 4, 0, 0, 3, 0, 5, 1, 0], the output should be [4, 2, 4, 3, 5, 1, 0, 0, 0, 0].

## Approach
We will use a two-pointer approach to iterate through the array and swap non-zero elements with the next available position. This approach ensures that all non-zero elements are moved to the front of the array while maintaining their relative order. We will initialize two pointers, one at the beginning of the array and one at the beginning of the array, and then we will iterate through the array.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void moveZeroes(vector<int>& nums) {
    int left = 0; // pointer for non-zero elements
    for (int right = 0; right < nums.size(); right++) {
        if (nums[right] != 0) {
            // swap non-zero element with the next available position
            swap(nums[left], nums[right]);
            left++;
        }
    }
}

int main() {
    vector<int> nums = {0, 1, 0, 3, 12};
    moveZeroes(nums);
    for (int num : nums) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Input: [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
```

## Key Takeaways
- We can solve this problem in O(n) time complexity by using a two-pointer approach.
- We need to maintain the relative order of non-zero elements, so we cannot simply sort the array.
- The space complexity is O(1) because we are modifying the input array in-place.