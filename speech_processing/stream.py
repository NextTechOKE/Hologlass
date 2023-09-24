import streamlit as st
import argparse

import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Create an ArgumentParser object
# parser = argparse.ArgumentParser()

# Add arguments for transcripts and summary
# parser.add_argument("--transcripts", type=str, help="Transcript text")
# parser.add_argument("--summary", type=str, help="Summary text")

# Parse the command-line arguments
# args = parser.parse_args()




st.title("Transcript and Summary")
st.header("Transcript")
# st.text(args.transcripts)
st.header("Summary")
result = supabase.table("summaries").select("*").execute().data[-1]
st.text(result["content"])
# st.text(args.summary)
