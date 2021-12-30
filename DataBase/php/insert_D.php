<HTML>
<Head>
<META http-equiv="content-type" content="text/html; charset=utf-8">
<title>대구병원</title>
</Head>
<body>
<style>
a { color : black; text-decoration:none;}
em {text-align:center; font-style : normal; font-size : 13px; display:inline-block;}
img {display : inline-block; position: fixed; top:27px; left:20px}
h2{display : inline-block}
h5, h6 { display : inline-block }
h5 { color : #1d2975 }
#header{width:100%; height:80px; display : block; border-bottom : 1px solid #333}
.st {display : inline-block; color:#333}
.name { display : inline-block; position: absolute; top:15px; right:90px}
.logout {width: 60px; height:20px; background:#0756a0;
		display : inline-block; border-radius : 8px; color:white; float:right;
		position:absolute; top : 35px; right : 21px; font-size:13px; text-align:center}
 #content{position:absolute; top:12%; left:5%; }
 #form{position: absolute; top:23%; left : 5%; text-align :center;
		display:block; width:13%; height:70%; border : 2.5px solid #1d2975; border-radius:10px;}
 main { display : inline-block }
 #m{position: absolute; top:23%; left : 26%; text-align :center;
		display:block; width:60%; height:70%; border : 2.5px solid #1d2975; border-radius:10px;}
  .m_text{ position:relative; top:38%; right:2.8%}
 a{display : block; padding-top : 9%; padding-right : 2.5%}
</style>
<div id = "header">
<img src="대구병원로고.png" width = 200, height = auto>
<div class = "name">
<h5>오은영</h5><h6>선생님</h6>
</div>
<div class= "logout">
<button  type='button' onclick="location.href='admin.php'">logout</button >
</div>
</div>
<div id = "content">
<h2>  환자 정보 관리 </h2>
<div class = "st">
 <strong> - 환자 정보 조회, 수정, 삭제 </strong>
</div>
</div>
<div id = "main">
<div id = "form">
<a href="select_D.php" > ▶ 환자정보조회 </a>
<a href="전체환자조회_대구.php" > ▶ 전체환자정보조회 </a>
<a href="insert_D.php" style="color:blue"> ▶ 신규환자등록 </a> 
<a href="update_D.php"  > ▶ 환자정보수정 </a>
<a href="delete_D.php" > ▶ 환자정보삭제 </a>
<a href="물품관리_대구.php" > ▶ 물품관리 </a>
</div>
<HTML>
<HEAD>
   <META http-equiv="content-type" content="text/html; charset=utf-8">
</HEAD>
<div id ="m">

<body>
<h1> 신규 환자 입력</h1>
<FORM METHOD="post" ACTION="insert_result_DD.php"class="from_text">
      
      환자 이름 : <INPUT TYPE = "text" NAME="patient_name"> <br>
      주민 번호 : <INPUT TYPE = "text" NAME="pid">  <br>
      검사일    : <INPUT TYPE = "text" NAME="check_date"> <br>
      코로나 확진여부 : <INPUT TYPE = "text" NAME="COVID19_test_result"> <br>
      확진일    : <INPUT TYPE = "text" NAME="COVID19_diagnosis"> <br>
      입원일    : <INPUT TYPE = "text" NAME="hospitalization_date"> <br>
      퇴원일    : <INPUT TYPE = "text" NAME="discharge_date"> <br>
      사망일    : <INPUT TYPE = "text" NAME="death_date"> <br>
      접종 여부 : <INPUT TYPE = "text" NAME="inoculation"> <br>
      접종 날짜 : <INPUT TYPE = "text" NAME="vaccination_date"> <br>
      접종한 백신 고유번호 : <INPUT TYPE = "text" NAME="vaccine_num"> <br>
      돌파감염여부 : <INPUT TYPE = "text" NAME="breakthrough_infection"> <br>
      <BR><BR>
      위 환자 정보를 입원 등록 하시겠습니까?
      <INPUT TYPE="submit" VALUE="환자 입원 등록">
</FORM>
</BODY>

</HTML>