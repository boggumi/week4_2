from django.db import models

# 데이터를 저장하장
class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='images/') 
     #이미지 업로드는 settigs.py에서 정의한 images/ 에 올리겠다
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title