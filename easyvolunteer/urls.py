from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),                               # 메인 페이지
    path('introduce', views.introduce, name='introduce'),            # 소개 페이지
    path('select', views.select, name='select'),                     # 기관/회원 회원가입 선택 페이지
    path('organ_signup', views.organ_signup, name='organ_signup'),   # 기관 회원 가입 페이지
    path('user_signup', views.user_signup, name='user_signup'),      # 일반 회원 가입 페이지
    path('login', views.login, name='login'),                        # 로그인 페이지
    path('mypage', views.mypage, name='mypage'),                     # 일반 회원 로그인 페이지 마이?0
    path('organ_mypage', views.organ_mypage, name='organ_mypage'),   # 기관 회원 로그인 페이지  마이?
    path('register', views.register, name='register'),               # 기관에서 봉사 등록 페이지
    path('quest', views.quest, name='quest'),                        # 일반 회원이 봉사 등록 페이지0
    path('point', views.point, name='point'),                        # 일반 회원이 포인트 사용하는 페이지0
    path('situation', views.situation, name='situation'),           # ++나의현황 페이지 --레벨과 봉사현황 제공
    path('modify', views.modify, name='modify'),                    #++ 정보 수정 페이지

]                                                                   
                                                                    
