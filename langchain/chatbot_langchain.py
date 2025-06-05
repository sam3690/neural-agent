import os
from dotenv import load_dotenv
from groq import Groq
from langchain.schema.messages import HumanMessage, AIMessage, SystemMessage
from langchain.memory import ConversationBufferMemory
from langchain.schema.runnable import RunnableLambda
from langchain.schema.output_parser import StrOutputParser
import colorama
from colorama import Fore, Style

colorama.init()

class GroqLangChainChatbot:
    def __init__(self):
        load_dotenv()
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )
        
        self.model_name = "deepseek-r1-distill-llama-70b"
        self.memory = ConversationBufferMemory(
            return_messages=True,
            memory_key="chat_history"
        )
        
        print(f"{Fore.GREEN}🤖 LangChain Groq Chatbot initialized with {self.model_name} model!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Type 'quit', 'exit', or 'bye' to end the conversation.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Type 'clear' to clear conversation history.{Style.RESET_ALL}\n")
    
    def _call_groq(self, messages):
        """Call Groq API with messages"""
        try:
            groq_messages = []
            for msg in messages:
                if isinstance(msg, SystemMessage):
                    groq_messages.append({"role": "system", "content": msg.content})
                elif isinstance(msg, HumanMessage):
                    groq_messages.append({"role": "user", "content": msg.content})
                elif isinstance(msg, AIMessage):
                    groq_messages.append({"role": "assistant", "content": msg.content})
        

            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=groq_messages,
                temperature=0.7,
                max_tokens=1024,
                top_p=1,
                stream=False
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Error calling Groq API: {str(e)}"
    
    def chat(self, user_input: str) -> str:
        """Process user input and return AI response using LangChain memory"""
        try:
            system_msg = SystemMessage(content="You are a helpful AI assistant. Provide clear, concise, and helpful responses.")
            chat_history = self.memory.chat_memory.messages
            messages = [system_msg] + chat_history + [HumanMessage(content=user_input)]
            ai_response = self._call_groq(messages)

            self.memory.chat_memory.add_user_message(user_input)
            self.memory.chat_memory.add_ai_message(ai_response)
            
            return ai_response
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def run_interactive_chat(self):
        """Run an interactive chat session"""
        print(f"{Fore.YELLOW}Welcome to the LangChain Groq Chatbot!{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Powered by {self.model_name} with LangChain memory{Style.RESET_ALL}\n")
        
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
        """Clear conversation memory"""
        self.memory.clear()
        print(f"{Fore.YELLOW}🧹 Conversation memory cleared!{Style.RESET_ALL}")
    
    def get_memory_stats(self):
        """Get memory statistics"""
        messages = self.memory.chat_memory.messages
        return {
            "total_messages": len(messages),
            "user_messages": len([msg for msg in messages if isinstance(msg, HumanMessage)]),
            "ai_messages": len([msg for msg in messages if isinstance(msg, AIMessage)])
        }


def main():
    """Main function to run the chatbot"""
    try:
        load_dotenv()
        
        # Check if GROQ_API_KEY is available
        if not os.getenv("GROQ_API_KEY"):
            print(f"{Fore.RED}❌ GROQ_API_KEY not found in environment variables!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Please make sure your .env file contains GROQ_API_KEY{Style.RESET_ALL}")
            return
        
        # Initialize and run the chatbot
        chatbot = GroqLangChainChatbot()
        chatbot.run_interactive_chat()
        
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to initialize chatbot: {str(e)}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
