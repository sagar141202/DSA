# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could complete one task or just be idle. However, there is a non-negative cooling interval `n` that means between two same tasks, there must be at least `n` intervals that CPU are doing different tasks or just be idle. You need to return the least number of intervals the CPU will take to finish all the given tasks.

## Approach
The approach is to use a priority queue to store the tasks and their frequencies. We then iterate over the tasks, scheduling them based on their frequencies and the cooling interval. The task with the highest frequency is scheduled first, and if the cooling interval is not met, we insert idle tasks.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <queue>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> count;
        for (char task : tasks) {
            count[task]++;
        }
        
        priority_queue<int> pq;
        for (auto& it : count) {
            pq.push(it.second);
        }
        
        int time = 0;
        while (!pq.empty()) {
            int i = 0;
            vector<int> temp;
            while (i <= n) {
                if (!pq.empty()) {
                    if (pq.top() > 1) {
                        temp.push_back(pq.top() - 1);
                    }
                    pq.pop();
                }
                time++;
                if (i == n) {
                    break;
                }
                i++;
            }
            for (int t : temp) {
                pq.push(t);
            }
            if (pq.empty() && time > tasks.size()) {
                break;
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
Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 0
Output: 6
```

## Key Takeaways
- Use a priority queue to store tasks based on their frequencies.
- Schedule tasks based on their frequencies and the cooling interval.
- Insert idle tasks if the cooling interval is not met.