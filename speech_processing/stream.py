import streamlit as st
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add arguments for transcripts and summary
parser.add_argument("--transcripts", type=str, help="Transcript text")
parser.add_argument("--summary", type=str, help="Summary text")

# Parse the command-line arguments
args = parser.parse_args()

st.title("Transcript and Summary")
st.header("Transcript")
st.text(args.transcripts)
st.header("Summary")
st.text(args.summary)
