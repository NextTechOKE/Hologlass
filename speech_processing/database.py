import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

supabase.table("summaries").insert({"content": "this is a summary"}).execute()

result = supabase.table("summaries").select("*").execute().data[-1]

print(result)