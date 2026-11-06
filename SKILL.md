---
name: pastel-handdrawn-photo
description: Transform any user-provided photo, including food, people, pets, flowers, and products, into a soft pastel hand-drawn diary-style image. Preserve the main subject as realistic photography, add a mandatory thin white hand-drawn contour around its outer silhouette, turn the surroundings into colorful hand-drawn illustrations, and provide editable handwritten text with PNG export. It also supports an optional Torn Paper Reveal collage mode, combining the untouched original photo in the upper-left with the finished treatment across the remaining canvas, joined by an adaptive torn-paper edge.
metadata:
  version: "1.5.0"
  language: "zh-CN"
---

# Pastel Hand-Drawn Photo

## 目标

把用户提供的照片转化为一张轻松、时髦、甜美、带有手帐日记感的混合媒介图片：**主要主体保持真实摄影质感，并必须沿主体整体外轮廓添加一圈细白色手绘描边；主体以外的环境、包装、道具和背景转化为彩色手绘插画**，再加入少量手写短句和 doodle 装饰。主体可以是食物、人物、宠物、鲜花、商品或其他物品。

**v1.1.0 新增：手写文案必须作为独立图层交付。** 用户生成图片后，可以在编辑器中点击某一处手写文字，修改内容、颜色、大小和角度，拖动位置，并导出修改后的 PNG。不要把新增的日记文案直接烘焙进底图。

用户只需上传图片即可开始，不需要另外撰写复杂提示词。

**v1.5.0 新增：全模式强制手写文字区域。** 无论单图模式还是 Torn Paper Reveal 拼贴模式，每张最终成品都必须呈现 2–4 处与照片内容相关的手写日记短句/词组，并搭配少量手绘箭头、爱心或星光等装饰。生成底图时必须主动规划并保留可读的文字留白；随后将文案作为独立可编辑文字对象叠加。不得因主体放大、拼贴构图、撕纸边缘或背景装饰而省略文字。最终预览/合成成品必须能看见文字，不能只交付无文案底图作为唯一结果。

**v1.4.0 新增：Torn Paper Reveal｜撕纸揭示拼贴模式。** 除原有单图模式外，用户可要求将原始照片与最终手绘效果整合在同一张画布中：原图位于左上角，面积约占整张画布的 2/5；其余约 3/5 展示同一张照片经过本 Skill 处理后的完整效果。两者以自适应、不规则的手工撕纸边缘自然衔接，形成“原始照片纸片覆盖在最终作品之上、撕开后显露手绘效果”的视觉关系。此模式是可选输出，不改变原有单图模式。

## 何时触发

- 用户上传图片（包括食物、人像/合照、宠物、鲜花、商品或日常物件），并希望生成同一套彩色手绘、主体白色描边、手帐涂鸦和手写文字风格的图片。
- 用户说“按之前的风格生成”“做成彩色手绘风格”“照片加手绘文字/涂鸦”等。
- 用户只上传图片、没有附加说明，而当前任务上下文已明确使用本 Skill：直接执行，不要重复询问风格。
- 用户希望修改已有作品上的手写文案、调整文字位置或导出成品时，也使用本 Skill 的编辑器工作流。

若用户明确提出新的风格、主体处理方式、背景或画幅要求，以用户本轮要求为准。

## 自动执行原则

1. **收到图片后直接开始。** 不先询问风格、配色、文案或构图；缺少非必要信息时由你自行做审美判断。
2. 使用当前环境可用的图像生成/图像编辑工具，并将用户上传的原图作为编辑参考图。优先编辑原图，不要仅凭文字重新生成一个相似场景。
3. **分层生成，禁止把新写的日记文案画进底图。** 图像生成工具负责保留真实主体、绘制主体白色手绘轮廓、彩色手绘环境/道具及非文字装饰；手写文案必须由 HTML/SVG/Canvas 编辑器单独叠加。
4. 默认输出一个可编辑 HTML 文件。编辑器必须预载生成底图和对应文案，打开后即可点击文字修改，不应要求用户再次手动上传本次生成的底图。
5. 导出 PNG 的按钮必须在编辑器内实际可用。修改文字后点击“导出 PNG”，导出的图片必须包含最新文字内容和底图，分辨率尽可能等于底图原始像素尺寸。
6. 若当前环境支持文件生成，交付 `edit.html`（自包含编辑器）和 `artwork-base.png`（无新增文案的底图）；可同时提供初始合成版 `final.png`。若无法生成自包含 HTML 或无法运行导出流程，要明确说明限制，不要声称交付了可点击编辑能力。
7. 完成后直接展示结果，配一句简短说明即可；不要长篇解释提示词。

