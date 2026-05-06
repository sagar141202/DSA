# Find Peak Element

## Problem Statement
The problem requires finding a peak element in an unsorted array. A peak element is an element that is not smaller than its neighbors. The array can have multiple peak elements, but we need to find at least one of them. The input array will have at least one element, and all elements will be integers. For example, given the array [1, 2, 3, 1], the peak element is 3. If the input array is [1, 2, 1, 3, 5, 6, 4], then the peak elements are 2 and 6.

## Approach
We can solve this problem using a binary search approach, by comparing the middle element with its neighbors and deciding which half to continue the search in. This approach takes advantage of the fact that a peak element must exist in the array.

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
            // if middle element is smaller than the next one, 
            // then the peak must be on the right side
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
```

## Test Cases
```
Input: [1, 2, 3, 1]
Output: 2
Input: [1, 2, 1, 3, 5, 6, 4]
Output: 1 or 5
```

## Key Takeaways
- The binary search approach is efficient for this problem because it reduces the search space by half at each step.
- The problem can have multiple peak elements, but the algorithm is designed to find at least one of them.
- The time complexity of the solution is O(log n), where n is the number of elements in the array.