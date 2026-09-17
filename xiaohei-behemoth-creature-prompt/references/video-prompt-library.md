# 巨兽异兽视频提示词模板库（五步法）

> 与图片模板库（`references/image-prompt-library.md`）配套使用：图片模板库定「异兽长什么样」
> （六维度静态外观），本库定「异兽怎么动、怎么震」（时序五步）。图生视频时两步都要用。

---

## 视频提示词五步法（Video Prompt Five-Step Framework）

**适用场景**：图生视频（即梦 / 可灵 / Sora / Runway 等）。图片提示词解决「异兽长什么样」，
视频提示词解决「异兽怎么动、怎么震、压迫感怎么递增」。五步顺序固定，不可调换——
每一步都建立在上一步之上，叠加后震撼感自然产生。

### 核心原则

1. **顺序锁死**：镜头运动 → 外观和动作 → 体量 → 光影 → 镜头特效。乱序则震撼感散架。
2. **时序细节是灵魂**：视频区别于图片的关键是「时间」——动作要写明持续几秒、缓缓/猛然、停留才消散。
3. **节奏对比**：日常画面流畅 + 关键瞬间强调（定格/震动/慢放），制造心跳节拍。
4. **与图片提示词衔接**：图片九层面（材质/纹理/光源/三色组合）作为 Step 2「外观」的素材库，视频五步在其上加运动与体量。

### 组装公式

```
视频提示词 = Step1 镜头运动 + Step2 外观和动作 + Step3 体量 + Step4 光影 + Step5 镜头特效
```

> 写作顺序即阅读顺序，五步依次成段，不要打散重组。

---

### Step 1 · 镜头运动（Camera Movement）

**写什么**：镜头怎么跟着异兽走。先定运镜方式，再定与异兽的相对运动关系。

| 运镜 | 中文片段 | English |
|---|---|---|
| 匀速推进跟拍 | 镜头匀速向前推进，全程跟着异兽移动，画面过渡顺滑 | camera pushes forward at steady speed, tracking the creature throughout, smooth transitions |
| 低角度仰拍推进 | 镜头贴地仰拍，缓缓向异兽推进，仰角持续递增 | ground-level low-angle dolly-in, slowly closing on the creature, tilt rising |
| 环绕运镜 | 镜头绕异兽缓慢环绕，始终保持正面朝向 | camera slowly orbits the creature, keeping it face-on throughout |
| 升降镜头 | 镜头自地面升起，从脚部扫向头部，展示全身体量 | crane shot rising from ground level, sweeping feet to head to reveal full scale |
| 手持跟拍 | 手持质感轻微晃动，模拟目击者视角 | handheld tracking with subtle shake, witness POV |
| 静止广角 | 镜头固定不动，异兽自身向镜头逼近 | locked-off wide shot, the creature itself advances toward the lens |

- `[V1.1]` 顺滑过渡：`画面过渡顺滑，无突兀切镜`
  EN: `smooth transitions, no jarring cuts`
- `[V1.2]` 持续逼近：`镜头与异兽距离持续缩短，压迫感递增`
  EN: `the gap between camera and creature keeps shrinking, dread building`
- `[V1.3]` 仰角递增：`随着异兽逼近，镜头仰角逐渐增大`
  EN: `camera tilt increasing as the creature closes in`

---

### Step 2 · 外观和动作（Appearance & Action）

**写什么**：异兽形态外观（材质纹理来自图片提示词维度 2）+ 动作时序。这一步是视频的灵魂。
动作必须带「时间细节」：持续几秒、缓缓/猛然、停留才消散——没有时序，视频就退回成图片。

> 外观素材直接调用图片提示词九层面（材质/纹理/光源/三色组合），本步只补「动作 + 时序」。

**动作节奏类**：
- `[V2.1]` 沉缓迈步：`迈步节奏舒缓，每一脚落地都力道极重`
  EN: `slow deliberate strides, each footfall landing with crushing force`
- `[V2.2]` 时序痕迹：`脚掌踩过地面留下[岩浆|冰霜|毒液]脚印，脚印范围宽阔，散发[滚烫红光|冷蓝光|荧绿光]，光亮停留三秒才消散`
  EN: `each paw leaves a [lava | frost | venom] footprint, wide and glowing [searing red | cold blue | sickly green], the glow lingering three seconds before fading`
- `[V2.3]` 缓动特效：`周身皮毛缠绕暗红色小火苗，火苗顺着毛发缓缓向上飘`
  EN: `small dark-red flames clinging to its fur, drifting slowly upward along the strands`
- `[V2.4]` 翼雾涌动：`两片翅膀之间不断涌出暗红流动光雾`
  EN: `a stream of dark-red luminous mist welling between its wings`
