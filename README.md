# Competition · Research · Visual Skills

面向创赛、科研和文档视觉工作的 **31 个轻量 Agent Skills**。每个入口都写明输入、工作步骤、产出、工具条件与可复制的调用例句。

[English](README.en.md) · [详细目录](catalog/skills.json) · [来源与分发范围](SOURCES.md) · [MIT License](LICENSE)

这个项目适合希望把项目资料变成BP、论文、演示和可交付文档的使用者，也适合维护自己的技能库。公开版使用 `crv-` 前缀，便于与已有技能区分。

## 项目是什么

**Competition · Research · Visual Skills，简称CRV Skills，是一套围绕“资料如何变成可靠交付物”组织的开源技能集合。**

它把创赛、科研写作和文档视觉任务拆成清楚的工作流程。每个技能都要求先识别任务、读取真实资料、确定证据，再完成相应的分析与输出。你可以只用一个技能处理局部任务，也可以沿着项目进程组合使用。

这里的Skill是一份供Agent读取的`SKILL.md`说明。它规定任务的输入、关键步骤、产出和边界；Agent根据说明调用当前环境中可用的工具。因此，安装技能后获得的是清楚的任务流程，实际读写Word、制作PPT、生成图像等仍需要相应工具。

### 解决哪些常见问题

|常见情况|CRV提供的处理方式|
|---|---|
|项目文件很多，却不清楚先写BP还是先改PPT|先用创赛总控整理事实、证据和目标，再选择内容主流程|
|技术介绍很长，用户价值和商业路径不清楚|分开审查需求、技术优势、验证与价值获取之间的关系|
|论文文字流畅，但方法、结果和结论衔接不足|围绕研究问题、证据与章节职责组织文本|
|图做出来了，却说不清单位、误差与比较条件|先确认数据定义，再选图型并保留可复查代码|
|PPT内容、视觉和可编辑需求混在一起|分别选择内容设计、原生编辑、SVG或图片版路线|
|用了很多技能，反而重复执行或互相覆盖|一次确定一个主流程，只为具体缺口追加辅助|
|说明只有“能做什么”，没有怎么开始|每个入口同时提供输入、产出、工具条件与调用例句|

### 适合哪些使用者

- **大学生创新创业团队**：整理商业计划、网评材料、路演与答辩内容。
- **研究生和科研人员**：组织论文、研究计划、审稿回复、学术英文与科研图件。
- **教师和技术项目团队**：把研究报告、实验记录或技术方案转成可阅读、可演示的材料。
- **文档与视觉工作者**：处理Word、PDF、表格、演示、图像、海报和动画等具体交付。
- **Agent技能维护者**：按类别选择入口，维护输入输出清楚、范围可控的个人工作流。

## 一个任务怎样走到交付

```mermaid
flowchart LR
    A[任务与真实资料] --> B[选择一个主技能]
    B --> C[分析事实与证据]
    C --> D[调用当前可用工具]
    D --> E[检查内容与文件]
    E --> F[交付结果与缺口说明]
```

内容分析和文件制作是两个需要衔接的环节。例如，`crv-contest-deck`负责规划每页的结论与证据；`crv-native-deck`负责使用实际演示工具制作或编辑PPTX。需要图片版路线时改选`crv-image-deck`，需要统一主题时再使用`crv-slide-design-system`。

你已经知道具体任务时，可以直接选专用技能。只改一页PPT、润色一段英文或提取一个PDF表格，都不需要先运行整个项目流程。

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

## 三类31个技能详解

### 创赛与商业：6个技能

帮助团队把项目事实组织成比赛能理解的商业论证、演示内容和答辩表达。

|技能入口|主要用途|预期交付|
|---|---|---|
|[crv-contest-router](skills/crv-contest-router/SKILL.md)|创赛任务总控：梳理创业竞赛项目材料，识别BP、PPT、答辩交付，选择一个主要工作流。|事实与证据清单、最小工作流选择、修改顺序|
|[crv-challenge-bp](skills/crv-challenge-bp/SKILL.md)|小挑创业计划书：撰写或审查挑战杯创业计划类BP，对齐实际模板、项目阶段和评分证据。|章节正文、证据对应表、待补信息|
|[crv-business-plan](skills/crv-business-plan/SKILL.md)|商业计划分章写作：根据项目事实与公开证据撰写市场、产品、商业模式、财务和实施章节。|章节分析、正式正文、来源与假设清单|
|[crv-contest-deck](skills/crv-contest-deck/SKILL.md)|创赛PPT内容设计：把创业项目转成网评、路演或答辩PPT的页序、结论和证据安排。|逐页内容稿、讲稿安排、证据与页面对应|
|[crv-business-review](skills/crv-business-review/SKILL.md)|商业逻辑审查：审查需求、技术价值、竞争差异和价值获取之间的断点，给出可执行修改。|逻辑问题、验证问题、修改建议|
|[crv-slide-logic](skills/crv-slide-logic/SKILL.md)|PPT单页逻辑：优化已有幻灯片的结论标题、信息主次和证据表达。|结论标题、删改清单、信息层级建议|

