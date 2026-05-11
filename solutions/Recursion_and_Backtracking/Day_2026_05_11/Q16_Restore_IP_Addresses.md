# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The string must not contain any leading zeros, unless the number is zero itself. For example, "25525511135" can be restored to ["255.255.11.135", "255.255.111.35"].

## Approach
The solution utilizes backtracking to generate all possible combinations of valid IP addresses. It iterates over the string, considering each possible segment of the IP address and checking its validity. If a segment is valid, it recursively generates all possible combinations for the remaining part of the string.

## Complexity
- Time: O(2^n * 4) where n is the length of the input string, as in the worst case, we have to consider two possibilities for each character and there are four segments in an IP address
- Space: O(n) for storing the recursive call stack and the current combination

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        backtrack(result, s, 0, {});
        return result;
    }

    void backtrack(vector<string>& result, string& s, int start, vector<string> current) {
        if (current.size() == 4) {
            if (start == s.size()) {
                string ip;
                for (int i = 0; i < current.size(); i++) {
                    ip += current[i];
                    if (i < current.size() - 1) ip += ".";
                }
                result.push_back(ip);
            }
            return;
        }

        for (int end = start + 1; end <= start + 3 && end <= s.size(); end++) {
            string segment = s.substr(start, end - start);
            if (isValid(segment)) {
                current.push_back(segment);
                backtrack(result, s, end, current);
                current.pop_back();
            }
        }
    }

    bool isValid(string segment) {
        if (segment.size() > 1 && segment[0] == '0') return false;
        int num = stoi(segment);
        return num >= 0 && num <= 255;
    }
};
```

## Test Cases
```
Input: "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Input: "0000"
Output: ["0.0.0.0"]
Input: "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

## Key Takeaways
- The key to solving this problem is to use backtracking to generate all possible combinations of valid IP addresses.
- We need to ensure that each segment of the IP address is valid by checking if it is between 0 and 255 and does not have leading zeros.
- The time complexity is exponential due to the backtracking, but it is necessary to generate all possible combinations.