def activity_selection(start, finish):
    n = len(start)
    activities = []
    i = 0

    # Sort activities by their finish times
    for j in range(n):
        activities.append((start[j], finish[j]))
    activities.sort(key=lambda x: x[1])

    # Select the first activity and iterate through the rest
    selected_activities = [activities[0]]
    for j in range(1, n):
        if activities[j][0] >= selected_activities[i][1]:
            selected_activities.append(activities[j])
            i += 1

    return selected_activities
