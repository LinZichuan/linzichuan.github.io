---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am currently a senior researcher at Tencent. I obtained my Ph.D. (2021) and B.S. (2016) in Computer Science at Tsinghua University, advised by [Guangwen Yang](https://scholar.google.com/citations?user=GYA--7MAAAAJ&hl=en).

Previously I was a visiting researcher at Stanford, where I was fortunate to advised by [Tengyu Ma](https://ai.stanford.edu/~tengyuma/). Before that, I spent three years of internship at Microsoft Research and worked closely with [Lintao Zhang](https://www.linkedin.com/in/lintao-zhang/), [Tao Qin](https://taoqin.github.io/) and [Li Zhao](https://scholar.google.co.jp/citations?user=b-LJkLQAAAAJ&hl=en). 

I am currently interested in research topics related to multimodal reasoning, agent, reinforcement learning, causal inference and their commercial applications.
Email: lzcthu12[at]gmail.com

<!--My research interests include reinforcement learning and deep learning. My goal is to develop sample-efficient reinforcement learning algorithms with strong robustness and interpretability. My research projects mainly involve episodic control, reward decomposition, disentangled representation learning, model-based RL and meta-RL. I am also interested in RL applications such as task-oriented dialogue systems. -->




Publications & Preprints 
======
<span style="font-weight: normal; font-size: 17px">($*$ indicates equal contribution, ${\dagger}$ indicates corresponding author)</span>

<style>
.pub-category {
  margin: 15px 0;
}
.pub-category-header {
  cursor: pointer;
  font-weight: bold;
  font-size: 18px;
  padding: 10px;
  background-color: #f5f5f5;
  border-radius: 5px;
  user-select: none;
  transition: background-color 0.3s;
}
.pub-category-header:hover {
  background-color: #e0e0e0;
}
.pub-category-header::before {
  content: "▶ ";
  display: inline-block;
  transition: transform 0.3s;
  margin-right: 5px;
}
.pub-category-header.expanded::before {
  transform: rotate(90deg);
}
.pub-category-content {
  display: none;
  padding: 10px 0 10px 20px;
}
.pub-category-content.expanded {
  display: block;
}
</style>

<!-- .pub-category-header.expanded {
  background-color: #e0e0e0;
} -->

<script>
function toggleCategory(categoryId) {
  const content = document.getElementById(categoryId + '-content');
  const header = document.getElementById(categoryId + '-header');
  if (content.style.display === 'none' || !content.classList.contains('expanded')) {
    content.style.display = 'block';
    content.classList.add('expanded');
    header.classList.add('expanded');
  } else {
    content.style.display = 'none';
    content.classList.remove('expanded');
    header.classList.remove('expanded');
  }
}

// Initialize all categories as expanded when page loads
function initializeCategories() {
  const categories = ['llm-agents', 'rl', 'causal-inference'];
  categories.forEach(function(categoryId) {
    const content = document.getElementById(categoryId + '-content');
    const header = document.getElementById(categoryId + '-header');
    if (content && header) {
      content.style.display = 'block';
      content.classList.add('expanded');
      header.classList.add('expanded');
    }
  });
}

// Try multiple ways to ensure the function is called
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeCategories);
} else {
  // DOM is already loaded
  initializeCategories();
}

// Also try on window load as a fallback
window.addEventListener('load', initializeCategories);
</script>

<div class="pub-category">
  
  <div class="pub-category-header" id="llm-agents-header" onclick="toggleCategory('llm-agents')">
    
    LLM/VLM/Agents
  
  </div>

  <div class="pub-category-content" id="llm-agents-content" markdown="1">

