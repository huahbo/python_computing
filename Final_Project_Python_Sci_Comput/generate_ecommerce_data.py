"""生成电商订单合成数据 ecommerce_orders.csv

字段：
- order_id
- order_date
- user_id
- product_id
- category
- price
- quantity
- city
- channel
- ad_campaign
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

n_orders = 2000

start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(365)]

categories = ["Electronics", "Clothes", "Books", "Food", "Home"]
cities = ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Hangzhou"]
channels = ["web", "app"]
campaigns = ["A", "B"]

rows = []
for i in range(n_orders):
    order_date = random.choice(dates)
    user_id = f"U{np.random.randint(1000, 2000)}"
    product_id = f"P{np.random.randint(100, 500)}"
    category = random.choice(categories)
    base_price = {
        "Electronics": (500, 2000),
        "Clothes": (50, 300),
        "Books": (20, 150),
        "Food": (10, 100),
        "Home": (80, 600),
    }[category]
    price = np.round(np.random.uniform(*base_price), 2)
    quantity = np.random.randint(1, 5)
    city = random.choice(cities)
    channel = random.choice(channels)
    ad_campaign = random.choice(campaigns)

    rows.append({
        "order_id": f"O{i+1:05d}",
        "order_date": order_date.strftime("%Y-%m-%d"),
        "user_id": user_id,
        "product_id": product_id,
        "category": category,
        "price": price,
        "quantity": quantity,
        "city": city,
        "channel": channel,
        "ad_campaign": ad_campaign,
    })

df = pd.DataFrame(rows)
df.to_csv("ecommerce_orders.csv", index=False, encoding="utf-8")
print("已生成 ecommerce_orders.csv，样本数：", len(df))
