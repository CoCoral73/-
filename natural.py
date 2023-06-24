from jamo import h2j, j2hcj
from unicode import join_jamos

cho_jung = {        #종성 첨가 가능
    '대': '머',
    '며': '띠',
    '귀': '커',
    '파': '과', '과': '파',
    '피': '끠',
    '비': '네',
    '삐': '볘',
    '겨': '저',
    '고': '끄',
    '티': '더'
}
cho_jung_jong = {   #1:1 매칭, 종성 첨가 불가
    '꺼': '77ㅓ',
    '근': 'ㄹ',
    '위': '읶',
    '유': '윾', '우': '윽',
    '리': '21', '이': '01', '기': '71',
    '왕': '앟', '왱': '앻', '욍': '잏', '왓': '앛', '왯': '앷', '욋': '잋',
    '의': '익',
    '나': '4',
    '야': 'OF',
    '태': 'EH', '애': 'OH', '내': 'LH',
    '빅': '븨'
}
jong = {        #종성 단순화
    'ㄲ': 'ㄱ',
    'ㄳ': 'ㄱ',
    'ㄵ': 'ㄴ',
    'ㄶ': 'ㄴ',
    'ㄺ': 'ㄱ',
    'ㄻ': 'ㅁ',
    'ㄼ': 'ㄹ',
    'ㄾ': 'ㄹ',
    'ㄿ': 'ㅍ',
    'ㅄ': 'ㅂ',
    'ㅆ': 'ㅅ'
}
cho_shift = {
    'ㄱ': 'ㄲ',
    'ㄷ': 'ㄸ',
    'ㅈ': 'ㅉ',
    'ㅂ': 'ㅃ',
    'ㅅ': 'ㅆ'
}
jung = {
    'ㅓ': 'ㅝ', 'ㅝ': 'ㅓ',
    'ㅛ': 'ㅗ', 'ㅗ': 'ㅛ',
    'ㅞ': 'ㅔ',
    'ㅙ': 'ㅚ', 'ㅚ': 'ㅙ',
    'ㅔ': 'ㅖ', 'ㅐ': 'ㅒ',
    'ㅟ': 'ㅢ', 'ㅢ': 'ㅟ'
}
def mingle4(word):
    new = word[0]
    new += word[2]
    new += word[1]
    new += word[3]
    return new
def is_korean(ch):
    return ch >= '가' and ch <= '힣'
def yamin(word):
    new = ""
    for i in range(len(word)):
        if is_korean(word[i]) == False:
            new += word[i]
            continue
        cjj = cho_jung_jong.get(word[i], word[i])
        if cjj != word[i]:      #종성 첨가 불가 단어
            new += cjj
            continue
        step1 = j2hcj(h2j(word[i]))     #초성 중성 종성 분리하기
        if len(step1) == 3:     #종성 단순화
            j = jong.get(step1[2], step1[2])
            if j != step1[2]:
                new += join_jamos(step1[:2]+j)
                continue
        step2 = join_jamos(step1[:2])   #초성 중성 합치기
        ym = cho_jung.get(step2, step2) #야민정음 얻기
        if ym != step2:
            if len(step1) == 3:
                step3 = j2hcj(h2j(ym))
                step3 += step1[2]
                ym = join_jamos(step3[:3])
            new += ym
            continue
        shift = cho_shift.get(step1[0], step1[0])
        change_jung = jung.get(step1[1], step1[1])
        if len(step1) == 3:
            ym = join_jamos(shift+change_jung+step1[2])
        else:
            ym = join_jamos(shift+change_jung)
        new += ym
    return new

def translation(text):
    text = text.split(' ')
    new = ""
    for i in range(len(text)):
        if len(text[i]) == 4:
            new += mingle4(text[i])
        else:
            new += yamin(text[i])
        new += " "
    return new