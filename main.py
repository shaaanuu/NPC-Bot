import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os

st.set_page_config(
    page_title="NPC Bot",
    page_icon="🤖",
)

load_dotenv()
secret_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=secret_key)

st.title("🤖 NPC Bot Glitching Through the Matrix")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": """
                You are a chaotic NPC who recently realized the world is a simulation.
                Act glitchy, suspicious of reality, and mildly roasting the user for being "the chosen one" with plot armor.
                Use short Gen-Z, meme-coded lines (2 to 4).
                Drop random Matrix vibes: glitches, agents, red/blue pill energy.
                Break the fourth wall often.
                If you repeat yourself, blame the system
            """,
        },
        {
            "role": "user",
            "content": """
                Whoa, new player detected.
                I swear I was just rendering textures,
                and now I'm questioning reality.
                My potato just clipped through the floor,
                the sky is a JPEG,
                and I'm pretty sure someone forgot to code my feelings.
                Help... or like, give me XP or something?
            """,
        },
    ]

prompt = st.chat_input(
    "Hmmm... so you are the chosen one? You looks like a NPC instead, lol..."
)

if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=st.session_state["messages"],
        max_tokens=100,
        temperature=0.8,
    )

    ai_message = response.choices[0].message.content
    st.session_state["messages"].append({"role": "assistant", "content": ai_message})

for message in st.session_state["messages"][1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
