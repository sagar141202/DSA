# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are represented as pairs of integers (start_time, finish_time), and the goal is to find the maximum number of non-overlapping activities. For example, if we have the following activities: (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14), the maximum number of non-overlapping activities is 4: (1, 4), (5, 7), (8, 11), (12, 14). The activities are non-overlapping if the finish time of one activity is less than or equal to the start time of the next activity.

## Approach
The algorithm sorts the activities based on their finish times and then iterates through the sorted activities, selecting the activities that do not overlap with the previously selected activity. This approach ensures that the maximum number of non-overlapping activities is selected. The key insight is to always choose the activity with the earliest finish time, as this leaves the most time for other activities.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start;
    int finish;
};

// Compare function to sort activities based on finish times
bool compareActivities(const Activity &a, const Activity &b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of non-overlapping activities
int selectActivities(vector<Activity> &activities) {
    // Sort the activities based on their finish times
    sort(activities.begin(), activities.end(), compareActivities);
    
    // Initialize the count of selected activities to 1 (the first activity)
    int count = 1;
    
    // Initialize the finish time of the last selected activity
    int lastFinish = activities[0].finish;
    
    // Iterate through the sorted activities
    for (int i = 1; i < activities.size(); i++) {
        // If the current activity does not overlap with the last selected activity, select it
        if (activities[i].start >= lastFinish) {
            count++;
            lastFinish = activities[i].finish;
        }
    }
    
    // Return the count of selected activities
    return count;
}

int main() {
    // Example usage
    vector<Activity> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    int maxActivities = selectActivities(activities);
    cout << "Maximum number of non-overlapping activities: " << maxActivities << endl;
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
Input: [(5, 9), (1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
Output: 3
```

## Key Takeaways
- The greedy algorithm is used to solve the activity selection problem by selecting the activities with the earliest finish times.
- The activities are sorted based on their finish times to ensure that the maximum number of non-overlapping activities is selected.
- The time complexity of the algorithm is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the activities.