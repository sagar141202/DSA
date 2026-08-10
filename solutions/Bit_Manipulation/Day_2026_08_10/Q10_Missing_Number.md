# Missing Number

## Problem Statement
Given an array of integers from 0 to n-1, where one number is missing, find the missing number. The array is of size n-1, and all numbers are unique. For example, if the input array is [0, 1, 2, 4], the missing number is 3. The array can contain negative numbers and duplicate numbers are not allowed. The missing number can be any integer from 0 to n-1.

## Approach
The approach involves using bitwise XOR operation to find the missing number. We XOR all numbers in the array with all numbers from 0 to n, and the result will be the missing number. This works because XOR of all numbers from 0 to n will give us the missing number.

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
        int res = n;
        for (int i = 0; i < n; i++) {
            res = res ^ i ^ nums[i];
        }
        return res;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {0, 1, 2, 4};
    cout << "Missing number: " << solution.missingNumber(nums);
    return 0;
}
```

## Test Cases
```
Input: [0, 1, 2, 4]
Output: 3
Input: [0, 1, 3]
Output: 2
```

## Key Takeaways
- The XOR operation has a property that `a ^ a = 0` and `a ^ 0 = a`, which makes it useful for finding the missing number.
- The time complexity of the solution is O(n), where n is the size of the input array.
- The space complexity of the solution is O(1), as we only use a constant amount of space to store the result.