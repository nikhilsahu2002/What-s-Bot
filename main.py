import streamlit as st

def process_message(user_input, media_file, chat_history):
    # Predefined responses
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "help": "I am a simple auto-reply bot. I can handle text messages and ignore media."
    }

    # Check if the user input has a predefined response
    for keyword, reply in responses.items():
        if keyword in user_input:
            return reply

    # Check if the user uploaded a media file
    if media_file is not None:
        return "Sorry, I can't handle media messages."

    # If no keyword is matched and no media file is uploaded, return a generic response
    return "Thanks for your message! I'll get back to you soon."

def main():
    st.title("WhatsApp Auto-Reply Bot")

    # Use session_state to persist data between button clicks
    session_state = st.session_state
    if not hasattr(session_state, 'chat_history'):
        session_state.chat_history = []

    user_input = st.text_input("You:")
    media_file = st.file_uploader("Upload a media file", type=["jpg", "png", "gif", "mp4"])

    if st.button("Send"):
        user_message = f"You: {user_input}"
        session_state.chat_history.append(user_message)
        
        response_text = process_message(user_input, media_file, session_state.chat_history)
        bot_message = f"Bot: {response_text}"
        session_state.chat_history.append(bot_message)

        # Display the chat history
        st.text_area("Chat History", value="\n".join(session_state.chat_history), height=200)

if __name__ == "__main__":
    main()
