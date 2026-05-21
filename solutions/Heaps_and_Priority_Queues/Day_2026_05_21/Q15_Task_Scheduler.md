# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z. Each letter represents a different task. A task could be done one unit of time per execution. For each unit of time, there can be multiple tasks if they are different. For a given a cool down interval `n`, find the least number of units of times that the CPU will take to finish all the given tasks with the given cool down interval `n`. If the number of units of time the CPU will take to finish all the given tasks is less than or equal to the length of tasks, then return the length of tasks. The tasks array has a length in the range [1, 50000]. The cool down interval `n` will be in the range [0, 100].

## Approach
To solve this problem, we use a max heap to store the frequency of each task and a queue to manage the cool down interval. We calculate the maximum frequency of tasks and use it to determine the minimum time units required. The max heap helps in efficiently selecting the task with the highest frequency.

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
        unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }
        
        int maxFreq = 0;
        int maxFreqCount = 0;
        for (auto& pair : freq) {
            if (pair.second > maxFreq) {
                maxFreq = pair.second;
                maxFreqCount = 1;
            } else if (pair.second == maxFreq) {
                maxFreqCount++;
            }
        }
        
        int ans = (maxFreq - 1) * (n + 1) + maxFreqCount;
        return max((int)tasks.size(), ans);
    }
};
```

## Test Cases
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
```

## Key Takeaways
- The least interval is determined by the task with the maximum frequency.
- The cool down interval `n` affects the scheduling of tasks and the calculation of the least interval.
- The max heap data structure can be used to efficiently manage task frequencies.