完整输入、步骤、边界和例句见[该类详细指南](docs/competition.md)。

### 科研与学术：5个技能

围绕研究问题、方法、结果与证据，处理写作、编辑、科研图和技术解释。

|技能入口|主要用途|预期交付|
|---|---|---|
|[crv-research-writing](skills/crv-research-writing/SKILL.md)|科研写作：根据真实研究材料组织论文、综述、研究计划或逐条审稿回复。|学术文本、论证缺口、引用与结果核对清单|
|[crv-academic-editing](skills/crv-academic-editing/SKILL.md)|学术英文编辑：编辑已有学术内容的段落逻辑、章节职责和英文表达，保留证据与结论边界。|编辑稿、主要修改原因、未解决的科学问题|
|[crv-scientific-figures](skills/crv-scientific-figures/SKILL.md)|科研静态图：将真实数据制作成可复查的静态科研图，交付绘图代码和图件。|绘图代码、SVG或PDF、预览与数据处理说明|
|[crv-technical-explainer](skills/crv-technical-explainer/SKILL.md)|技术讲解与答辩：把复杂技术改写成受众能跟上的条件、模型、推理与结论。|讲解骨架、短答与展开回答、追问清单|
|[crv-evidence-review](skills/crv-evidence-review/SKILL.md)|技术证据与取舍：比较技术方案的资料质量、实验条件、性能和代价，区分事实与推断。|证据对比、取舍建议、待验证问题|

完整输入、步骤、边界和例句见[该类详细指南](docs/academic.md)。

### 文档演示与视觉：20个技能

将已经明确的内容转化为指定格式的材料，并检查文件、视觉与实际可编辑范围。

