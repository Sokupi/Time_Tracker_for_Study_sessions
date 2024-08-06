import datetime

"""VARIABLES"""


def get_valid_int(prompt):  # Make sure that it cannot be a letter
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Must be a number")


def start_session():  # Where the time starts
    start_time = datetime.datetime.now()
    print("Study session started at %02d:%02d:%02d" % (start_time.hour, start_time.minute, start_time.second))
    return start_time


def end_session(start_time):  # Where the time ends
    end_time = datetime.datetime.now()
    duration = calculate_duration(start_time, end_time)
    print("Study session ended at %02d:%02d:%02d" % (end_time.hour, end_time.minute, end_time.second))
    print(f"Duration of the study: {duration}")
    sessions.append((start_time, end_time, duration))
    return end_time, duration


def calculate_duration(start_time, end_time):  # Calculates the duration
    duration = end_time - start_time
    return duration


sessions = []  # This is where the sessions are stored


def display_sessions():  # This displays the past sessions
    for i, session in enumerate(sessions, start=1):  # enumerate() says to list from the variable SESSIONS starting 1
        start_time, end_time, duration = session

        """ Format duration as hours, minutes, seconds"""

        total_seconds = int(duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_duration = f"{hours}h {minutes}m {seconds}s"
        print(f"Session {i}: Start: {start_time}, End: {end_time}, Duration: {formatted_duration}")


def main():
    start_time = None  # Initialize start_time to None
    while True:
        print("\n1. Start a new study session")
        print("2. End the current study session")
        print("3. View past sessions")
        print("4. Exit")
        print()
        choice = int(get_valid_int("Please enter the number: "))

        if choice == 1:
            start_time = start_session()
        elif choice == 2:
            if start_time:  # Check if start_time is not None
                end_session(start_time)
                start_time = None  # Reset start_time after ending the session
            else:
                print("No active session to end")  # Make sure that you cannot end session without starting one
        elif choice == 3:
            display_sessions()  # Calls on the display_sessions function
        elif choice == 4:  #
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()
