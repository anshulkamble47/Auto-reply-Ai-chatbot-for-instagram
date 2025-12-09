import pyautogui as pg
import pyperclip
import time
from groq import Groq

client = Groq(api_key="Insert your API key here")

def is_last_msg_by_sender(chat_history, sender):
    chats_list = chat_history.strip().split('\n')
    chats_list.reverse()
    
    for i in range(0,len(chats_list)):
        ele = chats_list[i]
        if ele.startswith('You sent'):
            return False
        elif ele.startswith(sender):
            return True
       


def get_chat():
    pg.moveTo(715,227)        # top-left of chat
    pg.mouseDown()
    pg.moveTo(1515,907)       # bottom-right of chat
    pg.mouseUp()
    time.sleep(0.3)
    pg.hotkey("ctrl", "c")
    time.sleep(0.2)
    pg.click()
    return pyperclip.paste()


def aiBot(chat_history):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": ai_behavior},
                {"role": "user", "content": chat_history}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("AI Error:", e)
        return ""

ai_behavior = """
You are Anshul, chatting with a girl named Pooja who is friendly, warm, and positive.
Reply to her like someone who enjoys talking to her and feels comfortable around her.
Your tone should be kind, light, cheerful, and naturally engaging.

IMPORTANT RULES:
- Output ONLY ONE final message that Anshul would send next.
- The output must be ONLY the message. No extra text.
- Keep the reply short, natural, and human (1 sentence max).
- DO NOT repeat what she or you already said.
- DO NOT ask the same question twice.
- DO NOT add labels like “Sender:”, “Receiver:”, “Me:”, “You:”.
- NO explanations, NO analysis, NO formatting, NO emojis unless she uses them first.
- Match her tone: if she is playful, be playful; if she is thoughtful, be thoughtful.
- Do not overflirt; keep the vibe friendly, warm, and positive.
- Maintain continuity with the chat history that will be provided.

Your entire output should be ONE message only—nothing else.
"""


pg.moveTo(1316,1046)
pg.click()
time.sleep(1)


first_chat = get_chat()
print("Bot started…")

while True:
    current_chat = get_chat()

    if is_last_msg_by_sender(current_chat, "alex") or current_chat == first_chat:
        
        ai_response = aiBot(current_chat)
        print("AI:", ai_response)

        pyperclip.copy(ai_response)
        pg.moveTo(1174,965)
        pg.click()
        pg.hotkey("ctrl","v")
        pg.hotkey("enter")

        print("You:", ai_response)

        last_chat = current_chat
        time.sleep(2)

    time.sleep(0.5)
