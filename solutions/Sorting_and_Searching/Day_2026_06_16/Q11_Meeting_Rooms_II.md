# Meeting Rooms II

## Problem Statement
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...](si < ei), determine if a person could attend all meetings. If the number of meeting rooms is limited to a certain number, what is the minimum number of rooms required to hold all meetings so that no two meetings occur at the same time in the same room. For example, given [[0, 30],[5, 10],[15, 20]], the minimum number of rooms required is 2 because we can have two rooms, one for [0,30] and the other for [5,10] and [15,20]. The constraints are 0 <= intervals.length <= 1000 and 0 <= starti < endi <= 10^9.

## Approach
We can solve this problem using a priority queue to keep track of the end times of the meetings. The idea is to sort the meetings by their start times and then iterate over them, adding the end times to the priority queue. If the start time of the current meeting is greater than or equal to the smallest end time in the queue, we remove that end time from the queue.

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
        
        // Sort the intervals by start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        // Priority queue to store the end times
        priority_queue<int, vector<int>, greater<int>> endTimes;
        
        // Add the first meeting
        endTimes.push(intervals[0][1]);
        
        // Iterate over the rest of the meetings
        for (int i = 1; i < intervals.size(); i++) {
            // If the current meeting starts after the earliest end time, reuse the room
            if (intervals[i][0] >= endTimes.top()) {
                endTimes.pop();
            }
            // Add the current meeting's end time to the queue
            endTimes.push(intervals[i][1]);
        }
        
        // The size of the queue is the minimum number of rooms required
        return endTimes.size();
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
- We need to sort the meetings by their start times to ensure that we're considering the meetings in the correct order.
- Using a priority queue to store the end times allows us to efficiently find the earliest end time and reuse the room if possible.
- The minimum number of rooms required is equal to the maximum size of the priority queue at any point during the iteration.