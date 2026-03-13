# 投资回报率统计器 (ROI Calculator)


## 功能说明

统计股票的两种投资回报率：
- **公式一**：股息率(TTM) = TTM分红 / 当前股价 × 100% 
- **公式二**：ROE/PB = ROE ÷ PB × 100%

## 支持股票

| 股票 | 股票代码 | 
|------|---------|
| 东阿阿胶 | SZ000423 |
| 五粮液 | SZ000858 |
| 贵州茅台 | SH600519 |
| 洋河股份 | SZ002304 |

## 数据来源

### 股价
- **数据源**：腾讯实时行情API (`get_stock_data_tencent`)

### 财务指标 (ROE、BPS)
- **数据源**：akshare `stock_financial_analysis_indicator_em`
- **PB计算**：股价 / BPS

### 分红数据 (TTM)
- **数据源**：akshare `stock_individual_spot_xq` (雪球接口)
- **字段**：`股息(TTM)` 和 `股息率(TTM)`

## 计算公式

### 公式一：股息率(TTM)
```
股息率(TTM) = TTM分红 / 当前股价 × 100%
```


### 公式二：ROE/PB
```
ROE/PB = ROE ÷ PB × 100%
（注：ROE不带百分号直接相除）
```

## 输出文件

输出目录：`data/output/`

### Excel文件
| 文件名 | 说明 |
|--------|------|
| `roi_YYYYMMDD_HHMMSS.xlsx` | ROI分析数据 |

### 图表文件
| 文件名 | 说明 |
|--------|------|
| `ROI_1_YYYYMMDD_HHMMSS.png` | 口径1（股息率）分析图 |
| `ROI_2_YYYYMMDD_HHMMSS.png` | 口径2（ROE/PB）分析图 |
| `ROI_YYYYMMDD_HHMMSS.png` | 综合对比图 |

## 使用方法

### 方式一：运行Python脚本
```bash
cd D:\code\git\roi_calculator
venv312\Scripts\python.exe main_fast.py
```

### 方式二：运行exe
```bash
dist\ROI_Calculator\ROI_Calculator.exe
```

### 方式三：双击批处理文件
- `start.bat` - 运行main_fast.py
- `start_enhanced.bat` - 运行main_enhanced.py（增强版）

## 自定义股票列表

### 方法一：外部配置文件（推荐）

将 `stocks.json` 文件放在 **exe同级目录** 或 **Python脚本同级目录**，程序会优先读取：

```json
[
    {"name": "东阿阿胶", "symbol": "SZ000423"},
    {"name": "五粮液", "symbol": "SZ000858"},
    {"name": "贵州茅台", "symbol": "SH600519"},
    {"name": "洋河股份", "symbol": "SZ002304"}
]
```

字段说明：
- `name`: 股票名称（显示用）
- `symbol`: 股票代码（必须与腾讯/akshare接口格式一致，如 `SZ000423`、`SH600519`）

**说明**：
- 如果 `stocks.json` 存在，优先使用外部配置
- 如果 `stocks.json` 不存在，使用内置的 `config.py` 配置

### 方法二：修改config.py

直接编辑项目目录下的 `config.py` 文件：

```python
STOCKS = [
    {"name": "新股票1", "symbol": "SZ000001"},
    {"name": "新股票2", "symbol": "SH600000"},
]
```

修改后需要重新构建exe。

## 项目结构

```
D:\code\git\roi_calculator\
├── main_fast.py          # 极速版主程序
├── main_enhanced.py      # 增强版主程序
├── config.py             # 内置股票列表配置
├── stocks.json           # 外部股票列表配置（可选）
├── roi.py                # ROI计算核心逻辑
├── requirements.txt      # Python依赖
├── start.bat             # 启动脚本（极速版）
├── start_enhanced.bat    # 启动脚本（增强版）
├── build.bat             # 构建exe脚本
├── README.md             # 说明文档
├── data/
│   ├── output/           # 输出目录
│   └── log/              # 日志目录
├── dist/
│   └── ROI_Calculator/   # exe构建输出
│       ├── ROI_Calculator.exe
│       └── stocks.json   # 外部配置文件模板（复制到exe同级目录使用）
└── venv312/              # Python 3.12虚拟环境
```

## 构建exe

```bash
build.bat
```

或手动执行：
```bash
venv312\Scripts\python.exe -m PyInstaller --onedir --name ROI_Calculator ...
```

## 日志文件

日志目录：`data/log/`

- `roi_fast_YYYYMMDD.log` - 极速版运行日志
- `roi_enhanced_YYYYMMDD.log` - 增强版运行日志

## 版本历史

### v2.0 (2026-01-16)
- 使用akshare `stock_individual_spot_xq` 接口获取TTM股息数据
- 简化数据源，统一使用雪球TTM数据
- 更新PNG文件命名规则

### v1.0
- 初始版本
- 使用akshare `stock_fhps_em` 接口获取分红数据
- 支持LTM和年度两种分红口径
