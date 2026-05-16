# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z. Each letter represents a different task. A task could be done one unit of time per execution. For each unit of time, CPU could complete one task or make a switch. Switching task needs 2 units of time. Find the least number of units of time that the CPU will take to finish all the given tasks with given cooling time `n`. If there are multiple possible answers, return the one with the least switches.

## Approach
The problem can be solved by using a priority queue to store the frequency of each task. We use a max heap to ensure the task with the highest frequency is always at the top. The algorithm involves popping the top task, scheduling it, and then pushing it back into the heap after the cooling time.

## Complexity
- Time: O(N log 26)
- Space: O(26)

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

        priority_queue<int> maxHeap;
        for (auto& pair : count) {
            maxHeap.push(pair.second);
        }

        int time = 0;
        while (!maxHeap.empty()) {
            vector<int> temp;
            for (int i = 0; i <= n; i++) {
                if (!maxHeap.empty()) {
                    int freq = maxHeap.top();
                    maxHeap.pop();
                    if (freq > 1) {
                        temp.push_back(freq - 1);
                    }
                }
                time++;
                if (maxHeap.empty() && temp.empty()) {
                    break;
                }
            }
            for (int freq : temp) {
                maxHeap.push(freq);
            }
        }
        return time;
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
- Use a priority queue to store the frequency of each task.
- Schedule the task with the highest frequency first.
- After scheduling a task, push it back into the heap after the cooling time.