import asyncio
import os
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.connectors.ai.open_ai import OpenAIChatPromptExecutionSettings

load_dotenv()


async def interactive_chat(kernel):
    chat_history = ChatHistory()
    chat_completion = kernel.get_service("groq-chat")
    settings = OpenAIChatPromptExecutionSettings()
    
    print("\n" + "="*70)
    print("🤖 Semantic Kernel - Minimaler Konsolenchat")
    print("="*70)
    print("\nTipp: Geben Sie 'exit', 'quit' oder 'bye' ein, um zu beenden.")
    print("Sie können auch 'clear' eingeben, um den Chat-Verlauf zu löschen.")
    print("-"*70 + "\n")
    
    while True:
        try:
    
            user_input = input("👤 Sie: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit', 'bye', 'q']:
                print("\n👋 Auf Wiedersehen!")
                break

            if user_input.lower() == 'clear':
                chat_history = ChatHistory()
                print("\n🗑️  Chat-Verlauf gelöscht.\n")
                continue

            chat_history.add_user_message(user_input)
            
            print("🤔 Denke nach...")
            response = await chat_completion.get_chat_message_contents(
                chat_history=chat_history,
                settings=settings
            )
            bot_response = response[0].content
            print(f"\n🤖 Bot: {bot_response}\n")
            print("-"*70)
            chat_history.add_assistant_message(bot_response)
            
        except KeyboardInterrupt:
            print("\n\n👋 Auf Wiedersehen!")
            break
        except Exception as e:
            print(f"\n❌ Fehler: {str(e)}\n")


async def main():

    os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL", "https://api.groq.com/openai/v1")
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    # Create kernel
    kernel = Kernel()

    service = OpenAIChatCompletion(
        service_id="groq-chat",
        ai_model_id="llama-3.3-70b-versatile"
    )
    kernel.add_service(service)

    await interactive_chat(kernel)

if __name__ == "__main__":
    asyncio.run(main())