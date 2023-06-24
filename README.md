# OpenAI function calling with FastAPI

A simple repo to test out OpenAI's new function calling freature available on newer models.

Written by Kitson Broadhurst for fun, use it as you please.

## Requirements

- Python 3
- pip

Installing the project should be simple, run the following command:
`pip install -r requirements.txt`

You will need two API keys, one for (OpenAI)[] and one for (OpenWeather)[https://openweathermap.org/].

Store them in a `.env` file locally:

```
OPENAI_API_KEY=
WEATHER_API_KEY=
```

## Running the app
Run the app using the following command:
`uvicorn main:app --reload`

The application will be available here:
`http://127.0.0.1:8000`

Interactive docs are available at:
`http://127.0.0.1:8000/docs`

From here, you can click "try it out" and "execute" to hit the endpoint and test the code.
