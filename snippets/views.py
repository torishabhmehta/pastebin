from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from snippets.forms import SnippetForm, Commentform
from snippets.models import Snippet
# Create your views here.

def create(request):
	if request.method=="GET":
		form = SnippetForm()
	elif request.method=="POST":
		form=SnippetForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			snippet = Snippet(title=data.get('title'), content=data.get('content'))
			snippet.save()
			return redirect('view', snippet.id)	
	return render(request, 'snippets/create.html', {'form':form})

def view(request, key):
	if Snippet.objects.filter(id=key).exists():
		snippet=Snippet.objects.get(id=key)
	else:
		raise Http404("Snippet does not exist")
	
	if request.method == "POST":
		form=Commentform(request.POST)
		print(form.is_valid())
		if form.is_valid():
			comment=form.save(commit=False)
			comment.snippet=snippet
			comment.save()
	form=Commentform()
	comments= snippet.comment_set.order_by('-datetime_created')
	return render(request, 'snippets/view.html', {'key' : key, 'title':snippet.title,'content': snippet.content, 'form':form, 'comments':comments}) 
