"""Module to read Instagram statistics and upload them to Dropbox for safekeeping"""

import pandas
import dropbox
from accounts import token as db_token
from os import listdir
from os.path import isfile, join
from get_stats import run


def read_overall_stats(filename):
    """Reads csv file and returns it as a pandas data frame"""
    return pandas.read_csv(".\\stats\\" + filename, parse_dates=['DATE'])


def upload_to_dropbox(dataframe, path, token):
    """uploads pandas dataframe to dropbox as csv"""
    dbx = dropbox.Dropbox(token)
    df_string = dataframe.to_csv(index=False)
    db_bytes = bytes(df_string)
    dbx.files_upload(
        f=db_bytes,
        path=path,
        mode=dropbox.files.WriteMode.overwrite
    )


def all_files_upload():
    """Gets files from stats folder and uploads them sends them to dropbox function"""
    file_data_path = './stats/'
    file_list = [f for f in listdir(file_data_path) if isfile(join(file_data_path, f))]
    for individual_file in file_list:
        upload_path = "/individual_reports/" + individual_file
        if 'instaPyStats.csv' in individual_file:
            upload_path = "/" + individual_file
        if '.csv' in individual_file:
            data_frame = read_overall_stats(individual_file)
            upload_to_dropbox(data_frame, upload_path, db_token)


if __name__ == '__main__':
    run()  # runs the 'Get stats' code
    all_files_upload()
