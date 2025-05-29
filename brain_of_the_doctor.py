#STEP 1: SETUP GROQ API KEY
from dotenv import load_dotenv
import os
load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
#print(GROQ_API_KEY)

#STEP 2: CONVERT IMAGE TO REQUIRED FORMAT
import base64
#image_path="acne.jpg"
def encode_image(image_path):
 image_file=open(image_path,"rb")
 return base64.b64encode(image_file.read()).decode('utf-8')

#STEP 3: SETUP MULTIMODAL LLM
from groq import Groq

model="meta-llama/llama-4-scout-17b-16e-instruct"
query="Is there something wrong with my face?"
def analyze_image_with_query(query,model, encoded_image):
    client = Groq()
    
    messages=[
        {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": query
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}",
                },
            
            },
            
        ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content