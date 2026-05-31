# Restore IP Addresses

## Problem Statement
Given a string containing only digits, restore it by returning all possible valid IP address combinations. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The input string must not contain any leading zeros, unless the number is zero itself. For example, given the input "25525511135", the output should be ["255.255.11.135", "255.255.111.35"].

## Approach
The approach involves using backtracking to generate all possible combinations of four numbers from the input string, and then filtering out the invalid combinations. We will use a recursive function to explore all possible combinations.

## Complexity
- Time: O(2^n * n) where n is the length of the input string, because in the worst case, we have to explore all possible combinations of the string.
- Space: O(n) for storing the recursive call stack and the result.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        backtrack(result, "", s, 0, 0);
        return result;
    }
    
    void backtrack(vector<string>& result, string current, string& s, int start, int count) {
        if (count == 4) {
            if (start == s.size()) {
                result.push_back(current.substr(0, current.size() - 1));
            }
            return;
        }
        
        for (int i = 1; i <= 3; i++) {
            if (start + i > s.size()) break;
            string substr = s.substr(start, i);
            if ((substr.size() > 1 && substr[0] == '0') || stoi(substr) > 255) continue;
            backtrack(result, current + substr + ".", s, start + i, count + 1);
        }
    }
};

```

## Test Cases
```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
Input: "0000"
Output: ["0.0.0.0"]
Input: "101023"
Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
```

## Key Takeaways
- Use backtracking to generate all possible combinations of four numbers from the input string.
- Filter out invalid combinations by checking if the current substring is a valid IP address segment (i.e., between 0 and 255, inclusive, and no leading zeros unless the number is zero itself).
- Use a recursive function to explore all possible combinations and store the result in a vector.