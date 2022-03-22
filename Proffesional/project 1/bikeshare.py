import pandas as pd
import time

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    tries = 5

    city = input(
        """\nPlease enter the name of the city
1-chicago 
2-Newyork city 
3-washington \n
"""
    ).lower()
    # check if the city input is valid or not
    while city not in CITY_DATA.keys():
        print("\nPlease be sure from the country name\n")

        city = input(
            """\nPlease enter the name of the city
1-chicago 
2-Newyork city 
3-washington 
    """).lower()

# ---------------------------------------------------------------------
# --------------------------month--------------------------------------
# ---------------------------------------------------------------------

# repeat if the input month is invalid
    while tries > 0:
        month_list_name = ["January", "February",
                           "March", "April", "May", "June", "All"]
        month_list_number = [1, 2, 3, 4, 5, 6]
        month_value = input("""\nDo You want to enter the month in letters or intergers ?
1-Letter    (l)
2-Integer   (i)
\n""")

        if month_value == "l" or month_value == "letter":
            print("\nYou Have chosen to write month in letters\n ")
            get_month_name = input("""\nPlease enter the month name 
-January
-February
-March
-April
-May
-June
-all \n
""").capitalize()
            # repeat the input if the user enter invalid name
            while get_month_name not in month_list_name:
                print("\nPlease be sure from the month name\n")
                get_month_name = input(
                    """\nPlease Re-enter the month name \n""").capitalize()
            else:

                month = get_month_name
                break

        elif month_value == "i" or month_value == "integer":
            print("\nyou have chosen to write the month number\n")
            get_month_int = int(input("\nPlease enter the month number \n"))

            # repeat the input if the user enter invalid number
            while get_month_int not in month_list_number:
                print(
                    "\nPlease be sure from the month number , ONLY FIRST 6 MONTHS AVAILABLE\n")
                get_month_int = int(
                    input("\nPlease enter the month number\n "))

            else:
                month = get_month_int

                break

        else:
            print("\nError Found , Please be sure from Your entry\n")
            tries -= 1
            print(f"only {tries} tries left")

# ------------------------------------------------------------------
# ---------------------------Day------------------------------------
# ------------------------------------------------------------------

    while tries > 0:
        day_list_names = ["Saturday", "Sunday", "Monday",
                          "Tuesday", "Wednesday", "Thursday", "Friday", "All"]
        day_list_number = [0, 1, 2, 3, 4, 5, 6]

        day_value = input(
            """\nDo You want to Enter the day in letters or integer 
1-Letter    (l)
2-Integer   (i)
\n""")

        if day_value == "l" or day_value == "letter":
            get_Day_name = input("""\nplease enter the day name
-saturday
-sunday
-monday
-tuesday
-wednesday
-thursday
-friday
-all
\n""").capitalize()

            # repeat the input if the user enter invalid name
            while get_Day_name not in day_list_names:
                print(
                    "\nPlease be sure from the day name\n ")
                get_Day_name = input(
                    """\nplease Re-enter the day name\n """).capitalize()

            else:
                day = get_Day_name
                break

        elif day_value == "i" or day_value == "integer":
            get_Day_int = int(input("""\nplease enter the day number\n """))

            # repeat the input if the user enter invalid number
            while get_Day_int not in day_list_number:
                print(
                    "\nPlease be sure from the day number , IT START FROM MON = 0 ...SUN = 6\n ")
                get_Day_int = input("""please Re-enter the day name""")
            else:
                day = get_Day_int
                break
        else:
            print("\nError Found , Please be sure from Your entry\n")
            tries -= 1
            print(f"only {tries} tries left")

    return city, month, day


def load_Data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    # converting the starttime "str" obj into starttime "datetime" obj
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extracting the month and the day from the starttime
    df["month_name"] = pd.to_datetime(df["Start Time"]).dt.month_name()
    # extracting common month
    # month = get_month_name

    df["month_number"] = pd.to_datetime(df["Start Time"]).dt.month
    # month = get_month_int

    df["day_name"] = pd.to_datetime(df["Start Time"]).dt.day_name()
    df["day_number"] = pd.to_datetime(df["Start Time"]).dt.day_of_week
    if month != "All":

        if type(month) == int:
            df = df[df["month_number"] == month]
        elif type(month) == str:

            df = df[df["month_name"] == month]

    if day != "All":

        if type(day) == int:
            df = df[df["day_number"] == day]
        elif type(day) == str:

            df = df[df["day_name"] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month_name = df["month_name"].mode()[0]
    # print(f"The Most Common Month Is : {common_month}")
    # common_month_number = df["month_number"].mode()[0]
    print(
        f"\nThe Most Common Month Is : {common_month_name}")
    # ---------------------------------------
    # TO DO: display the most common day of week
    # df["day_common"] = pd.to_datetime(df["Start Time"]).dt.day_of_week

    common_day = df['day_name'].mode()[0]
    print(f"\nThe Most Common Day Is : {common_day}")

    # TO DO: display the most common start hour
    df["hour"] = pd.to_datetime(df["Start Time"]).dt.hour
    common_hour = df["hour"].mode()[0]
    print(f"\nThe Most Common Hour Is  : {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_Station = df["Start Station"].mode()[0]
    print(f"\nThe Most Common Start Station Is : {start_Station}")

    # TO DO: display most commonly used end station
    end_station = df["End Station"].mode()[0]
    print(f"\nThe Most Common End Station Is : {end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df["Route"] = df["Start Station"] + " - " + df["End Station"]

    common_frequency_route = df["Route"].mode()[0]
    print(f"\nThe Most Common combination Is : {common_frequency_route}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tripDuration = df["Trip Duration"].sum()

    print(f"\nTotal Trip duration : {(total_tripDuration/(60*60))} Hours.")

    # TO DO: display mean travel time
    mean_tripDuration = df["Trip Duration"].mean()

    print(f"Mean Trip Duration : {mean_tripDuration/60} Minute")

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # df = pd.DataFrame(CITY_DATA[city])
    # TO DO: Display counts of user types
    user_counts = df["User Type"].value_counts().to_frame()
    print(f"User Types are : {user_counts}")

    # TO DO: Display counts of gender
    if "Gender" in df:
        gender = df["Gender"].value_counts().to_frame()
        print(gender)
    else:
        print("\nUnfortunately, Gender is not here")
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_birth_year = df["Birth Year"].max()
        recent_birth_year = df["Birth Year"].min()
        common_birth_year = df["Birth Year"].mode()[0]

        print(f"\nEarliest year of birth is : {earliest_birth_year}")
        print(f"\nMost Recent year of birth is : {recent_birth_year}")
        print(f"\ncommon year of birth is : {common_birth_year}")
    else:
        print("\nUnfortunately, Birth Year is not provided Here")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def dis_raw_data(city):
    df = pd.read_csv(CITY_DATA[city])
    print("\nRaw Data is available to be displayed ...")
    i_loc = 0

    while True:
        raw_choice = input(
            "Do You Want To See 5 more raw Data ? Y or N ?\n ").lower()
        if raw_choice not in ["yes", "y", "no", "n"]:
            print("\ninvalid choice, please type yes or y ,no or n\n")
        elif raw_choice == "yes" or raw_choice == "y":
            print(df.iloc[i_loc:i_loc+5])
            i_loc += 5
        elif raw_choice == "no" or raw_choice == "n":
            print("Best Of Luck")
            break


def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_Data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        dis_raw_data(city)
        restart = input(
            "Do You Want to restart , yes or no ?\n ").lower().strip()

        if restart != "yes" and restart != "y":

            break


if __name__ == "__main__":
    main()

main()
