# Project 3: NBA-Player-Data
## Description:
* We attempted to analyze statistics on NBA players using machine learning tools, particularly K-Means analysis. We scraped data from https://www.basketball-reference.com/ to cluster players looking at 90 different statistics. Specicifically, we used K-Means testing in Scikit-Learn to cluster players into 8 categories.
# Why Cluster NBA Players?
We wanted to run k-means on NBA players in order to create less biased "player types" than the player types that many basketball fans already have in their mind. Fans and players have many conceptionsof player types; stars, shooters, rim protectors, point guards, small forwards, and many other types and roles of players may be used in the way fans and players understand and analyze NBA games. However these player roles and types can often be biased or unnecessarily restrictive. For instance there are many players that do not fit cleanly into one of the five traditional positions. While it would be disingenuous to say that our analysis is entirely unbiased, we hope that our work can provide new insights into player types and roles. 

## Built With:
* Pandas
* SciKit-Learn
* Matplotlib
* Numpy
* Beautiful Soup
## File Brakdown:
* bref_scrape: scrapes data from baskeball-reference. com and converts datafames to csv format.
* K-Means_final.ipynb: cleans data and runs k-means analysis, producing 8 clusters of players.
* Radar_Chart.ipynb: visualizations of cluster analysis.
## Contributors:
* https://github.com/phamdanielk
* https://github.com.bwalshdtan
* https://github.com/danfujii
* https://github.com/kdol2495
