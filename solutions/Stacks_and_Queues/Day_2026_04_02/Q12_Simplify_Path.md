# Simplify Path

## Problem Statement
Given an absolute path in a file system, simplify it by resolving '..' and '.' in the path. The path is guaranteed to start with a '/' and may or may not end with a '/'. There will be no '.' at the beginning or end of the path, and there will be no '..' at the beginning of the path. The path will contain at least one '/' and no consecutive '/'. For example, "/home/" and "/../" are not valid inputs. The function should return the simplified path.

## Approach
The algorithm uses a stack to store the directories in the path. When it encounters '..', it pops the last directory from the stack if it's not empty. When it encounters '.', it skips it. Otherwise, it pushes the directory into the stack.

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
        string res = "";
        for (int i = 0; i < path.length(); i++) {
            if (path[i] == '/') {
                if (res != "") {
                    if (res == "..") {
                        if (!st.empty()) st.pop();
                    } else if (res != ".") {
                        st.push(res);
                    }
                    res = "";
                }
            } else {
                res += path[i];
            }
        }
        if (res != "") {
            if (res == "..") {
                if (!st.empty()) st.pop();
            } else if (res != ".") {
                st.push(res);
            }
        }
        string simplifiedPath = "";
        while (!st.empty()) {
            simplifiedPath = "/" + st.top() + simplifiedPath;
            st.pop();
        }
        return simplifiedPath == "" ? "/" : simplifiedPath;
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
- Use a stack to store the directories in the path.
- Handle '..' and '.' separately to resolve them correctly.
- The function should return the simplified path, handling the case when the stack is empty.