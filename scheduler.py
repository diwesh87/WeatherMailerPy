__author__ = 'diwesh'


def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()

    except FileNotFoundError as err:
        print(err)

    return schedule