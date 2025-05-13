def iterative_activity_selector(activity):
    n = len(activity)
    A = [0]  # select the first activity (index 0)
    k = 0
    for m in range(1, n):
        if activity[m][0] >= activity[k][1]:
            A.append(m)
            k = m
    return A

#Activity -> (start_time, end_time), Addded dummy activity at index 0 for easier indexing
activity = [(0,0), (1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
n = len(activity)-1

#Sorting the activites with respect to the finish time
activity = sorted(activity, key = lambda x:x[1])

selected = iterative_activity_selector(activity)
print("Selected activities:", selected)
