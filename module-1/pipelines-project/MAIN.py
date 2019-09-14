from Functions import , get_players, clean_df_players, get_player_data, wrangle_df_player_data, get_season_stats

from outputs import print_file

def main(): 
    mm = MetroLineas()
    mm.scan()

    urls = mm.urls_lineas

    metro = {}
    for url in urls: 
        l = Linea(url)
        l.scan()
        metro[l.name] = l.paradas
    print(metro)
    print_file(metro)

 
    



    


if __name__ == "__main__": 
    main()
