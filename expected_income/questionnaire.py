from expect import expect

sizes = {
    0: '個人',
    1: '企業(2,000万円未満)',
    2: '企業(2,000万円以上)',
    3: '企業(5,000万円以上)',
    4: '企業(1億円以上)',
    5: '企業(10億円以上)',
}

years = {
    0: '1~5年',
    1: '5~9年',
    2: '10~14年',
    3: '15年~19年',
    4: '20~24年',
    5: '25~29年',
    6: '30~34年',
    7: '35年以上',
}

def ask(dict_data, name):
    answer = None
    while answer is None:
        print('{}を以下の数字から教えてください'.format(name))
        for key, value in dict_data.items():
            print(str(key) + ': ' + value)
        try:
            answer = int(input())
            if answer not in dict_data:
                raise ValueError
        except ValueError:
            answer = None
            print('指定された数字の中から指定してください')
    return answer

size = ask(sizes, '企業規模')
year = ask(years, '勤続年数')

expected_income = expect(size, year)
response = 'おそらくあなたの給与所得は年間{}千円程度です。'.format(expected_income)
print(response)