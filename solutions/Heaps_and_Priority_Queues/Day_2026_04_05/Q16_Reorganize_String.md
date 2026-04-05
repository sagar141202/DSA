# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it's impossible to reorganize the string, return an empty string. The string consists of lowercase English letters, and the length of the string is at most 10^5. For example, given the string "aab", the output should be "aba". Given the string "aaab", the output should be an empty string.

## Approach
We can use a max heap to store the frequency of each character. We pop the two most frequent characters from the heap, append them to the result string, and then push them back into the heap with decreased frequency. This process is repeated until the heap is empty or we cannot pop two characters from the heap.

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
        // count the frequency of each character
        unordered_map<char, int> count;
        for (char c : s) {
            count[c]++;
        }

        // create a max heap to store the frequency of each character
        priority_queue<pair<int, char>> maxHeap;
        for (auto& it : count) {
            maxHeap.push({it.second, it.first});
        }

        // reorganize the string
        string result;
        while (!maxHeap.empty()) {
            // pop the two most frequent characters from the heap
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();
            if (maxHeap.empty()) {
                // if there's only one character left, we cannot reorganize the string
                if (first.first > 1) {
                    return "";
                } else {
                    result += first.second;
                }
                break;
            }
            pair<int, char> second = maxHeap.top();
            maxHeap.pop();

            // append the two characters to the result string
            result += first.second;
            result += second.second;

            // push the two characters back into the heap with decreased frequency
            if (first.first > 1) {
                maxHeap.push({first.first - 1, first.second});
            }
            if (second.first > 1) {
                maxHeap.push({second.first - 1, second.second});
            }
        }

        return result;
    }
};
```

## Test Cases
```
Input: "aab"
Output: "aba"
Input: "aaab"
Output: ""
```

## Key Takeaways
- Use a max heap to store the frequency of each character.
- Pop the two most frequent characters from the heap, append them to the result string, and then push them back into the heap with decreased frequency.
- If there's only one character left in the heap and its frequency is greater than 1, we cannot reorganize the string.