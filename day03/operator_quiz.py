# #operator_quiz
# news = """총선이 끝난 뒤 전자상거래(이커머스) 월 회비와 치킨·버거 등 프랜차이즈 가격이 오른데 이어 이어 편의점에서 파는 생필품·가공란 가격이 일제히 인상된다. 정부의 ‘물가 안정’ 기조에 눈치를 보던 제조업체들이 잇따라 공급가를 올린 탓이다. 서민들의 물가 부담이 점차 커질 것으로 보인다.
#
# 16일 편의점 업계의 말을 종합하면, 대형 편의점 4사(씨유·지에스25·세븐일레븐·이마트24)는 다음달 1일부터 볼펜, 포스트잇, 라이터, 면도기, 생리대 등의 물품 가격을 모두 올린다.
#
# 편의점에서 판매하는 엘지유니참의 ‘쏘피 바디피트 내몸에 순한면’ 생리대 중간 크기(4개)는 2400원에서 2600원으로 8.3% 오르고, 대형 사이즈(16개)는 9400원에서 9500원으로 인상된다. 뉴트로지나 딥클린포밍클렌저(100g)도 8900원에서 9900원으로 1천원(11.2%) 오른다.
#
# 가공란 가격도 오른다. 계란 2개가 들어있는 감동란과 죽염동 훈제란은 각각 2200원에서 2400원으로 200원(9.1%) 오른다. 햇닭알로 만든 녹차훈제란(3개)은 2900원에서 3200원으로 300원(10.3%) 인상된다.
#
# 또 모나미 153볼펜 가격은 300원에서 400원으로 100원(33%), 스틱볼펜은 500원에서 600원으로 오른다. 스위트 돌라이터는 800원에서 900원으로, 미니돌라이터도 600원에서 700원으로 각각 100원씩 오른다. 도루코 페이스 면도기는 1900원에서 2100원으로 200원(10.5%), 페이스4면도기(3입)는 5200원에서 5700원으로 500원(9.6%) 각각 인상된다.
#
# 편의점 씨유 관계자는 “원부자재 가격 인상으로 제품 납품 가격이 인상됨에 따라 편의점 판매가도 올리게 된 상황”이라며 “인상 시점과 인상 폭은 편의점 4사에 동일하게 적용되지만, 업체별로 취급 품목은 조금씩 다르다”고 설명했다.
#
# 식품·유통업계에서는 선거가 끝나자마자 가격 인상이 잇따르고 있다. 앞서 유통업계 1위 기업인 쿠팡은 지난 13일부터 유료 회원 서비스인 와우 멤버십 월 회비를 4990원에서 7890원으로 58.1% 대폭 인상한 바 있다. 또 15일에는 치킨 프랜차이즈 굽네가 치킨 9개 제품 가격을 일제히 1900원씩 인상했고, 파파이스 역시 제품 가격을 평균 4%(100~800원) 올렸다."""
#
# word = input("검색 하고 싶은 단어:")
# result = word in news
# print(f"검색하신 단어는 뉴스 기사 내에 {result}")
password = input("비밀 번호 입력:")
result = "!" in password and "IT" in password
print(f"비밀번호가 요구 사항을 {result}")