from Functions import get_players, clean_df_players, get_player_data, wrangle_df_player_data, get_season_stats

from outputs import print_file

def main():
    df_players = get_players()
    filtered_players = clean_df_players(df_players)
    df_player_data = get_player_data()
    filtered_player_data = clean_df_players(df_player_data)
    df_season_stats = get_season_stats()
    filtered_df_season_stats = clean_df_season_stats(df_season_stats)
    complete_df_merge = merging_dfs(filtered_players,filtered_player_data,filtered_df_season_stats)
    filtered_complete_df = wrangle_complete_df(complete_df_merge)
    return filtered_complete_df

if __name__ == '__main__':
    main()
    

    '''
    
    max_pob = analyze_1(filtered)
    chart = visualize_1(max_pob)
    save_viz_3(chart, 'Most populated countries')
    pctchange = analyze_2(filtered)
    chart_pct = visualize_2(pctchange)
    save_viz_3(chart_pct, 'Population Percentage Change')
    '''