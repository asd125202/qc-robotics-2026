# Competition Information

Source page: https://qc-robotics-dev.aidlux.com/2026/

This note consolidates information read from the official client-rendered page and its official visual sections.

## Basic Facts

- Chinese title: `2026 高通具身智能与机器人大赛`
- English title on banner: `2026 Qualcomm Embodied Intelligence and Robotics Developer Contest`
- Competition period on banner: May to December 2026
- Main theme: embodied intelligence and robotics on Qualcomm edge AI / robotics hardware
- Organizer: Qualcomm Technologies, Inc.
- Co-organizer / operator: Chengdu APLUX Intelligent Technology Co., Ltd.
- Competition partners shown on the banner: APLUX, Arduino, Radxa

## Official Timeline

- 2026-05-07: official launch
- 2026-05-07 to 2026-07-20: preliminary round
- 2026-07-20 to 2026-07-31: finalist list review/publication and device distribution
- 2026-08-01 to 2026-11-01: final round
- 2026-12: award ceremony

Important submission detail from the project-book template:

- Preliminary project book submission deadline: 2026-07-20 11:59:59.
- Preliminary round requires project-book submission. Preliminary research output is encouraged and may be included through video, screenshots, photos, or a compressed package.
- Suggested project-book filename: `[project name]-[team name]`.
- Project-book format: `.docx` or `.pdf`.

## Event Positioning

The competition focuses on practical implementation of embodied intelligence and robotics, while also supporting future technology exploration.

The official intro emphasizes:

- edge AI and robot hardware/software ecosystems
- robot perception and interaction
- intelligent decision making
- motion control
- real-world deployment scenarios
- prototype polishing, scenario adaptation, and commercialization

## Tracks

### Standard Track

The standard track is based on Qualcomm Dragonwing QCS6490 and QCS8550 processors.

Focus:

- system-level capability instead of isolated algorithm demos
- complete closed loop across perception, AI inference, decision making, and control
- clear architecture
- stable runtime behavior
- reproducible engineering implementation
- real-environment deployment and demonstration
- deployable robotics and embodied intelligence applications with commercial potential

Candidate boards:

- APLUX Rhino X1 with Qualcomm Dragonwing QCS8550
- Radxa Dragon Q6A with Qualcomm Dragonwing QCS6490

### Pioneer Track

The pioneer track is based on the Qualcomm Dragonwing IQ-8275 processor.

Focus:

- forward-looking embodied intelligence and robotics exploration
- new model types
- heterogeneous computing
- collaboration between perception and control
- early-stage projects with a clear technical route and evolution potential
- feasibility validation for higher-end and industrial-grade processors

Candidate board:

- Arduino VENTUNO Q with Qualcomm Dragonwing IQ-8275

## Hardware

### APLUX Rhino X1

- Processor: Qualcomm Dragonwing QCS8550
- Track: Standard
- Described as an integrated edge AI development board for compute, control, and interaction.
- AI compute: 48 TOPS INT8
- CPU frequency shown: 3.2 GHz
- Intended strengths: lightweight model inference, multimodal perception, real-time processing, rich IO, sensor/actuator integration, efficient algorithm-hardware collaboration.
- Device page: https://developer.aidlux.com/
- Documentation: https://rhinopi.docs.aidlux.com/rhino-x1-aidlux/
- Hardware support email: `gubowen@aidlux.com`

### Arduino VENTUNO Q

- Processor: Qualcomm Dragonwing IQ-8275
- Track: Pioneer
- Described as a robotics and generative AI development platform from Arduino.
- NPU compute shown: up to 40 TOPS
- Integrates an STM32H5 microcontroller for low-latency execution and motor control.
- Memory/storage shown: 16 GB memory and support for 64 GB expandable storage.
- Device page: https://www.arduino.cc/product-ventuno-q

### Radxa Dragon Q6A

- Processor: Qualcomm Dragonwing QCS6490
- Track: Standard
- Designed for industrial IoT, edge intelligence, and intelligent terminal scenarios.
- Board size shown: 85 x 65 x 20 mm.
- Device page: https://radxa.com/products/dragon/q6a/
- Documentation: https://docs.aidlux.com/guide/hardware/other-development-board/Radxa
- Hardware support email: `prince@radxa.com`

