from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),                               # 메인 페이지(소개 페이지 포함됨) 00
    path('select', views.select, name='select'),                     # 기관/회원 회원가입 선택 페이지  
    path('organ_signup', views.organ_signup, name='organ_signup'),   # 기관 회원 가입 페이지
    path('user_signup', views.user_signup, name='user_signup'),      # 일반 회원 가입 페이지
    path('login', views.login, name='login'),                        # 로그인 페이지
    path('mypage', views.mypage, name='mypage'),                     # 일반  마이페이지 ///////////////////
    path('organ_mypage', views.organ_mypage, name='organ_mypage'),   # 기관 회원 마이페이지 /////////
    path('register', views.register, name='register'),               # 기관에서 봉사 등록 페이지 //////
    path('quest', views.quest, name='quest'),                        # 일반 회원이 봉사 목록 페이지 0
    path('quest_what', views.quest_what, name='quest_what'),         # 일반 회원이 선택한 봉사 설명 페이지 0
    path('point', views.point, name='point'),                        # 일반 회원이 포인트 사용 후 잔여 포인트 페이지 
    path('brands', views.brands, name='brands'),                     #++일반인 회원이 상품 고르는 페이지-브랜드선택 페이지 0
    path('goods', views.goods, name='goods'),                        #++일반인 회원이 상품 고르는 페이지-상품선택 페이지 0
    path('situation', views.situation, name='situation'),            # ++나의현황 페이지 --레벨과 봉사현황 제공 
    path('modify', views.modify, name='modify'),                     #++ 정보 수정 페이지 


]                                                                   

                                        #----------------------------수정과 꾸밈이 필요한 페이지는 * 표시   거의 완성은 00표시                            
