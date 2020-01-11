import sys
print(sys.argv)


def main():
    user_total_time_count = {}
    user_login_time = {}
    with open(sys.argv[1]) as f:
        for line in f:
            username, action, timestamp = line.strip().split(";")
            timestamp = int(timestamp)
            if action == "LOGIN":
                user_login_time[username] = timestamp
            elif action == "LOGOUT":
                time_in_this_session = timestamp - user_login_time[username]
                if username in user_total_time_count:
                    user_total_time_count[username] += time_in_this_session
                else:
                    user_total_time_count[username] = time_in_this_session
        for user, time in user_total_time_count.items():
            print(f"User {user} spent {time} sec. in system")

if __name__ == "__main__":
    main()