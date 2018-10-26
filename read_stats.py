import pandas
import glob

stats_file_list = (glob.glob(".\\stats\\*.csv"))

for stat_file in stats_file_list:
    print stat_file
    df = pandas.read_csv(stat_file, index_col='DATE', parse_dates=['DATE'])
    df["CHANGE_IN_FOLLOWERS"] = df['FOLLOWERS'].diff(1)
    df["CHANGE_IN_FOLLOWING"] = df['FOLLOWING'].diff(1)
    print(df.tail(5))
