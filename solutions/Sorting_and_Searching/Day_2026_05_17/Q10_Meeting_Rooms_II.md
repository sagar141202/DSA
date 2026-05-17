# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. If the person can attend all meetings, return 0. If the person cannot attend all meetings, return the minimum number of rooms required to hold all meetings. Each meeting interval is represented as a pair of integers (start, end), where start is the start time of the meeting and end is the end time of the meeting. Assume that all meetings are non-overlapping and that start times are distinct. For example, given [[0, 30],[5, 10],[15, 20]], the minimum number of rooms required is 2.

## Approach
We can solve this problem by using a priority queue to store the end times of the meetings. We first sort the meetings by their start times. Then, we iterate through the sorted meetings and for each meeting, we check if the earliest end time in the priority queue is earlier than the start time of the current meeting. If it is, we remove the earliest end time from the queue. Finally, we add the end time of the current meeting to the queue. The size of the queue at the end represents the minimum number of rooms required.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        
        // Sort the meetings by their start times
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Initialize a priority queue to store the end times of the meetings
        priority_queue<int, vector<int>, greater<int>> endTimes;
        
        // Initialize the minimum number of rooms required
        int minRooms = 0;
        
        // Iterate through the sorted meetings
        for (const auto& interval : intervals) {
            // If the earliest end time in the queue is earlier than the start time of the current meeting,
            // remove the earliest end time from the queue
            if (!endTimes.empty() && endTimes.top() <= interval[0]) {
                endTimes.pop();
            }
            
            // Add the end time of the current meeting to the queue
            endTimes.push(interval[1]);
            
            // Update the minimum number of rooms required
            minRooms = max(minRooms, (int)endTimes.size());
        }
        
        return minRooms;
    }
};
```

## Test Cases
```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Input: [[7, 10],[2, 4]]
Output: 1
```

## Key Takeaways
- Use a priority queue to efficiently manage the end times of the meetings.
- Sort the meetings by their start times to ensure that we process them in the correct order.
- The size of the priority queue at the end represents the minimum number of rooms required to hold all meetings.