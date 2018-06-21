# Author: Sheng Bian
# Date: April 28, 2017
# Description: This program read input from a file named act.txt. The
# file contains  lists of activity sets with number of activities in the
# set in the first line followed by lines containing the activity number,
# start time & finish time. The program will use last-to-start activity
# selection to output the number of activities selected and their order
# to the terminal.

# This method perform the activity selection last-to-start operation
def activitySelection(activities):
    selectedActivity = []
    # sort the activities by starting time
    activities = sorted(activities, key=lambda k: k['start'])
    # this is used to append first element in activities to selectedActivity
    activityTime = max([x['last'] for x in activities])

    while activities:
        activity = activities.pop()
        # if the finish time is smaller than or equal to previously selected activity, add to selectedActivity
        if activity['last'] <= activityTime:
            selectedActivity.append({
                'index': activity['index'],
                'start': activity['start']
            })
            activityTime = activity['start']

    return selectedActivity


# read data from act.txt file
with open("act.txt", "r") as file_input:
    lines = file_input.read().splitlines()
    # activitySets is used to store different sets of activity from file
    activitySets = []
    # activities is array to store all the activities in one set
    activities = []
    # read line by line
    while lines:
        line = lines.pop(0)
        # convert all the number into integer so that we can compare
        line = [int(num) for num in line.split(" ")]
        # if there is only one element or no new lines to read, append the existing activities to set
        if len(line) == 1 or not lines:
            if len(activities):
                activitySets.append(activities)
                # clean the activities
                activities = []
        else:
            # use dictionary to mark the index, start time and finish time
            activities.append({
                'index': line[0],
                'start': line[1],
                'last': line[2]
            })

    # call the function and print the selected activity according to assignment requirements
    i = 1
    for s in activitySets:
        print("Set " + str(i))
        selected = activitySelection(s)
        # sort the result array again by their start time
        selected = sorted(selected, key=lambda k: k['start'], reverse=False)
        print("Number of activities selected = " + str(len(selected)))
        print("Activities:" + (" ".join([str(x['index']) for x in selected])))
        print("")
        i = i + 1