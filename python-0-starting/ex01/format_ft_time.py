import datetime
import time

time_seconds = time.time()
formatted_seconds = "{:,.4f}".format(time_seconds)
formatted_scientific = "{:.2e}".format(time_seconds)


print("Seconds since January 1, 1970:", formatted_seconds, "or", formatted_scientific, "in scientific notation")
formatted_date = datetime.datetime.now().strftime("%b %d %Y")


print(formatted_date)