from typing import Dict, Any


class ROIResult:
    """投资回报率计算结果"""

    def __init__(self, stock_name: str, symbol: str, current_price: float,
                 dividend_per_share: float, roe: float, pb: float,
                 roi_formula1: float, roi_formula2: float):
        self.stock_name = stock_name
        self.symbol = symbol
        self.current_price = current_price
        self.dividend_per_share = dividend_per_share
        self.roe = roe
        self.pb = pb
        self.roi_formula1 = roi_formula1
        self.roi_formula2 = roi_formula2
        self.data_source = 'N/A'
        self.dividend_source = 'N/A'
        self.pb_source = 'N/A'
        # 增强版新增字段
        self.interim_dividend = 0  # 中期分红
        self.annual_dividend = 0   # 年度分红
        self.guaranteed_note = ''  # 保底分红备注


class ROICalculator:
    """投资回报率计算器"""

    def calculate(self, stock_data: Dict[str, Any]) -> ROIResult:
        """计算投资回报率"""
        name = stock_data.get('name', '')
        symbol = stock_data.get('symbol', '')
        current_price = stock_data.get('current_price', 0)

        financial = stock_data.get('financial', {})
        dividend_data = stock_data.get('dividend', {})

        dividend_per_share = self._get_dividend_per_share(dividend_data)
        roe = financial.get('roe', 0)
        pb = financial.get('pb', 0)

        # 如果有股息率数据（来自F10），直接使用
        dividend_yield = stock_data.get('dividend_yield', 0)
        if dividend_yield > 0:
            roi_formula1 = dividend_yield
        else:
            roi_formula1 = self._calc_roi_formula1(dividend_per_share, current_price)
        
        roi_formula2 = self._calc_roi_formula2(roe, pb)

        return ROIResult(
            stock_name=name,
            symbol=symbol,
            current_price=current_price,
            dividend_per_share=dividend_per_share,
            roe=roe,
            pb=pb,
            roi_formula1=roi_formula1,
            roi_formula2=roi_formula2
        )

    def _get_dividend_per_share(self, dividend_data: Dict[str, Any]) -> float:
        """获取每股分红"""
        if not dividend_data:
            return 0.0

        dividends = dividend_data.get('dividends', [])
        if not dividends:
            return 0.0

        latest = dividends[0]
        cash_div = latest.get('cash_div', 0)
        bonus_ratio = latest.get('bonus_ratio', 0)

        return float(cash_div) + float(bonus_ratio) * 0.1

    def _calc_roi_formula1(self, dividend: float, price: float) -> float:
        """公式一：分红 / 当前股价"""
        if price <= 0:
            return 0.0
        return (dividend / price) * 100

    def _calc_roi_formula2(self, roe: float, pb: float) -> float:
        """公式二：ROE / PB
        计算时不带百分号，直接相除
        例如：ROE=15.45, PB=4.41 → 15.45 / 4.41 = 3.50%
        """
        if pb <= 0:
            return 0.0
        return (roe / pb)

    def format_result(self, result: ROIResult) -> str:
        """格式化输出结果"""
        lines = [
            f"\n{'='*60}",
            f"  {result.stock_name} ({result.symbol})",
            f"{'='*60}",
            f"  当前股价: {result.current_price:.2f} 元",
            f"  每股分红: {result.dividend_per_share:.3f} 元",
            f"  ROE: {result.roe:.2f}%",
            f"  PB: {result.pb:.2f}",
            f"{'-'*60}",
            f"  投资回报率(公式一): {result.roi_formula1:.2f}%",
            f"  投资回报率(公式二): {result.roi_formula2:.2f}%",
            f"{'='*60}"
        ]
        return '\n'.join(lines)
