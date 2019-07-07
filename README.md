# LDA-based-on-partition-PLDA
提出基于划分的LDA主题模型 (PLDA)。对传统LDA模型进行改进，考虑中长篇文档篇章结构较为清晰，传统LDA在处理中长篇文档时不能识别每个篇章的主题，提出基于划分的LDA主题模型，对中长篇文档如新闻报道】国务院工作报告等按照段落进行划分，先拆后合，并将其效果与传统LDA、LSI及doc2vec进行比较。基于Sougou和Fudan语料库的分类实验验证了PLDA效果最优。
论文被 Annals of Data science 录用。
