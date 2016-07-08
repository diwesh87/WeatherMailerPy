__author__ = 'diwesh'
import weather
import mailer
import scheduler


def get_emails():
    emails = {}

    try:
        email_file = open('email_list.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()

    except FileNotFoundError as err:
        print(err)
    return emails


def main():
    emails = get_emails()

    schedule = scheduler.get_schedule()

    forecast = weather.get_weather_forecast()

    mailer.send_emails(emails, schedule, forecast)

main()
