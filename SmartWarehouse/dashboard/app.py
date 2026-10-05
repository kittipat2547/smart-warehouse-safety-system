import os
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from database.db import get_event_counts, get_events, get_inventory


st.set_page_config(
    page_title="Smart Warehouse Dashboard",
    page_icon="🏭",
    layout="wide",
)

st.title("🏭 Smart Warehouse Dashboard")
st.caption("Safety & Inventory Management System")

raw_events = get_events(200)
inventory = get_inventory()
counts = get_event_counts()


def safe_event_counts(event_name):
    return counts.get(event_name, 0)


col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Events", len(raw_events))
col2.metric("No Helmet", safe_event_counts("NO_HELMET"))
col3.metric("No Vest", safe_event_counts("NO_VEST"))
col4.metric("Danger Zone", safe_event_counts("DANGER_ZONE"))

st.divider()

st.subheader("Safety Events")
if raw_events:
    event_df = pd.DataFrame(
        raw_events,
        columns=["ID", "Timestamp", "Camera", "Event", "Confidence", "Image"],
    )
    event_df = event_df.sort_values("ID", ascending=False).reset_index(drop=True)
    st.dataframe(event_df, use_container_width=True, hide_index=True)

    recent_events = event_df.head(5)
    st.write("Recent event images")
    event_cols = st.columns(min(5, len(recent_events)))
    for idx, row in recent_events.iterrows():
        image_path = row["Image"]
        if image_path and os.path.exists(image_path):
            with event_cols[idx % len(event_cols)]:
                st.image(image_path, caption=f"{row['Event']} - {row['Timestamp']}", width=220)
else:
    st.info("ยังไม่มีข้อมูล Event")

st.subheader("Inventory")
if inventory:
    inventory_df = pd.DataFrame(
        inventory,
        columns=["ID", "Product Code", "Product Name", "Quantity", "Location"],
    )
    st.dataframe(inventory_df, use_container_width=True, hide_index=True)
else:
    st.info("ยังไม่มีข้อมูล Inventory")
