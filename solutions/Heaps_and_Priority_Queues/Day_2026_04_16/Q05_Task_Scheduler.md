# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z, and in between them, there are some idle time denoted by '.'. The system has a limited capacity, so at any point in time, it can only process a fixed number of tasks. Given the number of CPUs (n) and the task array (tasks), determine the least number of time units required to schedule all the tasks. Each task can be completed in one time unit, and two tasks of the same type cannot be executed in the same time unit.

## Approach
We can use a priority queue to store the frequency of each task and a queue to store the tasks that are waiting to be executed. The priority queue will be sorted based on the frequency of the tasks, and the queue will store the tasks that have been executed and are waiting for the cooldown period to finish.

## Complexity
- Time: O(n log k)
- Space: O(k)

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
        int maxCountTask = 0;
        for (auto& pair : count) {
            if (pair.second > maxCount) {
                maxCount = pair.second;
                maxCountTask = 1;
            } else if (pair.second == maxCount) {
                maxCountTask++;
            }
        }
        
        int ans = (maxCount - 1) * (n + 1) + maxCountTask;
        return max((int)tasks.size(), ans);
    }
};
```

## Test Cases
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
```

## Key Takeaways
- Use a priority queue or a hash map to store the frequency of each task.
- Use a queue to store the tasks that are waiting to be executed.
- Calculate the maximum frequency of tasks and the number of tasks with the maximum frequency.