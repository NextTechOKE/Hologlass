import streamlit as st
import argparse

import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)



result = supabase.table("summaries").select("*").execute().data[-1]
st.title("Hologlass Dashboard")
st.text("Your recent conversation and its recap will be displayed below")
st.header("Transcript")
st.text(result["transcript"])
# st.text(args.transcripts)
st.header("Summary")
st.text(result["summary"])
# st.text(args.summary)
