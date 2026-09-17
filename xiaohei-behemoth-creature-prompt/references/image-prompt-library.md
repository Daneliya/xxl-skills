# 巨兽异兽图片提示词模板库（六维度）

本文件是 `xiaohei-behemoth-creature-prompt` 技能的**图片提示词**素材库。六个维度各自独立成节，每一节提供
**关键词池** 与 **可直接拼贴的模板片段**（中文 + English 双语）。组合方式见 `SKILL.md` 的
「组装公式」章节。视频提示词（图生视频）见 `references/video-prompt-library.md` 五步法模板库。

> 用法约定：
> - `[____]` 为必填/待替换参数；`(____)` 为可选参数；`A | B | C` 为多选一。
> - 英文片段为国际主流生图模型（Midjourney / Stable Diffusion / Flux）优化写法；
>   中文片段适用于即梦、可灵、通义万相等中文生图模型。二者可互换，不必同时使用。
> - 强度词分三档：`弱 = slight / faint`，`中 = prominent / heavy`，`强 = overwhelming / colossal`。

---

## 维度 1：体型与比例（Scale & Proportion）

**作用**：巨兽的「巨」必须通过参照物对比才能成立。单独写 big/huge 没有画面感，
要让观众从参照物中自行推断体积。

### 参照物锚点（Reference Anchors）

| 参照物 | 中文片段 | English |
|---|---|---|
| 山岳 | 身躯高耸入云，山峰只及它的腰际 | its shoulders dwarf the mountain peaks |
| 城市 | 一座现代化城市在它脚下如同玩具积木 | a modern metropolis looks like toy blocks beneath its feet |
| 森林 | 百年古树在它爪下细如草茎 | ancient trees appear as thin grass blades under its claws |
| 云层 | 头颅破开云海，云层只到它胸口 | its head pierces the cloud sea, clouds reach only its chest |
| 人类 | 微小的人类剪影站在它的趾缝间 | tiny human silhouettes stand between its toes |
| 海洋 | 它自深海立起，海浪仅没到它的膝盖 | it rises from the deep, waves barely reach its knees |
| 鸟类 | 群鸟环绕它飞行，小如飞虫 | flocks of birds circle it, small as gnats |
| 巨型建筑 | 巨型环形圣殿/金字塔群只及它的腰际 | colossal ring-temples / pyramid clusters reach only its waist |

### 模板片段（Template Blocks）

- `[T1.1]` 山岳级：`通体如山岳般庞大的[生物]，行走时地动山摇`
  EN: `a [creature] as massive as a mountain range, each step shaking the earth`
- `[T1.2]` 破云级：`身形突破云层，云海在它脚下翻涌如浪`
  EN: `a silhouette towering above the clouds, sea of clouds churning below its chest`
- `[T1.3]` 剪影级：`它以天空为背景呈现剪影，占据画面四分之三的高度`
  EN: `a colossal silhouette filling three quarters of the frame against the sky`
- `[T1.4]` 渺小参照：`画面底部的[人物|城堡|船只]小如蝼蚁，衬托出它的伟岸`
  EN: `tiny [figures | castles | ships] at the bottom of the frame emphasize its overwhelming scale`
- `[T1.5]` 局部特写：`只露出半只巨爪，爪尖便已覆盖整片[山谷|街区]`
  EN: `extreme close-up of a single claw that alone covers an entire [valley | city block]`
- `[T1.6]` 建筑级：`城市级巨型遗迹在它身下如沙盘模型，最高的塔楼群只到它的膝盖`
  EN: `city-scale colossal ruins beneath it like a sand-table model, the tallest towers reaching only its knees`
- `[T1.7]` 城市级：`整座古城只占画面底部一角，它的身影覆盖三分之二的天空`
  EN: `an entire ancient city confined to the bottom corner of the frame, its form covering two thirds of the sky`

### 强度调节

| 档位 | 词 |
|---|---|
| 弱 | 数层楼高 several stories tall |
| 中 | 与山峰齐平 rivalling the mountains |
| 强 | 超越山岳、遮蔽天空 beyond mountains, blotting out the sky |

---

## 维度 2：形态与特征（Anatomy & Features）

**作用**：给出可辨识的独特生理结构，配合皮肤/鳞片/毛发的微观细节，让异兽「活」起来。

### 结构关键词池（Structural Features）

多头 / 多眼 / 骨刺外露 / 背甲 / 巨翼 / 分叉长尾 / 犄角 / 利爪 / 触须 / 鳍翼 /
火焰鬃毛 / 水晶结晶体 / 共生植物 / 机械改造 / 深渊黏液

- `[T2.1]` 鳞甲类：`全身覆满黑曜石般的鳞片，鳞片缝隙间透出暗红火光`
  EN: `covered in obsidian-like scales, crimson embers glowing between the gaps`
- `[T2.2]` 毛皮类：`蓬乱的雪白毛发在狂风中翻卷，皮毛下隐约可见岩石般的肌肉束`
  EN: `unkempt white fur whipping in the gale, rock-like muscle cords shifting beneath`
