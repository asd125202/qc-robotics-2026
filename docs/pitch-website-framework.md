# Pitch Website Framework

Use this structure for new competition pitch websites. The previous pages are useful research artifacts, but every new investor-grade page should read like a clear seed pitch before it becomes a technical memo.

The benchmark is YC / Airbnb-style clarity: the page should persuade a smart stranger who has no patience for robotics jargon. It must first prove a painful problem and a compelling business wedge, then explain why Qualcomm + LeRobot makes the product unfairly strong.

## Required Narrative Order

1. **One-line company**
   - What is it, for whom, and what outcome does it create?
   - Avoid starting with technology names.

2. **Problem**
   - Name the painful, expensive, frequent problem.
   - Use concrete buyer language, not generic macro trends.

3. **Why now**
   - Show what changed: policy, hardware, model capability, labor shortage, buyer budget, regulation, platform shift.

4. **Insight**
   - State the non-obvious belief.
   - Example: “养老机器人不是替代护工，而是把护理团队的覆盖能力放大。”

5. **Solution**
   - Explain the product in simple terms.
   - Use 3 outcome bullets before architecture.

6. **Product**
   - Show the actual workflow.
   - What does the user do first? What does the robot do? What gets recorded? What improves next week?

7. **Market**
   - Use transparent math and authoritative sources.
   - Separate TAM/SAM/beachhead when possible.

8. **Business model**
   - One line revenue model.
   - Then package/pricing/pilot structure.

9. **Go-to-market**
   - First buyer, first wedge, pilot motion, expansion path.

10. **Competition**
   - List what exists and why it is incomplete.
   - Be specific and respectful.

11. **Moat**
   - Data flywheel, distribution, integrations, hardware reference design, compliance evidence, switching costs.

12. **Why Qualcomm**
   - Make Qualcomm necessary, not decorative.
   - Tie to edge AI, cameras, connectivity, power, security, reference design, and developer ecosystem.

13. **Demo / ask**
   - What will be shown in the competition?
   - What support, device, partner, or pilot is needed next?

## Required Page Sections

Every new pitch page should have the following visible sections, in this approximate order:

- Hero / one-line company.
- Problem.
- Why now.
- Insight.
- Solution.
- Product workflow.
- Market wedge.
- Business model.
- Go-to-market.
- Competition.
- Moat.
- Why Qualcomm.
- Demo / ask.
- Sources.

If a page skips one of these, it needs a deliberate reason in the companion `docs/*.md` file.

## Page Rule

The first three screens should answer:

- Who has the problem?
- Why is the problem urgent now?
- What product solves it in one sentence?

Research details, architecture, and source links belong after the pitch spine is established.

## Quality Bar

- The first sentence should say who uses the product and what outcome they get.
- The problem should be expressed in buyer language: cost, delay, labor, risk, revenue, compliance, uptime, or customer experience.
- The solution should be understandable without knowing ROS, LeRobot, QNN, or Qualcomm product names.
- The GTM should name a first buyer, a first workflow, a paid pilot shape, and an expansion path.
- The competition section should name real alternatives and state why they are incomplete without insulting them.
- The moat should describe accumulating advantage: data, workflow lock-in, integrations, certification evidence, distribution, or hardware reference design.
- The Qualcomm section should make Qualcomm necessary, not decorative.
- The ask should be specific enough that a judge, partner, or sponsor knows what help would accelerate the project.

## Avoid

- Starting with “we use Qualcomm + LeRobot” before explaining the buyer pain.
- Macro-only slides with no buyer.
- Technology-first architecture before solution clarity.
- “All-in-one platform” claims without a first wedge.
- Huge market numbers without a specific beachhead.
- Medical, safety, or compliance promises beyond evidence.