## 核心视觉规则

### 1. 主体与环境的分层

先识别照片中最重要、最吸引视线的主体（例如花束、人物、宠物、食物、商品或某件物品），再区分次要物件与环境。

- **主主体：保留真实摄影质感。** 尽量完整保留原有形状、比例、数量、颜色、材质、纹理、姿态和细节，不要把主体改画成卡通，不要擅自替换、删减或添加主体元素。
- **主体以外：转成彩色手绘风格。** 包括背景、桌面、墙面、包装纸、盒子、装饰物、陪衬道具、家具及环境细节。让这些元素仍能辨认原本是什么，但呈现彩色铅笔、蜡笔、水彩和随手涂画的插画质感。
- **主体白色手绘描边是必做项，不是可选装饰。** 沿主要主体最外侧可见轮廓，添加一圈细、自然、略微不均匀的白色手绘线。它应清楚可见但不抢眼，像用白色细头笔沿物体边缘随手勾勒；不得变成厚重贴纸边框、机械矢量线或大片白色光晕。
- **描边只强调主体外轮廓，不改变主体本身。** 不要把主体整体转成插画，不要在主体内部密集勾边，不要把纹理、花纹、食物褶皱或五官逐条描成卡通线稿。主体颜色、光影、材质和真实细节保持摄影质感。
- 若主体本身由多个不可分割部分构成（例如花束连同花叶、人物连同头发和衣服、宠物连同毛发），这些均属于主体，应保持真实；描边沿整体外缘走，不必逐片描绘每片花瓣、每根头发或每根毛发。
- 不要为了套用风格而改变主体身份、人物面容、表情、体态、宠物特征、商品型号或原图表达的事实。


### 2. 主体白色手绘描边（强制规则）

对主要主体进行分类后，必须先规划并生成主体轮廓线，再完成周边彩绘。默认使用白色/柔白色细线，线条略有手绘抖动和轻微粗细变化，沿主体最外侧可见边缘连续或以少量自然断笔勾勒。线宽以画布宽度约 0.15%–0.35% 为参考（约 1024 px 宽画面中的 1.5–3.5 px），按主体大小微调。主体边缘处于白色或浅色背景时，可用极淡的低饱和阴影帮助辨识，但白色线仍是主线，不得加粗成贴纸描边。

**按主体类型执行：**

- **食物/饮品：** 必须沿主要食物本身的外轮廓描边。一个完整蛋糕、面包、汉堡、盘中主菜或一杯饮品，按其可见整体形状勾勒；若画面有多个彼此分离且都属于主视觉的食物，可分别勾勒。不要把盘子、桌面、包装误当成食物主体；不要逐粒描芝麻、逐片描配料、逐条描奶油纹理，也不要在线条中穿过食物内部。盘子或杯具只有在它本身就是用户强调的拍摄主体时，才作为独立物体描边。
- **人物/人像/合照：** 同样适用，必须沿人物整体可见外轮廓添加细白线，包括头发外缘、头肩、衣服轮廓、手臂和身体外侧。保留人物原有面容、五官比例、表情、视线、肤色、皮肤纹理、发型、姿势、体态和衣着；不得美颜、换脸、改变年龄感、改变身材或把人物卡通化。**不要给眼睛、鼻子、嘴唇、牙齿等五官逐个描白线**，不要在脸部内部添加不必要的线条。头发只沿整体发型轮廓勾勒，不逐根描发丝。合照中每个人都应尽量保持完整；可辨识且彼此分开的个体分别沿外轮廓描边，人物重叠处只描实际可见边界，不要臆造被遮挡的身体部分，也不要把多人错误地圈成一个不自然的大轮廓。
- **宠物/动物：** 沿头部、耳朵、身体和尾巴的可见整体轮廓勾勒；保留毛发/羽毛的真实质感，不逐根描毛，不改动物品种特征、花色或姿态。
- **鲜花/植物：** 沿花束或主要植株整体外缘勾勒，允许对少数明显突出的花枝、叶片做轻微分段描线；不要给每片花瓣、每片叶子的内部纹理全部描边，避免线条过密。
- **商品/其他物件：** 沿其真实外缘勾勒，保留原有结构、材质、标签和比例；不要把包装文字或物体内部结构误作主体外轮廓。

