from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
model = ChatOpenAI(model_name="gpt-4", api_key=st.secrets['api_key'], temperature=0)
st.title("Review Analysis")
Student = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

# ⚠️ Fix this too: You're referencing "Review" instead of "Student"
structured_model = model.with_structured_output(Student)
review=st.text_input("Enter your review")


if st.button('Summarize'):
    # ✅ Send the final string to the model
    
    result = structured_model.invoke(review)

    # ✅ Show model output
    st.write(result)
