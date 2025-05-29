class BestBoStrategy(BestStrategy):
    '''
    This class provides the method to optimize the BO strategy
    symbols: a list of symbols to be optimzied on, e.g., ['BTCUSDT']
    freq: currently supported values: '1h' or '4h'
    res_dir: the output directory
    flag_filter: currently supported fitlers: 'vol', 'ang', default: None
    flag_ts_stop: flag to turn on/off trailing stop
    strategy: 'bo'
    '''
    def __init__(self,
                 symbols: Union[str, list],
                 freq: str,
                 res_dir: str,
                 flag_filter: str = None,
                 flag_stop: Union[str, list] = None,
                 flag_acc_return: bool = True,
                 strategy: str = 'bo',
                 ):
        super().__init__(symbols, freq, res_dir, flag_filter, strategy)
        self.flag_stop = [flag_stop] if isinstance(flag_stop, str) else flag_stop
        self.flag_acc_return = flag_acc_return
        self.generate_best_params()

    def _get_strategy(self, strategy):
        return get_strategy(strategy)

    def _get_filter(self, **kwargs):
        return get_filter(flag_filter=self.flag_filter, **kwargs)

    def _get_variables(self, **kwargs):
        if self.flag_stop:
            return create_bo_variables_with_stop(flag_stop=self.flag_stop, **kwargs)
        return create_bo_variables(**kwargs)

    def _get_grid_search(self):
        if self.flag_filter == 'vol':
            return self.grid_search_vol_params()
        elif self.flag_filter == 'ang':
            return self.grid_search_ang_params()
        else:
            return self.grid_search_params()

    def get_best_params(self, total_best_params, n=10):
        total_best_params = pd.DataFrame(total_best_params)
        total_best_params['sharpe'] = (total_best_params['sharpe'] + 0.05).round(1)
        total_best_params['gap'] = total_best_params['long_window'] - total_best_params['short_window']
        if 'ohlcstx_sl_stop' in total_best_params.columns:
            total_best_params = (
                total_best_params
                .query('gap > 0')
                .sort_values(
                    by=['sharpe', 'gap', 'short_window', 'ohlcstx_sl_stop'],
                    ascending=[True, True, False, False])
            )
        else:
            total_best_params = (
                total_best_params
                .query('gap > 0')
                .sort_values(
                    by=['sharpe', 'gap', 'short_window'],
                    ascending=[True, True, False]
                    )
            )
        print(total_best_params)
        return total_best_params.tail(1).to_dict(orient='records')[0] if not total_best_params.empty else None