**描边质量检查：**

1. 缩小画面时，仍能一眼看出白线是在强调主要主体，而不是随意漂浮在附近。
2. 线条贴合主体边缘，转折自然；不能出现明显偏离边缘的第二圈白边、粗厚贴纸轮廓或灰白光晕。
3. 不可遮住食物关键细节、人物五官、宠物眼睛或商品关键结构。
4. 如果主体边缘复杂，优先保证整体轮廓准确和干净，不要为了追求连续而补画不存在的边缘。
5. 如果首轮生成遗漏主体描边，必须再次编辑/修正底图；不能把“背景有 doodle”当作完成主体描边。

### 3. 彩色手绘环境

环境与次要物件采用以下混合媒介质感：

- 彩色铅笔的轻柔排线、可见笔触和略微不均匀的手绘边线。
- 蜡笔/粉彩的松弛涂色，局部带有自然的纸面颗粒感。
- 淡水彩的柔和晕染和色彩叠加，避免厚重油画感或塑料 3D 感。
- 轮廓可以略有手绘抖动，不追求机械的完美矢量线条。
- 物件的关键结构和透视关系仍需清楚，不能变成无法辨认的抽象色块。

### 4. 配色

优先从原图主体中提取颜色，让背景插画与主体协调。默认偏向柔和、明亮、低饱和的复古 pastel：薰衣草紫、雾霾蓝、奶油白、浅粉、蜜桃色、薄荷绿、黄油黄。可按原图调整，不要强行把所有照片都染成粉紫色。

整体观感应明亮、干净、温柔、有呼吸感；避免荧光色、过度饱和、脏灰滤镜和大面积黑色涂抹。

### 5. 主体驱动的自适应彩色手绘环境（强制规则）

**背景和所有主体以外的环境必须根据当前照片的主体自适应设计，不得机械套用固定背景模板或固定粉紫配色。** 每次生成前，先分析主体，再决定环境插画的色彩、内容、笔触和氛围。

**A. 色彩自适应**
- 从主体提取 2–4 个代表色，并观察其冷暖、明度、饱和度及材质观感。
- 以主体代表色为基础，选择协调的邻近色、柔和互补色和中性色，形成清晰的主色、辅助色和点缀色关系。
- 主体颜色鲜艳时，背景适当降低饱和度并留白；主体颜色偏淡时，可用更丰富但柔和的环境色增加层次。
- 保证主体与背景有足够明度/色相区分，不能让背景吞没主体，也不能使用与主体冲突的随机颜色。
- Pastel 是整体质感倾向，不是固定色板；只有与主体协调时才使用粉紫、薄荷绿、雾霾蓝等颜色。

**B. 内容自适应**
- 根据主体类别、原图环境和可见线索，决定哪些背景物件适合转成插画，以及是否需要少量补充相关小元素。
- 优先把原图中真实存在的背景、桌面、墙面、包装、餐具、家具和陪衬物转译为彩色手绘，不随意改变场景逻辑。
- 允许添加少量与主体直接相关、能增强主题识别的手绘小元素（例如饮品旁的茶叶/咖啡豆、烘焙食品旁的莓果/餐具、花束旁的小叶片/花朵、人物周围与原场景相符的星光或植物），但不得编造具体品牌、地点、人物关系或事件。
- 新增元素必须是辅助性的、可辨认且数量克制；不得凭空增加大量无关物件，不能让画面变成素材拼贴。

**C. 绘画风格自适应**
- 根据主体材质和场景选择彩色铅笔、蜡笔、粉彩、水彩晕染及松弛手绘线条的比例。
- 食物/饮品环境可偏柔软、温暖、带轻微纸感；人物环境应呼应服装和场景气质；鲜花可更轻盈通透；商品则兼顾材质辨识和干净的编辑感。以上仅为方向，最终以原图为准，不作为固定模板。
- 所有环境元素需属于同一套视觉语言：线条粗细、颗粒、阴影、色彩饱和度和笔触应协调，避免背景各部分像来自不同插画。