- `[T2.3]` 甲壳类：`背负裂谷般龟裂的巨型甲壳，甲壳上苔藓与矿物晶体共生`
  EN: `a titanic carapace cracked like a canyon, moss and mineral crystals growing on it`
- `[T2.4]` 骨甲类：`脊椎与肩胛处长出惨白的骨刺，如同倒插的利剑`
  EN: `pale bone spikes jutting from spine and shoulders like inverted blades`
- `[T2.5]` 多首类：`三个头颅各自低吼，中间的巨颅睁开第三只竖瞳`
  EN: `three heads growling separately, the central one opening a third vertical pupil`
- `[T2.6]` 触须类：`面部垂落数十条墨色触须，触须末梢泛着幽蓝荧光`
  EN: `dozens of ink-black tentacles hanging from its face, tips glowing faint blue`
- `[T2.7]` 异化细节：`皮肤布满远古符文般的伤疤，伤口深处有异物蠕动`
  EN: `scarred hide marked with ancient rune-like wounds, something writhing deep inside`

### 细节纹理强化（Texture Boost）

- `超细节：鳞片每片都有独立的高光与阴影，反映周围环境`
  EN: `hyper-detailed scales with individual highlights and reflections`
- `毛发根根分明，可数出每一根纤维`
  EN: `fur rendered strand by strand, every fiber countable`
- `皮肤质感模拟岩层/皮革/金属，岁月与战斗的痕迹清晰可见`
  EN: `hide textured like rock strata / tanned leather / forged metal, worn by ages of battle`

---

## 维度 3：光影与氛围（Lighting & Atmosphere）

**作用**：光影决定情绪的「体感」。逆光制造神秘压迫，闪电与熔岩制造狂暴，
浓雾制造未知恐惧。这是史诗感的主要来源。

### 光源类型（Light Sources）

| 光源 | 中文片段 | English |
|---|---|---|
| 逆光 | 背对夕阳形成纯黑剪影，轮廓被金色光晕勾勒 | backlit as a pure black silhouette, rimmed with golden halo |
| 体积光 | 厚重云层中投下巨大光柱，光柱中尘埃与雨丝清晰可见 | god rays piercing heavy clouds, dust and rain visible within the beams |
| 闪电 | 一道闪电恰好照亮它的头颅，其余皆沉入黑暗 | a single lightning bolt illuminating its head, everything else plunged in darkness |
| 熔岩 | 地缝熔岩映红它的腹部，热气扭曲了空气 | magma glow from the cracks reddening its belly, heat distorting the air |
| 冷月 | 惨白月光勾勒出它森然的轮廓，影子拖得极长 | pale moonlight tracing its grim silhouette, casting a long shadow |
| 圣光 | 它周身缠绕神圣般的辉光，光芒与黑暗角力 | divine-like radiance coiling around it, light wrestling with darkness |

### 氛围元素（Atmosphere Elements）

- `[T3.1]` 浓雾：`浓雾在它脚下翻涌，身体轮廓半隐半现`
  EN: `dense fog churning at its feet, body half-hidden in the mist`
- `[T3.2]` 烟尘：`它行经之处尘土冲天，遮天蔽日`
  EN: `dust clouds erupting in its wake, blotting out the sky`
- `[T3.3]` 雷暴：`风暴雷云在它头顶盘旋，闪电不断劈落`
  EN: `a storm vortex swirling above its head, lightning striking down repeatedly`
- `[T3.4]` 压迫词：`氛围阴沉压抑，危机一触即发`
  EN: `ominous, menacing atmosphere, dread permeating the scene, a sense of awe`

---

## 维度 4：动态与姿态（Action & Posture）

**作用**：静态的巨兽是「雕塑」，动态的巨兽才是「灾难」。动作赋予画面叙事张力。

### 动作类型（Action Types）

| 动作 | 中文片段 | English |
|---|---|---|
| 咆哮 | 仰天咆哮，声浪震碎方圆数里的岩石 | roaring at the sky, shockwaves shattering rocks for miles |
| 扑击 | 前肢高高扬起，正欲扑向渺小的猎物 | rearing up on hind legs, about to pounce on a tiny prey |
| 腾空 | 巨翼展开，腾空而起带起漫天尘土 | wings fully spread, launching into the air amid a storm of dust |
| 俯冲 | 自云层之上俯冲而下，气流撕裂天空 | diving from above the clouds, air tearing apart in its wake |
| 甩尾 | 长尾横扫，拦腰截断一片森林 | tail sweeping across, leveling an entire forest |
| 吐息 | 张开巨口喷出毁灭性的[龙焰|寒霜|雷电] | unleashing a devastating [dragonfire | frost | lightning] breath |
| 践踏 | 巨足落下，大地龟裂，房屋接连塌陷 | a single footstep cracking the earth, buildings collapsing in sequence |
| 凝视 | 低伏于地，竖瞳锁定猎物，蓄势待发 | crouched low, vertical pupils locked on prey, coiled to strike |

