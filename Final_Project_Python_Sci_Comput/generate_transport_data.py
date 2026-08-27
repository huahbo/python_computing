"""生成交通网络合成数据：stations.csv, edges.csv, flows.csv"""

import numpy as np
import pandas as pd
from itertools import combinations
from datetime import datetime, timedelta

np.random.seed(42)

# 站点
n_stations = 10
stations = pd.DataFrame({
    "station_id": range(n_stations),
    "name": [f"Station_{i}" for i in range(n_stations)],
    "x": np.random.uniform(0, 10, size=n_stations),
    "y": np.random.uniform(0, 10, size=n_stations),
})
stations.to_csv("stations.csv", index=False)

# 边（线路）
edges_list = []
for i, j in combinations(range(n_stations), 2):
    if np.random.rand() < 0.3:  # 30% 概率连边
        travel_time = np.random.randint(3, 15)
        capacity = np.random.randint(500, 2000)
        edges_list.append((i, j, travel_time, capacity))

edges = pd.DataFrame(edges_list, columns=["from_station", "to_station", "travel_time", "capacity"])
edges["edge_id"] = edges.index
edges.to_csv("edges.csv", index=False)

# 选一条边生成客流时间序列
if len(edges) == 0:
    raise ValueError("没有生成任何边，请调整随机种子或概率。")

target_edge = edges.iloc[0]
edge_id = target_edge["edge_id"]

start_date = datetime(2024, 1, 1)
n_days = 200
dates = [start_date + timedelta(days=i) for i in range(n_days)]

base_flow = 1000
flows = []
for i, d in enumerate(dates):
    weekday = d.weekday()
    weekend_factor = 1.2 if weekday >= 5 else 1.0
    seasonal = 100 * np.sin(2 * np.pi * i / 30)
    noise = np.random.normal(0, 50)
    flow = max(0, base_flow * weekend_factor + seasonal + noise)
    flows.append(flow)

flow_df = pd.DataFrame({
    "date": [d.strftime("%Y-%m-%d") for d in dates],
    "edge_id": [edge_id] * len(dates),
    "passenger_flow": flows,
})
flow_df.to_csv("flows.csv", index=False)

print("已生成 stations.csv, edges.csv, flows.csv")