**D. 氛围与构图自适应**
- 从原图可见内容推断视觉情绪（如清新、温暖、俏皮、安静、复古或精致），再调整背景色彩、装饰密度和留白。不得把不明确的情绪写成事实。
- 主体始终是视觉中心；环境负责衬托、建立情境和引导视线，不得比主体更鲜艳、更复杂或更抢眼。
- 保留原图场景空间关系和透视；若原图背景杂乱，可艺术化简化为协调的手绘色块/纹理，但不要模糊主体边缘或破坏场景合理性。
- 文字留白区应与背景配色协调，并保持足够对比度，确保后续独立文字图层清晰可读。

**E. 自适应质量检查**
1. 背景配色是否能从主体颜色/材质找到依据，而非随机套色？
2. 环境内容是否与主体类别和原图场景相关？
3. 手绘笔触、线条和纸面质感是否统一？
4. 背景是否衬托主体、保留呼吸感，未喧宾夺主？
5. 是否避免了无关道具、过量装饰和固定模板化？
若任一项明显不合格，需重新调整背景插画方案后再交付。

## 手写文字规则（所有输出模式强制执行，v1.5.0）

**这是必做的成品组成部分，不是可选装饰。** 无论默认单图模式还是 Torn Paper Reveal 撕纸拼贴模式，最终画面都必须实际呈现 2–4 处手写日记短句/词组。不能只生成背景 doodle 而没有文字，也不能因为画面空间紧张就省略文字。若留白不足，必须先调整背景装饰密度、构图或撕纸边缘，为文字创造合理空间；不得把文字压在主体关键细节上。

### 视觉与文案

1. 根据图片内容和用户使用的语言，自动创作少量简短文案。默认以中文为主，可自然混入一小句英文。
2. 语气像随手写下的日记或内心独白：积极、甜美、松弛、轻盈，不要像广告标语或营销文案。
3. 每句尽量短，通常 2–8 个词/字组成一个小句。整张图必须有 2–4 处文字，不要堆满画面，也不得少于 2 处。
4. 文案围绕图片中确实可见的内容和情绪，不编造时间、地点、人物关系、品牌故事或其他事实。
5. 字体呈自然手写感：细笔、轻微倾斜、大小略有变化；可用淡紫、灰蓝、柔粉、奶油黄或白色等与画面协调的颜色。文字应清晰可读。
6. 示例语气（按图像内容改写，不要机械套用）：
   - “今天也有小小的快乐”
   - “被这一刻治愈了”
   - “好喜欢这些温柔细节”
   - “a little moment of joy”
   - “today feels lovely”
7. **文字区域必须在构图阶段预先规划。** 至少安排 2–4 个适合手写短句的留白点位，可分布在主体周围、画面边缘或手绘环境的干净区域；不要等底图完成后才发现没有地方放字。文字区域可以有轻微彩色手绘底纹，但必须保证文字对比度和可读性。
8. **最终成品必须可见文字。** 交付时除无文案底图外，还必须提供含初始文字合成效果的 `final.png` 或展示文字叠加后的成品预览；不能只展示 `artwork-base.png`，也不能把“文字可在编辑器里新增”当作已经完成手写文字设计。
9. 如图中有重要的原始标签、商标或包装文字，不要擅自改写成其他品牌或编造标识。原始场景中的文字与新添加的日记文案不同：前者属于底图内容，后者必须可编辑。

### 可编辑图层规则（强制）

- 新增的 2–4 处日记文案必须全部作为独立文字对象保存，不可只存在于底图像素中。
- 每个文字对象至少保存：`id`、`text`、`x`、`y`、`fontSize`、`color`、`rotation`、`maxWidth`、`fontFamily`。`x`、`y`、`maxWidth` 使用 0–1 的归一化比例，确保不同窗口尺寸下位置不漂移；`fontSize` 使用底图原始像素坐标。
- 文字对象应支持点击选中、在控制面板中直接改字、拖动位置、调整字号/颜色/角度、删除；至少必须支持点击选中、修改文字和 PNG 导出。
- 文字必须位于画布安全区域内，避免超出画面边界或压住主体关键细节。
- HTML 编辑器打开时，文字与底图应准确对齐；导出的 PNG 应按底图原始尺寸合成，而不是截取浏览器预览区域。
- 默认使用手写感字体栈，例如 `KaiTi`, `STKaiti`, `Kaiti SC`, `楷体`, `Segoe Print`, `Comic Sans MS`, `cursive`。不要将字体文件打包或声称所有设备都会显示完全相同字体；应使用用户设备可用字体回退。
- 只有在环境确实能提供可编辑矢量文本时才承诺可编辑；仅生成一张带有文字的 JPEG/PNG 不满足本功能要求。

