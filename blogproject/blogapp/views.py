from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

def home(request):
    blogs= Blog.objects 
    #쿼리셋 blogs란 변수에 Blog클래스의 모든 objecdts들을 담는다
    blog_list = Blog.objects.all()
    #블로그 모든 글들을 대상으로
    paginator = Paginator(blog_list, 3)
    #블로그 객체 세개를 한페이지로 자르기
    page = request.GET.get('page')
    #page란 변수에 get방식으로 얻어낸 데이터 중에서 key값이 page인 valuer값을 얻고 싶다
    posts = paginator.get_page(page)
    #(page), 즉 페이지 넘버에 해당하는 페이지를 불러와라
    #사전형으로 return해주기
    return render(request, 'home.html',  {'blogs' : blogs, 'posts':posts })
    # {} 얘들은 home.html 띄우면 거기에 {}들도 띄워라

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    # ...404(어떤 클래스로 object들을 get할 껀지, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()  #Blog란 클래스로 부터 blog란 객체를 생성
    blog.title = request.GET['title']  #blog 객체안에 title, body..를 가져옴
    blog.body = request.GET['body']  #워드카운트 할 때 한거
    blog.pub_date = timezone.datetime.now()
    blog.save()  #blog란객체에 쭉 넣은 내용(위에 세줄)을 db에 저장해라
    return redirect('/blog/'+str(blog.id))
# 글쓰기하면 바로 detail 페이지로 넘어갈 수 있도록 설정함
# redirect(넘기고 싶은 url)

    # create는 입력받은내용을 데이터베이스에 넣어주는 함수

def blogpost(request):
    # 1. 입력된 내용 처리 기능 -> post
    # 2. 빈페이지 띄워주는 기능 -> get
    if request.method == 'POST':
        form = BlogPost(request.POST) #form이란 변수에 post로 입력된 내용 담아줌
        if form.is_valid():
            post = form.save(commit=False) #아직저장하지 마셈
            post.pub_date = timezone.now() #요건 함수안에서 저장됨
            post.save()
            return redirect('home') 
            
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form': form})