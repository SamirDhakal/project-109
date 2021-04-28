import pandas as pd
import statistics
import csv

df = pd.read_csv('StudentsPerformance.csv')
math = df['math score'].tolist()
reading = df['reading score'].tolist()
writing = df['writing score'].tolist()

math_mean = statistics.mean(math)
reading_mean = statistics.mean(reading)
writing_mean = statistics.mean(writing)

math_median = statistics.median(math)
reading_median = statistics.median(reading)
writing_median = statistics.median(writing)

math_mode = statistics.mode(math)
reading_mode = statistics.mode(reading)
writing_mode = statistics.mode(writing)

math_sd = statistics.stdev(math)
reading_sd = statistics.stdev(reading)
writing_sd = statistics.stdev(writing)

print("Mean, median and mode of math score is {}, {}, {}".format(math_mean, math_median, math_mode))
print("Mean, median and mode of reading score is {}, {}, {}".format(reading_mean, reading_median, reading_mode))
print("Mean, median and mode of writing score is {}, {}, {}".format(writing_mean, writing_median, writing_mode))

math_first_sd_start, math_first_sd_end = math_mean - math_sd, math_mean + math_sd
math_second_sd_start, math_second_sd_end = math_mean - (2*math_sd), math_mean + (2*math_sd)
math_third_sd_start, math_third_sd_end = math_mean - (3*math_sd), math_mean + (3*math_sd)

reading_first_sd_start, reading_first_sd_end = reading_mean - reading_sd, reading_mean + reading_sd
reading_second_sd_start, reading_second_sd_end = reading_mean - (2*reading_sd), reading_mean + (2*reading_sd)
reading_third_sd_start, reading_third_sd_end = reading_mean - (3*reading_sd), reading_mean + (3*reading_sd)

writing_first_sd_start, writing_first_sd_end = writing_mean - writing_sd, writing_mean + writing_sd
writing_second_sd_start, writing_second_sd_end = writing_mean - (2*writing_sd), writing_mean + (2*writing_sd)
writing_third_sd_start, writing_third_sd_end = writing_mean - (3*writing_sd), writing_mean + (3*writing_sd)

math_listofdata_within1sd = [result for result in math if result > math_first_sd_start and result < math_first_sd_end]
math_listofdata_within2sd = [result for result in math if result > math_second_sd_start and result < math_second_sd_end]
math_listofdata_within3sd = [result for result in math if result > math_third_sd_start and result < math_third_sd_end]

reading_listofdata_within1sd = [result for result in reading if result > reading_first_sd_start and result < reading_first_sd_end]
reading_listofdata_within2sd = [result for result in reading if result > reading_second_sd_start and result < reading_second_sd_end]
reading_listofdata_within3sd = [result for result in reading if result > reading_third_sd_start and result < reading_third_sd_end]

writing_listofdata_within1sd = [result for result in writing if result > writing_first_sd_start and result < writing_first_sd_end]
writing_listofdata_within2sd = [result for result in writing if result > writing_second_sd_start and result < writing_second_sd_end]
writing_listofdata_within3sd = [result for result in writing if result > writing_third_sd_start and result < writing_third_sd_end]

print("{}% of math data lies within 1sd".format(len(math_listofdata_within1sd)*100.0/len(math)))
print("{}% of math data lies within 2sd".format(len(math_listofdata_within2sd)*100.0/len(math)))
print("{}% of math data lies within 3sd".format(len(math_listofdata_within3sd)*100.0/len(math)))

print("{}% of reading data lies within 1sd".format(len(reading_listofdata_within1sd)*100.0/len(reading)))
print("{}% of reading data lies within 2sd".format(len(reading_listofdata_within2sd)*100.0/len(reading)))
print("{}% of reading data lies within 3sd".format(len(reading_listofdata_within3sd)*100.0/len(reading)))

print("{}% of writing data lies within 1sd".format(len(writing_listofdata_within1sd)*100.0/len(writing)))
print("{}% of writing data lies within 2sd".format(len(writing_listofdata_within2sd)*100.0/len(writing)))
print("{}% of writing data lies within 3sd".format(len(writing_listofdata_within3sd)*100.0/len(writing)))