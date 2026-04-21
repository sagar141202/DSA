# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single number. The integer could appear only once or more than once, but it will always appear an odd number of times. The array will contain at least one element, but will not contain more than 10000 elements. The elements of the array will be in the range [-10000, 10000]. For example, given the array [2, 2, 1], the function should return 1, because 1 appears only once in the array. Given the array [4, 1, 2, 1, 2], the function should return 4, because 4 appears only once in the array.

## Approach
The algorithm uses bitwise XOR operation to find the single number. XOR of all elements gives the single number because XOR of a number with itself is 0 and XOR of a number with 0 is the number itself. This approach works because every element appears twice except for one, so all the numbers that appear twice will cancel each other out.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        // XOR of all elements gives the single number
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
};
```

## Test Cases
```
Input: [2, 2, 1]
Output: 1
Input: [4, 1, 2, 1, 2]
Output: 4
```

## Key Takeaways
- The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`, which makes it useful for finding the single number in the array.
- The algorithm has a time complexity of O(n) because it needs to iterate over all elements in the array.
- The algorithm has a space complexity of O(1) because it only uses a constant amount of space to store the result.