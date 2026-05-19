# Missing Number

## Problem Statement
Given an array of integers from 1 to n, where one number is missing, find the missing number. The array is of size n-1, and the numbers are in the range [1, n]. The missing number can be any number in the range. For example, if the input array is [1, 2, 4], the missing number is 3. If the input array is [1, 3, 4], the missing number is 2.

## Approach
The approach is to use bitwise XOR operation to find the missing number. We XOR all numbers in the range [1, n] and all numbers in the input array. The result will be the missing number. This works because XOR of all numbers in the range [1, n] and all numbers in the input array will cancel out all numbers that appear twice, leaving only the missing number.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMissingNumber(vector<int>& nums) {
    int n = nums.size() + 1;
    int xor_all = 0;
    int xor_nums = 0;
    
    // XOR all numbers in the range [1, n]
    for (int i = 1; i <= n; i++) {
        xor_all ^= i;
    }
    
    // XOR all numbers in the input array
    for (int num : nums) {
        xor_nums ^= num;
    }
    
    // The missing number is the XOR of all numbers and all numbers in the input array
    return xor_all ^ xor_nums;
}

int main() {
    vector<int> nums = {1, 2, 4};
    cout << findMissingNumber(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 4]
Output: 3
Input: [1, 3, 4]
Output: 2
Input: [2, 3, 4]
Output: 1
```

## Key Takeaways
- The XOR operation has a property that `a ^ a = 0` and `a ^ 0 = a`, which makes it useful for finding the missing number.
- The XOR operation can be used to find the missing number in an array of integers from 1 to n.
- The time complexity of the solution is O(n), where n is the size of the input array plus one.