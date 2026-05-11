# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single number. The integer could appear only once or more than once as long as it appears an odd number of times. The array is not sorted, and the size of the array is not fixed. For example, in the array `[2, 2, 1]`, the single number is `1`. In the array `[4, 1, 2, 1, 2]`, the single number is `4`.

## Approach
The algorithm uses bit manipulation to find the single number. It initializes a variable `result` to 0 and then iterates over the array, performing a bitwise XOR operation between `result` and each element. The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`, so all elements that appear twice will cancel out, leaving only the single number.

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
        // Iterate over the array and perform XOR operation
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
- The time complexity of this solution is O(n), where n is the size of the array, because we only need to iterate over the array once.
- The space complexity is O(1), which means the space required does not change with the size of the input array, making it very efficient.