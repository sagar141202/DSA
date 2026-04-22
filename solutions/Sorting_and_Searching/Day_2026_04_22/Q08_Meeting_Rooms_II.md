# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings. The meetings are non-overlapping if a meeting ends before the next meeting starts. The task is to find the minimum number of rooms required to accommodate all the meetings. For example, if we have intervals [[0,30],[5,10],[15,20]], we need 2 rooms because [5,10] and [0,30] overlap, and [15,20] overlaps with both of them. The constraints are that the input array will have at least one meeting and at most 100,000 meetings, and the duration of each meeting will be at least 1 hour.

## Approach
The algorithm sorts the meeting intervals by their start times and uses a priority queue to track the end times of the meetings. This way, we can always find the meeting that ends the earliest and reuse its room. The intuition is that if a meeting ends before the next meeting starts, we can reuse the room.

## Complexity
- Time: O(N log N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        
        // Sort the intervals by start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Priority queue to store the end times
        priority_queue<int, vector<int>, greater<int>> endTimes;
        
        // Initialize the queue with the end time of the first meeting
        endTimes.push(intervals[0][1]);
        
        // Iterate over the rest of the meetings
        for (int i = 1; i < intervals.size(); i++) {
            // If the current meeting starts after the earliest end time, update the earliest end time
            if (intervals[i][0] >= endTimes.top()) {
                endTimes.pop();
            }
            // Add the end time of the current meeting to the queue
            endTimes.push(intervals[i][1]);
        }
        
        // The size of the queue is the minimum number of rooms required
        return endTimes.size();
    }
};
```

## Test Cases
```
Input: [[0,30],[5,10],[15,20]]
Output: 2
Input: [[7,10],[2,4]]
Output: 1
```

## Key Takeaways
- We need to sort the meeting intervals by their start times to ensure that we process them in the correct order.
- Using a priority queue to track the end times allows us to efficiently find the meeting that ends the earliest and reuse its room.
- The size of the priority queue at the end of the algorithm is the minimum number of rooms required to accommodate all the meetings.