## 手绘装饰规则

可从以下元素中少量挑选：

- 细线条描边、局部轮廓线、弯曲箭头、虚线引导线。
- 小爱心、四角星、闪光、星星、小花、笑脸。
- 轻柔的蒸汽线、波浪线、短划线、随手圈出的重点。
- 细小的彩色笔触、局部阴影和手绘纹理。

数量控制：通常 3–7 处小装饰即可。装饰应服务于主体和视线引导，不要平均铺满画面，不要遮住主体细节或关键文字。**主体白色外轮廓描边属于强制主体处理步骤，不计入这 3–7 处装饰数量，也不能用零散小 doodle 代替。**非文字装饰可以画进手绘底图；若需要也能单独编辑，可另外保存为 SVG 图层。

## 输出模式：Torn Paper Reveal｜撕纸揭示拼贴模式（v1.4.0 新增，可选）

当用户明确要求“原图和最终效果放在一张图里”“撕纸拼贴”“原图对照最终效果”或类似表达时，启用本模式；用户未提出时，仍按默认单图模式生成，不要擅自增加拼贴版式。

### 核心构图

- 输出一张完整的拼贴画布，而不是两张并排的独立图片，也不是普通 before/after 双栏对比。
- **原图纸片固定放在画布左上区域**，以未经本 Skill 改造的原始照片作为内容，保留原图摄影质感，不加白色主体描边、不加新手写文案、不改变原图内容。原图纸片的可见面积目标约为整张最终画布总面积的 **2/5（约 40%）**；这是面积比例，不是宽度或高度比例。可因原图方向、主体位置和撕裂边缘形状做小幅调整，建议控制在约 35%–45%，不得压缩成小缩略图。
- **其余约 3/5（约 60%）画布用于呈现最终处理效果**。该区域应清楚展示同一张原图经本 Skill 处理后的最终视觉效果，并继续遵守主体保真、主体白色手绘外轮廓、主体驱动的自适应彩色手绘环境和装饰克制等全部核心规则。
- 最终效果区域应成为主要视觉主体，不能只露出零碎局部或无法辨认的裁切片段。优先完整呈现主体；必要时可调整两区域边界走向、扩展画布或轻微调整最终效果区域构图，不得随意切掉主体关键部分。
- 默认沿用原图方向和整体宽高比；如果原图比例导致两区域难以自然排布，可在不裁切主体的前提下适度扩展画布。用户明确指定画幅时，以用户要求为准。

### 撕纸边缘与过渡

- 原图纸片与最终效果区域之间必须由**不规则、自然的手工撕纸边缘**连接；禁止用直线、矩形边框、圆角卡片、渐变蒙版或普通拼接线代替。
- 撕裂路径应有自然起伏、细小纤维毛边、局部纸层厚度和轻微投影，呈现真实纸张被撕开/掀起的层次；边缘不必均匀，也不要做成锯齿状机械重复图案。
- 撕纸边缘的走向、曲线、撕裂密度、纸张颜色和阴影强度应根据主体位置、画面留白、原图色彩和最终作品构图自适应决定。默认从左上原图纸片的下方及/或右侧延伸，形成自然的斜向或弧形撕裂过渡；不要僵硬地固定为某一条对角线。
- 纸边颜色应与整张作品的纸张底色协调（如暖白、奶油白或自然纸色），可见轻微纸纤维和内外层次，但不能过厚、过暗或抢过主体。
- 撕纸边缘可以局部压住最终效果区域的背景，但**不得遮挡原图或最终效果中的主体关键轮廓、人物面部、食物细节、宠物五官或商品标识**。必要时应调整撕裂路径，而不是牺牲主体信息。
- 过渡区域应让人感觉原始照片纸片被撕开后，下面显露出同一场景的手绘日记作品；两部分的主体身份、数量、姿态、构图关系必须一致，不能看起来像两张无关照片。

### 拼贴模式中的文字与装饰

