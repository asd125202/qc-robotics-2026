const stages = [
  ["采集", "示教 episode 进入数据集"],
  ["清洗", "保留成功与失败片段"],
  ["训练", "云 GPU 训练 ACT 策略"],
  ["评估", "回放验证成功率与延迟"],
  ["部署", "生成 Qualcomm 边缘包"],
  ["运行", "本体执行并回流数据"],
];

const clouds = {
  china: {
    label: "中国云版本",
    providers: "PAI / AutoDL / 腾讯云",
    jobs: [
      ["ACT-grasp-v3", "阿里云 PAI", "训练中", "warn"],
      ["failure-replay-v1", "AutoDL", "已完成", "ok"],
    ],
  },
  global: {
    label: "海外云版本",
    providers: "Runpod / Lambda / Modal",
    jobs: [
      ["ACT-grasp-v3", "Runpod A100", "训练中", "warn"],
      ["eval-export-v2", "Modal", "已完成", "ok"],
    ],
  },
};

const state = {
  cloud: "china",
  stage: 2,
  devices: [
    ["Rhino X1 / QCS8550", "在线 · 34ms · ACT-grasp-v2", "ok"],
    ["Dragon Q6A / QCS6490", "待接入 · compact profile", "warn"],
    ["VENTUNO Q / IQ-8275", "规划中 · industrial profile", "warn"],
  ],
  datasets: [
    ["tabletop-pick-v1", "128 episodes · 42 failure clips", "ok"],
    ["human-recover-v1", "18 interventions · pending review", "warn"],
    ["mobile-inspect-v0", "simulation seed · draft", "warn"],
  ],
  models: [
    ["act-grasp-v2.qedge", "86% success · 34ms latency", "ok"],
    ["act-grasp-v3-candidate", "training · expected +6%", "warn"],
    ["smolvla-lab-draft", "research track · not deployed", "warn"],
  ],
  skills: [
    ["桌面抓取", "QCS8550 verified · rollback ready", "ok"],
    ["失败接管", "collects recovery clips", "ok"],
    ["移动巡检", "needs hardware route test", "warn"],
  ],
  storyboard: [
    ["产品开场", "机器人仍像早期组装电脑"],
    ["本体核心", "Qualcomm edge core 与安全边界"],
    ["云端训练", "LeRobot dataset 与 GPU job"],
    ["边缘部署", "模型回到本体低延迟执行"],
    ["商业收束", "硬件、训练、技能、运维、教育"],
  ],
};

const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => Array.from(document.querySelectorAll(selector));

function itemTemplate([title, detail, badge = "ok"]) {
  return `
    <article class="item">
      <div class="item-row">
        <div>
          <strong>${title}</strong>
          <span>${detail}</span>
        </div>
        <span class="badge ${badge}">${badge === "ok" ? "正常" : "关注"}</span>
      </div>
    </article>
  `;
}

function renderStages() {
  $("#stage-track").innerHTML = stages
    .map(([title, detail], index) => `
      <article class="stage ${index === state.stage ? "active" : ""}">
        <strong>${String(index + 1).padStart(2, "0")} · ${title}</strong>
        <span>${detail}</span>
      </article>
    `)
    .join("");
}

function renderLists() {
  const cloud = clouds[state.cloud];
  $("#cloud-label").textContent = cloud.label;
  $("#provider-label").textContent = cloud.providers;
  $("#device-list").innerHTML = state.devices.map(itemTemplate).join("");
  $("#dataset-list").innerHTML = state.datasets.map(itemTemplate).join("");
  $("#job-list").innerHTML = cloud.jobs.map(itemTemplate).join("");
  $("#model-list").innerHTML = state.models.map(itemTemplate).join("");
  $("#skill-list").innerHTML = state.skills.map(itemTemplate).join("");
  $("#storyboard").innerHTML = state.storyboard
    .map(([title, detail]) => `<article><strong>${title}</strong><span>${detail}</span></article>`)
    .join("");
  $("#metric-devices").textContent = state.devices.length;
  $("#metric-jobs").textContent = cloud.jobs.length;
  $("#metric-success").textContent = state.stage >= 4 ? "91%" : "86%";
  $("#metric-latency").textContent = state.stage >= 5 ? "31ms" : "34ms";
}

function render() {
  renderStages();
  renderLists();
}

$$(".seg").forEach((button) => {
  button.addEventListener("click", () => {
    state.cloud = button.dataset.cloud;
    $$(".seg").forEach((item) => item.classList.toggle("active", item === button));
    render();
  });
});

$(".advance").addEventListener("click", () => {
  state.stage = (state.stage + 1) % stages.length;
  render();
});

$$(".rail-item").forEach((button) => {
  button.addEventListener("click", () => {
    $$(".rail-item").forEach((item) => item.classList.toggle("active", item === button));
    const target = document.querySelector(`[data-panel="${button.dataset.view}"]`);
    if (target) {
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    } else {
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  });
});

render();
