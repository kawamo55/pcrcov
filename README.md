# pcrcov
組込AI研究所 Programed by M.kawase  
荻原和樹様の公開しているcovid19データのsammary.csvを比較可視化するpythonプログラム  
参考データ：https://github.com/kaz-ogiwara/covid19  
  
新型コロナウイルスPCR検査件数と感染者数を回帰分析（Kernal Ridge[polynomial]）で分析してみました。  
gitで元データを取得する部分と、データ加工部分を追加  
pcrcov.py  
  
データ取得コマンド(shell script)  
getPCRD  
  
平均PCR検査数・感染者数・重傷者数グラフ化プログラム  
pcov2.py  
感染者数の傾きは、実効再生産数に近い値のはずですがグラフを増減関係を大きく見せつために一定倍していることに注意

データ加工部はダイアモンドプリンセスの影響を避けるため3月1日のデータから取得   
データの推移を安定させるため検査数、感染者数の７日平均値を使うようにしています。   

