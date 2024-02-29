# Read exam time and arrival time
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

# Convert both exam time and arrival time into minutes
exam_total_minutes = exam_hour * 60 + exam_minute
arrival_total_minutes = arrival_hour * 60 + arrival_minute

# Calculate the difference in minutes
time_difference = arrival_total_minutes - exam_total_minutes

# Determine if the student is early, on time, or late
if time_difference > 0:
    print("Late")
elif -30 <= time_difference <= 0:
    print("On time")
else:
    print("Early")

abs_time_difference = abs(time_difference)

hours = abs_time_difference // 60
minutes = abs_time_difference % 60

if hours == 0:
    print(f"{minutes} minutes {'before' if time_difference < 0 else 'after'} the start")
else:
    print(f"{hours}:{minutes:02d} {'hours before' if time_difference < 0 else 'hours after'} the start")
