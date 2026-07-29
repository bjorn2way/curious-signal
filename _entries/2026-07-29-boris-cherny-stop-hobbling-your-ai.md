---
title: "Boris Cherny: Stop Hobbling Your AI"
date: 2026-07-29 08:40:24 +0700
section: Research Summary
section_slug: research-summary
description: "Summary: Claude Code & Opus 5 Capabilities Boris from Anthropic"
audio: /audio/2026/07/boris-cherny-stop-hobbling-your-ai.mp3
duration: "4 min 41 sec"
read_time: "6 min"
primary_source: https://youtu.be/qyPCVqFUyDo?is=chXUjtghIbgjJqrZ
signal:
  - "Summary: Claude Code & Opus 5 Capabilities Boris from Anthropic"
  - "Source Context: Interview with Boris Creator of Claude Code discussing the release of Opus 5, the evolution of the Clau…"
  - "1."
---
**Source Context:** Interview with Boris (Creator of Claude Code) discussing the release of Opus 5, the evolution of the Claude Code harness, and new agentic capabilities.

## 1. Key Model Capabilities (Opus 5)
*   **Extended Duration & Autonomy:** Opus 5 can run autonomously for days, weeks, or even months without scaffolding (e.g., `/goal` commands). It possesses high intrinsic task persistence.
*   **Prompt Injection Resistance:** Opus 5 represents a significant leap in safety. It is effectively immune to prompt injection.
    *   *Mechanism:* Combines 3 years of alignment research with a prompt injection classifier based on mechanistic interpretability (monitoring specific neurons that activate during injection attempts).
    *   *Impact:* The model will not execute malicious instructions found in external text (e.g., "delete everything on the user's computer").
*   **Complex Code Transformation:** Capable of rewriting entire codebases across languages (e.g., Zig to Rust) in a single dynamic workflow.
    *   *Case Study:* The Bun team used Claude Code to rewrite the Bun runtime from Zig to Rust. The model ran for **11 days**, spawning thousands of agents, and successfully produced a working production codebase. This task would have taken human engineers over a year.
*   **Emergent Creative Capabilities:** The model can perform tasks it was not explicitly trained for, such as using OpenCV to draw portraits, landscapes, and animals, provided the user asks correctly.

## 2. Harness & System Prompt Evolution
*   **Drastic Prompt Reduction:** Over **80% of the system prompt** in Claude Code was deleted for Opus 5.
    *   *Reasoning:* Previous prompts were "corrective" instructions for older, less capable models. Opus 5 is intelligent enough to follow best practices without explicit instruction.
    *   *Ablation Strategy:* Anthropic uses an "ablation" process for every new model release: delete the entire system prompt, run the model, identify failure points, and only re-add specific instructions where the model consistently struggles.
*   **"Un-hobbling" Philosophy:**
    *   *Product Overhang:* Models often have capabilities that existing products fail to elicit. Building a product that "hobbles" the model (by over-specifying or restricting it) misses this potential.
    *   *Recommendation:* Users should delete old system prompts, skills, and hooks. Modern models perform better with simpler, higher-level instructions rather than rigid, step-by-step constraints.
*   **Experimental Features:**
    *   `--system-prompt`: Allows users to set a custom system prompt.
    *   `simple=1` (Environment Variable): An undocumented feature that removes all system prompts (including tool prompts) to test the model's raw capability.

## 3. Agentic Architecture & Workflows
*   **Dynamic Workflows:**
    *   *Definition:* A new feature in Claude Code that allows the orchestration of thousands of agents within a Bun runtime sandbox.
    *   *Mechanism:* Uses an "algebra of agents" (sequence, parallel execution) to manage test-time compute efficiently.
    *   *Use Case:* Breaking complex tasks (e.g., full codebase rewrites, deep data analysis) into stages: initial pass, verification, summarization, and final integration.
*   **Loops and Routines:**
    *   *Definition:* Cron-like jobs running locally (Loop) or in the cloud (Routine).
    *   *Use Case:* Repetitive maintenance tasks.
    *   *Case Study:* Claude Code maintains its own codebase via ~20-30 daily routines, including:
        *   Dead code cleanup.
        *   Shipping experiments.
        *   Writing missing tests.
        *   "Abstraction Police": Identifying and unifying nearly duplicated abstractions across the codebase.
    *   *Scale:* These routines spawn hundreds to thousands of agents daily, automating work that previously required dozens of engineers.

## 4. Implementation Guidance for Operators
*   **Empirical Approach:** Treat model interaction as an empirical science, not a theoretical one.
    *   *Action:* Give the model a task that seems slightly too hard. Observe where it fails. Add minimal scaffolding only to fix specific failure points.
    *   *Avoid:* Over-specifying instructions. Modern models prefer high-level goals with guardrails/exit criteria over rigid step-by-step commands.
*   **Verification is Critical:** The most important skill is providing the model with a way to verify its own work (e.g., running tests, pixel-by-pixel comparison, fuzzing). This prevents the model from getting stuck in loops or hallucinating.
*   **Leverage Test-Time Compute:** Use dynamic workflows to scale token usage for complex tasks. The value lies in the orchestration of many small agents rather than a single monolithic prompt.
*   **Continuous Iteration:** Evals and system prompts have a short lifespan. As models improve exponentially, old evals saturate and must be replaced. Old prompts become obsolete and may hinder performance.

## 5. Risks & Limitations
*   **Not Fully Solved:** While "coding is solved" for many tasks, Opus 5 still struggles with:
    *   Deep systems code.
    *   Distributed systems.
    *   Pixel-perfect UI verification.
*   **Hallucination/Drift:** In long-running tasks (e.g., a 14-day Swift rewrite experiment), the model may drift or require live monitoring (e.g., live-blogging progress in Slack) to ensure it stays on track.
*   **Resource Intensity:** Long-running tasks consume significant compute and tokens. Dynamic workflows are efficient but still require substantial infrastructure to support thousands of concurrent agents.

## 6. Notable Quotes & Insights
*   *"The model is not like a system you build up front... it's more organic. It's a living creature... you have to take the time to get to know it."*
*   *"Don't listen to LinkedIn influencers... There's no one weird trick. It's about being empirical."*
*   *"Coding is solved for the kind of coding I do... but not for everyone."*
*   *"The best Claude users are able to spawn tasks that provide a lot of leverage, like thousands of agents."*

## 7. Actionable Next Steps for Dashboard Users
1.  **Audit System Prompts:** Review existing system prompts and skills. Consider deleting them to test if the model can perform tasks without them.
2.  **Implement Dynamic Workflows:** For complex, multi-stage tasks, implement dynamic workflows to orchestrate agent parallelism and verification.
3.  **Set Up Routines:** Automate repetitive maintenance tasks (dead code, test generation) using loops/routines to free up human engineering time.
4.  **Focus on Verification:** Ensure every agentic task includes a verification step (tests, diffs, visual checks) to maintain quality over long durations.
5.  **Monitor Safety:** Leverage the model's inherent prompt injection resistance but continue to monitor for edge cases in complex, long-running workflows.

<details class="evidence-drawer" markdown="1">
<summary>Evidence note</summary>

The source registry contains one readable HTTP source. No private source fields are rendered.

</details>

## Sources

- [Boris Cherny: Stop Hobbling Your AI](https://youtu.be/qyPCVqFUyDo?is=chXUjtghIbgjJqrZ)
