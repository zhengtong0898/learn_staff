# notebook

&nbsp;  
### 阅读是什么?
阅读是系统的掌握新知识(专业技能)、快速传承经验(历史、传记)、陶冶精神(励志、传奇、爱情、哲学)的力量.

**知识传递的变迁**  
1. 在古代, 人类想要掌握一项技能有两种途径, 第一种途径是跟着师傅的言传身教来接受传承.   
第二种途径就是自己探索、研究、受挫折、消停、再继续探索、研究、受挫折循环往复直到实现自己的期望.   
2. 在往后, 人类通过纸质写作来(唯一的途径)留下毕生有价值知识, 让后人可以通过阅读来加速学习的过程.  
3. 最近几十年, 随着视频、动画的兴起, 让知识更生动学习更有趣味性, 最终的效果是提高大家的兴趣, 最终不再抗拒学习.    

**新兴技术的局限**  
1. 仍然缺少能够承受住时间沉淀的经典.  
2. 更多的是娱乐性质的内容, 抢走更多本应该用来与 *学习*、*陪伴*、*无聊*、*思考* 的时间.  
3. 更多的是碎片化的知识、不是系统化的知识.  

阅读、视频都能够透过许多人的经验总结，省去原本需要花很大的时间去探索、去研究、去体验、  
受过挫折的一个过程、或者一个新的认知，因此这是可以快速学习的一个途径.  

&nbsp;  
### 如何成为一个靠谱的人?  
1. 靠谱: 按时完成工作安排的事情, 或者自己计划完成的事情, 先讲完成再讲完美.  
2. 完美: 如果想要做得更好, 就需要在做完的基础上反复总结, 试图找到可改进的点, 并思考如何去改进它.  
3. 评估: 如果评估一件事情两周可以做完, 但是实际上三、四周才做完, 那么就是评估能力不足,   
   &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;需要思考中间被哪些事情block了, 这些事情是否可以被量化, 是否可以被当作下次评估耗时的理由和经验.   
   &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;如果不具备准确的评估能力, 那么任何计划都不可能被有效的执行以及达到符合预期的效果.  


&nbsp;  
### 如何管理自己的情绪?  
从小到大我们一直被教导做人要(正面情绪): 乐观、开朗、积极、向上、坚强、勇敢、自信、高效率、动作要快;     
不鼓励或贬低这些行为(负面情绪): 懒散、马大哈、沮丧、恐惧、紧张、焦虑、纠结、悲伤、急躁;     
现代的文明病例如(失眠、忧郁症、癌症)很多时候与自身的负面情绪情绪失调息息相关;     
正面情绪和负面情绪就像是太极中的阳和阴, 当阳被过度消耗后阴就被悄悄扩大, 它在潜移默化的影响着人的情绪.  
正视自己的负面情绪, 接纳它并尝试找到什么情况下能够明显感觉到它的出现, 需要做些什么才能让它得到缓解甚至是放下.  
[参考资料-1](https://youtu.be/Ueoyveyz5LU?t=933) 、 [参考资料-2](https://www.youtube.com/watch?v=ygA-6CaH6Qg)  


&nbsp;  
### 如何阅读源码?  
1. 入门: 必须先从`tutorial教程`理解功能开始, 然后才到理解源码.  
2. 调试: 必须先掌握断点调试的能力.
3. 作用: 以函数或方法为单位去理解每一行代码, 并推导出它的作用.  
4. 关系: 需要经常梳理对象和对象之间的关系, 如果不组成这样的关系会怎样, 会不会有更好的组合方式?  
5. 单测: 复杂代码需要翻阅单元测试代码, 配合断点调试去理解, 若仍不理解就设计一个或多个用例去运行和理解.  
6. 流程: 一个大的功能会随着不同的参数进入不同的流程分支, 有必要为每个分支画一个流程图、时序图、状态图.  
7. 算法: 这个通常只有扎实的算法功底才会识别框架中的特定算法, 才能快速理解, 否则将会被算法阻挡在门外.  
8. 模式: 在面向对象的世界里, 对象都是离散(各自独立)的, 因此就需要特定的模式去抽象和组合它们.  
9. 视角: 第3点强调的是细节(每一行代码的理解), 而这里强调要善于`zoom out`去关注它们的`control`.  
10. 策略: 
    > 由于对象是离散的, 在分析源码的时候我会先将对象列出来,   
    > 但不会立刻分析所有的方法, 而是根据教程将需要用到的方法进行分析.  
    > 这种分析策略将问题的分为两个象线, 一个是重要且紧急的, 一个是重要不紧急的.  
    > 重要且紧急的指的是主流程必经的执行链路的方法, 是需要分析的.  
    > 重要不紧急的指的是非主流程的特殊场景的执行链路的方法, 后面有时间在慢慢补充.  

&nbsp;  
### 如何成为专家?  
1. 看准行业深挖相关技术原理, 坚持周期性跟踪论文, 积累和善用关键评价标准等.   
2. 看问题把自己站位放高点, 如果你是相关的项目经理, 开发老大, 甚至vp, 你想从报告里得到些什么信息.  
3. 对岗位和行业趋势有敏感度, 多参加峰会, 并将峰会趋势主题进行研究.  
4. 学会可视化数据，觉得自己不足就多做ppt，培养报告思路和报告呈现.  
