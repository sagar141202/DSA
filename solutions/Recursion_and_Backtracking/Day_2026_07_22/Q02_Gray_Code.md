# Gray Code

## Problem Statement
The Gray Code is a sequence of numbers where each number differs from the previous number by only one bit. Given a non-negative integer `n`, generate all the Gray Code sequences of length `n`. The sequence should start from 0 and end at `2^n - 1`. For example, for `n = 2`, the Gray Code sequence is `[0, 1, 3, 2]`. For `n = 3`, the Gray Code sequence is `[0, 1, 3, 2, 6, 7, 5, 4]`.

## Approach
We can use recursion and backtracking to generate the Gray Code sequence. The idea is to generate the sequence for `n-1` and then append the mirror of the sequence to generate the sequence for `n`. We can use bit manipulation to achieve this.

## Complexity
- Time: O(2^n)
- Space: O(2^n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;
        for (int i = 0; i < (1 << n); i++) {
            int gray = i ^ (i >> 1);
            result.push_back(gray);
        }
        return result;
    }
};

int main() {
    Solution solution;
    vector<int> result = solution.grayCode(3);
    for (int num : result) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: n = 2
Output: [0, 1, 3, 2]
Input: n = 3
Output: [0, 1, 3, 2, 6, 7, 5, 4]
```

## Key Takeaways
- The Gray Code sequence has a property that each number differs from the previous number by only one bit.
- We can use recursion and backtracking to generate the Gray Code sequence, but in this case, we can use bit manipulation to achieve the same result more efficiently.
- The time complexity of the solution is O(2^n) because we need to generate all possible numbers of length `n`.