|技能入口|主要用途|预期交付|
|---|---|---|
|[crv-docx](skills/crv-docx/SKILL.md)|Word文档编辑：使用当前可用工具创建或修改Word文档，并验证内容与版式。|DOCX文件、修改说明、必要的渲染检查|
|[crv-pdf](skills/crv-pdf/SKILL.md)|PDF读取与处理：选择当前PDF工具完成提取、拆合、填表或排版检查。|处理结果、输出文件、识别或版式限制说明|
|[crv-spreadsheets](skills/crv-spreadsheets/SKILL.md)|表格与数据分析：使用表格工具编辑工作簿、检查公式和单位，并形成可追溯结果。|工作簿或表格、公式与假设说明、结果核对|
|[crv-native-deck](skills/crv-native-deck/SKILL.md)|原生PPT编辑：创建或修改含原生对象的PPTX，检查实际渲染和可编辑范围。|PPTX文件、预览、可编辑性说明|
|[crv-source-to-deck](skills/crv-source-to-deck/SKILL.md)|材料转分析型演示：将报告或数据转换为有证据支持、结论清楚的分析型演示稿。|证据提纲、逐页计划、实际工具生成的演示|
|[crv-svg-deck](skills/crv-svg-deck/SKILL.md)|SVG演示制作路线：按统一设计约束制作SVG页面，并在具备导出工具时转为PPTX。|SVG页面、设计约束、可用时的PPTX导出|
|[crv-image-deck](skills/crv-image-deck/SKILL.md)|图片版演示路线：规划视觉优先的图片版演示，并明确图片与可编辑内容的区别。|逐页视觉说明、页面图片、具备工具时的组装文件|
|[crv-slide-design-system](skills/crv-slide-design-system/SKILL.md)|演示主题与版式：定义可复用的演示配色、字体、画幅、网格与页面版式规则。|主题规则、版式规范、页面样例要求|
|[crv-document-coauthoring](skills/crv-document-coauthoring/SKILL.md)|文档共创：与用户迭代需求、结构和正文，使文档对目标读者可用。|结构与正文、未解决问题、读者可用性检查|
|[crv-technical-docs](skills/crv-technical-docs/SKILL.md)|技术与接口文档：基于实际代码、接口与运行方式编写可操作的技术文档。|使用或开发文档、接口说明、可验证示例|
|[crv-readme](skills/crv-readme/SKILL.md)|开源README：为公开仓库写清项目用途、快速开始、能力范围和维护方式。|README、可复制示例、文档链接|
|[crv-internal-comms](skills/crv-internal-comms/SKILL.md)|内部沟通材料：将真实进展、决策、问题和行动整理成适合组织内部阅读的材料。|进度或事件说明、决策与行动、待确认事项|
|[crv-public-article](skills/crv-public-article/SKILL.md)|公开文章与公众号：根据真实素材完成选题、文章、润色、审稿或发布前内容检查。|选题或文章、修改说明、发布前问题|
|[crv-web-to-markdown](skills/crv-web-to-markdown/SKILL.md)|公开网页转Markdown：将可访问的公开网页正文转换成带来源的Markdown。|Markdown正文、来源链接、提取限制|
|[crv-image](skills/crv-image/SKILL.md)|图像生成与编辑：规划并使用当前图像工具完成位图生成或编辑，核对结果是否符合用途。|实际生成图、必要的变体、结果说明|
|[crv-poster](skills/crv-poster/SKILL.md)|静态视觉与海报：为明确传播目标设计海报或静态视觉，交付实际图件。|版面方案、PNG或PDF等图件、素材说明|
|[crv-generative-art](skills/crv-generative-art/SKILL.md)|可复现算法艺术：用程序和确定性参数制作可复现的原创生成艺术。|源代码、参数与种子、可用时的预览|
|[crv-gif](skills/crv-gif/SKILL.md)|动画GIF：制作适合指定渠道的循环动画并检查尺寸、帧率和文件体积。|GIF文件、预览、尺寸帧率等参数|
|[crv-brand](skills/crv-brand/SKILL.md)|用户品牌规范：将用户提供的品牌颜色、字体、标志与使用条件应用到指定材料。|品牌应用规则、材料修改、一致性检查|
|[crv-theme](skills/crv-theme/SKILL.md)|文档与视觉主题：为文档、演示或网页建立适配内容的主题规则并验证代表页面。|配色与字体规则、组件映射、代表页面检查|

完整输入、步骤、边界和例句见[该类详细指南](docs/documents.md)。

### 怎样区分容易混用的入口

|你正在做的事|优先入口|选择依据|
|---|---|---|
|重写一份BP正文|crv-challenge-bp或crv-business-plan|按比赛或章节目标组织连续论证|
|检查BP为什么说服不了人|crv-business-review|定位需求、证据、价值和商业路径的断点|
|规划一套比赛PPT|crv-contest-deck|安排页序、单页结论与证据|
|改善已有PPT的一页|crv-slide-logic|只处理这一页的逻辑、标题和信息主次|
|修改已有可编辑PPTX|crv-native-deck|保留原生结构和约定编辑范围|
|从报告形成分析型演示|crv-source-to-deck|先提取证据并建立论证顺序|
|制作视觉优先的图片演示|crv-image-deck|按页面图像表达，明确编辑能力依赖|
|重构学术内容或起草章节|crv-research-writing|组织研究问题、方法、结果与引用|
|编辑已有科学内容的英文|crv-academic-editing|先保持主张与证据，再改结构和语言|
|比较技术方案能否成立|crv-evidence-review|比较来源质量、实验条件与性能代价|

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

## 四个完整使用场景

以下场景展示的是如何组织请求。项目、资料和结果都是待你填入的内容，不代表仓库自带真实项目或实验成果。

### 场景一：从创赛资料到BP和路演

你已有产品说明、样机测试、用户访谈和一份旧BP。先用`crv-contest-router`整理哪些是事实、哪些仍是计划，确定最影响本轮交付的问题。随后由BP技能形成正文，再用`crv-contest-deck`转成页级内容。制作文件时，根据可编辑需求选择具体演示路线。

```text
$crv-contest-router
输入：项目资料目录、真实测试记录、访谈记录和本次评分表。
阶段：已有样机，正在准备创业竞赛。
任务：先找出需求、验证和商业路径之间的断点，再重写最薄弱的一章。
输出：正式正文、每项关键主张对应的证据，以及待补事项。
```

这条路线的重点是先形成可信的内容。商业逻辑审查和单页优化只在出现相应问题时追加，不需要每次把6个创赛入口全部运行一遍。

### 场景二：从真实研究到论文与科研图

