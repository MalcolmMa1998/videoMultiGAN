# Video Multi GAN
使用树状决策从文本生成视频，而使用GAN决策。 使用LM将文本注释或语句编码为嵌入，然后将其与随机向量组合以生成相关的视频和图像。

## 视频生成模型
1. VAEGAN
2. 具有潜在变量优化功能的VAEGAN
3. VAEGAN具有抗重建损失
4. VAEGAN +抗重建损失+潜在变量模型
5. 具有不同Hyper参数的上述模型的变体

## 模型结构
* 基于LSTM的下一帧创建模型
* Wasserstein GAN设置标识符
* 基于词嵌入的LM
* 基于注意力的分类结构模型

## Training model
* 相关模型在```Tensorflow> = v1.2```中
* 使用上述模型进行实验
* 通过基于句子的注释自行生成的弹跳MNIST进行训练
* gensim预训练的fastText Wikipedia工作嵌入用于将标记嵌入为向量
* 基于非注意力的模型最初用于生成起始帧。
* GAN树训练寻找区别特征（未经验证）。

## 数据集
1. UCF101 : 3 channel image
2. Bouncing MNIST

## 文献资料
1. 我们使用Sync-DRAW开发我们的数据集（https://github.com/syncdraw/Sync-DRAW）
2. UCF101可从蒙特利尔大学获得
3. 我们使用多个GPU训练（或单个K80或Titan X）
4. 目前无法进行集群迁移

### 由于可能会有相关的出版物，因此此处不会更新结果。
