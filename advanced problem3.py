import pprint
import requests

# 응답 중 정기예금 상품들의 옵션 리스트를 출력하도록 구성합니다.
# 이 때, 원하는 데이터만 추출하여 새로운 리스트를 만들어 반환하는 함수를 작성하시오.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 출력합니다.
# 3. 위의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 4. 3번에서 저장된 값을 반복하며, 원하는 데이터만 추출 및 가공하여 결과 리스트에 저장합니다.

def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = '41cbcf4f950a39cf6df006fea04b2c9f'
    url = 'https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

    params = {
        'auth' : api_key,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }

    response = requests.get(url, params = params).json()
    option_list = response['result']['optionList']
    return option_list
    
option_list = get_deposit_products()
arr = []
for i in option_list:
        new_dict = dict()
        new_dict['금융상품코드'] = i['fin_prdt_cd']
        new_dict['저축 금리'] = i['intr_rate']
        new_dict['저축기간'] = i['save_trm']
        new_dict['저축금리유형'] = i['intr_rate_type']
        new_dict['저축금리유형명'] = i['intr_rate_type_nm']
        new_dict['최고 우대금리'] = i['intr_rate2']
        arr.append(new_dict)




#금융상품코드 fin_prdt_cd
#저축 금리 : intr_rate
#저축기간 save_tm
#저축금리유형 intr_rate_type
#저축금리유형명 intr_rate_type_nm
#최고 우대금리 : intr_rate2



    
# # 아래 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     # json 형태의 데이터 반환
#     result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(arr)