## Preliminary Round

Participation:

- Register through the official activity page.
- Submit the preliminary project book before the July 20 deadline.
- Project-book template is linked from the page.

Scoring:

| Criterion | Meaning | Points |
| --- | --- | ---: |
| Team fit | Team members' education/work background, technical capability, innovation ability, and collaboration | 20 |
| Project feasibility | Whether the team can implement the goal, functions, and performance under current technical and contest constraints within the required time | 50 |
| Project completeness | Whether design is reasonable, fits business logic and needs, describes product/service clearly, and includes a complete implementation plan | 30 |
| Total |  | 100 |

## Final Round

Participation:

- Finalists should develop and deploy the selected project on the competition-specified device they receive.
- Final work must be submitted before 2026-11-01.
- Keep the project in a runnable state; excellent projects may be shown in the 2026 contest work exhibition area.

Final submission package includes, but is not limited to:

- Real operation demo video, within 3 minutes, showing startup/runtime on the device and main functions.
- Project introduction PPT explaining technical implementation, features, application scenario, market potential, and social value.
- Complete code resource package, optional but encouraged, used as supporting material for judging.

Final scoring:

| Criterion | Meaning | Points |
| --- | --- | ---: |
| Technical completeness | Reasonable software/hardware architecture, clear technical route, complete perception/decision/control/execution modules, stable system operation, high integration, reproducible and verifiable onsite | 20 |
| Technical innovation | Innovation in algorithm, model, control, or hardware architecture; new solution to domain pain points; differentiated technical highlight | 10 |
| Qualcomm processor application | Deep use of Qualcomm processor compute, AI engine, core technical features, and ecosystem advantages; efficient deployment/migration showing processor value | 10 |
| Technical forward-looking value | Fits trends in robotics, embodied intelligence, and multimodal large models; extensible and evolvable; suitable for future complex scenarios | 10 |
| Project completeness | Complete closed loop across requirement analysis, solution design, R&D, testing, documentation, drawings, code, video material, division of labor, progress, and results | 10 |
| Functional innovation | Novel function design that solves difficult traditional-solution scenarios; innovative interaction, task mode, or application experience; practical and easy to use | 20 |
| Product definition | Accurate scenario pain-point identification, clear positioning, clear target users/core value/function boundaries, reasonable product logic, high scenario fit | 10 |
| Commercial potential | Real application scenario, clear market demand, feasible implementation, cost controllability, clear business model, scalability, and economic/social value | 10 |
| Total |  | 100 |

## Awards

The award pool is shown as approximately CNY 716,000 total value.

| Award | Count | Prize value |
| --- | ---: | ---: |
| Grand Prize | 1 | CNY 120,000 |
| Platinum Award | 2 | CNY 70,000 |
| Gold Award | 4 | CNY 40,000 |
| Silver Award | 6 | CNY 20,000 |
| Commercial Potential Award | 8 | CNY 12,000 |
| Excellence Award | 10 | CNY 8,000 |

Prize notes from the page:

- Prizes are Qualcomm-product-related electronic consumer products.
- The grand prize is a major product with Snapdragon Digital Chassis.
- Stated values include tax; the organizer handles required 20% individual occasional-income tax withholding for personal prize recipients.

## Judging Panel

- 毛嵩: Qualcomm Ventures China, Managing Director
- 孙海: Qualcomm Technologies China, Senior Marketing Director
- 沈波: Qualcomm Technologies China, Engineering Director
- Stefano Implicito: Qualcomm Technologies, Arduino Business Marketing Director
- 孙晓刚: APLUX Intelligent Technology, CEO
- 王培瑶: Radxa, General Manager

## Registration Eligibility

The registration section states:

- The competition is open to society: individuals, companies, creator teams, and similar participants may register.
- Government agencies and related organizations/employees, Qualcomm, competition partners and their affiliates/employees, and restricted persons or legal entities are excluded.
- Participants must own the relevant intellectual property rights for submitted work, including legal authorization where needed.
- Participants agree that organizers and partners may use submitted work materials in competition promotion.
- By joining, participants declare that they meet the qualification requirements and accept disqualification if they do not.
- Each participant may join only one team. Duplicate or alias participation may cancel participation qualification, results, and awards.

