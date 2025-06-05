import os
from dotenv import load_dotenv
from groq import Groq
import colorama
from colorama import Fore, Style

# Initialize colorama for colored terminal output
colorama.init()

class GroqChatbot:
    def __init__(self):

        load_dotenv()
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )
        self.model_name = "deepseek-r1-distill-llama-70b"
        self.conversation_history = []
        
        print(f"{Fore.GREEN}🤖 Groq Chatbot initialized with {self.model_name} model!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Type 'quit', 'exit', or 'bye' to end the conversation.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Type 'clear' to clear conversation history.{Style.RESET_ALL}\n")
    
    def chat(self, user_input: str) -> str:
        """Process user input and return AI response"""
        try:
            self.conversation_history.append({"role": "user", "content": user_input})

            messages = [
                {"role": "system", "content": "You are a helpful AI assistant. Provide clear, concise, and helpful responses."}
            ] + self.conversation_history
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.7,
                max_tokens=1024,
                top_p=1,
                stream=False
            )

            ai_response = response.choices[0].message.content.strip()
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            
            return ai_response
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def run_interactive_chat(self):
        """Run an interactive chat session"""
        print(f"{Fore.YELLOW}Welcome to the Groq Chatbot!{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Powered by {self.model_name}{Style.RESET_ALL}\n")
        
        while True:
            try:
                user_input = input(f"{Fore.GREEN}You: {Style.RESET_ALL}").strip()
                if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                    print(f"{Fore.YELLOW}👋 Goodbye! Thanks for chatting!{Style.RESET_ALL}")
                    break
                if user_input.lower() == 'clear':
                    self.clear_memory()
                    continue

                if not user_input:
                    continue
                print(f"{Fore.CYAN}AI: {Style.RESET_ALL}", end="", flush=True)
                response = self.chat(user_input)
                print(response)
                print()
                
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}👋 Goodbye! Thanks for chatting!{Style.RESET_ALL}")
                break
            except Exception as e:
                print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")
    
    def clear_memory(self):
        """Clear conversation history"""
        self.conversation_history = []
        print(f"{Fore.YELLOW}🧹 Conversation history cleared!{Style.RESET_ALL}")
    
    def get_conversation_count(self):
        """Get the number of messages in conversation history"""
        return len(self.conversation_history)


def main():
    """Main function to run the chatbot"""
    try:
        load_dotenv()
        if not os.getenv("GROQ_API_KEY"):
            print(f"{Fore.RED}❌ GROQ_API_KEY not found in environment variables!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Please make sure your .env file contains GROQ_API_KEY{Style.RESET_ALL}")
            return
        chatbot = GroqChatbot()
        chatbot.run_interactive_chat()
        
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to initialize chatbot: {str(e)}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()