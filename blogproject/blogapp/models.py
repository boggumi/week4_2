from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title 
        # blog에 글을 등록했을때 blog object란
        # 글 제목대신 우리가 설정한 title이 뜨도록 하는 함수

    def summary(self):
    #자기 자신은 객체로 받음
        return self.body[:100]   
        #자기 자신의 본문내용 중 상한선 100글자


