from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import (AboutView, 
                    IndexView, 
                    ArticleListView, 
                    ArticleDetailView,
                    ArticleCreateView,
                    ArticleUpdateView,
                    ArticleDeleteView,
)

app_name = 'articles'


urlpatterns = [
    # 바로 class 집어넣기
    path('about/', TemplateView.as_view(template_name="articles/about.html")),
    # 기존의 function base
    path('about2/', views.about2),
    # 제일 권장되는 방법
    path('about3/', AboutView.as_view()),
    # 전체 조회 
    path('index/', views.index),
    # 기존방법(index views func로 조회후 templates에서 나타내기)
    path('index2/', IndexView.as_view()),
    

    # CBV(index views class로 조회 후 여기서 메서드로 호출)
    # 제넉리뷰: 기존의 반복작업을 효율적으로 처리하자(ArticleLIstview, detailview)
    # 클래스하나로 전체조회, 단일조회 기능 모두 수행 가능(개편하네)
    # 추가적인 정보를 더해주고싶을때 (get_context_Data)
    path('', ArticleListView.as_view(), name='index'),
    # Detailview
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    # update할때 Formview하면 get post 등등 다양하게 분기설정해야하는데 귀찮으니까
    # 1. get_absoult_url fuc을 model에 추가(update 성공했을 때 redirect 되는 위치설정)
    # 2. 생성/업데이트/삭제 설정
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete'),
]


    # 누가 작성했는지 표시기능도 추가해주자 model create에서 추가
    # 누가 작성했는지 알려면 login 기능이필요하고 login 기능을 구현하려면 authentification이 필요
    # accounts app 만들어주기 -> accounts에는 기존에 만들어진 url들이 있음
    # template이 registration으로 경로가 조금 다름
    # 로그인하고나서 createform에 valid 추가
    



