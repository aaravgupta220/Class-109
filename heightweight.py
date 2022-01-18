import csv
from os import stat
import statistics
from tkinter import W
import pandas as pd

reader = pd.read_csv("HeightWeight.csv")

height_list = reader["Height(Inches)"].to_list()
weight_list = reader["Weight(Pounds)"].to_list()

#mean median mode for height and weight

height_mean = statistics.mean(height_list)
height_median = statistics.median(height_list)
height_mode = statistics.mode(height_list)
height_stdev = statistics.stdev(height_list)
weight_mean = statistics.mean(weight_list)
weight_median = statistics.median(weight_list)
weight_mode = statistics.mode(weight_list)
weight_stdev = statistics.stdev(weight_list)

print("Mean, median and mode of height is {}, {} and {} respectively".format(height_mean, height_median, height_mode))
print("Mean, median and mode of weight is {}, {} and {} respectively".format(weight_mean, weight_median, weight_mode))

#1, 2 and 3 standard deviations for height 

height_1_stdev_start, height_1_stdev_end = height_mean - height_stdev, height_mean + height_stdev

height_2_stdev_start, height_2_stdev_end = height_mean - (2 * height_stdev), height_mean + (2 * height_stdev)

height_3_stdev_start, height_3_stdev_end = height_mean - (3 * height_stdev), height_mean + (3 * height_stdev)

#1, 2 and 3 standard deviation for weight

weight_1_stdev_start, weight_1_stdev_end = weight_mean - weight_stdev, weight_mean + weight_stdev

weight_2_stdev_start, weight_2_stdev_end = weight_mean - (2 * weight_stdev), weight_mean + (2 * weight_stdev)

weight_3_stdev_start, weight_3_stdev_end = weight_mean - (3 * weight_stdev), weight_mean + (3 * weight_stdev)

# percentage of data within 1, 2, and 3 standard deviations of height

height_list_of_data_within_1_stdev = [result for result in height_list if result > height_1_stdev_start and result < height_1_stdev_end]

height_list_of_data_within_2_stdev = [result for result in height_list if result > height_2_stdev_start and result < height_2_stdev_end]

height_list_of_data_within_3_stdev = [result for result in height_list if result > height_3_stdev_start and result < height_3_stdev_end]

# percentage of data within 1, 2, and 3 standard deviations of weight

weight_list_of_data_within_1_stdev = [result for result in weight_list if result > weight_1_stdev_start and result < weight_1_stdev_end]

weight_list_of_data_within_2_stdev = [result for result in weight_list if result > weight_2_stdev_start and result < weight_1_stdev_end]

weight_list_of_data_within_3_stdev = [result for result in weight_list if result > weight_3_stdev_start and result < weight_1_stdev_end]

# printing data for height and weight (stdev)

print("{}% of data for height lies within 1st standard deviation".format(len(height_list_of_data_within_1_stdev) * 100.0 / len(height_list)))

print("{}% of data for height lies within 2nd standard deviation".format(len(height_list_of_data_within_2_stdev) * 100.0 / len(height_list)))

print("{}% of data for height lies within 3rd standard deviation".format(len(height_list_of_data_within_3_stdev) * 100.0 / len(height_list)))

print("{}% of data for weight lies within 1st standard deviation".format(len(weight_list_of_data_within_1_stdev) * 100.0 / len(weight_list)))

print("{}% of data for weight lies within 2nd standard deviation".format(len(weight_list_of_data_within_2_stdev) * 100.0 / len(weight_list)))

print("{}% of data for weight lies within 3rd standard deviation".format(len(weight_list_of_data_within_3_stdev) * 100.0 / len(weight_list)))