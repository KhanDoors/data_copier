import pandas as pd


fp = "/Users/syykhan/desktop/retail_db_json/order_items/part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e"


df = pd.read_json(fp, lines=True)

print(df.count())
print(df.describe())


df.columns
df.dtypes

df[["order_item_order_id", "order_item_subtotal"]]

df[df["order_item_order_id"] == 2]
