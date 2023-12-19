from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render 
from django.http import JsonResponse 
from .models import *
# Importing the langchain and llama2 related functions
from langchain.callbacks.streaming_stdout import StreamingStdOutCallBackHandler
from langchain.llms import LlamaCpp 
from llama_cpp import Llama 


# loading the model 
model_path = "...../llama-2-7b.ggmlv3.q8_0.bin"

llm = Llama(model_path=model_path)

def llmprediction(request):
    query = request.GET['query']
    
    result = llm(query,
                 max_tokens = 100,
                 echo = True)
    
    return Response({'Result': result})