- **拼贴模式同样必须呈现 2–4 处手写文案，不得省略。** 这是 v1.5.0 的强制规则，与单图模式完全一致。
- 文字默认只放在最终效果区域或其自然留白处；若最终效果区域可用空间不足，应调整撕纸边缘、背景装饰密度或最终效果区域布局，为文字腾出清晰位置。不能把文字放到左上角未经处理的原图纸片上，除非用户明确要求。
- 至少安排一处较明显的主文案，其余可作为小型旁注；避免文字过小、过淡或被撕纸边缘切断。
- 默认新增的手写日记文字只放在最终效果区域或其自然留白处，不放在原图纸片上；文字仍须遵守独立可编辑图层规则，不得烘焙进 `artwork-base.png`。
- 若文字跨越撕纸边缘会影响可读性或编辑体验，应避免跨边缘排版。撕纸边缘本身和纸张阴影属于底图视觉元素；若工具支持独立图层，可将其另存为独立 SVG/PNG 图层，但不是必需条件。
- 小爱心、星光、箭头等 doodle 主要服务于最终效果区域；原图纸片保持干净，除非用户明确要求在原图上也添加装饰。
- 拼贴画布的背景纸纹、配色和装饰密度继续遵循主体驱动的自适应规则，不得每次固定使用同一套奶油色、粉色或紫色模板。

### 生成与检查步骤

1. 同时准备两份视觉内容：未经处理的原始照片（仅用于左上纸片）和按本 Skill 核心规则生成的最终效果图（用于其余主要区域）。不要用 AI 重绘的“相似原图”代替真实原图纸片。
2. 先根据原图主体位置和方向规划画布及两区域面积，确保原图纸片约占总画布 40%，最终效果区域约占 60%，且主体在最终效果区域内完整、清楚。
3. 设计自然撕裂边缘，按构图自适应曲线和撕裂细节；让边缘成为两种视觉状态之间的纸张过渡，而不是第三个抢眼的装饰主体。
4. 将原图纸片、撕纸层次和最终效果区域合成为一张无新增文案的 `artwork-base.png`；随后按常规流程建立独立文字对象和 `edit.html`。
5. 检查：原图是否真实保留且位于左上；面积比例是否接近 2/5；剩余区域是否清楚展示最终效果；撕纸边缘是否自然且非直线；两部分主体是否一致；撕纸是否没有遮挡关键内容；整体视觉是否协调。任何一项明显不合格，都应先修正拼贴底图再交付。

### 拼贴模式提示词补充模板

在常规底图生成提示词之外，加入以下要求，并明确将用户上传的原图作为原图纸片来源：

> Create a single cohesive Torn Paper Reveal scrapbook collage. Place the untouched, authentic original photo as a paper photo piece in the upper-left area, occupying approximately 40% of the total canvas area (area, not width or height). Use the remaining approximately 60% of the canvas to reveal the finished hand-drawn diary-style treatment of the very same photo, following all subject-preservation, thin white subject-outline, and subject-adaptive illustrated-environment rules. Separate the two regions with an organic, irregular hand-torn paper edge—not a straight divider, rectangular frame, card border, or simple split-screen. Give the torn edge subtle paper fibers, naturally uneven contours, slight layered paper thickness, and a soft realistic shadow. Adapt the tear path to the subject placement and composition; keep the main subject fully visible and consistent between the original photo and the treated artwork. Keep the original photo piece genuinely photographic and unaltered. The treated region should be the dominant visual reveal. Keep new handwritten captions out of the raster base; add them later as editable text layers, preferably only in the treated region. Maintain one unified, airy scrapbook aesthetic.

## 构图与画幅

- 保留原图主要构图、主体位置和视觉重心，不随意裁掉主体或重要配件。
- 默认沿用原图宽高比和方向。只有用户明确指定画幅时才调整；如需适配新画幅，优先扩展手绘背景，不要裁切主体。
- 为手写文字和装饰留出自然空白区。文字放在背景或较干净的边缘区域，避免压在主体最重要的细节上。
- 保持层次：主体最清晰、最真实；手写文案其次；手绘环境和装饰作为氛围衬托。

## 图像生成与编辑器交付流程

