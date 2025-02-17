
# 二元一次方程组  
**二元:** 两个未知数, 通常是 x 和 y.  
**一次:** 未知数不带平方.  


&nbsp;  
### 判断是否有解
&nbsp;  
> **有无穷多的解:** $ {a_1 \over a_2} = {b_1 \over b_2} = {c_1 \over c_2} $

&nbsp;  
> **有唯一解:** $ {a_1 \over a_2} \ne {b_1 \over b_2}  $  

&nbsp;  
> **无解:** $ {a_1 \over a_2} = {b_1 \over b_2} \ne {c_1 \over c_2} $  



&nbsp;  
### 解方程  

> 代入消元法  

- **例-1**  
  $
  \begin{align}
      \begin{cases}
           x   +   y  = 3 \\\\\\\\
          {x \over y} = 5  
      \end{cases}
  \end{align}
  $  
  &nbsp;  
  **判断是否有解**  
  暂无  
  &nbsp;  
  **解方程**  
  转换: $ x = 3 - y $     
  代入: $ { 3 - y \over y } = 5 $  
  过程: $ 3 - y = 5y $  
  过程: $ 3 = 5y + y $  
  过程: $ 3 = 6y $  
  过程: $ {3 \over 6} = {6y \over 6} $  
  过程: $ {1 \over 2} = y $  
  结果: $ y = {1 \over 2} $  
  代入: $ x + {1 \over 2} = 3 $  
  过程: $ x = 3 - {1 \over 2} $  
  过程: $ x = {6 \over 2} - {1 \over 2} $  
  结果: $ x = {5 \over 2} $  
  结论: $ \begin{cases}
              x = {5 \over 2} \\\\
              y = {1 \over 2}  
          \end{cases}
        $

&nbsp;  
> 加减消元法  

- **例-2**  
  $
  \begin{align}
      \begin{cases}
           2x +  y  = 7 \\\\\\\\
           4x - 2y  = 6  
      \end{cases}
  \end{align}
  $  
  &nbsp;  
  **判断是否有解**  
  暂无  
  &nbsp;  
  **解方程(减法)**  
  转换: $ (2x + y) - (4x - 2y) = (7 - 6) $  
  公约: $ (2x * 2) + (y * 2) = (7 * 2) $  
  结果: $ 4x + 2y = 14 $  
  过程: $ (4x + 2y) - (4x - 2y) = (14 - 6) $  
  过程: $ 4x + 2y - 4x + 2y = 8 $  
  移位: $ 4x - 4x + 2y + 2y = 8 $  
  过程: $ 4y = 8 $  
  过程: $ y = {8 \over 4} $  
  结果: $ y = 2 $  
  代入: $ 2x + 2 = 7 $  
  过程: $ 2x = 7 - 2 $  
  过程: $ 2x = 5 $  
  结果: $ x = {5 \over 2}$  
  结论: $ \begin{cases}
              x = {5 \over 2} \\\\
              y = {1 \over 2}  
          \end{cases}
        $

&nbsp;  
- **例-3**  
  鸡、兔共35只, 共94条腿, 求鸡兔各几只?  
  $
  \begin{align}  
      \begin{cases}  
          x + y = 35 \\\\\\\\  
          2x + 4y = 94
      \end{cases}
  \end{align}
  $  
  &nbsp;  
  **判断是否有解**  
  暂无  
  &nbsp;  
  **解方程**  
  转换: $ (x + y) - (2x + 4y) = (35 - 94) $  
  公约: $ (x * 2) + (y * 2) = 35 * 2 $  
  结果: $ 2x + 2y = 70 $  
  过程: $ (2x + 2y) - (2x + 4y) = (70 - 94) $  
  过程: $ 2x + 2y - 2x - 4y = -24 $  
  移位: $ 2x - 2x + 2y - 4y = -24 $  
  过程: $ -2y = -24 $  
  过程: $ y = {-24 \over -2} $  
  结果: $ y = 12 $  
  代入: $ x + 12 = 35 $  
  过程: $ x = 35 - 12 $  
  结果: $ x = 23 $  
  结论: $\begin{cases}
              x = 23 \\\\
              y = 12 \\\\
         \end{cases}
        $  
  代入: $ 2x + 4y = 94 $  
  代入: $ (2 * 23) + (4 * 12) = 94 $  
  代入: $ 46 + 48 = 94 $   

  