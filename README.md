## :arrow_forward: How to get started

```
$ git clone https://github.com/wafuwafu13/chaos-generator.git
$ cd chaos-generator
$ pip install matplotlib

$ python time_series.py  or  python state_transition.py
$ x0の値を入力してください:  <input number>
$ lambdaの値を入力してください:  <input number>
```

## :speech_balloon: Description

社会学の授業を自力でコード化しました。詳しくは以下をご覧ください。
### [家族社会学 第2講 ロジスティック方程式とカオス反制御・制御から見出すシステム家族療法](https://kyoupurog.hatenablog.com/entry/2020/04/20/201717?_ga=2.133063371.454462925.1587375416-132769761.1586770378)

## :eyes: Show chart

x0 = 0.03 に固定

### 定常状態(1~<math xmlns='http://www.w3.org/1998/Math/MathML'> <mi> &#x03BB; <!-- greek small letter lambda --> </mi> </math>~3)

```time_series.py```

<img width="598" alt="スクリーンショット 2020-04-21 09 54 34" src="https://user-images.githubusercontent.com/50798936/79813304-3a159180-83b6-11ea-9b08-0bda35d82d7b.png">

```state_transition.py```

<img width="597" alt="スクリーンショット 2020-04-21 09 55 50" src="https://user-images.githubusercontent.com/50798936/79813319-4ac60780-83b6-11ea-86fe-590bd4eff3dc.png">


### アトラクタ出現(3~<math xmlns='http://www.w3.org/1998/Math/MathML'> <mi> &#x03BB; <!-- greek small letter lambda --> </mi> </math>~3.57)

```time_series.py```

<img width="584" alt="スクリーンショット 2020-04-21 09 59 26" src="https://user-images.githubusercontent.com/50798936/79813526-df306a00-83b6-11ea-8db4-1d8a1e85eca6.png">

```state_transition.py```

<img width="584" alt="スクリーンショット 2020-04-21 09 59 44" src="https://user-images.githubusercontent.com/50798936/79813530-e192c400-83b6-11ea-82e8-7e3d3beceb85.png">


### カオス(3.57~<math xmlns='http://www.w3.org/1998/Math/MathML'> <mi> &#x03BB; <!-- greek small letter lambda --> </mi> </math>~4)


```time_series.py```

<img width="591" alt="スクリーンショット 2020-04-21 10 02 35" src="https://user-images.githubusercontent.com/50798936/79813692-4c43ff80-83b7-11ea-9f9a-b9d727c4b9d9.png">

```state_transition.py```

<img width="588" alt="スクリーンショット 2020-04-21 10 02 54" src="https://user-images.githubusercontent.com/50798936/79813696-4ea65980-83b7-11ea-9e96-72ef6e12abca.png">




