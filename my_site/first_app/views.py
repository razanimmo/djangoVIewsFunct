from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
articles={
    "sports":"Messi Win a Ballondoor",
    "financial":"dollar got high",
    "Politics":"Trump ear got injured with a bullet shot by a person with downsyndrom"
}


def sample_view(request,topic):
    try:
        result=articles[topic]
        return HttpResponse(articles[topic])
    except:
        return Http404('Generic Error 404')
        # return HttpResponseNotFound('<img src="https://as1.ftcdn.net/v2/jpg/06/70/54/58/1000_F_670545815_8tbejhXLRK0jmv1t6CIVonM7D0m48tEx.jpg" alt="Italian Trulli" style="width:1500px;height:700px;">')

#creating a dynamic view to add a numbers
def add_num(request,num1,num2):
    add_result=num1 + num2
    result=f"{num1} + {num2}={add_result}"
    return HttpResponse(result)

def num_page_redirect(request,num_redirct):
    key_list=list(articles.keys())
    topic=key_list[num_redirct]
    
    
    try:
        result=topic
        return HttpResponseRedirect(reverse("topic-page",args=[topic]))
    except:
        Http404("404 generic error")
    
