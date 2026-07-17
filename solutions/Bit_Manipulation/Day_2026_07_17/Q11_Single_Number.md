# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single number. The integer could appear only once or more than once in the array, but the others appear exactly twice. The array is not sorted, and the single number can be any integer in the array. For example, given the array `[2, 2, 1]`, the function should return `1`, and given the array `[4, 1, 2, 1, 2]`, the function should return `4`.

## Approach
The algorithm uses bitwise XOR operation to find the single number. XOR of a number with itself is 0, and XOR of a number with 0 is the number itself. So, XOR of all numbers in the array will give the single number. This approach works because XOR operation has the property of `a ^ a = 0` and `a ^ 0 = a`.

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
        // XOR of all numbers in the array
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
- The XOR operation can be used to find the single number in an array where every element appears twice except for one.
- The XOR operation has the property of `a ^ a = 0` and `a ^ 0 = a`, which makes it suitable for this problem.
- The time complexity of this solution is O(n), where n is the number of elements in the array, and the space complexity is O(1), which means the space required does not change with the size of the input array.