from InstagramAPI import InstagramAPI as instapi
import datetime
import csv
from pathlib2 import Path
from accounts import user_data

accounts = user_data


def get_data(account):
    InstagramAPI = instapi(account[0], account[1])
    InstagramAPI.login()
    InstagramAPI.getProfileData()
    return InstagramAPI, InstagramAPI.LastJson['user']['pk']


def append_to_csv(usr_name, following, followers):
    filename = './stats/' + usr_name + '.csv'
    today = datetime.datetime.today().strftime('%d/%m/%Y')
    with open(filename, mode='a') as insta_file:
        stat_writer = csv.writer(insta_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        stat_writer.writerow([today, followers, following])
    return 'Finished appending data to "' + usr_name + '" history file'


def generate_new_csv(usr_name):
    my_file = Path("./stats/" + usr_name + ".csv")
    if my_file.is_file():
        return 'The history file for "' + usr_name + '" already exists'
    else:
        filename = './stats/' + usr_name + '.csv'
        with open(filename, mode='a') as insta_file:
            stat_writer = csv.writer(insta_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            stat_writer.writerow(['DATE', 'FOLLOWERS', 'FOLLOWING'])
        return "New history file created for user: " + usr_name


def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return len(followers)


def getTotalFollowing(api, user_id):
    """
    Returns the list of following of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    following = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        following.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return len(following)


def append_to_csv_overall(usr_name, following, followers):
    filename = './stats/instaPyStats.csv'
    today = datetime.datetime.today().strftime('%d/%m/%Y')
    with open(filename, mode='a') as insta_file:
        stat_writer = csv.writer(insta_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        stat_writer.writerow([today, usr_name, followers, following])
    return 'Finished appending data from "' + usr_name + '" to overall history file'


def generate_new_csv_overall():
    my_file = Path("./stats/instaPyStats.csv")
    if my_file.is_file():
        return 'The overall File already exists'
    else:
        filename = "./stats/instaPyStats.csv"
        with open(filename, mode='a') as insta_file:
            stat_writer = csv.writer(insta_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            stat_writer.writerow(['DATE', 'USER_NAME', 'FOLLOWERS', 'FOLLOWING'])
        return "New overall history file created"


def run():
    print generate_new_csv_overall()

    for account in accounts:
        try:
            api, usr_id = get_data(account)
            user_name = account[0]
            followers = getTotalFollowers(api, usr_id)
            following = getTotalFollowing(api, usr_id)
            print generate_new_csv(user_name)
            print append_to_csv(user_name, following, followers)
            print append_to_csv_overall(user_name, following, followers)
        except:
            print "Fucking " + str(account[0]) + " didn't work right"


if __name__ == '__main__':
    run()
    print "Done saving stats!"
