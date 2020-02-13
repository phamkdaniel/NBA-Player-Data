from contextlib import closing
from requests import get

from bs4 import BeautifulSoup
import pandas as pd

from functools import reduce

def get_page(url):
    """ Returns page from url as soup.

    :param url: url of page
    :type url: string
    """
    with closing(get(url)) as resp:
        html = resp.content
    return BeautifulSoup(html, 'html.parser')

def get_table(url):
    """ Grabs stats table from basketball-reference and converts to DataFrame.

    :param url: url of page
    :type url: string
    """
    soup = get_page(url)
    table = soup.find('table')
    tr = table.find_all('tr')

    table_stats = []
    for i in range(len(tr)):
        td = tr[i].find_all('td')
        if td:
            row_dict = {'rank': tr[i].find('th').text}
            for item in td:
                row_dict[item['data-stat']] = item.text        
            table_stats.append(row_dict)

    stats_df = pd.DataFrame(table_stats)
    return stats_df

def get_stats(year):
    """ Given the ending year of season, grabs and merges tables from basketball-reference 
    and exports to csv.

    :param year: ending year of basketball season
    :type year: string
    """
    # base url of basketball-reference and stat metrics
    base_url = "https://www.basketball-reference.com/leagues/"
    stat_measures = [
        "totals",
        "per_game",
        "per_minute",
        "per_poss",
        "advanced"
    ]

    # create list of DataFrames from each page
    df_list = []
    for metric in stat_measures:
        url = f'{base_url}NBA_{year}_{metric}.html'
        print(f'processing {url}')
        df_list.append(get_table(url))

    # merge all stats DataFrames
    merged_df = reduce(lambda x,y: pd.merge(x,y), df_list)

    # remove dummy columns
    merged_df = merged_df.drop(columns = ['ws-dum', 'bpm-dum', ''])

    # set index
    merged_df = merged_df.set_index('rank')

    # save to csv
    merged_df.to_csv(f'Data/NBA_player_stats_{year}_raw.csv')

    print('done')
    return merged_df

if __name__=="__main__":
    year = 2019
    get_stats(year)
