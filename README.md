# expected_income
## 本アプリの概要
scikit-learnによって線形回帰分析を行い、所属する企業の企業規模および勤続年数を基に給与所得を推定するアプリになります。

データセットの基となったファイル(expected_income/14.xlsx)は、以下よりダウンロードできます。

[民間給与実態統計調査 民間給与実態統計 結果表 14 第14表](https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00351000&bunya_l=03&tstat=000001012969&cycle=7&year=20180&month=0&tclass1=000001012970&stat_infid=000031884678&result_back=1)

## 使用技術
### 言語
Python
### プラグイン
- Jupyter Notebook
- openpyxl
- pandas
- scikit-learn
### OS
macOS

## 動作環境
| 技術 | バージョン |
| ---- | ---- |
| Python | 3.8.2 |
| Jupyter Notebook | 6.0.3 |
| openpyxl | 3.0.3 |
| pandas | 1.0.3 |
| scikit-learn | 0.22.1 |
| macOS | catalina 10.15.4 |

## 使用方法
### 学習済みモデルのpickle化
scikit-learnがインストールされていない、あるいはバージョンが違う場合は確実に学習済みモデル(expected_income/trainend-model.pickle)が
そのままでは利用できません。
また、PythonのバージョンやOSが違う場合、学習済みモデルがそのままでは利用できない場合があります。
その際には、以下のnotebookを利用して、学習済みモデルをpickle化しなおしてください。
expected_income/machine_learning.ipynb

### コマンドからの実行
expected_incomeフォルダに移動し、以下のコマンドを入力します。
```terminal:command
python questionnaire.py
```

その後、ターミナル上で企業規模、勤続年数を選択肢(数字)から聞かれますので、答えを入力してください。
そうしますと、推定された年間給与所得が表示されます。