### 运动感强化（Motion Boost）

- `动作瞬间定格，动态模糊的残影增加速度感`
  EN: `frozen mid-action, motion blur trails conveying immense speed`
- `地面被掀起的气浪向四周扩散，草木伏倒`
  EN: `shockwave rippling outward, flattening grass and trees`
- `肢体肌肉紧绷，青筋暴起，力量感呼之欲出`
  EN: `muscles taut and veins bulging, raw power about to explode`

### 构图朝向（Camera-Facing Composition，视频生成首选）

**面向镜头的巨兽在视频推近时压迫感持续递增；侧面/背影适合静态图，视频中张力会流失。
图生视频提示词必须包含以下至少 2 条：**

- `[T4.1]` 正对镜头：`它正面朝向镜头，头颅占据画面上半部，俯瞰一切`
  EN: `facing the camera head-on, its head filling the upper half of the frame, looking down on everything`
- `[T4.2]` 直视观者：`双瞳锁定观者，瞳孔深处倒映着[燃烧的城市 | 闪电 | 月影]`
  EN: `both pupils locked on the viewer, tiny reflections of a burning city / lightning / the moon within`
- `[T4.3]` 逼近压迫：`它正迈步向镜头逼近，画面底部是仓皇逃窜的微小人群`
  EN: `striding toward the camera, tiny panicked crowds scattering at the bottom of the frame`
- `[T4.4]` 低角度仰拍：`镜头贴地仰视，它的下巴高过天际线，四肢如巨柱压向镜头`
  EN: `ground-level camera looking up, its chin above the skyline, limbs like giant columns looming over the lens`
- `[T4.5]` 视野挤压：`近大远小的透视将头部放大数倍，画面边缘被它的身体撑满`
  EN: `extreme one-point perspective enlarging the head several-fold, its body bulging past the frame edges`

---

## 维度 5：环境与背景（Environment & Background）

**作用**：巨兽的「灾难性」通过环境的毁灭状态来呈现。环境不只是背景，而是巨兽威力的直接证据。

### 场景类型（Scene Types）

| 场景 | 中文片段 | English |
|---|---|---|
| 山川崩裂 | 远山崩裂滑坡，巨石如雨点滚落 | distant mountains splitting apart, boulders raining down |
| 风暴肆虐 | 十二级风暴卷起海面，巨浪拍碎悬崖 | a tempest whipping the sea into towering waves that shatter the cliffs |
| 火山爆发 | 天边火山喷发，岩浆河流向它脚下 | a volcano erupting on the horizon, rivers of lava streaming toward it |
| 废墟城市 | 残破的现代城市被它踏为废墟，火光四起 | a ruined modern city trampled to rubble beneath it, fires burning |
| 古战场 | 白骨遍野的古战场上，旌旗残破 | an ancient battlefield littered with bones and torn banners |
| 冰封荒原 | 极地冰原裂开巨大的冰缝，冷气升腾 | a polar wasteland splitting into yawning ice crevasses, cold mist rising |
| 深渊海域 | 海面突然隆起，海水自它脊背倾泻而下 | the ocean bulging upward as seawater cascades off its back |
| 巨型建筑遗迹 | 环形圣殿/金字塔群/巨型城墙在它身下如沙盘，断柱与流沙填满画面 | colossal ring-temple / pyramid / giant wall ruins beneath it, broken columns and sand filling the frame |

### 环境互动（Environmental Interaction）

- `它破开云层，云层被撕出巨大的空洞`
  EN: `bursting through the cloud layer, tearing a massive hole in the sky`
- `巨爪落处，山体像豆腐一样被切开`
  EN: `a single claw carving through a mountain like soft clay`
- `整片天空被它的阴影遮蔽，白昼转为黄昏`
  EN: `its shadow darkening the land, day turning to dusk`
- `它碾过城墙，整段城墙像饼干一样塌陷`
  EN: `crushing through a city wall, the whole section collapsing like a biscuit`
- `它的阴影盖过整座古城，街道陷入黄昏般的黑暗`
  EN: `its shadow swallowing the entire ancient city, streets plunged into dusk-like darkness`
- `最高的灯塔只到它的肘部，塔楼群在它肩头以下`
  EN: `the tallest lighthouse reaching only its elbow, the tower clusters passing beneath its shoulder`

### 场景贴合：动作→环境反应 绑定表（Scene Binding）

**原则**：场景不是装饰，而是巨兽行为的**直接结果**。每个动作必须对应一个可看见的
环境反应，让观众从环境读出巨兽的威力。**动作与环境永远成对出现。**

