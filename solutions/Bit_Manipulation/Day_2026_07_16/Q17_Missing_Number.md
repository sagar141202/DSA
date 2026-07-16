# Missing Number

## Problem Statement
The problem requires finding a missing number in an array of integers from 0 to n, where n is the size of the array. The array contains all integers from 0 to n except one. For example, given the array [0, 1, 3], the missing number is 2. The array can contain duplicate elements, but the missing number will always be unique.

## Approach
The approach to solve this problem is to use bitwise XOR operation to find the missing number. The XOR of all numbers from 0 to n and the XOR of all numbers in the array will give the missing number.

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
        int xor_arr = 0;
        
        // Calculate XOR of all numbers from 0 to n
        for (int i = 0; i <= n; i++) {
            xor_all ^= i;
        }
        
        // Calculate XOR of all numbers in the array
        for (int num : nums) {
            xor_arr ^= num;
        }
        
        // The missing number is the XOR of xor_all and xor_arr
        return xor_all ^ xor_arr;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {0, 1, 3};
    cout << "Missing Number: " << solution.missingNumber(nums) << endl;
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
- The bitwise XOR operation has a property that a ^ a = 0 and a ^ 0 = a, which makes it useful for finding the missing number.
- The time complexity of the solution is O(n) because we need to iterate over all numbers from 0 to n and all numbers in the array.
- The space complexity of the solution is O(1) because we only use a constant amount of space to store the XOR results.