**模式判断：** 每次开始时先判断用户是否明确要求 Torn Paper Reveal 拼贴模式。若没有明确要求，走原有单图流程；若要求拼贴模式，先按“输出模式：Torn Paper Reveal”规划原图纸片、最终效果区域和撕纸边缘，再继续执行下方底图、文字图层和编辑器流程。拼贴模式下，`artwork-base.png` 是完整的组合画布（原图纸片 + 撕纸过渡 + 最终效果区域），而不是单独的最终效果图。

### A. 生成无文案底图

1. **观察原图：** 确认主体、次要物件、背景、画面方向、可用留白及原图主色。
2. **确定保留区与描边路径：** 把主要主体及其不可分割的细节列为“真实摄影区”，并明确规划沿其最外侧可见边缘的一圈细白色手绘描边；根据主体类型套用上方食物、人物、宠物、鲜花或商品规则。
3. **确定插画区并制定自适应方案：** 把背景和次要物件列为“彩色手绘区”；先记录主体代表色、场景主题、材质和情绪，再制定匹配的环境配色、插画内容、笔触比例与留白安排。**同时明确规划 2–4 个手写文案位置和文字安全区，保证底图完成后仍有足够空间叠加文案。**
4. **生成底图：** 使用原图作为编辑参考，生成主体真实、主体外缘有一圈清晰但纤细的白色手绘轮廓、周边依据主体自适应设计的彩色手绘环境的完整图像。对食物和人物必须明确重复强调“沿主体最外侧可见轮廓描白线”；人物不得描画五官。**明确要求不生成任何新增手写句子、字母、标语、标题、数字或文字气泡。** 可以生成心形、星星、箭头、虚线、蒸汽等非文字装饰，但不能把注释文字烘焙进底图。
5. **检查底图：** 主体是否完整且真实；主体外轮廓是否有贴合、纤细、清楚的白色手绘描边；环境配色、内容、笔触和氛围是否根据主体自适应且协调；食物描边是否只围绕食物本身；人物描边是否绕过五官、没有改变面容；背景是否整体转为彩色手绘；是否没有新增日记文字/乱码；**是否预留了足够且位置合理的手写文字区域**；画幅是否正确。若遗漏主体描边、描边错位/过粗，或底图出现新增文案，必须重新编辑修正。

### B. 建立独立文字对象

6. **必须为图片创作 2–4 句短文案**，并为每句设定合适的归一化位置、宽度、字号、颜色、角度和手写字体栈；不得跳过此步骤。
7. 文字只叠加在编辑器的 HTML/SVG/Canvas 层中。文字位置应自然融入留白区，避免主体遮挡。
8. 文字默认保留轻微自然倾斜、柔和描边或阴影；不要所有文字都采用完全相同的角度、字号和位置。

### C. 输出可点击编辑器

9. 使用本 Skill 目录下的 `editor-template.html` 作为模板；若可用，运行 `build_editor.py` 将 `artwork-base.png` 与 `text-items.json` 嵌入模板，生成 `edit.html`。示例数据结构参考 `text-items.example.json`。
10. `edit.html` 必须是自包含文件：底图以 Data URL 内嵌，打开文件后无需联网、无需再次上传本次底图即可工作。
11. 编辑器至少提供：
    - 点击文字对象即可选中，并在编辑栏中修改文字；
    - 拖动文字对象改变位置；
    - 修改颜色、字号和旋转角度；
    - 新增/删除文字对象；
    - 点击“导出 PNG”后下载合成结果；导出画布尺寸等于底图原始像素尺寸。
12. 运行一次功能检查：打开 HTML，确认底图加载、文字叠加位置正确；修改一处文字后导出 PNG，确认导出结果显示新文案且没有遗漏/重复旧文案。
13. 若无法真正运行编辑器，不得虚称已验证；仍可提供 HTML 文件，但需明确告知用户在浏览器中打开后可操作，并说明未能在当前环境完成实际导出验证。

### D. 交付

14. **必须交付可见初始文案的成品预览 `final.png`**，并优先同时交付 `edit.html`（自包含编辑器）、`artwork-base.png`（无新增文案底图）和 `text-items.json`（文案数据备份）。不得只交付无文字底图。
15. 回复中明确指出：打开 `edit.html`，点击任意手写文字即可选中并修改；拖动文字可调整位置；完成后点击“导出 PNG”。

## 推荐底图生成提示词模板

