# Reusable Five-Task Prompt Set

Replace variables in braces. Run the tasks in order for a full system.

## Task 0: Guided Intake For A Tailored Full Report

Use this when the user wants a complete industry report or knowledge system but has not provided enough context.

```text
使用 $build-industry-knowledge-system，先不要直接开始研究。

请先用一轮问题引导我补全研究简报，问题包括：
行业/细分赛道、市场范围、研究目标、我的岗位角色或身份、目标用户、
已有资源与约束、必须分析的竞品/平台/账号、重点维度、报告深度、输出语言和保存位置。

我回答后，请你整理成 Research Brief，然后直接从头到尾生成完整行业认知体系，
包括行业数据库、竞品深挖、平台内容分析、三级知识地图和持续情报系统。
```

## Full-System Prompt With Intake Answers

```text
使用 $build-industry-knowledge-system，从头到尾搭建 {市场} 的 {行业/细分赛道} 行业认知体系。

我的身份/岗位角色是：{角色}。
研究目标是：{目标}。
目标用户/客户是：{目标用户}。
已有资源或约束是：{资源/约束}。
必须分析的竞品/平台/账号是：{竞品/平台/账号；没有就你来选}。
重点维度是：{重点维度}。
报告深度是：{快速版/标准版/深度版}。
输出语言和保存位置是：{语言/路径}。

请先整理 Research Brief，然后直接执行完整五模块：
1. 行业数据库
2. 竞品网站深度分析
3. 平台 Top 账号与内容分析
4. 三级行业知识地图
5. 持续情报系统

所有现代事实必须联网核验并标注来源和日期，明确区分事实、推断和建议。
最终报告正文、知识库正文和最后总结默认全部用中文输出。
最后运行完整性审计，并告诉我生成了哪些关键文件。
```

## Task 1: Establish The Industry Database

```text
使用 $build-industry-knowledge-system，为 {市场} 的 {行业} 建立完整行业数据库，
研究目标是 {目标}。

建立并连接品牌、产品、用户痛点、关键词、社区、竞品、商业模式和机会点八个维度。
使用最新公开证据，标注来源和动态数据日期，区分事实、推断和建议。
创建行业总入口、各维度地图和最重要节点的专项记录。
```

## Task 2: Deep-Dive A Competitor

```text
使用 $build-industry-knowledge-system，在现有 {行业} 数据库中深度分析竞品
{竞品名称/域名}。

分析导航、分类体系、产品与 Offer、定价、套餐/订阅、信任与声明、转化路径、
内容 SEO、社交分发、商业模式、优势、短板和应对方案。
更新或链接相关数据库记录，清晰标记推断结论。
```

## Task 3: Analyze Top Social Content

```text
使用 $build-industry-knowledge-system，分析 {市场} 中影响 {行业} 买家的
{平台} Top {N} 账号。

定义排名范围和采集日期，分析账号定位、更新频率、内容任务、近期可访问内容表现、
爆款内容、Hook、形式、时长、CTA 和变现路径。
输出可执行的内容策略，并说明数据限制。
```

## Task 4: Generate The Knowledge Map

```text
使用 $build-industry-knowledge-system，把现有 {行业} 数据库整合为三级行业知识地图。

展示产业结构层级、节点关系、依赖链、反馈回路、竞争强度、增长信号、
内容/研究缺口、优先机会、谨慎进入区域和持续追踪指标。
说明哪些结论来自现有数据库，哪些需要新增研究。
```

## Task 5: Establish Continuous Intelligence

```text
使用 $build-industry-knowledge-system，为 {行业} 建立持续情报系统。

包含精选信息源订阅清单、每周竞品变化监控、每日内容增长追踪、趋势自动归档和
行业决策周报。创建可复用模板、配置和可运行监控脚本。
采集失败必须标记为缺失数据，不能当作“没有变化”。
```
