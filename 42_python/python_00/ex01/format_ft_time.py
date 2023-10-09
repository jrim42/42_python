import time as time

current_time = time.time()

formatted_time = time.strftime("%b %d %Y", time.localtime(current_time))

seconds_since_epoch = round(current_time, 4)
formatted_seconds = '{:,.4f}'.format(seconds_since_epoch)
scientific_notation = f"{seconds_since_epoch:.2e}"

print(f"Seconds since January 1, 1970: {seconds_since_epoch} or {scientific_notation} in scientific notation")
print(formatted_time)