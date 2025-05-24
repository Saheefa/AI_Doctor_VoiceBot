#STEP 1: SETUP GROQ API KEY
from dotenv import load_dotenv
import os
load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#STEP 2: CONVERT IMAGE TO REQUIRED FORMAT
import base64
image_path="acne.jpg"
image_file=open(image_path,"rb")
encoded_image=base64.b64encode(image_file.read()).decode('utf-8')

#STEP 3: SETUP MULTIMODAL LLM
from groq import Groq
client=Groq
model="meta-llama/llama-4-scout-17b-16e-instruct"
