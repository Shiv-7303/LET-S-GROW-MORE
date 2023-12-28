import json


class SimpleChatBot:
    def __init__(self):
        self.qa_dict = self.load_qa_from_json("knowledge.json")

    def load_qa_from_json(self, json_file):
        try:
            with open(json_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{json_file}' not found.")
            return {}

    def get_response(self, question):
        return self.qa_dict.get(question, "I don't understand that question.")


def main():
    chatbot = SimpleChatBot()

    print("Simple ChatBot: Hello! Ask me anything or type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Simple ChatBot: Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print("Simple ChatBot:", response)


if __name__ == "__main__":
    main()
