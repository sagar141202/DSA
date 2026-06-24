# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z. Each letter represents a different task. Tasks could be done without original order. Each task could be done one time at least. For each pair of same tasks, they must have at least one other task scheduled between them. The time between two same tasks is defined as the time the CPU takes to complete all the tasks between them. Return the least number of units of times that the CPU will take to complete all the given tasks.

## Approach
The approach involves using a priority queue to store the frequency of each task and a queue to store the tasks that are waiting to be scheduled. The task with the highest frequency is scheduled first, and if there are multiple tasks with the same frequency, they are scheduled in any order.

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
        unordered_map<char, int> count;
        for (char task : tasks) {
            count[task]++;
        }
        
        int maxCount = 0;
        int maxCountTasks = 0;
        for (auto& pair : count) {
            if (pair.second > maxCount) {
                maxCount = pair.second;
                maxCountTasks = 1;
            } else if (pair.second == maxCount) {
                maxCountTasks++;
            }
        }
        
        int ans = (maxCount - 1) * (n + 1);
        ans += maxCountTasks;
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
- Use a hash map to count the frequency of each task.
- Calculate the maximum frequency and the number of tasks with the maximum frequency.
- Calculate the minimum time units required to complete all tasks based on the maximum frequency and the cooling time n.