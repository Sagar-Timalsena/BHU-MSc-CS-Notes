def recursive_activity_selector(activity, k, n):
    m = k + 1
    #Skip all the activities which start before the last selected activity
    while m <= n and activity[m][0] < activity[k][1]:
        m += 1
    if m <= n:
        return [m] + recursive_activity_selector(activity, m, n)
    else:
        return []


#Activity -> (start_time, end_time), Addded dummy activity at index 0 for easier indexing
activity = [(0,0), (1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
n = len(activity)-1

#Sorting the activites with respect to the finish time
activity = sorted(activity, key = lambda x:x[1])

selected = recursive_activity_selector(activity, 0, n)
print("Selected activities:", selected)
