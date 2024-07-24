import streamlit as st
from bot.bot import start_bot, stop_bot, send_message

st.title('Telegram Bot Manager')

if st.button('Start Bot'):
    start_bot()
    st.success('Bot started successfully!')

if st.button('Stop Bot'):
    stop_bot()
    st.success('Bot stopped successfully!')

chat_id = st.text_input('Enter chat ID to send a message:')
message_text = st.text_area('Message to send:')
if st.button('Send Message'):
    if chat_id and message_text:
        send_message(chat_id, message_text)
        st.success('Message sent successfully!')
    else:
        st.error('Please provide both chat ID and message text.')