你已有研究问题、方法、数据和实验结果。`crv-research-writing`负责组织具体章节，`crv-scientific-figures`负责让图件与数据处理过程可复查。已有科学论证需要英文编辑时，再使用`crv-academic-editing`。

```text
$crv-research-writing
输入：真实方法说明、实验记录、现有图表和参考文献。
任务：撰写方法与结果部分，保留参数、比较条件和结论边界。
输出：章节正文、图表引用对应和仍缺少的可复现信息。
```

针对图件，可以单独提出：

```text
$crv-scientific-figures
输入：原始数据、字段单位、重复实验和误差定义。
任务：绘制方法对比图，明确比较条件。
输出：数据处理与绘图代码、SVG/PDF和预览图。
```

论文、图件和摘要应使用同一套真实结果。写作流程可以揭示缺失证据，但不能把未完成实验写成已经完成。

### 场景三：把一份报告做成可演示材料

先用`crv-source-to-deck`梳理报告中的事实、冲突和决策问题，形成逐页论证。若需要交给别人修改，选择`crv-native-deck`并说明哪些文字、图表必须原生可编辑；若更重视整页视觉，选择`crv-image-deck`并接受相应编辑限制。

```text
$crv-source-to-deck
输入：报告、数据表、可使用的图片和现有模板。
受众：需要理解结论与行动建议的读者。
任务：整理成12页分析型演示，先给每页结论和证据来源。
输出：逐页内容，再使用当前实际工具制作PPTX并检查渲染。
约束：关键文字和数据图表需要可编辑，保留来源与假设。
```

主题、颜色和版式可以用`crv-slide-design-system`统一。主题配置、SVG页面、整页图片和PPTX母版分别是不同交付物，应在请求中写清。

### 场景四：为一个技术项目完善开源说明

当项目已有代码和使用方式，可以用`crv-readme`写首页，用`crv-technical-docs`补充接口与开发文档。文档内容需要回到真实实现与可复现命令。

```text
$crv-readme
输入：这个仓库的代码、配置、运行命令和已有文档。
读者：第一次接触项目的使用者。
任务：说明用途、安装、最小示例、实际输出与工具条件。
输出：可以直接放到仓库首页的README，核对所有命令和本地链接。
```

## 与原本地技能的关系

这个公开仓库从三类实际工作需求中整理了新的轻量流程，使用独立的`crv-`名称。原本地标签到公开入口的对照记录在[SOURCES.md](SOURCES.md)，方便已有用户查找任务。

公开版重新编写了流程、说明、示例与管理脚本，保留的是清楚的任务分工。它没有打包原本地目录，也没有复制第三方完整的生成引擎、模板库、人物身份设定或私有资料。`crv-image-deck`不能仅凭名称被理解为包含SlideMuse引擎，`crv-svg-deck`也不等于已安装ppt-master。

原始材料的来源与许可需要分别核对。本仓库MIT许可证适用于仓库中的原创内容，不能用来改变第三方原件的许可。

## 常见使用问题

### 只会聊天也能开始使用

可以先让Agent阅读某个`SKILL.md`，并提供任务和资料。文字分析、提纲与审查意见通常可以先完成。需要读写文件、生成图片或渲染图表时，再确认当前环境是否具备对应工具。

### 安装完成后的工具条件

安装脚本只复制技能说明和许可证，不安装模型、插件、软件或API权限。能否实际制作Word、PPTX、PDF或图像，取决于你的Agent和运行环境。对应条件在每个技能的“工具条件”中列出。

### 不必一次安装或加载全部技能

可以只安装一个入口，或只选择一个类别。使用时先确定主任务，已知具体交付就直接选专用入口。辅助流程应围绕实际问题追加，避免重复分析和互相改写。

### 已有同名技能时

安装器会在写入前检查本次所选目标，遇到已有目录就停止。它不会覆盖、合并或删除已有技能。你可以选择其他兼容目标目录，或先自行比较版本与内容。

### “输出成功”的判断

内容稿应检查事实、引用与结论；文件还应检查能否打开、版式和对象是否符合约定。PPTX存在不代表所有元素可编辑，公式写入工作簿不代表已经重算，科研图导出不代表统计方法已经验证。

### 高校申请材料的范围

当前仓库集中在创赛、科研和文档视觉三类，没有打包另一套高校奖助、评优、身份或大创申报子技能。科研或商业流程可以辅助技术与商业论证，正式申报仍应以具体学校的通知和表格为依据。

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