- `[V2.5]` 眼瞳自发光：`双眼如同两颗燃烧的火球，自带灼热红光`
  EN: `eyes like twin burning spheres, radiating searing red light`
- `[V2.6]` 翅骨质感：`翅膀骨架如同坚硬黑铁`
  EN: `wing bones like hardened black iron`

**面向镜头类**（视频必备，与图片 T4.1–T4.5 衔接）：
- `[V2.7]` 正面逼近：`异兽正面朝向镜头，一步步向镜头走来`
  EN: `the creature faces the camera, walking step by step toward the lens`
- `[V2.8]` 瞳孔锁定：`双瞳始终锁定观者，瞳孔深处倒映[燃烧的城市 | 闪电 | 月影]`
  EN: `both pupils locked on the viewer throughout, reflections of [a burning city | lightning | the moon] deep within`

---

### Step 3 · 体量（Mass & Weight）

**写什么**：用物理反馈表现「重」。异兽的重量必须让环境做出可见反应，观众才信它「巨」。
没有体量反馈，再大的模型也只是飘在画面里的贴图。

- `[V3.1]` 地面下陷：`每一步踩下去地面都会微微下陷，留下深浅起伏的压痕`
  EN: `each step makes the ground sink slightly, leaving rolling indentations`
- `[V3.2]` 建筑震颤：`巨型建筑在它每一步下轻微晃动，瓦片滑落`
  EN: `colossal structures trembling with each step, tiles sliding off`
- `[V3.3]` 水面隆起：`它入水时海面整片隆起，波浪向四方推开`
  EN: `the sea bulging upward as it enters, waves radiating outward`
- `[V3.4]` 飞鸟惊起：`远处群鸟被它的脚步惊起，黑压压飞离`
  EN: `distant flocks startled into flight by its footfalls, dark clouds of birds fleeing`
- `[V3.5]` 尘浪扩散：`每一步掀起环形尘浪，向四周扩散`
  EN: `each step kicking up a ring of dust expanding outward`
- `[V3.6]` 冰面开裂：`它踏过冰原，冰面呈放射状崩裂，裂缝随脚步蔓延`
  EN: `it treads the ice field, radial cracks spreading from each step`

---

### Step 4 · 光影（Lighting & Atmosphere）

**写什么**：环境对异兽存在的光影反应。光影随异兽而变——热浪扭曲、光雾涌动、阴影游移。
这一步把「异兽存在」和「世界被它改变」绑在一起。

- `[V4.1]` 热浪扭曲：`异兽周身热浪翻滚，空气受热扭曲，视线出现轻微晃动变形`
  EN: `heat waves rolling off the creature, the air warping and shimmering, vision subtly distorting`
- `[V4.2]` 冷雾下沉：`它呼出的寒气贴地蔓延，白雾如潮水淹没街道`
  EN: `its frozen breath hugging the ground, white fog flooding the streets like a tide`
- `[V4.3]` 光雾涌动：`翼间/甲壳间不断涌出流动光雾，随呼吸明灭`
  EN: `luminous mist welling between its wings/plates, pulsing with its breath`
- `[V4.4]` 阴影游移：`它的巨大阴影随移动扫过城市，所到之处白昼转暗`
  EN: `its vast shadow sweeping across the city as it moves, daylight turning to dusk in its wake`
- `[V4.5]` 火星飘升：`周身火星/灰烬缓缓向上飘升，在逆光中闪烁`
  EN: `sparks and ash drifting slowly upward, twinkling against the backlight`
- `[V4.6]` 磷光染水：`它身周的海水被磷光染成幽青，水雾在逆光中闪烁`
  EN: `the surrounding sea dyed ghostly cyan by its phosphor, mist twinkling in the backlight`

---

### Step 5 · 镜头特效（Camera FX）

**写什么**：节奏控制——日常流畅 + 关键瞬间强调。这是震撼感的「心跳节拍」：平时顺滑，
落地震一下、定格一帧，观众的心跳就被牵住了。

- `[V5.1]` 落地定格：`异兽每一次脚掌落地时画面短暂清晰定格，单帧画面干净无虚影`
  EN: `each footfall triggers a brief freeze-frame, the single frame crisp with no motion blur`
- `[V5.2]` 镜头震动：`异兽迈步时镜头伴随轻微震动，模拟地面传导的冲击`
  EN: `subtle camera shake with each step, simulating the shock transmitted through the ground`
- `[V5.3]` 日常流畅：`日常画面观感流畅，无明显卡顿`
  EN: `smooth playback between impacts, no stutter`
- `[V5.4]` 慢动作强调：`关键动作（扑击/吐息/咆哮）瞬间放慢，强化张力`
  EN: `key actions (pounce / breath / roar) slowed for a beat to heighten tension`
