from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv('OPENAI_KEY',None)

def chatbot(request):
    chatbot_response =None
    
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            temperature=0.6, # we control level of creativity and variation
            #high temprature -> more diverse and creative, lower temprature -> more predictable and conservative.
            max_tokens=256   # response with max 256 words
            # stop='.'
            )
        print(response)
        chatbot_response = response["choices"][0]["text"]
    return render(request,'index.html',{"response":chatbot_response})