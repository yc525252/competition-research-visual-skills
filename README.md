# Competition · Research · Visual Skills

面向创赛、科研和文档视觉工作的 **31 个轻量 Agent Skills**。每个入口都写明输入、工作步骤、产出、工具条件与可复制的调用例句。

[English](README.en.md) · [详细目录](catalog/skills.json) · [来源与分发范围](SOURCES.md) · [MIT License](LICENSE)

这个项目适合希望把项目资料变成BP、论文、演示和可交付文档的使用者，也适合维护自己的技能库。公开版使用 `crv-` 前缀，便于与已有技能区分。

## 先选一个入口

|大类|数量|推荐从这里开始|详细说明|
|---|---:|---|---|
|创赛与商业|6|[crv-contest-router](skills/crv-contest-router/SKILL.md)、[crv-contest-deck](skills/crv-contest-deck/SKILL.md)|[创赛指南](docs/competition.md)|
|科研与学术|5|[crv-research-writing](skills/crv-research-writing/SKILL.md)、[crv-scientific-figures](skills/crv-scientific-figures/SKILL.md)|[科研指南](docs/academic.md)|
|文档演示与视觉|20|[crv-native-deck](skills/crv-native-deck/SKILL.md)、[crv-docx](skills/crv-docx/SKILL.md)、[crv-image](skills/crv-image/SKILL.md)|[文档视觉指南](docs/documents.md)|

## 最快使用

无需先安装任何Python依赖，也可以打开对应的 `SKILL.md`，让你的Agent读取并按任务使用。支持自动发现技能的环境可安装后使用如下句式：

```text
$crv-contest-router
输入：项目资料目录、比赛模板和已有BP。
任务：先统一事实与证据，再选择合适流程重写最薄弱的一章。
输出：正式正文、证据缺口和下一步建议。
```

`$技能名` 是否自动识别取决于宿主。不能自动识别时，请明确提供实际 `SKILL.md` 路径。不要一次加载全部31份正文。

## 安装与查询

管理脚本使用 **Python 3.10及以上**，只依赖标准库：

```bash
git clone https://github.com/yc525252/competition-research-visual-skills.git
cd competition-research-visual-skills
python scripts/list_skills.py
python scripts/list_skills.py --search PPT
python scripts/install.py --category competition --dry-run
python scripts/install.py --category competition
```

默认安装到 `CODEX_HOME/skills`，未设置 `CODEX_HOME` 时使用用户目录下的 `.codex/skills`。只安装一个入口或指定其他兼容目录：

```bash
python scripts/install.py --skill crv-research-writing
python scripts/install.py --category academic --target ../my-project/.agents/skills
```

已有同名目标会使安装在写入前停止；安装器不会覆盖现有技能。`--dry-run`显示计划但不写入。其他宿主的发现机制请按其实际说明配置；脚本只复制文件，不修改宿主设置，也不自动获得模型或服务权限。

## 能做什么，工具要准备什么

这31个入口是可阅读、可安装的任务工作流。它们组织输入、分析与验证；实际文件、图像或图表仍由当前Agent可用工具完成。

|任务|工具条件|交付说明|
|---|---|---|
|BP、正文、审查、讲稿|能读取用户资料的Agent|可先交付文本；输出文件时需对应编辑工具|
|Word、PDF、工作簿|实际文件编辑、解析或渲染工具|本仓库不提供厂商引擎或工作簿重算引擎|
|PPTX、SVG演示|实际制作、渲染和导出工具|应分别说明原生对象、图片和可编辑范围|
|图像、图片PPT、GIF|实际图像生成、设计或动画工具|未取得工具能力时只交付计划，不声称文件已生成|
|科研图|绘图库与用户真实数据|区分误差类型、统计依据与导出格式|

本项目不内置第三方完整PPT流水线、模型、字体、模板或原项目脚本。原始本地标签和许可观察见 [SOURCES.md](SOURCES.md)。这些原创轻量流程的功能范围已在各入口说明，不表示与历史标签对应的第三方项目完整等价。

## 推荐组合

|你的任务|最小组合|
|---|---|
|创赛BP|`crv-contest-router`选择`crv-challenge-bp`或`crv-business-plan`|
|创赛PPT|`crv-contest-deck`；具体制作再选原生、SVG或图片路线|
|论文与科研图|`crv-research-writing`，按需追加`crv-academic-editing`或`crv-scientific-figures`|
|技术答辩|主内容流程配合`crv-technical-explainer`|
|报告转演示|`crv-source-to-deck`配合当前实际演示工具|
|开源项目说明|`crv-readme`或`crv-technical-docs`|

一个任务通常只需要一个主流程。案例与数字必须有来源；计划、预测、意向和已完成事实分别表达。对外发送、公开发布或其他外部动作依照用户明确授权执行。

## 示例与验证

- [创赛调用示例](examples/competition.md)
- [科研调用示例](examples/academic.md)
- [文档与演示调用示例](examples/documents.md)
- [功能范围与验证边界](docs/capabilities.md)

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

上述检查覆盖目录、元数据、文档链接、内容范围与安装器行为，不代表31个业务场景都已执行，也不验证外部模型或渲染服务。

## 仓库结构

```text
skills/             31个独立SKILL.md入口
catalog/skills.json 机器可读目录与说明数据
docs/               三类详细解释与能力边界
examples/           不含私有材料的调用示例
scripts/            查询、安装与结构验证
tests/              安装器与选择行为检查
SOURCES.md          历史标签、许可观察和分发范围
```

欢迎改进具体流程、补充可复现实例和工具条件。贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。新贡献需有清楚来源，不应包含私有资料、服务凭据或许可不明的第三方实现。
