from django.shortcuts import HttpResponseRedirect, render
import markdown2

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entry(request, title):
    
    if util.get_entry(title):
        return render(request, f"encyclopedia/entry.html", {
            "content": markdown2.markdown(util.get_entry(title)),
            "title": title
        })
    else:
        return render(request, f"encyclopedia/error.html")
    
def search(request):
    query = request.POST.get('q', 'notfound')
    if util.get_entry(query):
        return render(request, f"encyclopedia/entry.html", {
            "content": markdown2.markdown(util.get_entry(query)),
            "title": query
        })
    else:
        matched_entries = [ e for e in util.list_entries() if (query.lower() in e.lower()) ]
        return render(request, f"encyclopedia/results.html", {
            "entries": matched_entries,
            "query": query
        })


# def search(request):
#     entries = util.list_entries()
#     find_entries = []
#     # find_entries = list()
#     search_box = request.POST.get("q", "").capitalize()

#     if search_box in entries:
#         return HttpResponseRedirect(f"wiki/{search_box}")
        
#     for entry in entries:
#         if search_box in entry:
#             find_entries.append(entry)
#         else:
#             print(f'{find_entries}')
#     if find_entries:
#         return render(request, "encyclopedia/search.html", {
#           "search_result": find_entries,
#           "search": search_box
#     })
#     else:
#         return render(request, "encyclopedia/search.html", {"no_result": f"No results for {search_box}"})