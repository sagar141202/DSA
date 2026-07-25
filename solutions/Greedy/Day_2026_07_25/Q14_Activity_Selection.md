# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are represented as pairs of integers, where the first integer is the start time and the second integer is the finish time. For example, if we have two activities (1, 4) and (3, 5), we cannot select both activities because they overlap. However, if we have activities (1, 2) and (2, 3), we can select both activities because they do not overlap.

## Approach
The algorithm sorts the activities based on their finish times and then iterates over the sorted activities, selecting the activities that do not overlap with the previously selected activity. This approach ensures that we select the maximum number of activities that can be performed. The key idea is to always select the activity with the earliest finish time.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start, finish;
};

// Comparison function to sort activities based on finish times
bool compareActivities(const Activity &a, const Activity &b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of activities
int selectActivities(vector<Activity> &activities) {
    // Sort the activities based on finish times
    sort(activities.begin(), activities.end(), compareActivities);
    
    // Initialize the count of selected activities
    int count = 0;
    
    // Initialize the finish time of the last selected activity
    int lastFinish = 0;
    
    // Iterate over the sorted activities
    for (const auto &activity : activities) {
        // Check if the current activity does not overlap with the last selected activity
        if (activity.start >= lastFinish) {
            // Select the current activity
            count++;
            lastFinish = activity.finish;
        }
    }
    
    // Return the count of selected activities
    return count;
}

int main() {
    // Example usage
    vector<Activity> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    cout << "Maximum number of activities: " << selectActivities(activities) << endl;
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- Sort the activities based on their finish times to ensure that we select the activity with the earliest finish time.
- Iterate over the sorted activities and select the activities that do not overlap with the previously selected activity.
- Use a comparison function to sort the activities based on their finish times.