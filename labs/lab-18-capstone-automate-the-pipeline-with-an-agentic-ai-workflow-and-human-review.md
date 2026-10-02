# Lab 18 — CAPSTONE — Automate the Pipeline with an Agentic AI Workflow and Human Review

**Course:** Business Transformation with AI Agents (C997)  
**Topic 03:** Implementing and Managing Business Innovation with Generative AI Tools  
**Focus:** design and build an agentic workflow that automates the business innovation process end to end, with human review and governance built in.  
**Tools:** n8n (recommended), Make.com, Copilot Studio or Zapier; plus your Lab 3-11 tool accounts

## Goal

The capstone. Everything you did by hand in Labs 3-12 becomes an automated agentic workflow — research, canvas, script, assets and deck — with a HUMAN REVIEW GATE before anything is published, and the Lab 14 guardrails enforced in the flow.

## What you'll build

A working agentic workflow that takes a business idea as input, runs the research-to-content pipeline through AI agents, pauses for human approval, and delivers the finished asset set — with the run logged for audit.

## Before you start

- Sign in to the tools listed above with your own free-tier account.
- Use fictitious or non-confidential material only — never enter personal, client or commercially sensitive data into a public generative AI tool.
- Verify every AI-generated fact, figure and citation before you rely on it.

## Step-by-step

1. Map the pipeline as a flow BEFORE building: Input (business idea) → Research agent → Evaluation agent → Canvas agent → Script agent → HUMAN REVIEW GATE → Asset generation (voice, music, video) → Deck assembly → Output + notification. Draw it; you cannot automate a process you cannot draw.
2. Open n8n (n8n.io — free cloud trial or self-hosted) and create a new workflow. Add a Form trigger that accepts the business idea, the target audience and the desired call to action.
3. RESEARCH AGENT — add an AI Agent node with a web-search tool. System prompt: 'Research the market for the submitted idea. Return market size, three competitors, the customer problem and three source URLs. Only state facts you can cite.' Automates Lab 3.
4. EVALUATION AGENT — add a second agent that scores the idea on the Lab 4 rubric (business value, feasibility, data readiness, risk, strategic fit) and returns a structured JSON verdict with a recommendation.
5. TIP — force STRUCTURED OUTPUT (JSON) between agents. Free-text handoffs break downstream nodes as soon as the model phrases things differently; a defined schema makes the workflow reliable.
6. CANVAS + SCRIPT AGENTS — chain two more agents: one drafts the nine-block canvas from the research, the next writes the 60-second script from the canvas and the research. Each receives the previous agent's structured output.
7. HUMAN REVIEW GATE — this is the most important node. Insert a Wait-for-approval step (n8n's Wait node with an approval form, or a Teams/Slack approval message) that sends the human reviewer the research, the canvas and the script, and PAUSES the workflow. Nothing downstream runs until a person approves.
8. TIP — place the gate BEFORE the expensive, hard-to-reverse steps. Video generation costs credits and publishing is public; approving the script first means a bad idea is stopped while it is still cheap. Give the reviewer approve / reject / request-changes, and route rejection back to the script agent with the reviewer's comments.
9. ASSET GENERATION — after approval, call the ElevenLabs API for the voiceover and your video tool for the scenes, then store the assets. Add an error branch so a failed generation notifies a human instead of silently producing nothing.
10. GUARDRAILS — implement your Lab 14 controls in the flow: validate that no prohibited data is in the input, treat all retrieved web content as untrusted (prompt-injection defence), restrict each agent to only the tools it needs, and add an AI-disclosure field to every output.
11. AUDIT LOG — append each run to a Google Sheet or database: timestamp, input idea, each agent's output, who approved, when, and the final asset links. This is your AUDITABILITY principle made real, and what an assessor or regulator would ask to see.
12. Run the workflow end to end with a fresh business idea. Deliberately REJECT at the review gate once and confirm the flow routes back and does not proceed to asset generation. A gate that cannot stop the process is not a gate.

## Test it

Your workflow runs from a submitted idea through research, evaluation, canvas and script; it PAUSES at the human review gate and only continues on approval; a rejection routes back without generating assets; every run is logged with the approver and timestamp; and you can point to where each Lab 14 guardrail is enforced.

## What you learned

- Design and build an agentic workflow that automates the business innovation process end to end, with human review and governance built in.
- You produced: A working agentic workflow that takes a business idea as input, runs the research-to-content pipeline through AI agents, pauses for human approval, and delivers the finished asset set — with the run logged for audit.
- You practised verifying and challenging AI output rather than accepting the first draft.

---

*Business Transformation with AI Agents · C997 · Tertiary Infotech Academy Pte Ltd · Version v1.0*
