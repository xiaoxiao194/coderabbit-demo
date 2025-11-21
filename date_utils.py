from datetime import datetime

def days_between(date1, date2):
    # 故意写错格式
    d1 = datetime.strptime(date1, "%Y/%m/%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")

    # 故意去掉 abs
    return (d2 - d1).days
