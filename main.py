from fastapi import FastAPI
from dotenv import load_dotenv
import json
import utils
import weather

functions = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and country code. Please use ISO 3166 country codes",
                },
                "format": {
                    "type": "string",
                    "enum": ["imperial", "metric"],
                    "description": "The temperature unit to use. Infer this from the users location.",
                },
            },
            "required": ["location", "format"],
        },
    },
]

load_dotenv()  # take environment variables from .env

app = FastAPI()

@app.post("/")
async def root():
    # Mock messages, this can be a conversation with the user.
    # The AI should converse with the user until it gets a request for weather details
    # and the location the user is at. As you can see fromt he mock if the user asks the weather,
    # the AI should ask what location
    messages = []
    messages.append({"role": "system", "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."})
    messages.append({"role": "user", "content": "What's the weather like today"})
    messages.append({"role": "assistant", "content": "Sure, could you please provide me with the location?"})
    messages.append({"role": "user", "content": "I'm in London, England."})

    def request_with_function_call(request_messages):
        chat_response = utils.chat_completion_request(
            request_messages, functions=functions
        )
        assistant_message = chat_response.json()["choices"][0]["message"]
        request_messages.append(assistant_message)

        if assistant_message.get("function_call") and assistant_message["function_call"]["name"] == "get_current_weather":
            # we only have one function call but 
            arguments = json.loads(assistant_message['function_call']['arguments'])

            # we have a get_current_weather function to excecute
            weather_data = weather.get_current_weather(arguments['location'], arguments['format'])
            request_messages.append({"role": "function", "name": "get_current_weather", "content": str(weather_data) })

            return request_with_function_call(request_messages)

        if assistant_message.get("content"):
            return assistant_message.get("content")

        return "Oops something went wrong!"
    
    message_to_user = request_with_function_call(messages)
    return {"message": message_to_user}
