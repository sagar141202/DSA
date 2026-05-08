# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z. Each letter represents a different task, and tasks could be done without original order. Each task could be done one time at least. The platform can do one task at a time, and the cooling time is n units of time. The function should return the least number of units of time that the CPU will take to finish all the given tasks. For example, tasks = ["A","A","A","B","B","B"], n = 2, the function should return 8 because the order is A -> B -> idle -> A -> B -> idle -> A -> B.

## Approach
The algorithm uses a max heap to store the frequency of each task and a queue to handle the cooling time. It iterates through the tasks, pushes them into the max heap, and then pops the task with the highest frequency and pushes it into the queue. After the cooling time, it pushes the task back into the max heap if it's not finished.

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
        // Create a frequency map for tasks
        unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }
        
        // Create a max heap for tasks
        priority_queue<int> maxHeap;
        for (auto& pair : freq) {
            maxHeap.push(pair.second);
        }
        
        int time = 0;
        queue<pair<int, int>> q; // <frequency, cooldown>
        
        while (!maxHeap.empty() || !q.empty()) {
            time++;
            if (!maxHeap.empty()) {
                int freq = maxHeap.top();
                maxHeap.pop();
                if (freq > 1) {
                    q.push({freq - 1, n});
                }
            }
            if (!q.empty()) {
                auto& p = q.front();
                p.second--;
                if (p.second == 0) {
                    if (p.first > 0) {
                        maxHeap.push(p.first);
                    }
                    q.pop();
                }
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
- Use a max heap to store the frequency of each task
- Use a queue to handle the cooling time
- Iterate through the tasks and update the max heap and queue accordingly
- The time complexity is O(n log k) where n is the number of tasks and k is the number of unique tasks.