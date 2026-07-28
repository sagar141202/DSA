# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z. Each letter represents a different task. Tasks could be done without original order. Each task could be done one time at least. The platform can do one task at a time. We can complete tasks in any order, but we cannot do the same task twice in less than n time intervals (i.e., n is the cooling interval). For example, if n = 3, the task A cannot be done twice within 3 time intervals. We need to find the least number of time units to complete all tasks.

## Approach
The algorithm uses a priority queue to store the frequency of each task. We then schedule the tasks based on their frequency, ensuring that the same task is not done twice within the cooling interval. The time complexity is reduced by using an unordered map to store task frequencies and a max heap to schedule tasks.

## Complexity
- Time: O(N log K)
- Space: O(N)

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
                    temp.push_back(maxHeap.top() - 1);
                    maxHeap.pop();
                }
            }
            for (int i : temp) {
                if (i > 0) {
                    maxHeap.push(i);
                }
            }
            time += maxHeap.empty() ? temp.size() : n + 1;
        }
        return time;
    }
};
```

## Test Cases
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 0
Output: 6
```

## Key Takeaways
- Use a max heap to store task frequencies and schedule tasks efficiently.
- Implement a cooling interval by using a temporary vector to store tasks that are being cooled down.
- Calculate the time units by considering the max heap size and the cooling interval.