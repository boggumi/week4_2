from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':  #우리가 signup.html에서 정보저장방식을 metho="post"라 해줌
        if request.POST['password1'] == request.POST['password2']:
            user= User.objects.create_user(username= request.POST['username'], password=request.POST['password1'])
            #위에는 아이디를 만들어주는 함수
            auth.login(request, user)
            #위 코드는 회원가입후 자동로그인 함수
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        # 우리 회원이 맞는지 확인시켜주는 함수
        if user is not None:
            auth.login(request, user) #로그인시켜줌
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')