## Registration Form Fields

The online registration form asks for:

- Contact name
- Gender
- Email
- Team name
- Preferred competition device
- Project name
- Team members: name, role, contact method
- Team type: company, maker, student, individual, or other
- Optional notes
- WeChat ID
- Mainland China phone number and verification code

Conditional team information:

- Company: company name, website, industry
- Maker: graduation school, focus areas, team honors
- Student: school, major, degree, grade, advisor
- Individual: personal introduction
- Other: team overview

The team-member UI allows up to 5 members.

## Work Upload

The upload page requires:

- Registration phone number
- Phone verification code
- Uploaded work file

The upload note says the work can be submitted only once and cannot be modified; multiple files should be packaged before upload.

## Technical Training

Training/share sessions shown on the page:

| Date/time | Session | Speaker |
| --- | --- | --- |
| 2026-05-21 20:00 | Qualcomm AI application development tools chain and model library | 李万俊, Qualcomm Technologies China, Senior Staff Engineer |
| 2026-05-28 20:00 | Rhino X1 helps accelerate the era where everyone is a developer | 陈鹏, APLUX, Senior Technical Engineer |
| 2026-06-11 20:00 | Radxa Dragon Q6A: quickly start a robot development journey | 陈家立, Radxa OS Software Engineer |
| 2026-06-16 20:00 | From champion to entrepreneur: my growth path | 李江浩, Suzhou Xietong Jinhua founder, ROS evangelist |
| 2026-07-07 20:00 | Qualcomm robot development platform selection and competition techniques | 周三奇, Qualcomm Technologies China, Senior Product Marketing Manager |

Replay/live links embedded in the page:

- https://live.csdn.net/room/csdnnews/7upzigzP
- https://live.csdn.net/room/csdnnews/mcsWHKdA
- https://live.csdn.net/room/csdnnews/2jyfJDAn
- https://live.csdn.net/room/csdnnews/mn2gDW0z
- https://live.csdn.net/room/csdnnews/dUE51v8N

## Event Updates

The official page lists these news/update links:

- 2026-06-15: Public class, previous champion shares robotics-track growth path: https://mp.weixin.qq.com/s/_4V-pn6hoG8FQtcOqS95-w
- 2026-06-12: Developer-made AIGC contest video: https://weixin.qq.com/sph/Ax3nLHcOK
- 2026-06-08: Radxa quick-start robot development public class: https://mp.weixin.qq.com/s/HhHloIUoaIYJz1qvzEAQYA
- 2026-05-26: Rhino X1 public class: https://mp.weixin.qq.com/s/0PX5kLkA5sLDio9k70_Ojg
- 2026-05-18: Qualcomm engineer explains core development points: https://mp.weixin.qq.com/s/kzkeHtSmiPlGFUWMkd_WTg
- 2026-05-12: Arduino VENTUNO Q contest article: https://mp.weixin.qq.com/s/GwFTlRyJyaZw_wO0OrWf3A
- 2026-05-08: Radxa Dragon Q6A contest article: https://mp.weixin.qq.com/s/Ig5Xd1THqyveNIJYFIZ5Yw
- 2026-05-08: Chengdu High-tech article: https://web.csp.chinamcloud.com/cms/cdgxqrmt_html/APP/fglm/4896168563.shtml?share=true
- 2026-05-08: Developer note: https://mp.weixin.qq.com/s/fvpguPEpurMKl0QeFvFNkw
- 2026-05-07: Qualcomm developer zone launch article: https://www.csdn.net/article/2026-05-07/160847830
- 2026-05-07: Qualcomm developer community Weibo announcement: https://weibo.com/3805442325/QEerd0peo
- 2026-05-07: APLUX registration announcement: https://mp.weixin.qq.com/s/SWP4rmfxgsNUClMaOB8cMg

## Contact

- Competition email: `QC-robotics-dev@aidlux.com`
- Email subject should include `【大赛】`.
- The page also shows a QR code for the competition discussion group.

## Previous Contests

- 2024 Qualcomm Edge Intelligence Innovation Application Contest: https://qc-ieiot-challenge.aidlux.com/2024/
- 2025 Qualcomm Edge Intelligence Innovation Application Contest: https://qc-ieiot-challenge.aidlux.com/2025/
