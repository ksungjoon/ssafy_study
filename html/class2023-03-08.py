# css 기본기
# css 원칙
# 모든 요소는 네모 (박스모델)이고 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.
# content -글이나 이미지 등 요소의 실제 내용
# padding -테두리 안쪽의 내부 여백 요소에 적용된 배경색, 이미지는 padding까지 적용
# broder -테두리 영역
# margin -테두리 바깥의 외부 여백 배경색을 지정할 수 없다
# . 은 class # 은 아이디
# div 는 한줄 다 차지하는 특성을 가지고 있다
# 인라인은 딱 자기 content요소까지만 차지 -- span

# display : block
# 줄 바꿈이 일어나느 요소(다른elem를 밀어낸다!)
# 화면 크기 전체의 가로폭을 차지한다
# 블록 레벨 요소 안에 인랑니 레벨 요소가 들어 갈 수 있음
# ex ) div/ ul,ol,li/p/hr/form
# display : inline
# 줄 바꿈이 일어나지 않는 행의 일부 요소
# content를 마크업 하고 있는 만큼만 가로폭을 차지한다
# width height margin -bottom을 지정할 수 없다
# 상하 여백은 line-height로 지정한다
# ex ) span/a/img/input,label/b,em,i,strong


# display 다시보기

# relative : 상대 위치
# 자기 자신의 static 위치를 기준으로 이동

# absolute : 절대 위치
# 요소를 일반적으로 문서 흐름에서 제거후 레이아웃 공간을 차지 하지 않음
# static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 body)


# 인프런