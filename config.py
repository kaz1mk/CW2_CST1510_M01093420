import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class CFG:
    gemini_key = os.getenv("GEMINI_API_KEY")
    gemini_model = "gemini-2.5-flash"
    db_path = os.getenv("DB_PATH", "multi_domain_platform.db")  # default path


    @staticmethod
    def get_gemini_model(model_name=None):
        model_name = model_name or CFG.gemini_model
        if not CFG.gemini_key:
            raise RuntimeError("GEMINI_API_KEY not found in .env")
        genai.configure(api_key=CFG.gemini_key)
        return genai.GenerativeModel(model_name)
