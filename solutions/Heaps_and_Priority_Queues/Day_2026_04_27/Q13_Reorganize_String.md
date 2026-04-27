# Reorganize String

## Problem Statement
Given a string `s`, reorganize the string such that no two adjacent characters are the same. If it's impossible to reorganize the string, return an empty string. The string consists of lowercase English letters and the length of the string is at most 100. For example, given `s = "aab"`, the output should be `"aba"`. If `s = "aaab"`, the output should be an empty string because it's impossible to reorganize the string.

## Approach
The algorithm uses a max heap to store characters and their frequencies. It pops the two most frequent characters from the heap, adds them to the result string, and then pushes them back into the heap with decreased frequencies. This process continues until the heap is empty or only one character is left with a frequency greater than 0.

## Complexity
- Time: O(N log N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string reorganizeString(string s) {
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }
        
        priority_queue<pair<int, char>> maxHeap;
        for (auto& it : freq) {
            maxHeap.push({it.second, it.first});
        }
        
        string result;
        while (!maxHeap.empty()) {
            if (maxHeap.size() < 2 && maxHeap.top().first > 1) {
                return "";
            }
            
            auto first = maxHeap.top();
            maxHeap.pop();
            auto second = maxHeap.top();
            maxHeap.pop();
            
            result += first.second;
            result += second.second;
            
            if (--first.first > 0) {
                maxHeap.push(first);
            }
            if (--second.first > 0) {
                maxHeap.push(second);
            }
        }
        
        return result;
    }
};

int main() {
    Solution solution;
    string s = "aab";
    cout << solution.reorganizeString(s) << endl;
    return 0;
}
```

## Test Cases
```
Input: s = "aab"
Output: "aba"

Input: s = "aaab"
Output: ""
```

## Key Takeaways
- Use a max heap to store characters and their frequencies.
- Pop the two most frequent characters from the heap, add them to the result string, and then push them back into the heap with decreased frequencies.
- If only one character is left with a frequency greater than 0, or if the heap has less than two elements and the top element's frequency is greater than 1, it's impossible to reorganize the string.