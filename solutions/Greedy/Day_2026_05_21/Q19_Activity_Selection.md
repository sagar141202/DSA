# Activity Selection

## Problem Statement
Given a set of activities with their start and end times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. The goal is to find the maximum number of non-overlapping activities that can be selected.

## Approach
The algorithm uses a greedy approach, sorting the activities based on their end times and then selecting the activities that do not overlap with the previously selected activities. This approach ensures that the maximum number of activities can be selected.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start, end;
};

// Compare function to sort activities based on their end times
bool compare(Activity a, Activity b) {
    return a.end < b.end;
}

// Function to select the maximum number of activities
int activitySelection(Activity arr[], int n) {
    // Sort the activities based on their end times
    sort(arr, arr + n, compare);

    // Initialize the count of selected activities
    int count = 1;

    // Initialize the end time of the last selected activity
    int lastEnd = arr[0].end;

    // Iterate over the activities
    for (int i = 1; i < n; i++) {
        // Check if the current activity does not overlap with the last selected activity
        if (arr[i].start >= lastEnd) {
            // Increment the count of selected activities
            count++;

            // Update the end time of the last selected activity
            lastEnd = arr[i].end;
        }
    }

    // Return the count of selected activities
    return count;
}

int main() {
    // Example usage
    Activity arr[] = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Call the function to select the maximum number of activities
    int count = activitySelection(arr, n);

    // Print the result
    cout << "Maximum number of activities: " << count << endl;

    return 0;
}
```

## Test Cases
```
Input: [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
Output: 4
```

## Key Takeaways
- The greedy approach can be used to solve the activity selection problem by sorting the activities based on their end times.
- The time complexity of the algorithm is O(n log n) due to the sorting step.
- The space complexity of the algorithm is O(n) as it requires additional space to store the sorted activities.