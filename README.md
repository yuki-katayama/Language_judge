# Language_judge

# 日本語
## 初めに
lang_judge_easy.pyとlang_judge_diffc.pyは依存関係がないので、個別で使用する。

### lang_judge_easy.pyを実行
これは日本語、英語、韓国語、ベトナム語を判別している。
    学習データと、テストデータでは、入力を別々のものにしているが、しっかり判別できていることが確認できる。

### lang_judge_diffc.pyを実行
これは、日本語、韓国語、スペイン語、英語、ドイツ語を判別している。
    英語、スペイン語、ドイツ後は、アルファベットを使用する点で似ているが、学習量により可能にしている。

>学習させる文章はここを使用し、それぞれGoogle翻訳にかけて使用
    https://lipsum.sugutsukaeru.jp/index.cgi

* また、学習言語を増やすには、train && testフォルダに、(言語を表す2文字)_適当.txtを用意すると、種類を増やすことができる。


## English
## Introduction
lang_judge_easy.py and lang_judge_diffc.py are not dependent on each other, so they are used separately.


### Run lang_judge_easy.py
This discriminates between Japanese, English, Korean and Vietnamese.
    It identifies Japanese, English, Korean and Vietnamese, even though it uses different input for training and test data.

### Run lang_judge_diffc.py
It discriminates between Japanese, Korean, Spanish, English and German.
    The English, Spanish and German languages are similar in that they use the alphabet, but the amount of learning makes it possible.

>The sentences to be learned are used here, and then each sentence is used by Google Translate.
    https://lipsum.sugutsukaeru.jp/index.cgi

* You can also increase the number of languages by preparing (2 characters for language) _appropriate.txt in the train && test folder.
