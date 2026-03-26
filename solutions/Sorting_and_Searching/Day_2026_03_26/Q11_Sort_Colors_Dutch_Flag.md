# Sort Colors (Dutch Flag)

## Problem Statement
Given an array of integers containing only 0s, 1s, and 2s, sort the array in ascending order. The problem is also known as the Dutch Flag problem. The constraints are that we can only use a constant amount of space and must sort the array in-place. For example, if the input array is [2, 0, 2, 1, 1, 0], the output should be [0, 0, 1, 1, 2, 2].

## Approach
The algorithm uses three pointers to divide the array into four sections: elements less than 1, elements equal to 1, elements equal to 2, and unprocessed elements. The intuition is to maintain the relative order of the sections and swap elements to move them to their correct sections.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0, mid = 0, high = nums.size() - 1;
    // iterate through the array until mid pointer crosses the high pointer
    while (mid <= high) {
        // if current element is 0, swap it with the low element and increment both low and mid pointers
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        }
        // if current element is 1, just increment the mid pointer
        else if (nums[mid] == 1) {
            mid++;
        }
        // if current element is 2, swap it with the high element and decrement the high pointer
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
Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2]
```

## Key Takeaways
- The Dutch Flag problem can be solved using three pointers and in-place swapping.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.
- The solution can be applied to other problems that require partitioning an array into multiple sections based on certain conditions.