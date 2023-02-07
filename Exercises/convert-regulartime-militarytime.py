import datetime as dt
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(time_str):
    #In this line, we're using the map function to convert the values in the time string into integers.
    # We're calling the int function on each element in the list returned by time_str[:-2].split(":").
    # This line of code splits the time string into hours, minutes, and seconds, using the colon : as a separator.
    hour, minute, second = map(int, time_str[:-2].split(":"))
    #In this line, we're using slicing to extract the last two characters from the time string,
    # which represent AM or PM.
    am_pm = time_str[-2:]
    #In this line, we're using an if statement to check whether the time is in PM and the hour is not equal to 12.
    #If both conditions are true, then we add 12 to the hour, because in military time, PM hours are represented by
    #adding 12 to the hour in 12-hour time.
    if am_pm == "PM" and hour != 12:
        hour += 12
    #In this line, we're using another if statement to check whether the time is in AM and the hour is equal to 12.
    #If both conditions are true, then we set the hour to 0, because in military time, 12 AM is represented as 00:00.
    if am_pm == "AM" and hour == 12:
        hour = 0
    #In this line, we're using the datetime module to create a datetime object with the hour, minute, and second values.
    return f"{hour:02d}:{minute:02d}:{second:02d}"

if __name__ == '__main__':
     print(timeConversion("07:05:45PM"))
     print(timeConversion("11:05:45PM"))

#As for the time complexity of this code, it is indeed O(1), because it performs a constant amount of operations, regardless of the size of the input.
#The space complexity is also O(1), because it only uses a constant amount of memory, regardless of the size of the input.