| 巨兽动作 | 必须配对的环境反应（二选一以上） | English |
|---|---|---|
| 咆哮 | 声浪震裂山峰 / 震碎宫殿琉璃瓦 | shockwaves cracking peaks / shattering temple tiles |
| 扑击 | 大地龟裂，房屋像多米诺骨牌倒塌 | the ground splitting, buildings toppling like dominoes |
| 腾空 | 尘土遮天蔽日 / 翼下森林成片伏倒 | dust blotting the sky / forests flattening under its wings |
| 俯冲 | 气流撕裂云层形成尾迹空洞 | air tearing a tunnel through the clouds |
| 甩尾 | 拦腰截断森林 / 掀翻整片海面 | leveling a forest / whipping the sea into a wall of water |
| 吐息 | 所过之处熔岩凝固成河 / 大地覆满冰霜 | lava rivers hardening in its wake / the land freezing solid |
| 践踏 | 脚印化作湖泊 / 城墙塌陷成缺口 | footprints becoming lakes / city walls collapsing into gaps |
| 入水 | 海面隆起形成海啸 / 漩涡吞没船只 | the sea bulging into a tsunami / a maelstrom swallowing ships |
| 凝视 | 飞鸟成群坠落 / 空气凝滞、雾气下沉 | flocks of birds falling dead / the air going still, fog sinking |
| 沉睡 | 火山口随呼吸喷涌 / 大地随心跳脉动 | the volcano venting with each breath / the earth pulsing with its heartbeat |

**反向绑定**（环境反过来塑造巨兽观感）：
- `岩浆映红它的腹部，热气扭曲了轮廓` — magma glow reddening its belly, heat warping its outline
- `风暴撕扯着它的鬃毛与鳞片` — the storm tearing at its mane and scales
- `浓雾缠绕四肢，只露出山脊般的背脊` — fog coiling around its limbs, revealing only its ridged back

---

## 维度 6：色彩与风格（Color & Style）

**作用**：统一整张画面的视觉基调。先定色，再定风，最后缀质量词。

### 色调倾向（Color Palettes）

| 色调 | 中文片段 | English |
|---|---|---|
| 冷冽威严 | 整体以暗蓝、铁灰、霜白为主，点缀冷银高光 | dominated by deep blue, iron grey and frost white, accented with cold silver |
| 狂暴炽热 | 以熔岩橙红、焦黑、暗金为主，明暗对比强烈 | molten orange-red, charred black and dark gold, high contrast |
| 暗黑压抑 | 近乎单色的暗黑绿/紫灰，仅保留少量血红点缀 | near-monochrome dark green / violet-grey, sparse blood-red accents |
| 史诗暗金 | 暗金色调，青铜与琥珀交织，庄重而古老 | dark gold and bronze with amber tones, ancient and majestic |
| 圣洁辉光 | 白色与淡金为主，像神殿壁画般庄重 | whites and pale gold, solemn like temple frescoes |

### 艺术风格（Art Styles）

| 风格 | 中文片段 | English |
|---|---|---|
| 电影感 | 史诗奇幻电影剧照，广角镜头，浅景深 | epic fantasy movie still, wide-angle lens, shallow depth of field |
| 概念艺术 | 电影概念艺术，笔触豪放，层次分明 | cinematic concept art, bold brushwork, layered composition |
| 水墨 | 泼墨山水风格，浓淡干湿变化丰富 | chinese ink-wash painting style, expressive dry and wet strokes |
| 浮世绘 | 日本浮世绘风格，波浪纹样与云纹装饰 | ukiyo-e woodblock style with stylized waves and clouds |
| 克苏鲁暗黑 | 洛夫克拉夫特式黑暗奇幻，压抑扭曲 | lovecraftian dark fantasy, oppressive and twisted |
| 复古版画 | 19世纪博物学铜版画风格，细密排线 | 19th-century naturalist engraving, fine cross-hatching |
| 3D 写实 | 次世代 3D 渲染，PBR 材质，真实光影 | next-gen 3D render, PBR materials, physically-based lighting |

### 质量后缀（Quality Suffix）

- `8k 超高清，超精细细节，最佳画质，光影真实`
  EN: `8k, ultra-detailed, intricate details, best quality, photorealistic lighting`
- 常用英文组合：`cinematic lighting, dramatic composition, masterpiece, award-winning`

### 三色组合法（Tri-Color System，必用）

**参考专业 CG 巨兽的配色规律：暗部占 60%+，高光集中，只保留 1–2 个高饱和点缀色。**
避免「五颜六色」。固定公式：**主色（大面积基底）+ 辅色（中面积过渡）+ 点缀色（小面积高饱和）**。

| 组合 | 主色 | 辅色 | 点缀色 | 情绪 |
|---|---|---|---|---|
| 熔岩系 | 炭黑 charred black | 暗血红 dark blood red | 焦橙 burning orange | 狂暴毁灭 |
| 深渊系 | 深海藏蓝 abyssal navy | 湿炭黑 wet charcoal | 冷青生物光 cyan bioluminescence | 神秘恐惧 |
| 冰渊系 | 冰川蓝 glacier blue | 霜白 frost white | 血红橙 eye glow orange-red | 冷酷神圣 |
| 沙暴系 | 沙金 sand gold | 风化石灰 weathered stone grey | 朱红 vermilion | 荒凉野性 |
| 圣辉系 | 月白银 pale silver | 骨白 bone white | 鎏金 gold | 庄严威严 |
| 腐沼系 | 沼泽墨绿 swamp dark green | 泥灰 mud grey | 病态磷光 sickly phosphor green | 腐朽诡异 |