- `[V5.5]` 动静切换：`快速运动时局部动态模糊，落地瞬间切换为清晰定格`
  EN: `localized motion blur during fast moves, cutting to a crisp freeze on impact`

### 五步法质量检查（视频提示词出片前自查）

- [ ] 五步是否按顺序写全？（镜头→外观动作→体量→光影→镜头特效）
- [ ] Step 2 是否有时序细节（停留几秒/缓缓/猛然）？没有则补。
- [ ] Step 3 体量是否有可见的环境物理反馈？
- [ ] Step 5 是否有「日常流畅 + 关键瞬间强调」的节奏对比？
- [ ] 是否面向镜头（V2.7/V2.8）？视频生成必备。
- [ ] 外观素材是否来自图片提示词九层面（材质/纹理/光源/三色组合）？

---

### 视频完全体示例（五步法标准写法）

#### 视频 V1：虎身四翼火兽（五步法范例 · 暖系狂暴）

```
## 镜头运动
镜头匀速向前推进，全程跟着异兽移动，画面过渡顺滑。

## 外观和动作
异兽长着虎身与四片巨翼，迈步节奏舒缓，每一脚落地都力道极重。脚掌踩过地面会留下
岩浆脚印，脚印范围宽阔，散发滚烫红光，光亮会停留三秒才消散。周身皮毛缠绕暗红色
小火苗，火苗顺着毛发缓缓向上飘；翅膀骨架如同坚硬黑铁，两片翅膀之间不断涌出暗红
流动光雾；双眼如同两颗燃烧的火球，自带灼热红光。异兽正面朝向镜头，一步步向镜头
走来，双瞳始终锁定观者。

## 体量
异兽身形无比沉重，每一步踩下去地面都会微微下陷，留下深浅起伏的压痕。

## 光影
异兽周身热浪翻滚，空气受热扭曲，视线会出现轻微晃动变形。

## 镜头特效
日常画面观感流畅，异兽每一次脚掌落地时画面会短暂清晰定格，异兽迈步时镜头伴随
轻微震动。每回脚掌踩地瞬间，单帧画面干净无虚影。
```

#### 视频 V2：深渊巨鲨（五步法 · 深海磷光系）

```
## 镜头运动
镜头贴海面仰拍，缓缓向巨鲨推进，仰角随它破浪升高而递增，画面过渡顺滑。

## 外观和动作
巨鲨自黑海破浪而起，灰黑皮齿如锉刀层层排列，背鳍如断裂城墙，口中三排半透明锯齿
交错。它正面朝向镜头，缓缓张开巨口逼近，双瞳锁定观者，瞳孔深处倒映倾覆的灯塔。
每摆一次尾，海面掀起一道海啸浪墙，浪墙推进两秒后拍碎在城墙。皮齿缝隙的磷光随呼吸
明灭，寄生藤壶在海风中颤动。

## 体量
巨型海港要塞只到它背鳍根部，它每破一次浪，港口城墙微微下沉震颤，灯塔向海倾斜，
碎船板在浪间翻滚。

## 光影
惨白月光从云隙洒下，磷光在皮齿缝间如鬼火明灭，巨鲨身周的海水被磷光染成幽青，
水雾在逆光中闪烁。

## 镜头特效
日常画面流畅，巨鲨每次甩尾破浪瞬间画面短暂定格，单帧干净无虚影；它张开巨口的
瞬间镜头轻微震动，浪墙拍墙时画面慢放半秒强化冲击。
```

#### 视频 V3：玄冥冰蛟（五步法 · 冰渊冷系）

```
## 镜头运动
镜头自冰原地面升起，从冰蛟尾部扫向头部，随后固定低角度仰拍，缓缓向前推进，
画面过渡顺滑。

## 外观和动作
冰蛟自极寒之渊昂首，冰晶鳞片层叠如冻湖，霜角结满冰棱，正面朝向镜头缓缓游进，
双瞳锁定观者，瞳孔深处倒映冻结的宫殿尖顶。每吐一口气，寒雾贴地蔓延三秒不散，
鳞面折射极光随身体扭动流转。

## 体量
冰封巨城只到它胸口，它每游过一段，冰面下陷开裂，冰川高塔向两侧倾倒，碎冰如雪崩
滚落。

## 光影
冷月与极光在它背后交织，体积光柱穿透暴风雪；它呼出的寒气让空气凝结成冰晶，
视线在冷雾中晃动变形。

## 镜头特效
日常画面流畅，冰蛟每次昂首吐息瞬间画面短暂定格，单帧干净无虚影；它游进时镜头
伴随轻微震动，冰塔倾倒时画面慢放一拍强化崩塌感。
```
