# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could complete one task or just be idle. However, there is a non-negative cooling interval `n` that means between two same tasks, there must be at least `n` intervals that CPU are doing different tasks or just be idle. You need to return the least number of intervals the CPU will take to finish all the given tasks.

## Approach
The approach is to use a priority queue to store the frequency of each task and a variable to store the number of intervals. We will pop the task with the highest frequency from the queue, decrement its frequency, and increment the intervals. If the queue is not empty and the number of intervals is less than or equal to the cooling interval, we will push the task back into the queue.

## Complexity
- Time: O(n log k)
- Space: O(k)

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

        priority_queue<int> maxHeap;
        for (auto& pair : count) {
            maxHeap.push(pair.second);
        }

        int intervals = 0;
        while (!maxHeap.empty()) {
            int i = 0;
            vector<int> temp;
            while (i <= n) {
                if (!maxHeap.empty()) {
                    if (maxHeap.top() > 1) {
                        temp.push_back(maxHeap.top() - 1);
                    }
                    maxHeap.pop();
                }
                intervals++;
                if (maxHeap.empty() && temp.empty()) {
                    break;
                }
                if (i == n) {
                    for (int freq : temp) {
                        maxHeap.push(freq);
                    }
                }
                i++;
            }
        }
        return intervals;
    }
};
```

## Test Cases
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
```

## Key Takeaways
- Use a priority queue to store the frequency of each task.
- Use a variable to store the number of intervals.
- Pop the task with the highest frequency from the queue, decrement its frequency, and increment the intervals.
- If the queue is not empty and the number of intervals is less than or equal to the cooling interval, push the task back into the queue.