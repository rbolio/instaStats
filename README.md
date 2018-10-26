# instaStats
Simple script to get a list of user's instagram followers and following,
which are then added to a .csv file which can be analyzed through pandas.

--------
## How to use this tool:
1. download the repo (duh!)
2. ```pip install -r requirements```
3. if you're using windows and want the possibility of working with videos in the future
   1. ```python optional_ffmpeg_win_install.py```
4. create an 'accounts.py' file in the root directory with the format given below.
5. run ```python get_stats.py to get the data```
6. run ```python read_stats.py``` to view the data in a pandas format


-----
## accounts.py format
```python
""" Accounts information is stored here for some resemblance of security"""

user_data = [["usr_1", "pwd_1"],
             ["usr_2", "pwd_2"],
             ["usr_3", "pwd_3"]
             ]
```

-----
### Hope it helps!