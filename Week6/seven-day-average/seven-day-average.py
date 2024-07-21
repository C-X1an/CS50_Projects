import csv
import requests
from collections import deque


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):

    previous_cases = {}
    new_cases = {}
    for row in reader:
        state = row['state']
        cases = row['cases']
        if state not in previous_cases:
            previous_cases[state] = cases
            new_case = cases
        else:
            new_case = int(cases) - int(previous_cases[state])
        if state not in new_cases:
            new_cases[state] = deque(maxlen=14)
            new_cases[state].append(new_case)
        else:
            new_cases[state].append(new_case)
        previous_cases[state] = cases
    return new_cases

# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in new_cases:
        if state in states:
            total_0 = sum(list(new_cases[state])[:7])
            average_0 = int(total_0 / 7)
            total_1 = sum(list(new_cases[state])[-7:])
            average_1 = int(total_1 / 7)
            percent = int((average_1 - average_0) / average_0)
            if percent > 0:
                print(state, "had a 7-day average of", average_1, "and an increase of", percent, '%')
            else:
                print(state, "had a 7-day average of", average_1, "and an decrease of", percent, '%')

main()
