#!/bin/python3

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time-bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        if time-bound == 'yes':
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time-bound == 'no':
            print(f"Reminder: '{task}' is a high priority task. You can work on it when you have time.")

    case 'medium':
        if time-bound == 'yes':
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. You can work on it when you have time.")
    case 'low':
        if time-bound == 'yes':
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

