# Simplify Path

## Problem Statement
Given an absolute path, simplify it by resolving the `.` and `..` directories. The path is made up of directories separated by `/`. A `.` directory refers to the current directory, while a `..` directory refers to the parent directory. The function should return the simplified path. For example, given the path `/home/`, the function should return `/home`. Given the path `/../`, the function should return `/`. Given the path `/home//foo/`, the function should return `/home/foo`. The path will not contain any files, only directories.

## Approach
We will use a stack to keep track of the directories in the path. When we encounter a `..` directory, we will pop the last directory from the stack if it is not empty. When we encounter a `.` directory, we will skip it. When we encounter a normal directory, we will push it to the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        stack<string> st;
        string dir = "";
        for (char c : path) {
            if (c == '/') {
                if (dir == "..") {
                    if (!st.empty()) st.pop();
                } else if (dir == ".") {
                    // do nothing
                } else if (dir != "") {
                    st.push(dir);
                }
                dir = "";
            } else {
                dir += c;
            }
        }
        if (dir == "..") {
            if (!st.empty()) st.pop();
        } else if (dir == ".") {
            // do nothing
        } else if (dir != "") {
            st.push(dir);
        }
        string result = "";
        while (!st.empty()) {
            result = "/" + st.top() + result;
            st.pop();
        }
        if (result == "") return "/";
        return result;
    }
};
```

## Test Cases
```
Input: "/home/"
Output: "/home"
Input: "/../"
Output: "/"
Input: "/home//foo/"
Output: "/home/foo"
```

## Key Takeaways
- Use a stack to keep track of the directories in the path.
- Handle the `.` and `..` directories separately.
- Remove any duplicate `/` characters in the path.