import Functions
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
    best_50_df = Best_50(URL)
    final_NBA50_df = best_50_df(best_50_df, complete_df_merge)
    clean_final_NBA50_df = wrangle_final_NBA50_df(final_NBA50_df)
    NBA_player_stats = get_player_info(clean_final_NBA50_df)
    return NBA_player_stats

    

if __name__ == '__main__':
    main()