### 材质-色彩绑定（Material-Color Binding）

色彩必须长在材质上才有质感。**每个颜色词都建议绑定一个材质词**：

- `风化青铜的铜绿 + 金丝纹饰` — patinated bronze verdigris with gold filigree
- `浸透海水的湿黑岩鳞片` — waterlogged black stone scales
- `覆霜冰壳，内部透出幽蓝` — frosted ice shell glowing deep blue within
- `熔岩凝皮，裂纹中透出橙红` — cooled lava crust, orange glowing through cracks
- `焦枯树皮般的粗糙皮肤` — bark-like charred skin
- `珍珠质贝壳般的虹彩鳞片` — iridescent pearl-like scales

### 明暗节奏（Lighting Rhythm）

- `大面积暗部 + 少量强高光，主体从黑暗中浮现`
  EN: `vast dark areas with sparse bright highlights, subject emerging from darkness`
- `背景亮、主体暗（剪影），边缘被光晕勾勒`
  EN: `bright background, dark subject silhouette, rimmed by glowing edge light`
- `光比强烈（1:8），阴影近乎全黑`
  EN: `high contrast ratio, shadows falling to near-black`

---

## 负面提示词（Negative Prompts，通用）

- `low quality, blurry, deformed anatomy, extra limbs, extra fingers, watermark, text, logo, jpeg artifacts, oversaturated, boring composition, small scale, mundane, flat lighting`
- 中文：`低质量，模糊，解剖结构错误，多余肢体，多余手指，水印，文字，标志，压缩失真，过饱和，构图平淡，缺乏压迫感`

---

## 多维度完全体示例（参考素材风格）

以下两条示例示范「六维度全开 + 场景贴合绑定 + 三色组合」的完整写法，
色彩参数来自对实际参考素材的量化分析。

### 完全体 A：熔岩白猊（暖系 · 参考「火系」素材色调：炭黑 45% + 暗血红 25% + 焦橙 15%）

```
主体定义：一只山岳般雪白的巨猊，鬃毛由熔岩与余烬构成
[体型] 它立起时高过东方三重楼阁，宫殿在它爪下如积木
[形态] 黑曜石鳞片嵌于四肢，毛发根根分明覆满火星，皮肤裂纹中透出熔岩光
[光影] 背后火山喷发，逆光将它的雪白身躯压成剪影，轮廓被熔岩红光勾勒，热气扭曲空气
[动态] 它仰天咆哮，声浪震碎数里外的琉璃瓦
[场景] 岩浆河沿街奔流，点燃倒塌的木构楼阁，飞灰与火星漫天
[色彩] 炭黑 + 暗血红 + 焦橙三色组合，明暗比 1:8
[风格] 东方奇幻电影写实，低角度广角，体积感强
[质量] 8k 超高清，PBR 材质
```

**EN**：
```
a mountain-sized snow-white celestial lion with a mane of lava and live embers,
towering above three-tiered Chinese pagodas that look like toys beneath its claws,
obsidian scales plating its limbs, fur rendered strand by strand with sparks clinging
to it, molten light glowing through cracks in its hide, a volcano erupting behind it
silhouetting the white body, rimmed by crimson lava glow with heat-warped air,
roaring at the sky, shockwaves shattering tiled rooftops for miles, lava rivers
rushing through the streets igniting collapsed timber towers, ash and embers filling
the air, palette of charred black, dark blood red, and burning orange, high contrast
1:8 lighting, oriental epic fantasy realism, low-angle wide shot, 8k, PBR materials
Negative: low quality, blurry, watermark, text, extra limbs, oversaturated, flat lighting
```

### 完全体 B：雾海冰鹿（冷系 · 参考「冰系」素材色调：雾蓝灰 40% + 深靛 30% + 银白剪影）

```
主体定义：一只破云而立的雪白巨鹿，鹿角如冰晶珊瑚林
[体型] 它立于极地冰湖之上，头颅高过云端，云海只到胸口
[形态] 鹿角分叉如冰晶树冠，覆满霜花，白毛在寒风中翻卷，蹄下冰面呈放射状裂纹
[光影] 惨白月光穿透漩涡云，银色体积光柱落在它身上，周围浓雾翻涌
[动态] 它缓缓转头回望，目光冰冷如冰川
[场景] 冰湖倒映剪影，湖面冰缝向四方崩裂，远处极光在云涡中明灭
[色彩] 雾蓝灰 + 深靛 + 银白剪影，点缀淡金
[风格] 史诗概念艺术，广角低角度，剪影构图
[质量] 8k 超高清
```