- [AdaptVision: Efficient Vision-Language Models via Adaptive Visual Acquisition](https://arxiv.org/abs/2512.03794) <br>
**Zichuan Lin\***, Yicheng Liu\*, Yang Yang, Lvfang Tao, Deheng Ye <br>
arXiv:2512.03794, 2025 [[Project Page](https://adaptvision.github.io/)]

- [SeeNav-Agent: Enhancing Vision-Language Navigation with Visual Prompt and Step-Level Policy Optimization](https://arxiv.org/abs/2512.02631) <br>
Zhengcheng Wang\*, **Zichuan Lin\***, Yijun Yang, Haobo Fu, Deheng Ye <br>
arXiv:2512.02631, 2025

- [EntroPIC: Towards Stable Long-Term Training of LLMs via Entropy Stabilization with Proportional-Integral Control](https://arxiv.org/abs/2511.15248) <br>
Kai Yang, Xin Xu, Yangkun Chen, Weijie Liu, Jiafei Lyu, **Zichuan Lin**, Deheng Ye, Saiyong Yang <br>
arXiv:2511.15248, 2025

- [CausalMACE: Causality Empowered Multi-Agents in Minecraft Cooperative Tasks](https://arxiv.org/abs/2508.18797) <br>
Qi Chai, Zhang Zheng, Junlong Ren, Deheng Ye, **Zichuan Lin**, Hao Wang <br>
**EMNLP** 2025

- [Joint System-Wise Optimization for Pipeline Goal-Oriented Dialog System](https://arxiv.org/abs/2106.04835) <br>
**Zichuan Lin**, Jing Huang, Bowen Zhou, Xiaodong He, Tengyu Ma <br>
<!--arxiv 2021 -->

  <!-- </div> -->

</div>

<div class="pub-category">
  
  <div class="pub-category-header" id="rl-header" onclick="toggleCategory('rl')">
  
    Reinforcement Learning
  
  </div>

  <div class="pub-category-content" id="rl-content" markdown="1">

- [Multi-agent In-context Coordination via Decentralized Memory Retrieval](https://arxiv.org/abs/2511.10030) <br>
Tao Jiang, **Zichuan Lin$^{\dagger}$**, Lihe Li, Yi-Chen Li, Cong Guan, Lei Yuan, Zongzhang Zhang, Yang Yu, Deheng Ye <br>
**AAAI** 2026 **(Oral)**

- [Revisiting Discrete Soft Actor-Critic](https://arxiv.org/abs/2209.10081) <br>
Haibin Zhou, Tong Wei, **Zichuan Lin**, Junyou Li, Deheng Ye, Qiang Fu, Wei Yang <br>
**TMLR** 2024

- [CurrMask: Learning Versatile Skills with Automatic Masking Curricula](https://openreview.net/forum?id=xGc7I6UWAq) <br>
Zhihui Xie, Yao Tang, **Zichuan Lin**, Deheng Ye, Shuai Li <br>
**NeurIPS** 2024

- [Replay-enhanced Continual Reinforcement Learning](https://arxiv.org/abs/2311.11557) <br>
Tiantian Zhang, Kevin Z. Shen, **Zichuan Lin**, Bo Yuan, Xueqian Wang, Xiu Li, Deheng Ye <br>
**TMLR** 2023

- [A Survey on Transformers in Reinforcement Learning](https://arxiv.org/abs/2301.03044) <br>
Wenzhe Li\*, Hao Luo\*, **Zichuan Lin\***, Chongjie Zhang, Zongqing Lu, Deheng Ye <br>
**TMLR** 2023

- [Future-conditioned Unsupervised Pretraining for Decision Transformer](https://arxiv.org/abs/2305.16683) <br>
Zhihui Xie, **Zichuan Lin**, Deheng Ye, Qiang Fu, Wei Yang, Shuai Li <br>
**ICML** 2023

- [Dynamics-Adaptive Continual Reinforcement Learning via Progressive Contextualization](https://arxiv.org/abs/2209.00347) <br>
Tiantian Zhang, **Zichuan Lin**, Yuxing Wang, Deheng Ye, Qiang Fu, Wei Yang, Xueqian Wang, Bin Liang, Bo Yuan, Xiu Li <br>
**TNNLS** 2023

- [JueWu-MC: Playing Minecraft with Sample-efficient Hierarchical Reinforcement Learning](https://arxiv.org/abs/2112.04907) <br>
**Zichuan Lin\***, Junyou Li\*, Jianing Shi\*, Deheng Ye, Qiang Fu, Wei Yang <br>
**IJCAI** 2022 **(Long Oral top3%)** 
(The champion solution of NeurIPS 2021 [MineRL](https://www.aicrowd.com/challenges/neurips-2021-minerl-diamond-competition/leaderboards) research competition)

- [Model-based Adversarial Meta-Reinforcement Learning](https://arxiv.org/abs/2006.08875) [[code](https://github.com/LinZichuan/AdMRL)]  <br>
**Zichuan Lin**, Garrett Thomas, Guangwen Yang, Tengyu Ma  <br>
**NeurIPS** 2020

- [RD$^2$: Reward Decomposition with Representation Decomposition](https://papers.nips.cc/paper/2020/file/82039d16dce0aab3913b6a7ac73deff7-Paper.pdf)   <br>
**Zichuan Lin\***, Derek Yang\*, Li Zhao, Tao Qin, Guangwen Yang, Tie-yan Liu <br>
**NeurIPS** 2020

- [Episodic Reinforcement Learning with Associative Memory](https://openreview.net/forum?id=HkxjqxBYDB&noteId=HkxjqxBYDB)  <br>
Guangxiang Zhu\*, **Zichuan Lin\***, Guangwen Yang, and Chongjie Zhang  <br>
**ICLR** 2020

- [Object-Oriented Dynamics Learning through Multi-Level Abstraction](https://arxiv.org/abs/1904.07482)  <br>
Guangxiang Zhu\*, Jianhao Wang\*, Zhizhou Ren\*, **Zichuan Lin** and Chongjie Zhang  <br>
**AAAI** 2020

- [Distributional Reward Decomposition for Reinforcement Learning](https://arxiv.org/abs/1911.02166)  <br>
**Zichuan Lin**, Li Zhao, Derek Yang, Tao Qin, Guangwen Yang, and Tie-yan Liu  <br>
**NeurIPS** 2019

- [Fully Parameterized Quantile Function for Distributional Reinforcement Learning](https://arxiv.org/abs/1911.02140) [[code](https://github.com/microsoft/FQF)] <br>
Derek Yang, Li Zhao, **Zichuan Lin**, Jiang Bian, Tao Qin, and Tie-yan Liu  <br>
**NeurIPS** 2019

<!--
- [Unified Policy Optimization for Robust Reinforcement Learning](http://proceedings.mlr.press/v101/lin19a.html)  <br>
**Zichuan Lin**, Li Zhao, Jiang Bian, Tao Qin, and Guangwen Yang  <br>
ACML 2019 **(Oral)**
-->
- [Episodic Memory Deep Q-Networks](https://arxiv.org/abs/1805.07603) [[code](https://github.com/LinZichuan/emdqn)]  <br>
**Zichuan Lin**, Tianqi Zhao, Guangwen Yang, and Lintao Zhang  <br>
**IJCAI** 2018

- [Sample Dropout: A Simple yet Effective Variance Reduction Technique in Deep Policy Optimization](https://arxiv.org/abs/2302.02299) <br>
**Zichuan Lin**, Xiapeng Wu, Mingfei Sun, Deheng Ye, Qiang Fu, Wei Yang, Wei Liu <br>
<!--arxiv 2023 -->

- [Pretraining in Deep Reinforcement Learning: A Survey](https://arxiv.org/abs/2211.03959) <br>
Zhihui Xie, **Zichuan Lin**, Junyou Li, Shuai Li, Deheng Ye <br>
<!--arxiv 2022 -->

  <!-- </div> -->

</div>


<div class="pub-category">

  <div class="pub-category-header" id="causal-inference-header" onclick="toggleCategory('causal-inference')">

    Causal Inference
  
  </div>

  <div class="pub-category-content" id="causal-inference-content" markdown="1">

- [PIPCFR: Pseudo-outcome Imputation with Post-treatment Variables for Individual Treatment Effect Estimation](https://arxiv.org/abs/2512.18737) <br>
**Zichuan Lin\***, Xiaokai Huang\*, Jiate Liu, Yuxuan Han, Jia Chen, Xiapeng Wu, Deheng Ye <br>
arXiv:2512.18737, 2025 [[Code](https://github.com/LinZichuan/PIPCFR)]

  <!-- </div> -->

</div>





<!-- Awards & Honors section -->


<!-- 
Awards & Honors
======

- 北京市优秀博士生, 2021.
- 清华国家奖学金 (Top 1%) , 2018 & 2020.
- [清华大学年度人物提名](https://mp.weixin.qq.com/s/OtJSuCslUEhj2x59Mctixw)，每年20名, 2019. 
- [清华微信公众号采访](https://mp.weixin.qq.com/s/eqKkSmXaBXZVKtjG6s-dPg), 2018. 
- [清华大学十佳优秀运动员](https://mp.weixin.qq.com/s/_K68zJjTLo4zgzc4RE0WnQ)，每年10名, 2017. 
- 清华计算机系本科优秀毕业论文, 2016.
- 首都高校乒乓球比赛男子单打四连冠, 2013-2016.
- 全国中学生乒乓球锦标赛男子双打第三名, 2012.
- 乒乓球国家一级运动员, 2006 & 2012.
- 世界中学生乒乓球锦标赛团体冠军, 2011. -->


<!-- - 84 Innovative Future Scholarship (Top 1%) at department of Computer Science at Tsinghua University, 2020. -->
<!-- - Tsinghua Scholarship for Overseas Graduate Study, 2019. -->
<!-- - Excellence in the Microsoft Research Asia Internship Program, 2018. [[Media Coverage](https://mp.weixin.qq.com/s/KM69I6NycCPUtHapNvATVA)] -->
<!-- - Top 2 in Tsinghua Mathematical Contest in Modeling, 2016. -->


<!--
Manuscripts
======
- [Pretraining in Deep Reinforcement Learning: A Survey](https://arxiv.org/abs/2211.03959) <br>
Zhihui Xie, **Zichuan Lin**, Junyou Li, Shuai Li, Deheng Ye <br>
arxiv 2022

- [Revisiting Discrete Soft Actor-Critic](https://arxiv.org/abs/2209.10081) <br>
Haibin Zhou, **Zichuan Lin**, Junyou Li, Deheng Ye, Qiang Fu, Wei Yang <br>
arxiv 2022

- [Joint System-Wise Optimization for Pipeline Goal-Oriented Dialog System](https://arxiv.org/abs/2106.04835) <br>
**Zichuan Lin**, Jing Huang, Bowen Zhou, Xiaodong He, Tengyu Ma <br>
arxiv 2021
-->

<!--
Talks
======
- JueWu-MC: Playing Minecraft with Sample-efficient Hierarchical Reinforcement Learning <br>
IJCAI, Long Oral, 2022


- Model-based Adversarial Meta-Reinforcement Learning -->

<!--[[videos](https://slideslive.com/38931355/modelbased-adversarial-metareinforcement-learning?locale=en)]-->

<!--
ICML, BIG Workshop, 2020

- Unified Policy Optimization for Reinforcement Learning [[slides](https://drive.google.com/open?id=1N-YhYJpPImix0nQFpVixrhi_c-Xr3EVd)] <br>
Nagoya, Japan, 2019

- Towards Sample-efficient, Interpretable and Robust Reinforcement Learning [[slides](https://drive.google.com/open?id=1gAz23bdgeMrzKFmZc9H4fYs792zXW9Ot)] <br>
Wuxi, China, 2019

- Episodic Memory Deep Q-Networks [[slides](https://drive.google.com/open?id=1hSdLZBnmb5jOGyYkz0cwk24fApRRgu7H)] <br>
Stockholm, Sweden, 2018

- Reinforcement Learning: Episodic Memory and Learning to Run [[slides](https://drive.google.com/file/d/16nCWKtAJW7VqLTyydQtUipD3cmrgZUMT/view?usp=sharing)] <br>
MSRA, Beijing, 2017
-->

<!--
Experience and Services
======
- Reviewer: NeurlPS, ICML, ICLR, AAAI
- Teaching Assistant: Software Engineering (Undergraduate Course, Spring 2016)
-->

<!--
Contact
======
- Email: lastname + zc16 at mails dot tsinghua dot edu dot cn

<a href="https://clustrmaps.com/site/1b2e1" title="Visit tracker"><img src="//www.clustrmaps.com/map_v2.png?d=38tnS4bll5XgaykJkqqgl4v3F3ocQMWiBSN-2_sgxrA&cl=ffffff"></a>
-->

