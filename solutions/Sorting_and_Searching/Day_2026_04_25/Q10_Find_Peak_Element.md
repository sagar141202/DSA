# Find Peak Element

## Problem Statement
Given an array of integers, find a peak element. A peak element is an element which is not smaller than its neighbors. The array may contain multiple peak elements, in that case, return the index of any one of the peak elements. The input array will always have at least one element and the answer will always exist.

## Approach
We will use a modified binary search algorithm to find the peak element. The idea is to compare the middle element with its neighbors and move towards the side that has a larger element.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            // if mid element is smaller than the next one, then the peak must be on the right side
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } 
            // otherwise, the peak must be on the left side
            else {
                right = mid;
            }
        }
        return left;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3, 1};
    cout << solution.findPeakElement(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 3, 1]
Output: 2
Input: [1, 2, 1, 3, 5, 6, 4]
Output: 5
```

## Key Takeaways
- The binary search approach is efficient for this problem because it reduces the search space by half at each step.
- The time complexity of this solution is O(log n) because we are using a binary search approach.
- The space complexity is O(1) because we are not using any extra space that scales with the input size.