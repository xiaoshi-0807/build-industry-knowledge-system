# Build Industry Knowledge System

一套可复用的 Codex Skill，用于从零搭建任意行业的完整认知体系。

## 五个模块

1. 建立行业数据库：品牌、产品、痛点、关键词、社区、竞品、商业模式、机会点。
2. 深度分析竞品网站：产品架构、Offer、转化、内容、SEO 与商业模式。
3. 分析平台 Top 账号与内容：定位、内容类型、爆款结构与可执行策略。
4. 生成三级行业知识地图：节点关系、增长信号、竞争强度与机会排序。
5. 搭建持续情报系统：信息源订阅、竞品监控、趋势追踪和行业周报。

## 安装

将 `build-industry-knowledge-system` 文件夹复制到：

```text
~/.codex/skills/
```

也可以下载仓库内的 `build-industry-knowledge-system.skill.zip` 后解压安装。

## 使用

```text
使用 $build-industry-knowledge-system 从头到尾搭建美国宠物补充剂行业认知体系。
```

也可以只执行一个模块：

```text
使用 $build-industry-knowledge-system 深度分析竞品网站 example.com。
```

五条可复用任务提示词位于：

```text
build-industry-knowledge-system/references/task-prompts.md
```

## 自动生成项目骨架

```bash
python3 build-industry-knowledge-system/scripts/scaffold_industry_system.py \
  --industry "Home Fitness Equipment" \
  --market "United States" \
  --output "/absolute/path/to/project"
```

## 审计项目完整性

```bash
python3 build-industry-knowledge-system/scripts/audit_industry_system.py \
  /absolute/path/to/project
```

## 设计原则

- 构建相互连接的决策系统，而不是五份孤立报告。
- 动态事实、排名、价格、规模和法规必须核验并标注日期。
- 明确区分观察事实、分析推断和行动建议。
- 后续模块持续复用并更新前序行业数据库。

