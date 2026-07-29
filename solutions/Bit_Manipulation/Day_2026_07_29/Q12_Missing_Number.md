# Missing Number

## Problem Statement
Given an array of integers from 0 to n, where n is the length of the array, find the missing number in the array. The array is guaranteed to have one and only one missing number. For example, if the input is [0, 1, 3], the output should be 2. The array can have duplicate numbers and the missing number can be anywhere in the range.

## Approach
The approach to solve this problem is to use bit manipulation to find the missing number. We can use XOR operation to find the missing number. The XOR of all numbers from 0 to n and the XOR of all numbers in the array will give us the missing number.

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
        int xor_all = 0;
        // XOR of all numbers from 0 to n
        for (int i = 0; i <= n; i++) {
            xor_all ^= i;
        }
        // XOR of all numbers in the array
        for (int num : nums) {
            xor_all ^= num;
        }
        return xor_all;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {0, 1, 3};
    cout << solution.missingNumber(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [0, 1, 3]
Output: 2
Input: [4, 0, 3, 1]
Output: 2
```

## Key Takeaways
- The XOR operation has the property that a ^ a = 0 and a ^ 0 = a, which makes it suitable for finding the missing number.
- The time complexity of the solution is O(n) because we are iterating over the array and the range of numbers from 0 to n.
- The space complexity of the solution is O(1) because we are using a constant amount of space to store the result.