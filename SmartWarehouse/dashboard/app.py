import sys
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from database.db import init_database, get_events, get_inventory


st.set_page_config(
    page_title="Smart Warehouse Dashboard",
    page_icon="🏭",
    layout="wide"
)

init_database()

st.title("🏭 Smart Warehouse Dashboard")
st.caption("Safety & Inventory Management System")

events = get_events(200)
inventory = get_inventory()

event_types = [row[3] for row in events]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Events", len(events))
col2.metric("No Helmet", event_types.count("NO_HELMET"))
col3.metric("No Vest", event_types.count("NO_VEST"))
col4.metric("Danger Zone", event_types.count("DANGER_ZONE"))

st.divider()

st.subheader("Safety Events")

if events:
    df = pd.DataFrame(
        events,
        columns=["ID", "Timestamp", "Camera", "Event", "Confidence", "Image"]
    )
    st.dataframe(df, use_container_width=True)
else:
    st.info("ยังไม่มีข้อมูล Event")

st.subheader("Inventory")

if inventory:
    inventory_df = pd.DataFrame(
        inventory,
        columns=["ID", "Product Code", "Product Name", "Quantity", "Location"]
    )
    st.dataframe(inventory_df, use_container_width=True)
else:
    st.info("ยังไม่มีข้อมูล Inventory")
