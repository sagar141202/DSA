# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The input array will have at least one element, but not more than 10,000 elements. The elements in the array will be in the range [-10,000, 10,000] to [10,000, 10,000]. For example, if the input array is [2,2,1], the function should return 1, because 1 appears only once in the array. If the input array is [4,1,2,1,2], the function should return 4.

## Approach
The algorithm uses the XOR operation to find the single number. The XOR of a number with itself is 0, and the XOR of a number with 0 is the number itself. Therefore, all numbers that appear twice will cancel each other out, leaving only the single number. This approach works because the XOR operation has the properties of commutativity, associativity, and identity.

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
        // XOR all numbers in the array
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
};
```

## Test Cases
```
Input: [2,2,1]
Output: 1
Input: [4,1,2,1,2]
Output: 4
```

## Key Takeaways
- The XOR operation can be used to find the single number in an array where every element appears twice except for one.
- The XOR operation has the properties of commutativity, associativity, and identity, which makes it suitable for this problem.
- The time complexity of this solution is O(n), where n is the number of elements in the array, and the space complexity is O(1), which means it uses constant space.