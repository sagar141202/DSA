# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z, and in between them a number representing cooling time. For example, "A2B3C" means CPU needs to do task A, then cooling for 2 units, do task B, then cooling for 3 units, and finally do task C. The question is to determine the least number of units of time that the CPU needs to complete the given tasks. The cooling time cannot be used to do other tasks.

## Approach
We can use a priority queue to store the tasks along with their cooling times. The task with the nearest cooling time expiration will be executed first. This approach ensures that the CPU is utilized efficiently and the cooling time is minimized.

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
        unordered_map<char, int> task_counts;
        for (char task : tasks) {
            task_counts[task]++;
        }
        
        priority_queue<int> pq;
        for (auto& task : task_counts) {
            pq.push(task.second);
        }
        
        int time = 0;
        while (!pq.empty()) {
            vector<int> temp;
            for (int i = 0; i <= n; i++) {
                if (!pq.empty()) {
                    if (pq.top() > 1) {
                        temp.push_back(pq.top() - 1);
                    }
                    pq.pop();
                }
                time++;
                if (pq.empty() && temp.empty()) {
                    break;
                }
                if (i == n) {
                    for (int task : temp) {
                        pq.push(task);
                    }
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
Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 0
Output: 6
```

## Key Takeaways
- The key to solving this problem is to utilize a priority queue to manage tasks based on their counts.
- We use a temporary vector to hold tasks that are not yet ready to be executed due to their cooling times.
- The time complexity of O(n log n) arises from the use of the priority queue and the iteration over tasks.