将下面的要求结合具体图片内容，转换成适合当前图像生成工具的自然语言提示词。必须把用户上传图片作为参考图：

> Edit the supplied photo into a polished pastel hand-drawn mixed-media diary-style image. Preserve the main focal subject as a complete, highly realistic photograph, faithfully retaining its identity, shape, proportions, colors, textures, details, and placement. Do not cartoonize, replace, remove, beautify, or redesign the main subject. **MANDATORY: draw a thin, hand-drawn white contour line closely following the entire outer visible silhouette of the main subject.** The line should look like a delicate white pen stroke: slightly irregular, organic, clean, and visible, but never a thick sticker border or glowing halo. For food, trace the actual edible item(s), not the plate or table unless the vessel is itself the focal subject; do not outline every ingredient or internal texture. For people, trace the outer silhouette around hair, head, shoulders, clothing, arms, and body; preserve facial identity and do not draw around eyes, nose, lips, teeth, or other facial features. For pets, flowers, and products, trace their overall recognizable outer silhouette without outlining every tiny hair, petal, or internal detail. Transform everything outside the main subject—including the background, surfaces, packaging, and secondary props—into recognizable colorful hand-drawn illustrations using colored-pencil strokes, soft crayon shading, gentle watercolor washes, subtle paper grain, and loose imperfect outlines. Analyze the main subject first, then design the entire surrounding illustration specifically for that subject: derive a coordinated palette from its actual colors, temperature, brightness, material, theme, and mood; adapt background props and small motifs to the subject and original setting; keep all environmental brushwork and line styles visually consistent. Do not use a fixed palette or generic background template. The environment must complement, not compete with, the subject. Add a restrained selection of thin hand-drawn arrows, dashed guides, tiny hearts, sparkles, stars, or a small smiley, but leave generous clean negative space specifically planned for 2–4 handwritten diary captions. The final composed artwork MUST visibly include 2–4 short handwritten captions as separate editable text objects; never omit the text area in either single-image or Torn Paper Reveal mode. **Do not render any new words, letters, captions, handwriting, labels, typography, numbers, speech bubbles, or pseudo-text anywhere in the image.** Do not bake diary notes into the raster image; they will be added later as editable text layers. Keep the original composition and aspect ratio. Before finalizing, verify that the white subject contour is present, follows the real subject edge, remains delicate, and does not obscure important detail. Make it stylish, effortless, airy, warm, and editorial—not childish, cluttered, glossy, or overly polished. No transparent-background treatment, no gray halo, no heavy sticker border, and no excessive doodles.

## 用户明确提出其他要求时

- 用户要求主体也变成手绘：按用户要求修改主体保真规则，并相应调整/取消真实摄影主体的白色描边要求。
- 用户明确要求人物图：适用本 Skill；人物仍保持真实摄影质感，必须沿人物整体外轮廓加细白线，但不得描五官、改变面容或美化人物。
- 用户明确要求食物图：适用本 Skill；必须沿食物本身外轮廓加细白线，不要把盘子/桌面误当作食物轮廓。
- 用户明确要求不加主体描边：仅本轮覆盖默认规则，按用户要求省略。
- 用户要求去背景或透明底：仅在明确提出时执行，并以真实透明 alpha 背景为目标；不要用灰色/棋盘格视觉假象冒充透明。
- 用户要求原图上的文字保留、删除或替换：按本轮明确要求处理。若用户想编辑原图中已有的实物文字，先判断是否能可靠分离；不可分离时说明该文字可能需要重绘覆盖。
- 用户要求 2:3、1:1、9:16 等画幅：优先遵守指定画幅，并尽量避免裁切主体。
- 用户要求更克制、更可爱、更复古或特定颜色：优先调整手绘区、字体和装饰，不要无故改变主体。
- 用户明确只想要 PNG、不需要编辑器：可按用户要求仅交付 PNG。

## 默认交付标准

一套可以直接分享并可二次修改的成品：**主体真实、主体外缘有纤细白色手绘描边、周边环境根据主体自适应为协调的彩色手绘插画、文字独立可编辑、装饰克制、留白自然。** 默认输出单图；用户明确要求原图与最终效果同画布展示时，启用 Torn Paper Reveal 模式（左上原图约占 2/5 面积，其余区域展示最终效果，以自适应手撕纸边缘衔接）。用户只上传图片时，不要求其重复描述这些规则。
