from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('log.txt', 'a') as f:
            f.writelines(f'{name} Написал(-а): {message} (Телефон для связи: {phone})/')
    return render(request, 'catalog/contacts.html')