import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Unicodeのコードポイント頻度測定 --- (*1)


def count_codePoint(str):
    # Unicodeのコードポイントをアドレスとする配列を用意 --- (*2)
    counter = np.zeros(65535)

    for i in range(len(str)):
        # 各文字をUnicodeのコードポイントに変換 --- (*3)
        code_point = ord(str[i])
        if code_point > 65535:
            continue
        # 対応するアドレスの出現回数をインクリメント --- (*4)
        counter[code_point] += 1

    # 各要素を文字数で割って正規化 --- (*5)
    counter = counter/len(str)
    return counter


# 学習用データの準備
ja_str = '私は千鳥が大好きです'
en_str = 'I love chidori'
co_str = '나는 정열을 사랑 해요'
ve_str = 'Tôi yêu Chidori'

x_train = [count_codePoint(ja_str), count_codePoint(
    en_str), count_codePoint(co_str), count_codePoint(ve_str)]
y_train = ['ja', 'en', 'co', 've']

# 学習する --- (*6)
clf = GaussianNB()
clf.fit(x_train, y_train)

# 評価用データの準備
ja_test_str = '私はtwitterを良く使います'
en_test_str = 'I often use Twitter'
co_test_str = '나는 Twitter를 자주 사용합니다'
ve_test_str = 'Tôi sử dụng Twitter rất nhiều'

x_test = [count_codePoint(en_test_str), count_codePoint(ve_test_str), count_codePoint(
    co_test_str), count_codePoint(ja_test_str)]
y_test = ['en', 've', 'co', 'ja']

# 評価する --- (*7)
y_pred = clf.predict(x_test)
print(y_pred)
print("正解率 = ", accuracy_score(y_test, y_pred))
