import numpy as np

# Generating dummy data
temp_avg = np.array([27, 28, 31, 28, 29])

# daily temp of 5 cities for 30 days
temp_daily = np.random.normal(loc=29, scale=2, size=(5,30))
# Rounding off the temp to 1 digit
temp_daily = temp_daily.round(1)
