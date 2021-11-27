import uuid


count = 1


def fibonacci(n: int, side=None, uid=None) -> int:
    """
                                          6
                             /                         \
                           5                          4
                   /               \              /       \
                  4                3             3         2
             /         \          / \           / \       / \
           3            2        2  1          2   1     1   0
         /   \         / \      / \           / \
       2      1       1   0    1   0         1  0
     /   \
    1     0


    count: 1; n: 6; side: None; uid=None                                  # 树根
    count: 2; n: 5; side: left; uid=1debf168                              # 左侧树开始递归
    count: 3; n: 4; side: left; uid=a9704379                              # 左侧树递进
    count: 4; n: 3; side: left; uid=17d31150                              # 左侧树递进
    count: 5; n: 2; side: left; uid=7a2bea9e                              # 左侧树递进
    count: 6; n: 1; side: left; uid=6fad05df                              # 左侧树递进
    count: 7; n: 0; side: right; uid=6da59f4e                             # 左侧树回归
    count: 8; n: 2; side: left; uid: 7a2bea9e; result: 1                  # 回归合并
    count: 8; n: 1; side: right; uid=39b7308f                             # 左侧树回归
    count: 9; n: 3; side: left; uid: 17d31150; result: 2                  # 回归合并
    count: 9; n: 2; side: right; uid=2cd91aff                             # 左侧树回归, 回归对象是一个子树, 需要再次递进和回归
    count: 10; n: 1; side: left; uid=8cf1e7b2
    count: 11; n: 0; side: right; uid=1da660ee
    count: 12; n: 2; side: right; uid: 2cd91aff; result: 1
    count: 12; n: 4; side: left; uid: a9704379; result: 3                 # 回归合并
    count: 12; n: 3; side: right; uid=d35c8038                            # 左侧树回归, 回归对象是一个子树, 需要再次递进和回归
    count: 13; n: 2; side: left; uid=e1f2f394
    count: 14; n: 1; side: left; uid=6832cf49
    count: 15; n: 0; side: right; uid=86efb8e6
    count: 16; n: 2; side: left; uid: e1f2f394; result: 1
    count: 16; n: 1; side: right; uid=bd628831
    count: 17; n: 3; side: right; uid: d35c8038; result: 2
    count: 17; n: 5; side: left; uid: 1debf168; result: 5                 # 回归合并, 左侧树递归结束
    count: 17; n: 4; side: right; uid=7064a0b8                            # 右侧树开始递归
    count: 18; n: 3; side: left; uid=ea0f08c2                             # 右侧树递进
    count: 19; n: 2; side: left; uid=2571d53f                             # 右侧树递进
    count: 20; n: 1; side: left; uid=49411dcd                             # 右侧树递进
    count: 21; n: 0; side: right; uid=da20799e                            # 右侧树回归
    count: 22; n: 2; side: left; uid: 2571d53f; result: 1                 # 回归合并
    count: 22; n: 1; side: right; uid=ccc31a12                            # 右侧树回归
    count: 23; n: 3; side: left; uid: ea0f08c2; result: 2                 # 右侧树合并
    count: 23; n: 2; side: right; uid=95aa32ac                            # 右侧树回归, 回归对象是一个子树, 需要再次递进和回归
    count: 24; n: 1; side: left; uid=c24c18db
    count: 25; n: 0; side: right; uid=6d08464d
    count: 26; n: 2; side: right; uid: 95aa32ac; result: 1
    count: 26; n: 4; side: right; uid: 7064a0b8; result: 3                # 回归合并, 右侧树递归结束
    count: 26; n: 6; side: None; uid: None; result: 8
    8
    """
    global count
    print(f"count: {count}; n: {n}; side: {side}; uid={str(uid).split('-')[0] if uid else uid}")
    count += 1
    if n == 0:                                                                                       # 满足终止层层递进条件
        return 0
    elif n == 1:                                                                                     # 满足终止层层递进条件
        return 1
    else:
        result = fibonacci(n - 1, "left", uuid.uuid4()) + fibonacci(n - 2, "right", uuid.uuid4())   # 最终返回结果给外部程序
        print(f"count: {count}; n: {n}; side: {side}; uid: {str(uid).split('-')[0]}; result: {result}")
        return result


def fibonacci_origin(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_origin(n - 1) + fibonacci_origin(n -2)


def main():
    print(fibonacci(6))


if __name__ == '__main__':
    main()
