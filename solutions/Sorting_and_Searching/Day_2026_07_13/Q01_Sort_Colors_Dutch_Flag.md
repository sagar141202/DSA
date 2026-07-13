# Sort Colors (Dutch Flag)

## Problem Statement
Given an array with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively. The solution should have a time complexity of O(n) and a space complexity of O(1). For example, given the array [2,0,2,1,1,0], the function should return [0,0,1,1,2,2].

## Approach
The algorithm uses three pointers to divide the array into four sections: red, white, unknown, and blue. The red pointer is used to track the position of the next red element, the white pointer is used to track the position of the next white element, and the blue pointer is used to track the position of the next blue element. The algorithm iterates through the array, swapping elements as necessary to maintain the correct order.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    int red = 0; // pointer for the next red element
    int white = 0; // pointer for the next white element
    int blue = nums.size() - 1; // pointer for the next blue element

    while (white <= blue) {
        if (nums[white] == 0) {
            // if the current element is red, swap it with the element at the red pointer
            swap(nums[red], nums[white]);
            red++;
            white++;
        } else if (nums[white] == 1) {
            // if the current element is white, move to the next element
            white++;
        } else {
            // if the current element is blue, swap it with the element at the blue pointer
            swap(nums[white], nums[blue]);
            blue--;
        }
    }
}
```

## Test Cases
```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Input: [2,0,1]
Output: [0,1,2]
Input: [0]
Output: [0]
```

## Key Takeaways
- Use three pointers to divide the array into four sections: red, white, unknown, and blue.
- Iterate through the array, swapping elements as necessary to maintain the correct order.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.