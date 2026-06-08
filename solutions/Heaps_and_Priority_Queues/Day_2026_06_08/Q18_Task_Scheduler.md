# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to complete, where different letters represent different tasks. The length of the array is n. The CPU can complete one task per unit of time. However, it has a cooling system that after completing a task, it needs at least 'n' units of time before completing the same task again. The function should return the least number of units of time that the CPU will take to complete all the given tasks.

## Approach
The approach to solve this problem is to use a priority queue to store the frequency of tasks and a variable to store the maximum frequency. Then, calculate the total time units required to complete all tasks based on the maximum frequency and the total number of tasks.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // Create a frequency map for tasks
        unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }
        
        // Find the maximum frequency
        int maxFreq = 0;
        for (auto& it : freq) {
            maxFreq = max(maxFreq, it.second);
        }
        
        // Calculate the number of tasks with maximum frequency
        int maxFreqCount = 0;
        for (auto& it : freq) {
            if (it.second == maxFreq) {
                maxFreqCount++;
            }
        }
        
        // Calculate the total time units required
        int totalTime = (maxFreq - 1) * (n + 1) + maxFreqCount;
        
        // Return the maximum of total time and tasks size
        return max((int)tasks.size(), totalTime);
    }
};
```

## Test Cases
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
```

## Key Takeaways
- Use a frequency map to store the frequency of tasks.
- Calculate the maximum frequency and the number of tasks with maximum frequency.
- Calculate the total time units required based on the maximum frequency and the cooling time 'n'.