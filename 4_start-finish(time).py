def read_hour() :
    hour = int(input("Enter hour: "))
    hour = hour*3600
    return hour 
def read_minute() :
    minute = int(input("Enter minute: "))
    minute = minute*(60) 
    return minute
def read_second() :
    second = int(input("Enter second: "))
    return second
def to_seconds(hour, minute, second) :
    to_seconds = hour + minute + second
    return to_seconds
def time_elapsed(start_time, finish_time) :
    time_elapsed = finish_time - start_time
    hour_elapsed = time_elapsed // 3600
    minute_elapsed = ( time_elapsed % 3600 ) // 60
    second_elapesd = ( time_elapsed % 3600 ) % 60
    all_time = f"{hour_elapsed} hours {minute_elapsed} minutes {second_elapesd} seconds."
    return all_time

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print(start_time)
print(finish_time)
print(finish_time - start_time)
print('Elapsed time is', time_elapsed(start_time, finish_time))