from jqdatasdk import *
auth('13585707695', 'woshidi1')

q=query(finance.FUND_MAIN_INFO).filter(finance.FUND_MAIN_INFO.underlying_asset_type_id==402001)
df=finance.run_query(q)
df.to_csv('data/stock_fund_info.csv')

for main_code in df['main_code']:
    q_net_value=query(finance.FUND_NET_VALUE).filter(finance.FUND_NET_VALUE.code==str(main_code)).order_by(finance.FUND_NET_VALUE.day.desc())
    df_net_value=finance.run_query(q_net_value)
    df_net_value.to_csv('data/fund_net_value_' + main_code + '.csv')

