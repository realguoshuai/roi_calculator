# 投资回报率统计器配置
#
# 数据来源:
# - 价格: 腾讯实时API (get_stock_data_tencent)
# - ROE/BPS: akshare stock_financial_analysis_indicator_em
# - 分红(TTM): akshare stock_individual_spot_xq (雪球接口)
#
# 字段说明:
# - 股息(TTM): 最近12个月累计分红
# - 股息率(TTM): TTM股息率

# 默认股票列表
STOCKS = [
    {"name": "东阿阿胶", "symbol": "SZ000423"},
    {"name": "五粮液", "symbol": "SZ000858"},
    {"name": "贵州茅台", "symbol": "SH600519"},
    {"name": "洋河股份", "symbol": "SZ002304"}
]

# 保底分红备注（从公司公告获取，需要手动更新）
# 说明：部分公司会在年报中披露未来三年保底分红承诺
GUARANTEED_DIVIDEND_NOTES = {
    "SH600519": "【保底分红】贵州茅台：需查阅公司公告确认是否有未来三年保底分红承诺",
    "SZ000858": "【保底分红】五粮液：需查阅公司公告确认是否有未来三年保底分红承诺",
    "SZ000423": "【保底分红】东阿阿胶：需查阅公司公告确认是否有未来三年保底分红承诺",
    "SZ002304": "【保底分红】洋河股份：需查阅公司公告确认是否有未来三年保底分红承诺",
}

# 自定义ROE配置（覆盖接口数据）
# 优先级：自定义ROE > 年度ROE > 季度ROE
CUSTOM_ROE = {
    "SZ002304": 20.0,  # 洋河股份ROE自定义20%
}

# 输出目录
DATA_DIR = "data/output"
