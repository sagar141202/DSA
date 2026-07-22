# Missing Number

## Problem Statement
The problem requires finding a missing number in an array of integers from 0 to n, where n is the size of the array. The array contains all numbers from 0 to n except one. The missing number can be found using bit manipulation. For example, given the array [0, 1, 3], the missing number is 2. The array can contain duplicate numbers, but the missing number is unique. The constraints are 0 <= n <= 10^4.

## Approach
The approach involves using XOR operation to find the missing number. The XOR of all numbers from 0 to n and the XOR of all numbers in the array will result in the missing number. This is because XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int xorAll = 0;
        // XOR of all numbers from 0 to n
        for (int i = 0; i <= n; i++) {
            xorAll ^= i;
        }
        // XOR of all numbers in the array
        for (int num : nums) {
            xorAll ^= num;
        }
        return xorAll;
    }
};
```

## Test Cases
```
Input: [0, 1, 3]
Output: 2
Input: [4, 0, 3, 1]
Output: 2
```

## Key Takeaways
- The XOR operation has a property that a ^ a = 0 and a ^ 0 = a, which can be used to find the missing number.
- The time complexity of the solution is O(n), where n is the size of the input array.
- The space complexity of the solution is O(1), as it only uses a constant amount of space.