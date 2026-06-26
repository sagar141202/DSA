# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return an empty string. The string consists of lowercase English letters and the length of the string is at most 100.

## Approach
We can use a max heap to store the frequency of each character. We then pop the two most frequent characters from the heap, append them to the result string, and decrease their frequencies. We repeat this process until the heap is empty or only one character is left with a frequency greater than 0.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string reorganizeString(string s) {
        // Create a frequency map
        map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Create a max heap
        priority_queue<pair<int, char>> maxHeap;
        for (auto it : freq) {
            maxHeap.push({it.second, it.first});
        }

        string result;
        while (!maxHeap.empty()) {
            // Pop the two most frequent characters
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();
            if (maxHeap.empty()) {
                // If only one character is left, return an empty string if its frequency is greater than 1
                if (first.first > 1) {
                    return "";
                } else {
                    result += first.second;
                }
                break;
            }
            pair<int, char> second = maxHeap.top();
            maxHeap.pop();

            // Append the characters to the result string
            result += first.second;
            result += second.second;

            // Decrease the frequencies
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
- Pop the two most frequent characters from the heap and append them to the result string.
- Decrease the frequencies of the characters and repeat the process until the heap is empty.