**EN**：
```
a snow-white stag-god standing above the clouds on a polar ice lake, head rising past
the cloud layer, chest-level mists churning below, antlers branching like frozen coral
forests crusted with hoarfrost, fur whipping in the cold gale, radial cracks spreading
from its hooves across the ice, pale moonlight piercing a spiral storm of clouds,
silver god-rays falling on its form, dense fog rolling around its legs, head turning
slowly with glacier-cold eyes, the frozen lake mirroring its silhouette, ice crevasses
splitting the ground in all directions, aurora flickering within the cloud vortex in the
distance, palette of misty blue-grey, deep indigo, and silver-white silhouette with pale
gold accents, solemn epic concept art, wide-angle low-angle composition, 8k
Negative: blurry, watermark, text, deformed antlers, flat colors, oversaturated
```

---

## 面向镜头 · 宏大建筑 完全体示例（视频生成首选）

以下两条示范「9 层面全开 + 面向镜头构图（T4.1–T4.5）+ 城市级巨型建筑场景」的完整写法，
主体正对镜头、直视观者，适合直接用于图生视频（即梦 / 可灵 / Sora）。

### 完全体 C：深渊烛龙（视频向 · 面向镜头 + 沉没巨城，深海黑蓝系）

```
主体定义：一只三首深渊烛龙自黑海立起，正面朝向镜头
[体型·建筑参照] 沉没的环形巨城只到它胸口，最高的灯塔只及它的肘部，货船如漂木
[形态] 湿黑岩鳞片层层堆叠缝隙渗水，背脊节状骨棘泛青，下颌垂落数十条触须，末梢冷青荧光如深海灯盏
[纹理] 鳞片独立高光，黏液拉丝，触须末梢发光点清晰可数
[光影] 惨白月光自云隙洒下压成剪影，背后闪电撕开天幕，侧光勾勒鳞片起伏
[动态·面向镜头] 三颗头颅正对镜头，六只竖瞳锁定观者，瞳孔深处倒映燃烧的灯塔
[场景反应] 海水自脊背倾泻成瀑布，海啸吞没环形港口，沉没神殿的廊柱在浪中翻倒
[色彩] 深海藏蓝+湿炭黑+冷青荧光三色组合，明暗比 1:10
[情绪] 克苏鲁式不可名状的压抑恐惧
[镜头] 低角度广角仰拍，底部微小人群在城墙溃逃，正面朝向镜头
[质量] 8k 超高清，PBR 材质
```

**EN**：
```
a three-headed abyssal candle-dragon rising from the black sea, facing the camera
head-on, a sunken ring-city reaching only its chest, the tallest lighthouse touching
its elbow, cargo ships like driftwood; scales of waterlogged black rock layered with
water seeping from the gaps, bone ridges glowing pale cyan, dozens of ink-black
feelers trailing from its jaws, each tip a single cold-cyan bioluminescent lamp;
pale moonlight crushing its bulk into silhouette, lightning tearing the sky behind
it, side light tracing every scale; three heads turned straight at the lens, six
vertical pupils locked on the viewer, burning lighthouse reflections deep within;
seawater cascading off its back like waterfalls, a tidal wave swallowing the ring
harbor, temple columns toppling in the surge; palette of abyssal navy, wet charcoal,
cold-cyan bioluminescence, 1:10 light-dark ratio, unspeakable lovecraftian dread;
low-angle wide shot, tiny crowds fleeing along the doomed city walls at the bottom
of the frame, facing the camera, 8k, ultra-detailed, PBR
Negative: low quality, blurry, watermark, text, extra heads, deformed teeth,
oversaturated, flat lighting, camera showing its back
```

### 完全体 D：沙暴翼龙（视频向 · 面向镜头 + 巨型古城，沙金橙红系）

```
主体定义：一只沙漠级巨翼龙正对镜头，自沙暴中缓缓立起
[体型·建筑参照] 巨型金字塔群只到它腰部，残破的竞技场城墙如沙堆，塔楼群在它肩头以下
[形态] 沙金鳞片风化皮革磨砂质感，翼膜半透明，朱红与青绿条纹如绸缎反光，血管在膜中隐现
[纹理] 翼骨尖端焦黑开裂，鳞片间积沙，刮痕累累
[光影] 正午烈日硬质逆光，半透明翼缘透出熔金橙红，光线穿过尘埃形成体积光柱
[动态·面向镜头] 双翼收拢压向镜头，头颅俯低，竖瞳锁定观者，瞳孔深处倒映燃烧的古城
[场景反应] 翼击掀起爆炸般沙尘，沙丘如浪翻卷，古城墙头旗帜倒卷上天
[色彩] 沙金+焦橙+青绿点缀三色组合，明暗比 1:4
[情绪] 炽热、狂野、力量即将宣泄的压迫
[镜头] 低角度仰拍，底部微小人群在塔楼下逃窜，正面朝向镜头
[质量] 8k 超高清，写实生物设计
```

