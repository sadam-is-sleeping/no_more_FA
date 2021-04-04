# no_more_FA
지각 한 번, 결석 두 번. 개강이 이제 겨우 한 달 지났는데 벌써부터 이러면 안 된다. **FA 멈춰!**

## Plans
- Windows 기반
- eclass.sogang.ac.kr 에서 Selenium으로 정보 가져오기
- Python 또는 C# (pywin32 쓰면서 복잡해질 바에는 아예 C#에서 작업하는 것도 고려)

***Python:***
- [keyboard](https://github.com/boppreh/keyboard)
- [pywin32](https://github.com/mhammond/pywin32)

***C#***

## InfoGathering
//div[@id="index-leftarea02"]/div[1]/ol  
get all \<li> elements, between term_info(1학기, 비정규과목)  
\<em> split() -> [과목명, (과목코드)]  
kj value -> kjcode  
\<span> split() -> [요일, 시간] (if 비어있으면 알세, skip)  
or  
//table[@class="course-datatable"]/tbody  
get all \<tr> elements  
tr[1] -> 시간  
tr[2] -> 과목명(과목코드)  
  
eclassRoom(kjcode); --> eclass.sogang.ac.kr/ilos/st/course/submain_form.acl  
//div[@id="subject-nm-form"]/input[3] -> value is kjcode  
eclass.sogang.ac.kr/ilos/st/course/online_list_form.acl  
eclass.sogang.ac.kr/ilos/st/course/zoom_list_form.acl  
  
