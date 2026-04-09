# Missing Number

## Problem Statement
Given an array of integers from 1 to n, where one number is missing, find the missing number. The array is of size n and contains distinct integers. For example, if the input array is [1, 2, 4], the missing number is 3. The integers in the array are from 1 to n, where n is the size of the array plus one.

## Approach
The approach is to use bitwise XOR operation to find the missing number. We XOR all numbers from 1 to n and all numbers in the array, the result will be the missing number. This is because XOR of a number with itself is 0, and XOR of a number with 0 is the number itself.

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
        // XOR all numbers from 1 to n
        for (int i = 1; i <= n; i++) {
            xor_all ^= i;
        }
        // XOR all numbers in the array
        for (int num : nums) {
            xor_all ^= num;
        }
        return xor_all;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 4};
    cout << solution.missingNumber(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 4]
Output: 3
Input: [1, 2, 3, 5]
Output: 4
```

## Key Takeaways
- The XOR operation can be used to find the missing number in an array.
- The XOR operation has a time complexity of O(1) and a space complexity of O(1), making it efficient for large inputs.
- The XOR operation can be used to solve other problems, such as finding the single number in an array where every element appears twice.