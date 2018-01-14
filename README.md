# ボケてAI

# 開発環境

* mac OSX 10.11.6
* python 3.5
* anaconda 4.4.0

# 環境構築

* anacondaインストール
  * https://www.anaconda.com/download/

* python環境セットアップ

```
# conda create -n bokete_ai python=3.5
# source activate bokete_ai
# conda info -e
# source deactivate # 終了時
# pip install tensorflow
# pip install keras
# pip install scrapy
# pip install Pillow
# pip install pandas
# pip install mojimoji
# pip install matplotlib
```

* mecab
  * [mecabインストール](http://taku910.github.io/mecab/#install-unix)
    * mecab-ipadic のconfigureはutf8で行う `./configure --with-charset=utf8`
  * 新語辞書を追加
    * [Pythonからmecab-ipadic-neologdを使う](https://qiita.com/satzz/items/fec3292a9b552a693728)
  * mecabインストール後 `pip install mecab-python3` を実行

* jupyter notebook

```
# conda install jupyter
# ipython kernel install --user --name=bokete_ai --display-name=bokete_ai
# jupyter kernelspec list
Available kernels:
  bokete_ai    /Users/username/Library/Jupyter/kernels/bokete_ai
  python3      /Users/username/.pyenv/versions/anaconda3-4.4.0/share/jupyter/kernels/python3
```

# 実行

### 1. 学習データ収集

* scrapyでボケてサイトから収集
* boketeScrapyで実行

```
# cd boketeScrapy/boketeScrapy
# scrapy bokete -o legend.csv
```

### 2. 学習

* スクレイピングしたデータを加工して学習させる
* jupyter notebookを起動して `vgg_seq2seq.ipynb` を開く
* notebookの各ステップを実行していく
  * 学習ステップはmbp(core-i5/RAM8G)で丸４日以上かかった

```
# cd ../
# jupyter notebook
```

### 3. ボケる

* 新しい画像を入力して出力（ボケ）を確認する
* `vgg_seq2seq.ipynb` の最終ステップで画像パスを指定して実行する
