# Challenge: Insight Donation Analytics Challenge

Using political campaign contributions data, analyze loyalty trends, namely identify areas of repeat donors and calculate how much they're spending. 
The Federal Election Commission regularly publishes campaign contributions, and while we don’t want to pull specific donors from those files — because using that information for fundraising or commercial purposes is illegal — we want to identify areas (zip codes) that could be sources of repeat campaign contributions. 

# Dependencies
Written in Python 3.x
```
import sys
import math
import re
import bisect
from datetime import datetime
```

# Challenge summary
Given two input files: 

1. `percentile.txt`, holds a single value -- the percentile value (1-100) used by python script to calculate specific percentile

2. `itcont.txt`, has a line for each campaign contribution that was made on a particular date from a donor to a political campaign, committee or other similar entity. 

write a script that processes each line of `itcont.txt`. For each record identified as coming from a repeated donor, calculate the running perceintle of contributions from repeat donors, total number of transactions from repeat donors and total amount of donations streaming in from repeat donors so far for that calendar year, recipient and zip code. 


#### Identifying repeat donors
For the purposes of this challenge, if a donor had previously contributed to any recipient listed in the `itcont.txt` file in any prior calendar year, that donor is considered a repeat donor. Also, for the purposes of this challenge, you can assume two contributions are from the same donor if the names and zip codes are identical.


## Percentile computation

The first line of `percentile.txt` contains the percentile you should compute for these given input pair. For the percentile computation use the **nearest-rank method** [as described by Wikipedia](https://en.wikipedia.org/wiki/Percentile).



## Repo directory structure

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── donation-analytics.py
    ├── input
    │   └── percentile.txt
    │   └── itcont.txt
    ├── output
    |   └── repeat_donors.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── percentile.txt
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── repeat_donors.txt
            ├── your-own-test_1
                ├── input
                │   └── your-own-input-for-itcont.txt
                |── output
                    └── repeat_donors.txt

