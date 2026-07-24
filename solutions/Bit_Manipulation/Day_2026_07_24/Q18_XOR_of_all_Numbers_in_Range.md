# XOR of all Numbers in Range

## Problem Statement
Given a range of numbers from 0 to n, find the XOR of all numbers in this range. The range is inclusive, meaning it includes both 0 and n. For example, if n = 3, the XOR of all numbers in the range would be 0 ^ 1 ^ 2 ^ 3 = 4, but if n = 4, the XOR would be 0 ^ 1 ^ 2 ^ 3 ^ 4 = 4 as well because 4 is not included in the XOR operation due to its properties. The input n will be a non-negative integer.

## Approach
The approach involves using the properties of XOR operation. We can observe that XOR of all numbers from 0 to n can be calculated using a simple formula based on the last two bits of n. If the last bit of n is 1, then the XOR will depend on the second last bit.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int xorOfRange(int n) {
        // If n is even, XOR will be n
        if (n % 4 == 0) return n;
        // If n is odd and n % 4 == 1, XOR will be 1
        if (n % 4 == 1) return 1;
        // If n % 4 == 2, XOR will be n + 1
        if (n % 4 == 2) return n + 1;
        // If n % 4 == 3, XOR will be 0
        return 0;
    }
};

int main() {
    Solution solution;
    cout << solution.xorOfRange(3) << endl;  // Output: 4 is incorrect, it should be 0 ^ 1 ^ 2 ^ 3 = 4 but here n = 3 so, it's 0 ^ 1 ^ 2 ^ 3 = n which is incorrect hence corrected below.
    return 0;
}
```
However the above C++ code seems incorrect because n = 3, hence we are calculating 0 ^ 1 ^ 2 ^ 3 which is equal to n, so we should consider cases for n.

## Test Cases
```
Input: n = 3
Output: 4 is incorrect hence consider cases 
for n = 3: 0 ^ 1 ^ 2 ^ 3 = n which is incorrect
hence 
0 ^ 1 = 1 
1 ^ 2 = 3 
3 ^ 3 = 0 
corrected solution is below 
```
However the solution can be further simplified by observing pattern of result for different n.

## Key Takeaways
- XOR of all numbers from 0 to n follows a pattern.
- We can calculate it in constant time using a simple formula based on the last two bits of n.
- The correct C++ solution considering cases for n is 
```cpp
class Solution {
public:
    int xorOfRange(int n) {
        if (n % 4 == 0) return n;
        if (n % 4 == 1) return 1;
        if (n % 4 == 2) return n + 1;
        return 0;
    }
};
``` 
But here also it seems we missed something as here for n = 3 
0 ^ 1 ^ 2 ^ 3 = n 
However we are not calculating the XOR of all numbers but rather finding pattern so 
```cpp
class Solution {
public:
    int xorOfRange(int n) {
        int res = 0;
        for (int i = 0; i <= n; i++) {
            res = res ^ i;
        }
        return res;
    }
};
``` 
This solution works fine and calculates XOR of all numbers from 0 to n correctly but time complexity is O(n) here. However we can still simplify it by observing pattern 
For even n: n = 4k 
0 ^ 1 ^ 2 ^ ... ^ (4k - 2) ^ (4k - 1) ^ 4k 
= (0 ^ 1) ^ (2 ^ 3) ^ ... ^ ((4k - 2) ^ (4k - 1)) ^ 4k 
= 1 ^ 3 ^ ... ^ 4k - 1 
= (1 ^ 3) ^ (7 ^ 5) ^ ... 
This also results in 4k 
However for odd n: 
n = 4k + 1 
0 ^ 1 ^ 2 ^ ... ^ (4k - 1) ^ (4k) ^ (4k + 1) 
= (0 ^ 1) ^ (2 ^ 3) ^ ... ^ ((4k - 2) ^ (4k - 1)) ^ (4k) ^ (4k + 1) 
= 1 ^ 3 ^ ... ^ (4k - 1) ^ (4k) ^ (4k + 1) 
= (1 ^ 3) ^ ... ^ (4k + 1) 
= 4k + 1 
Similarly we can observe patterns for other cases as well. 
So correct C++ solution with O(1) time complexity can be written as:
```cpp
class Solution {
public:
    int xorOfRange(int n) {
        if (n % 4 == 0) return n;
        if (n % 4 == 1) return 1;
        if (n % 4 == 2) return n + 1;
        return 0;
    }
};
``` 
This solution correctly calculates the XOR of all numbers from 0 to n in constant time.