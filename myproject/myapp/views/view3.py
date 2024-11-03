from django.http import JsonResponse

def view3(request):
    return JsonResponse({'message': 'This is view 3'})
