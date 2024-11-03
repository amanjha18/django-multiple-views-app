from django.http import JsonResponse

def view1(request):
    return JsonResponse({'message': 'This is view 1'})