**EN**：
```
a desert-scale wyvern facing the camera, rising slowly from a sandstorm, giant
pyramid clusters reaching only its waist, ruined arena walls like heaps of sand,
tower clusters passing beneath its shoulder; sand-gold scales with weathered leather
grain, translucent wing membranes striped in vivid vermilion and teal, veins faintly
visible, shimmering like silk; scorched cracked wing-bone tips, sand caught between
scales, battle scars across the hide; blazing noon sun backlighting the wing edges
in molten orange, god-rays piercing the dust; wings folding toward the lens, head
lowered, vertical pupils locked on the viewer, a burning ancient city reflected deep
within; each wingbeat blasting out explosions of sand, dunes rolling like waves,
banners torn from the city walls spinning skyward; palette of sand gold, burnt
orange, teal-green accents, 1:4 light-dark ratio, scorching ferocious menace;
low-angle shot, tiny crowds scattering beneath the towers at the bottom of the
frame, facing the camera, 8k, ultra-detailed, realistic creature design
Negative: blurry main subject, watermark, text, extra wings, feathered wings,
cartoon, oversaturated, camera showing its back
```

### 完全体 E：雷泽巨猿（视频向 · 面向镜头 + 巨型古城废墟，暗金电弧系）

```
主体定义：一只山岳般庞大的雷泽巨猿，正面朝向镜头
[体型·建筑参照] 巨型城墙与塔楼群只及它腰际，王宫穹顶在它膝下如坟丘
[形态] 黑曜岩甲片嵌满焦黑毛发，雷痕在皮肤上蜿蜒，紫色符文随心跳明灭
[纹理] 毛发根根带电竖立，岩甲片缘焦裂渗光
[光影] 闪电自云顶劈落，逆光将它压成剪影，电弧蓝光沿鳞缝爬行
[动态·面向镜头] 双拳高高扬起正欲砸向镜头方向，竖瞳锁定观者，瞳孔深处倒映燃烧的宫殿
[场景反应] 拳风未至，城墙已成片崩塌，地面掀起环形气浪，碎石如雨
[色彩] 炭黑+暗血红+电弧紫金点缀，明暗比 1:8
[情绪] 狂暴毁灭，天崩地裂的压迫
[镜头] 低角度仰拍，底部微小人群自城门溃逃，正面朝向镜头
[质量] 8k 超高清，PBR 材质
```

**EN**：
```
a mountain-scale thunder ape facing the camera, giant city walls and tower clusters
reaching only its waist, palace domes like burial mounds beneath its knees; obsidian
armor plates studding singed black fur, lightning scars crawling across its hide,
violet runes pulsing with its heartbeat; fur standing on end crackling with static,
fractured armor edges glowing; lightning forking from the storm crown backlighting
its silhouette, arcs of blue electricity crawling along the scale seams; both fists
raised to smash toward the lens, vertical pupils locked on the viewer, a burning
palace reflected deep within; walls collapsing in sheets before the blow lands,
ring-shaped shockwaves flattening the ground, rubble raining down; palette of
charred black, dark blood red, and electric violet-gold accents, 1:8 light-dark
ratio, apocalyptic ferocity; low-angle shot, tiny crowds fleeing the city gate at
the bottom of the frame, facing the camera, 8k, ultra-detailed, PBR
Negative: low quality, blurry, watermark, text, deformed anatomy, extra limbs,
oversaturated, flat lighting, camera showing its back
```

### 完全体 F：腐沼古神（视频向 · 面向镜头 + 沉没神庙，腐沼磷光系）

```
主体定义：一只自腐沼立起的千眼古神，正面朝向镜头
[体型·建筑参照] 沉没的神庙群只到它胸口，断柱如牙签插在泥沼中
[形态] 腐木与苔藓覆盖的甲壳，下颌垂落黏稠触须，数百只眼睛布满头颅
[纹理] 甲壳裂隙渗出病态磷光，苔藓根须垂挂如帘
[光影] 惨绿月光穿透浓雾，磷光在黑暗中点染出轮廓
[动态·面向镜头] 头颅缓缓俯低逼近镜头，千百只眼睛同时锁定观者，瞳孔深处倒映雾中的鬼火
[场景反应] 沼泽气泡爆裂喷出毒雾，古树成片倾倒沉入泥中，神庙廊柱接连崩解
[色彩] 沼泽墨绿+泥灰+病态磷光点缀，明暗比 1:10
[情绪] 腐朽诡异的不可名状恐惧
[镜头] 贴地仰拍，底部微小逃难者深陷泥沼，正面朝向镜头
[质量] 8k 超高清
```

