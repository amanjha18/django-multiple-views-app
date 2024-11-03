from django.http import JsonResponse

def view2(request):
    return JsonResponse({'message': 'This is view 2'})
