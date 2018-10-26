import pandas
import glob
import dropbox
from accounts import token as db_token


def read_all_csvs():
    stats_file_list = (glob.glob(".\\stats\\*.csv"))
    for stat_file in stats_file_list:
        print stat_file
        df = pandas.read_csv(stat_file, index_col='DATE', parse_dates=['DATE'])
        df["CHANGE_IN_FOLLOWERS"] = df['FOLLOWERS'].diff(1)
        df["CHANGE_IN_FOLLOWING"] = df['FOLLOWING'].diff(1)
        print(df.tail(5))


def read_overall_stats():
    return pandas.read_csv(".\\stats\\instaPyStats.csv", parse_dates=['DATE'])


def to_dropbox(dataframe, path, token):
    dbx = dropbox.Dropbox(token)

    df_string = dataframe.to_csv(index=False)
    db_bytes = bytes(df_string)
    dbx.files_upload(
        f=db_bytes,
        path=path,
        mode=dropbox.files.WriteMode.overwrite
    )


dataframe = read_overall_stats()
print dataframe
to_dropbox(dataframe, "/data.csv", db_token)
