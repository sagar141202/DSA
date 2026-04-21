# Missing Number

## Problem Statement
Given an array of integers from 0 to n, where n is the length of the array, find the missing number in the array. The array only contains distinct integers. For example, given the array [0, 1, 3], the missing number is 2. The array can contain negative numbers and the missing number can also be negative.

## Approach
The approach to solve this problem is to use the XOR operation to find the missing number. The XOR of all numbers from 0 to n and the XOR of all numbers in the array will give the missing number. This is because XOR of all numbers from 0 to n will contain all bits set to 1, and XOR of all numbers in the array will contain all bits set to 1 except for the missing number.

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
        // calculate XOR of all numbers from 0 to n
        for (int i = 0; i <= n; i++) {
            xor_all ^= i;
        }
        // calculate XOR of all numbers in the array
        for (int num : nums) {
            xor_all ^= num;
        }
        return xor_all;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {0, 1, 3};
    cout << "Missing number: " << solution.missingNumber(nums) << endl;
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
- The XOR operation can be used to find the missing number in an array.
- The XOR of all numbers from 0 to n and the XOR of all numbers in the array will give the missing number.
- This solution has a time complexity of O(n) and space complexity of O(1).