**EN**：
```
a thousand-eyed elder god rising from a rotting swamp, facing the camera, sunken
temple clusters reaching only its chest, broken columns like toothpicks in the mud;
rotten-wood and moss-covered carapace, viscous feelers trailing from its jaws,
hundreds of eyes covering its head; sickly phosphor light seeping from carapace
cracks, moss roots hanging like curtains; pale green moonlight piercing the fog,
the glow tracing its shape in the dark; head lowering toward the lens, a thousand
eyes locking on the viewer, corpse-fires reflected deep within; swamp bubbles
bursting into venomous mist, ancient trees toppling and sinking into the mud,
temple columns crumbling one by one; palette of swamp dark green, mud grey, and
sickly phosphor accents, 1:10 light-dark ratio, unspeakable decay; ground-level
shot, tiny refugees sinking into the mire at the bottom of the frame, facing the
camera, 8k, ultra-detailed
Negative: low quality, blurry, watermark, text, extra eyes, deformed anatomy,
oversaturated, flat lighting, camera showing its back
```

### 完全体 G：玄冥冰蛟（视频向 · 面向镜头 + 冰封巨城，冰渊蓝白系）

```
主体定义：一条自极寒之渊昂首的玄冥冰蛟，正面朝向镜头
[体型·建筑参照] 冰封巨城只到它胸口，冰川高塔如冰锥立在它肩下
[形态] 冰晶鳞片层叠如冻湖，霜角分叉结满冰棱，吐息凝成雪雾
[纹理] 鳞面折射极光，冰棱根根通透
[光影] 冷月与极光在它背后交织，体积光柱穿透暴风雪
[动态·面向镜头] 长颈昂起，双瞳锁定观者，瞳孔深处倒映冻结的宫殿尖顶
[场景反应] 它呼气成风，城墙覆霜，冰缝自它身下向四方崩裂，塔楼逐座冰封倒塌
[色彩] 冰川蓝+霜白+血红橙眼点缀，明暗比 1:6
[情绪] 冷酷神圣的灭世寒意
[镜头] 低角度仰拍，底部微小身影蜷缩在冰墙后，正面朝向镜头
[质量] 8k 超高清
```

**EN**：
```
an abyssal frost wyrm raising its head from a polar abyss, facing the camera, a
frozen giant city reaching only its chest, glacier towers like icicles beneath its
shoulder; ice-crystal scales layered like a frozen lake, hoarfrost antlers branched
with icicles, breath condensing into snow mist; scale facets refracting the aurora,
every icicle crystal-clear; cold moonlight and aurora weaving behind it, god-rays
piercing the blizzard; long neck rising, both pupils locked on the viewer, a frozen
palace spire reflected deep within; each exhale a gale that frosts the city walls,
ice crevasses splitting the ground in all directions, towers icing over and
collapsing one by one; palette of glacier blue, frost white, and blood-orange eye
accents, 1:6 light-dark ratio, cold divine annihilation; low-angle shot, tiny
figures huddled behind the ice walls at the bottom of the frame, facing the camera,
8k, ultra-detailed
Negative: low quality, blurry, watermark, text, deformed anatomy, extra limbs,
oversaturated, flat lighting, camera showing its back
```

### 完全体 H：荒原巨象 · 青铜山神（视频向 · 面向镜头 + 古文明宫殿群，史诗暗金系）

```
主体定义：一头驮着古城的荒原巨象，正面朝向镜头
[体型·建筑参照] 巨型宫殿群只到它腰际，方尖碑如草茎插在荒原上
[形态] 风化青铜鳞甲披覆全身，象牙如断柱，甲片间苔藓与金丝纹饰共生
[纹理] 铜绿斑驳，金线刻痕在夕阳下泛光，象鼻布满沙痕
[光影] 落日逆光将它压成剪影，轮廓被暗金辉光勾勒，尘埃中体积光柱斜落
[动态·面向镜头] 它正迈步向镜头逼近，巨瞳俯视观者，瞳孔深处倒映坍塌的方尖碑
[场景反应] 每一步黄沙如浪涌起，宫殿残垣在它脚下震颤，穹顶成片塌落
[色彩] 史诗暗金+氧化铜绿+琥珀点缀，明暗比 1:5
[情绪] 远古苍凉，时间本身的重压
[镜头] 低角度仰拍，底部微小商队自废墟中逃散，正面朝向镜头
[质量] 8k 超高清
```

**EN**：
```
a colossal wasteland elephant carrying a ruined city on its back, facing the camera,
giant palace clusters reaching only its waist, obelisks like grass blades on the
plain; weathered-bronze armor plating its body, ivory tusks like broken columns,
verdigris and gold filigree growing between the plates; mottled copper-green,
gold-etched scars catching the setting sun, trunk scarred with sand; sunset
backlight crushing it into silhouette, rimmed by dark-gold halo, god-rays slanting
through the dust; striding toward the lens, giant eyes looking down on the viewer,
a collapsed obelisk reflected deep within; each step sending dunes rolling like
waves, palace ruins trembling beneath it, domes caving in; palette of dark gold,
oxidized bronze green, and amber accents, 1:5 light-dark ratio, ancient timeless
weight; low-angle shot, tiny caravans scattering from the ruins at the bottom of
the frame, facing the camera, 8k, ultra-detailed
Negative: low quality, blurry, watermark, text, deformed anatomy, extra limbs,
oversaturated, flat lighting, camera showing its back
```

---
