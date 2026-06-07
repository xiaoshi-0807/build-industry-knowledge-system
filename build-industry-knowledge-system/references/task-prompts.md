# Reusable Five-Task Prompt Set

Replace variables in braces. Run the tasks in order for a full system.

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
