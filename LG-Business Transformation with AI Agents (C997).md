# Business Transformation with AI Agents — Learner Guide

**Course Code:** C997  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 2 October 2026**

## Document Version Control Record

| Version | Date | Description of change | Author |
| --- | --- | --- | --- |
| 1.0 | 2 October 2026 | Initial release of the Business Transformation with AI Agents (C997) Learner Guide: 3 topics and 18 connected labs with step-by-step instructions, aligned to the v1.0 99-slide deck. | Tertiary Infotech Academy |

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Tools and Accounts](#before-you-start--tools-and-accounts)
- [Topic 01 — Introduction to Business Innovation and Generative AI](#topic-01--introduction-to-business-innovation-and-generative-ai)
  - [Lab 1 — Compare Predictive and Generative AI on a Business Task](#lab-1--compare-predictive-and-generative-ai-on-a-business-task)
  - [Lab 2 — Map the Generative AI Tool Landscape](#lab-2--map-the-generative-ai-tool-landscape)
  - [Lab 3 — Research a Business Idea with Perplexity and NotebookLM](#lab-3--research-a-business-idea-with-perplexity-and-notebooklm)
  - [Lab 4 — Evaluate and Prioritise Your Business Idea](#lab-4--evaluate-and-prioritise-your-business-idea)
- [Topic 02 — Designing Digital Architectures and Processes for Business Innovation](#topic-02--designing-digital-architectures-and-processes-for-business-innovation)
  - [Lab 5 — GROUP ACTIVITY — Run a Design Thinking Sprint in Design Thinking Studio](#lab-5--group-activity--run-a-design-thinking-sprint-in-design-thinking-studio)
  - [Lab 6 — GROUP ACTIVITY — Build a Business Model Canvas in BMC Studio](#lab-6--group-activity--build-a-business-model-canvas-in-bmc-studio)
  - [Lab 7 — Design the Digital Architecture for Your Solution](#lab-7--design-the-digital-architecture-for-your-solution)
  - [Lab 8 — Script a Marketing Video for Your Business Idea](#lab-8--script-a-marketing-video-for-your-business-idea)
  - [Lab 9 — Create the AI Voiceover](#lab-9--create-the-ai-voiceover)
  - [Lab 10 — Generate the Background Soundtrack with Suno](#lab-10--generate-the-background-soundtrack-with-suno)
  - [Lab 11 — Produce the Video with Kling and an AI Video Editor](#lab-11--produce-the-video-with-kling-and-an-ai-video-editor)
  - [Lab 12 — Build the Business Presentation with Your Video](#lab-12--build-the-business-presentation-with-your-video)
- [Topic 03 — Implementing and Managing Business Innovation with Generative AI Tools](#topic-03--implementing-and-managing-business-innovation-with-generative-ai-tools)
  - [Lab 13 — Risk-Assess Your Generative AI Pipeline](#lab-13--risk-assess-your-generative-ai-pipeline)
  - [Lab 14 — Define Security Guardrails and AI Ethics Principles](#lab-14--define-security-guardrails-and-ai-ethics-principles)
  - [Lab 15 — Develop the Implementation Action Plan](#lab-15--develop-the-implementation-action-plan)
  - [Lab 16 — Measure and Review Innovation Success](#lab-16--measure-and-review-innovation-success)
  - [Lab 17 — Build the Stakeholder Communication and Idea-Sharing Plan](#lab-17--build-the-stakeholder-communication-and-idea-sharing-plan)
  - [Lab 18 — CAPSTONE — Automate the Pipeline with an Agentic AI Workflow and Human Review](#lab-18--capstone--automate-the-pipeline-with-an-agentic-ai-workflow-and-human-review)
- [Putting It Together — The AIM Framework](#putting-it-together--the-aim-framework)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the course Business Transformation with AI Agents (C997), conducted by Tertiary Infotech Academy Pte Ltd. It provides the detailed, step-by-step instructions for all 18 hands-on labs, organised by the three course topics. Every lab maps to a Skills Framework ability or knowledge item and to one of the three learning outcomes, so completing the labs prepares you directly for the assessment.

Use this guide alongside the course slides and the lab files in the labs/ folder. The slides are deliberately visual and carry only each lab's objective, deliverable and verification step — the full numbered instructions live here in the Learner Guide.

All labs use generative AI tools on their free tiers. Sign up with your own account. Do not enter confidential, personal or client-identifying data into any public generative AI tool during this course; use fictitious or non-sensitive material for every exercise.


## Course Learning Outcomes

- LO1: Evaluate and investigate generative AI business strategies to identify viable opportunities compatible with organisational objectives.
- LO2: Develop action plans to implement business innovation with generative AI and design digital architectures to apply technologies across the business.
- LO3: Manage business innovation and facilitate information flow among stakeholders to review success and develop innovative ideas.


## Before You Start — Tools and Accounts

**What you need**

- A laptop with a modern web browser (Chrome or Edge recommended) and a stable internet connection.
- A personal email address you can use to register for the free tiers of the generative AI tools.
- A general-purpose AI chat assistant — ChatGPT, Google Gemini or Claude (all have a free tier).
- Perplexity for research with cited sources (free tier includes a limited number of deep research queries).
- An AI image tool — Adobe Firefly or Microsoft Designer (both give free credits).
- Gamma (gamma.app) for AI-generated presentations, and Canva for visual layout.
- Suno for AI music, and CapCut or Descript for video editing.
- A spreadsheet application — Microsoft Excel or Google Sheets — for the scoring and KPI labs.

**Set up your accounts before Lab 1**

Register for the tools above in advance so class time is spent on the business thinking rather than on sign-up screens. Free tiers change often; if a tool is unavailable on the day, the trainer will nominate an equivalent. The method taught in each lab matters more than the specific product.

**Responsible use in every lab**

- Never paste confidential, personal or client data into a public generative AI tool.
- Treat every AI output as a draft: verify facts, figures and citations before you rely on them.
- Check the licence terms of any generated image, music or video before any commercial use.
- Record which tool produced which artifact — you will need this for governance.
- Where an output will be published or sent to a customer, keep a human review step.

**How to work through a lab**

- Read the objective and the 'What you'll build' statement so you know the deliverable before you start.
- Follow the numbered steps in order; each lab builds on the artifact produced by the previous one.
- Finish with the 'Test it' check — if it does not pass, revisit the step it points to.
- Save every deliverable; each lab builds on the artifact produced by the previous one.


## Topic 01 — Introduction to Business Innovation and Generative AI

Predictive vs generative AI · GenAI tool landscape · evaluating business opportunities

**Key concepts**

- Predictive vs generative AI — Predictive AI scores and forecasts from historical data; generative AI creates new text, image, audio, video and code from a prompt.
- How GenAI works — A foundation model is pre-trained on a large corpus, then aligned; at inference a prompt is turned into tokens and completed one token at a time.
- Market momentum — The generative AI market is growing at a >35% CAGR; adoption has moved from experiment to core business process in under three years.
- Where value comes from — Four value levers: revenue growth, cost and productivity, risk mitigation and sustainability.
- The GenAI tool landscape — Text, image, speech and voice, music, video, digital human, 3D, office productivity, data analysis and IP tooling.
- Evaluating an opportunity — Screen each idea for business value, feasibility, data readiness, risk and fit with organisational objectives before committing.


### Lab 1 — Compare Predictive and Generative AI on a Business Task

Focus: distinguish current predictive AI from emerging generative AI and describe where each creates business value.

Goal: Run the same customer-feedback data through a predictive framing and a generative framing, then contrast what each produces and when a business should reach for which.

**What you'll build**

A one-page comparison table showing predictive vs generative output on the same business problem, with a recommendation on when to use each.   (Tools: ChatGPT, Google Gemini or Claude (free tier).)

**Step-by-step**

1. Open a GenAI chat assistant (ChatGPT, Gemini or Claude) and sign in with your own free account.
2. Paste this set of five customer reviews for a Singapore cafe: two praising the coffee but criticising the wait, two on pricing, one on staff friendliness.
3. PREDICTIVE framing — prompt: 'Classify each review as positive, negative or neutral and give the overall sentiment score.' Note the output is a label/score derived from existing data.
4. GENERATIVE framing — prompt: 'Write a personalised 60-word reply to each reviewer in a warm brand voice, and draft three ideas to cut wait time.' Note the output is new content that did not exist before.
5. TIP — be specific about ROLE, TASK, FORMAT and AUDIENCE. Compare 'write a reply' against 'You are a cafe owner. Write a 60-word reply to this reviewer in a warm, apologetic tone that offers a concrete fix.' The second prompt gives a usable answer; the first gives filler.
6. Record in a table what each framing produced, what data it needed, and the business decision each one supports. Write one sentence on when your organisation should use each.

**Test it**

Your table clearly shows predictive AI producing a label or forecast from historical data, and generative AI producing new content — and you can justify which one fits a named task in your organisation.

> **Note:** A standalone copy of this lab is in labs/lab-01-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 2 — Map the Generative AI Tool Landscape

Focus: survey generative AI tools across text, image, audio, video, digital human, productivity and data analysis.

Goal: Build a personal tool map by testing one tool in each of four modalities, so you can pick the right tool for a business need instead of defaulting to a chat assistant. These are the tools you will use for the rest of the course.

**What you'll build**

A tool map listing at least eight GenAI tools by modality, each with its business use case, pricing tier and one limitation you observed.   (Tools: ChatGPT/Gemini/Claude, Perplexity, Adobe Firefly or Microsoft Designer, Suno, Canva.)

**Step-by-step**

1. TEXT — use a chat assistant to draft a 100-word product announcement for a service in your industry.
2. RESEARCH — use Perplexity to find two 2026 statistics about GenAI adoption in your industry, and capture the source links it cites.
3. IMAGE — use Adobe Firefly or Microsoft Designer (free credits) to generate a hero image for that announcement. Record the exact prompt you used.
4. AUDIO — use Suno to generate a 30-second background track. Note the licence terms shown for free-tier output.
5. TIP — free tiers change constantly. Record for each tool: what the free tier allows, whether output carries a watermark, and whether commercial use is permitted. You will need this before publishing anything.
6. Record each tool in a table (modality, tool, business use case, free vs paid, one limitation you hit), then add three more from the slides so your map covers video, digital human and office productivity.

**Test it**

Your tool map covers at least four modalities you tested first-hand plus three more from the slides, and for each tool you can name the business task it best supports and one limitation.

> **Note:** A standalone copy of this lab is in labs/lab-02-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 3 — Research a Business Idea with Perplexity and NotebookLM

Focus: investigate business strategies, and the organisation's operating context, priorities, domain and environment, to identify business opportunities created by generative AI.

Goal: STAGE 1 OF THE PIPELINE. Choose the business idea you will carry through the whole course, then research it properly: Perplexity for the external market with cited sources, NotebookLM for synthesising the documents into a grounded briefing you can trust.

**What you'll build**

A research briefing on ONE chosen business idea: market size and trend, three competitors, the customer problem, and three verified sources — plus a NotebookLM notebook containing the underlying documents.   (Tools: Perplexity (Deep Research), Google NotebookLM, ChatGPT/Gemini/Claude.)

**Step-by-step**

1. CHOOSE YOUR IDEA — pick ONE business idea you will use for every remaining lab. Good candidates: an AI tutoring service, a sustainable food brand, an AI customer-support assistant, a wellness app, or a service from your own organisation. Write it in one sentence: 'A <product/service> for <customer> that <solves what>.'
2. PERPLEXITY — open perplexity.ai, select Deep Research mode, and prompt: 'Research the market for <your idea> in Singapore and Southeast Asia. Cover market size, growth trend, the top three competitors and what customers complain about. Cite your sources.'
3. TIP — Perplexity is only as good as its sources. Open at least THREE cited links and confirm the claim actually appears there. AI-cited statistics are frequently misattributed; an unverified number in a board paper destroys your credibility.
4. Run two follow-up prompts to go deeper: 'Who is the ideal customer and what do they pay today?' and 'What regulation or risk affects this market in Singapore?'
5. NOTEBOOKLM — open notebooklm.google.com, create a notebook named after your idea, and add your sources: paste the Perplexity findings, upload any PDF or report you found, and add relevant web links.
6. TIP — NotebookLM answers ONLY from the sources you give it, which is why it hallucinates far less than an open chat assistant. Every answer carries an inline citation — click it to jump to the exact passage. Use Perplexity to FIND sources, NotebookLM to REASON over them.
7. In NotebookLM ask: 'What is the core customer problem?', 'What are the three biggest risks to this idea?' and 'Where do my sources disagree?' Then generate the Briefing Doc from the Studio panel.
8. Write your research briefing on one page: the idea in one sentence, market size and trend, three competitors, the customer problem in the customer's own words, three verified sources, and the three biggest risks.

**Test it**

Your briefing fits one page, every statistic traces to a source you personally opened, and your NotebookLM notebook answers the core-problem question with an inline citation.

> **Note:** A standalone copy of this lab is in labs/lab-03-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 4 — Evaluate and Prioritise Your Business Idea

Focus: evaluate opportunities for viability, applicability to the organisation and compatibility with business goals.

Goal: STAGE 2 OF THE PIPELINE. Stress-test the idea from Lab 3 against alternatives using an explicit scoring rubric, so the decision to proceed can be defended to management rather than being a matter of taste.

**What you'll build**

A scored opportunity register comparing your chosen idea against five alternatives on business value, feasibility, data readiness, risk and strategic fit — with a defended recommendation.   (Tools: ChatGPT/Gemini/Claude, Excel or Google Sheets.)

**Step-by-step**

1. List your chosen idea from Lab 3 plus five alternatives — draw on Lab 2's tool map and your own operational pain points.
2. Create a scoring table with five criteria: business value, feasibility, data readiness, risk (reverse-scored) and strategic fit. Score each idea 1-5 on every criterion.
3. TIP — use the assistant as a CHALLENGER, not a cheerleader. Prompt: 'Act as a sceptical investor. For each of these six ideas, give the single strongest reason it would fail and the data I would need to disprove that.' Chat assistants agree too readily; you must explicitly ask them to argue against you.
4. Adjust your scores with what the challenge surfaced. Note any score you did NOT change and why — defending a score is as valuable as revising it.
5. Weight the criteria to match your organisation's current mandate (for example business value x2 if growth is the priority) and compute a weighted total per idea.
6. Rank all six, confirm or replace your Lab 3 choice, and write one sentence linking the winner to a named organisational objective. Record why the bottom idea was rejected — a defensible decision documents its discards.

**Test it**

Your register scores all six ideas on the five weighted criteria, your chosen idea maps to a named organisational objective, and you can explain why the lowest-ranked idea was rejected.

> **Note:** A standalone copy of this lab is in labs/lab-04-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


## Topic 02 — Designing Digital Architectures and Processes for Business Innovation

Business Model Canvas · Design Thinking · digital architecture · action planning

**Key concepts**

- Business planning methodologies — The Business Model Canvas, Value Proposition Canvas and Design Thinking give innovation a repeatable structure.
- AI-powered Business Model Canvas — Use GenAI to draft and stress-test each of the nine blocks, then validate the assumptions with evidence.
- Design Thinking with GenAI — Empathise, Define, Ideate, Prototype and Test — GenAI accelerates every stage, especially ideation and prototyping.
- Digital architecture layers — Data, model, orchestration, application and governance layers describe where AI sits in the business.
- Integration patterns — Chat assistant, RAG over company documents, workflow automation and autonomous agents are the four common patterns.
- From design to action plan — An action plan names the owner, milestone, resource, risk and success measure for every initiative.


### Lab 5 — GROUP ACTIVITY — Run a Design Thinking Sprint in Design Thinking Studio

Focus: apply a human-centred business planning methodology, accelerated by generative AI, to move from user problem to tested concept.

Goal: Before modelling the business, understand the USER. In teams of 3-5, run all five Design Thinking stages on the researched idea using the course's Design Thinking Studio ed-tool, with AI accelerating each stage and real people correcting it.

**What you'll build**

A completed five-stage Design Thinking workspace: an empathy map, one 'How might we' problem statement, twenty ideas narrowed to three, a prototype concept and a test plan — all captured in the shared studio.   (Tools: Design Thinking Studio (https://alfredang.github.io/designthinking/), ChatGPT/Gemini/Claude, your Lab 3 NotebookLM notebook.)

**Step-by-step**

1. FORM GROUPS of 3-5 (keep the same teams for Labs 5 and 6). Agree which team member's Lab 3 business idea the group will work on.
2. One member opens Design Thinking Studio at https://alfredang.github.io/designthinking/ and creates the workspace, then shares the QR code or link so the whole team joins and edits live.
3. EMPATHISE — use the built-in empathy map with its Says / Thinks / Does / Feels quadrants. Prompt an assistant: 'Generate a user persona and five interview questions for <the idea>, based on <your Lab 3 findings>.' Add its output as sticky notes.
4. TIP — then talk to a REAL person. Have one team member answer as an actual user (or interview someone outside the group) and CORRECT the AI's persona with what you actually hear. GenAI accelerates empathy work; it cannot replace contact with a real user.
5. DEFINE — cluster the empathy notes and converge on ONE problem statement in the form 'How might we <verb> for <persona> so that <outcome>?'. Use the voting feature to pick it.
6. IDEATE — prompt the assistant for twenty divergent ideas, add them as notes, then have the team VOTE to converge on the three most promising on feasibility and impact.
7. PROTOTYPE — describe the winning idea concretely: what the user sees, does and gets. Sketch the screen or service flow and capture it in the Prototype stage.
8. TEST — write a test plan naming what you would measure, with whom, and crucially what result would KILL the concept. A test that cannot fail is not a test.
9. Capture the workspace (screenshot or share link). The problem statement and winning concept feed straight into your Business Model Canvas in Lab 6.

**Test it**

Your team's studio workspace has an artifact in all five stages, the empathy map was corrected by a real person's input rather than left as the AI's draft, your problem statement follows the 'How might we' form, and your test plan names a specific measurable signal that would disprove the concept.

> **Note:** A standalone copy of this lab is in labs/lab-05-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 6 — GROUP ACTIVITY — Build a Business Model Canvas in BMC Studio

Focus: apply a business planning methodology and design how GenAI supports each part of the business model.

Goal: STAGE 3 OF THE PIPELINE, worked as a GROUP. In teams of 3-5, build a complete nine-block Business Model Canvas together in real time using the course's BMC Studio ed-tool, with AI drafting and challenging the content and the six canvas rules keeping it sharp.

**What you'll build**

A collaborative nine-block Business Model Canvas in BMC Studio (shareable Canvas ID), annotated with where GenAI creates value in each block, plus the three riskiest assumptions and how the team would test them.   (Tools: BMC Studio (https://alfredang.github.io/bcm/), ChatGPT/Gemini/Claude, your Lab 3 NotebookLM notebook.)

**Step-by-step**

1. WHAT A GOOD CANVAS LOOKS LIKE — read the six rules before you start. (1) Be SPECIFIC: 'busy working parents in Singapore with children aged 4-8' beats 'families'. (2) Every block must be TESTABLE — if no evidence could disprove it, it is a slogan, not a business model. (3) The nine blocks must be CONSISTENT: revenue must come from the segment you named, through the channel you listed. (4) Keep it to 3-5 notes per block; a canvas crammed with everything says nothing. (5) Write in the CUSTOMER's language, not internal jargon. (6) It is a HYPOTHESIS, not a plan — mark what is ASSUMED versus EVIDENCED.
2. FORM GROUPS of 3-5. Agree which team member's Lab 3 business idea the group will model, and appoint one person as the canvas owner.
3. The owner opens BMC Studio at https://alfredang.github.io/bcm/ and creates a new canvas named after the idea. Share the Canvas ID, invite link or QR code with the team — everyone joins the SAME canvas and you will see each other's initials appear live.
4. Read the built-in Strategyzer prompt questions shown in each block — they are there to spark the discussion. Start with CUSTOMER SEGMENTS and VALUE PROPOSITIONS; every other block depends on getting these two right.
5. Work the canvas as a team: add sticky notes with a title, description, category tag and priority. Divide the nine blocks among members, then review each other's blocks — the value of the group activity is the challenge, not the speed.
6. BRING IN AI — prompt an assistant: 'Act as a business model strategist. Draft a Business Model Canvas for <the idea, one sentence, plus the key findings from Lab 3>. Cover all nine blocks. For each block state the ASSUMPTION you are making and how it could be tested.' Add its best suggestions to the canvas as notes.
7. TIP — feed it your Lab 3 research in the prompt. An assistant given real market findings produces a specific canvas; one given only the idea returns a generic template you could have written yourself. Context is what separates a useful draft from filler.
8. Review every block against the six rules. GenAI drafts confidently but generically — as a group, REWRITE at least four blocks with specifics only your research supports, especially Customer Segments, Value Propositions and Revenue Streams.
9. For each of the nine blocks add one note: how generative AI could improve that block (for example AI-drafted proposals in Customer Relationships, or AI content generation in Channels).
10. Check consistency across the whole canvas: does the revenue stream come from the named segment, through the named channel, using the named key resources? Fix any block that does not connect.
11. VOTE as a team on the three riskiest assumptions, set their priority to high, and write how each could be tested cheaply within two weeks.
12. Capture the finished canvas (screenshot or the shared Canvas ID link) — you will place it in your presentation in Lab 12. Present your canvas to the class in 3 minutes and take one challenge question.

**Test it**

Your team's BMC Studio canvas has all nine blocks filled and mutually consistent, at least four blocks carry research-specific detail rather than the AI's generic draft, every block names a GenAI value-add, three high-priority assumptions are marked with a two-week test each, and every member contributed notes visible on the shared canvas.

> **Note:** A standalone copy of this lab is in labs/lab-06-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 7 — Design the Digital Architecture for Your Solution

Focus: design a digital architecture showing how AI technologies apply across the business.

Goal: Draw the end-to-end architecture for the solution across five layers, so the design shows data flow, integration points and governance controls rather than just a list of tool names.

**What you'll build**

A five-layer architecture diagram (data, model, orchestration, application, governance) with the integration pattern chosen and justified, and an explicit statement on whether confidential data leaves the organisation.   (Tools: Draw.io, Canva or a chat assistant with diagram output.)

**Step-by-step**

1. Choose your integration pattern: chat assistant, RAG over company documents, workflow automation, or autonomous agent. Write one line on why it fits your business idea.
2. DATA layer — list the actual data sources the solution needs, who owns each, and whether any holds personal or confidential data.
3. MODEL layer — name the model or service, and state whether data leaves your tenancy when it is called.
4. ORCHESTRATION layer — describe what connects data to model: the prompt, the retrieval step, the workflow tool or the agent logic.
5. APPLICATION layer — describe where the user actually interacts: a chat window, an intranet page, a Teams bot or an existing business system.
6. GOVERNANCE layer — add the controls: access rights, the human review point, logging, and what data must never enter the model. Draw all five layers with arrows for data flow and export the diagram.

**Test it**

Your diagram shows all five layers with data-flow arrows, names at least one specific control in the governance layer, and states explicitly whether confidential data leaves the organisation's boundary.

> **Note:** A standalone copy of this lab is in labs/lab-07-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 8 — Script a Marketing Video for Your Business Idea

Focus: chain generative AI tools into a repeatable content production process for the business.

Goal: STAGE 4 OF THE PIPELINE. Write and storyboard a 60-second video script for the researched idea, comparing how three different assistants handle the same creative brief.

**What you'll build**

A finished 60-second video script with a hook, three benefits and a call to action, broken into a 6-scene storyboard with visual direction and the exact voiceover line for each scene.   (Tools: ChatGPT, Google Gemini, Microsoft Copilot 365.)

**Step-by-step**

1. Write the creative brief first: the audience (from your canvas), the ONE message, the desired action, the tone, and the 60-second limit. A vague brief produces vague output from every tool.
2. Prompt all three assistants (ChatGPT, Gemini and Copilot 365) with the SAME brief: 'You are a marketing copywriter. Write a 60-second video script for <idea> aimed at <audience>. Open with a hook in the first 5 seconds, give three benefits, and close with the call to action <X>. Conversational tone. Mark the timing of each section.'
3. TIP — compare the three. ChatGPT tends to be the most creative, Gemini the most current (it can pull live web context), and Copilot 365 the most business-appropriate and able to draw on your own Microsoft 365 documents. Take the strongest hook from one and the clearest benefits from another — combining beats accepting any single draft.
4. Cut the script to 150 words maximum. Read it ALOUD with a stopwatch: 60 seconds of natural speech is about 150 words. If you cannot say it comfortably in time, it is too long — this is the most common failure in the next lab.
5. Ask an assistant to break the script into 6 scenes. For each scene record: the voiceover line, the visual description, and the on-screen text.
6. TIP — write visual descriptions for an AI video generator: name the SUBJECT, the SETTING, the CAMERA MOVE and the LIGHTING ('slow push-in on a young mother at a kitchen table, warm morning light'). 'A happy customer' is not enough for Kling to work with.
7. Sanity-check the script against your canvas: does the value proposition on screen match the one in your canvas? Fix whichever is wrong.

**Test it**

Your script reads aloud in 60 seconds or less, has a hook in the first five seconds, three clear benefits and one call to action, and your 6-scene storyboard gives each scene a voiceover line, a camera-ready visual description and on-screen text.

> **Note:** A standalone copy of this lab is in labs/lab-08-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 9 — Create the AI Voiceover

Focus: apply generative AI speech tools to produce a business-quality audio asset.

Goal: STAGE 5 OF THE PIPELINE. Turn the Lab 8 script into a natural-sounding voiceover with a text-to-speech tool, and learn the controls that separate a usable take from an obviously robotic one.

**What you'll build**

A clean 60-second voiceover audio file (MP3/WAV) of your script, with the voice, pace and emphasis deliberately chosen for your audience.   (Tools: ElevenLabs (recommended free tier), Microsoft Edge Read Aloud, Descript Overdub, or Google/Azure TTS.)

**Step-by-step**

1. Open ElevenLabs (elevenlabs.io) and sign up for the free tier, then go to Text to Speech.
2. Choose a voice that fits your audience and brand — listen to at least four before deciding. Age, accent and warmth all change how the message lands; a corporate B2B service and a children's education brand need different voices.
3. Paste your 150-word script and generate a first take. Listen critically for the words the model mispronounces or rushes.
4. TIP — punctuation IS your direction. A comma creates a short pause, a full stop a longer one, and an ellipsis... a dramatic beat. Break long sentences into short ones. Write numbers and acronyms the way you want them SAID ('twenty twenty-six', 'A-I') — this fixes most mispronunciation.
5. Adjust the stability and similarity settings: lower stability gives more emotional variation but less consistency; higher gives a steadier, flatter read. Regenerate until the take sounds natural.
6. TIP — ethics and law. Only clone a voice you own or have WRITTEN consent to use. Cloning a colleague's or a public figure's voice without permission is a legal and reputational risk, and disclosure is increasingly required. Check the licence terms before any commercial use.
7. Time the final take. If it runs over 60 seconds, cut words from the script rather than speeding up the voice — a rushed voiceover always sounds artificial. Download as MP3 and name it clearly.

**Test it**

Your voiceover plays cleanly, runs to 60 seconds or under, pronounces every product name and number correctly, and sounds natural when you play it to another learner.

> **Note:** A standalone copy of this lab is in labs/lab-09-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 10 — Generate the Background Soundtrack with Suno

Focus: apply generative AI music tools and handle the licensing of generated assets.

Goal: STAGE 6 OF THE PIPELINE. Create an original background track that supports the voiceover instead of competing with it, and check what the licence actually permits.

**What you'll build**

A 60-second background music track matched to the tone of your video, with its licence terms recorded.   (Tools: Suno (recommended), Udio, or an AI music generator of your choice.)

**Step-by-step**

1. Open suno.com and sign in with the free tier. Switch to Instrumental mode — a track with lyrics will fight your voiceover for the listener's attention.
2. Describe the music by GENRE, MOOD, INSTRUMENTATION and TEMPO, not by naming an artist: 'uplifting corporate acoustic, light piano and soft percussion, 90 BPM, warm and optimistic, no vocals'.
3. TIP — never prompt 'in the style of <artist>'. It produces derivative output and creates copyright exposure. Describe the SOUND you want instead; you will get a better and safer result.
4. Generate two or three variations and shortlist the one that matches your script's emotional arc. Play it UNDER your Lab 9 voiceover — the right track is one you stop noticing when the voice starts.
5. TIP — music must sit 15-20 dB below the voiceover. If you notice the music while listening to the words, it is too loud. Prefer tracks without a strong melody in the vocal frequency range.
6. Check and RECORD the licence terms for your free-tier output: whether commercial use is allowed, whether attribution is required, and who owns the track. Free-tier music is frequently non-commercial only — this matters before you publish.
7. Download the track and trim it to about 60 seconds to match the voiceover.

**Test it**

You have a 60-second instrumental track that fits your video's tone, sits comfortably under the voiceover when played together, and you can state exactly what its licence permits.

> **Note:** A standalone copy of this lab is in labs/lab-10-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 11 — Produce the Video with Kling and an AI Video Editor

Focus: combine multiple generative AI outputs into one finished business asset.

Goal: STAGE 7 OF THE PIPELINE. Generate the visual scenes from the Lab 8 storyboard, then assemble them with the Lab 9 voiceover and the Lab 10 soundtrack into a finished, captioned marketing video.

**What you'll build**

A finished 60-second marketing video combining AI-generated scenes, your AI voiceover, your AI soundtrack and captions — exported at 1080p.   (Tools: Kling AI (or Runway, Pika, Sora), CapCut or Descript, plus your Lab 9 and Lab 10 audio.)

**Step-by-step**

1. Open Kling AI (klingai.com) and sign in for free credits. Work from your Lab 8 storyboard, generating one clip per scene.
2. For each scene paste the visual description you wrote, naming subject, setting, camera move and lighting. Set the clip length to about 5 seconds and generate.
3. TIP — AI video generation is iterative and credit-limited. Expect to regenerate: hands, text and fast motion are the common failure points. Keep the camera move simple (slow push-in, gentle pan) — complex motion is where clips fall apart. Generate your most important scene first while you have credits.
4. TIP — keep visual consistency across scenes by reusing the same style words in every prompt ('warm morning light, shallow depth of field, cinematic'). Changing style between clips makes the video look assembled from stock rather than made for one brand.
5. Download the usable clips. Where a scene will not generate acceptably, substitute a still image from Firefly or Designer with a slow zoom — a clean still beats a broken clip.
6. Open CapCut (or Descript) and create a 1080p project. Import your clips, the Lab 9 voiceover and the Lab 10 soundtrack.
7. Lay the voiceover on the timeline FIRST, then cut the visuals to match it — the narration sets the pace, not the footage. Add the soundtrack on a separate track and lower it to 15-20 dB below the voice.
8. Add captions (CapCut auto-captions from the voiceover) and PROOFREAD them — auto-captions routinely mangle product names. Around 80% of social video is watched muted, so captions are not optional.
9. Add your on-screen text from the storyboard and a closing call-to-action frame. Export at 1080p and play it end to end.

**Test it**

Your exported video plays end to end at 1080p with synced visuals, an audible voiceover over quieter music, accurate captions and a clear call to action — and you can state which AI tool produced each element.

> **Note:** A standalone copy of this lab is in labs/lab-11-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 12 — Build the Business Presentation with Your Video

Focus: turn the work into a stakeholder-ready business case and communicate it.

Goal: Assemble everything from the pipeline — research, canvas, architecture and video — into a board-ready presentation that argues for the idea rather than merely describing it.

**What you'll build**

A published 10-slide business presentation with a share link, embedding your Lab 11 video and your Lab 6 canvas, ending with a clear ask.   (Tools: Gamma (recommended), Canva Presentations, or Microsoft Copilot in PowerPoint.)

**Step-by-step**

1. Open Gamma (gamma.app), create a free account and choose 'Generate a presentation from text'.
2. Paste a structured brief: the idea in one sentence, the Lab 3 market findings with sources, the Lab 4 score and why this idea won, the Lab 6 canvas summary, the Lab 7 architecture, and your ask.
3. TIP — Gamma writes better slides from a STRUCTURED brief than from a topic. Give it your actual findings and headings; give it only a topic and it returns generic filler you will have to delete.
4. Generate, then EDIT hard. Delete any slide that states a generic AI benefit and replace it with your own evidence. One idea per slide; no paragraphs.
5. Embed your Lab 11 video on its own slide, and place the Lab 6 canvas PNG on another. The video is your proof of execution — introduce it in one line so the audience knows what to watch for.
6. Add a slide with the measurable result you expect and the baseline you will compare against, then a final slide with a specific ask (budget, approval, or a pilot decision).
7. TIP — structure the argument as problem → evidence → solution → proof → ask. A deck that only describes the idea invites 'interesting, let us discuss later'; a deck that ends in a specific ask gets a decision.
8. Publish, copy the share link and present in 5 minutes. Take one challenge question and note how you would answer it with evidence.

**Test it**

Your deck has a working share link, plays the embedded video, shows the canvas, carries at least one verified source from Lab 3, and ends with a specific, decidable ask.

> **Note:** A standalone copy of this lab is in labs/lab-12-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


## Topic 03 — Implementing and Managing Business Innovation with Generative AI Tools

Best practices · legal, ethical and security issues · measuring success · stakeholder communication

**Key concepts**

- Implementation best practices — Start with a narrow high-value use case, keep a human in the loop, measure a baseline and scale only what works.
- Legal considerations — Copyright and training data, model output ownership, the EU AI Act and Singapore's PDPA obligations.
- AI ethics — Transparency, fairness, safety, explainability, privacy, security, responsibility, liability and auditability.
- Singapore governance — IMDA's Model AI Governance Framework and AI Verify give organisations a practical assurance toolkit.
- Security and data protection — Prompt injection, data leakage into public models, shadow AI and access control over AI systems.
- Measuring and reviewing success — Track adoption, cycle time, quality, cost per task and business outcome against the pre-AI baseline.
- Stakeholder communication — A communication plan, AI use policy and community of practice keep ideas flowing across the organisation.
- The AIM framework — Assess, Implement, Manage — a repeatable loop for running generative AI innovation.


### Lab 13 — Risk-Assess Your Generative AI Pipeline

Focus: identify and address legal, ethical and security issues in implementing business innovation with GenAI.

Goal: Run a structured risk assessment over the ACTUAL pipeline you built in Labs 3-12 — the research, canvas, script, voice, music, video and deck — and turn every finding into a named, owned control.

**What you'll build**

A risk register covering your own pipeline stage by stage: copyright, data protection, accuracy, disclosure and security, each with a specific control and an owner.   (Tools: Your Lab 3-11 artifacts, chat assistant, IMDA Model AI Governance Framework, PDPC guidelines.)

**Step-by-step**

1. Lay out your pipeline as a table with one row per stage: research (Lab 3), canvas (5), script (7), voiceover (8), music (9), video (10), deck (11). You are assessing what you actually built, not a hypothetical system.
2. COPYRIGHT AND OWNERSHIP — for each generated asset record who owns it and whether the free-tier licence permits commercial use. Check your Lab 10 music licence note and the Kling and ElevenLabs terms. Flag any asset you could NOT legally publish today.
3. ACCURACY — identify every factual claim in your video and deck. Which trace to a verified Lab 3 source, and which came from an AI draft nobody checked? An unverified statistic in a customer-facing video is the highest-likelihood failure in this pipeline.
4. DATA PROTECTION — list any personal data touched, and check handling against Singapore's PDPA obligations for consent, purpose and retention. Note anything you pasted into a public tool that should not have been.
5. DISCLOSURE — decide where you must tell the audience that content is AI-generated. Consider the AI presenter or cloned voice, generated imagery of 'customers', and the EU AI Act's transparency duties for synthetic media.
6. SECURITY — assess exposure to prompt injection (in a RAG or agent stage), confidential data leaking into a public model, shadow AI, and weak access control over the accounts holding your assets.
7. BIAS TEST — run the same prompt through your pipeline with two different demographic framings and compare the outputs for unjustified differences. Record the actual prompts and what you found.
8. For every red and amber finding write ONE specific control naming what changes, who owns it and how compliance is checked. A control that names no owner is a wish, not a control.

**Test it**

Every pipeline stage has at least one identified risk with a specific owned control, your bias test is recorded with the actual prompts used, and you can state which of your generated assets are and are not safe to publish commercially.

> **Note:** A standalone copy of this lab is in labs/lab-13-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 14 — Define Security Guardrails and AI Ethics Principles

Focus: establish the ethical principles and technical guardrails that govern generative AI use across the organisation.

Goal: Convert the risks found in Lab 13 into a working governance layer: the ethics principles the organisation commits to, and the concrete guardrails that enforce them in practice.

**What you'll build**

A one-page AI governance charter: eight ethics principles with what each means in practice, plus a guardrail table mapping each risk to an input, processing, output or human control.   (Tools: Chat assistant, IMDA Model AI Governance Framework, AI Verify, your Lab 13 risk register.)

**Step-by-step**

1. Adopt the eight AI ETHICS PRINCIPLES and write what each means concretely for YOUR pipeline: TRANSPARENCY (users know when AI is used), FAIRNESS (no unjustified bias against any group), SAFETY (the system behaves within intended bounds), EXPLAINABILITY (decisions can be understood and justified), PRIVACY (personal data protected and minimised), SECURITY (resists misuse and attack), RESPONSIBILITY (a named human owns each outcome), AUDITABILITY (decisions are logged and reviewable).
2. TIP — a principle without a behaviour is decoration. Write each as an observable commitment: not 'we value transparency' but 'every AI-generated video carries an on-screen AI-generated label and names the tools used in the description'.
3. INPUT GUARDRAILS — define what may never enter a prompt: personal data, customer records, unreleased financials, credentials, client-identifying material. State which tools are approved for which data classification.
4. PROCESSING GUARDRAILS — defend against prompt injection: treat all retrieved or uploaded content as untrusted, never let retrieved text change the system instruction, and restrict what tools an agent may call. This matters most for the Lab 18 agentic workflow.
5. OUTPUT GUARDRAILS — define what must be checked before anything is published: factual claims verified against a source, licence terms confirmed, brand and tone reviewed, and AI disclosure applied where required.
6. HUMAN-IN-THE-LOOP GUARDRAILS — decide exactly WHERE a human must approve. Rule of thumb: require human sign-off wherever output is customer-facing, carries legal or financial weight, or cannot be reversed. Name the approver role for each gate.
7. Map each Lab 13 risk to the guardrail that mitigates it in a table (risk → guardrail type → control → owner). Any risk with no guardrail is still open — say so rather than hiding it.
8. Write the one-page charter: the eight principles, the approved-tool list, the prohibited-data list, the disclosure rule, the human approval gates and where to ask for help.

**Test it**

Every principle is written as an observable behaviour, every Lab 13 red or amber risk maps to a named guardrail with an owner, and your human-approval gates are specific about who approves what before publication.

> **Note:** A standalone copy of this lab is in labs/lab-14-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 15 — Develop the Implementation Action Plan

Focus: apply best practices in the implementation process of business innovation, and develop a viable action plan in line with business strategy.

Goal: Convert the design and its governance into a costed, owned and sequenced 90-day plan a management team could approve and track.

**What you'll build**

A 90-day action plan with phased milestones, owners, resources, dependencies, a risk register and numeric go/no-go criteria.   (Tools: Excel or Google Sheets, chat assistant.)

**Step-by-step**

1. Define the scope of a 90-day pilot for your solution — narrow enough to finish, valuable enough to matter.
2. Break it into phases: prepare (weeks 1-2), build (3-6), pilot (7-10), review and decide (11-12).
3. For every milestone record the owner by role, the resource needed, the dependency and the completion date.
4. Carry the controls from Labs 13 and 14 into the plan as real work items with owners — governance that is not scheduled does not happen.
5. Add a risk register of at least five risks (data privacy, output accuracy, user adoption, cost overrun, vendor lock-in), each with a mitigation and an owner.
6. Use a chat assistant as a challenger: 'What is missing from this implementation plan, and what most commonly causes such pilots to fail?' Incorporate what is valid.
7. Define the week-12 go/no-go criteria as NUMBERS that would justify scaling, pausing or stopping.

**Test it**

Every milestone has a named owner role and date, the governance controls from Labs 13-14 appear as scheduled work, the risk register has five risks with mitigations, and the go/no-go criteria are numeric rather than subjective.

> **Note:** A standalone copy of this lab is in labs/lab-15-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 16 — Measure and Review Innovation Success

Focus: manage business innovation and review the success of its integration with business strategy.

Goal: Build the measurement system that shows whether the innovation actually worked, including the pre-AI baseline without which no improvement can be claimed.

**What you'll build**

A KPI dashboard defining baseline, target and review cadence across adoption, efficiency, quality, cost and business outcome, plus a counter-metric.   (Tools: Excel or Google Sheets, chat assistant.)

**Step-by-step**

1. Define your pre-AI baseline: how long the target task takes today, what it costs and its current quality. Without this, no improvement can be proven.
2. For your own pipeline this is concrete: how long did producing a marketing video take BEFORE (agency brief, shoot, edit) versus the hours it took you across Labs 8-11?
3. Set one KPI in each of five categories: adoption, efficiency, quality, cost and business outcome.
4. For every KPI record the definition, data source, baseline value, 90-day target and who reports it.
5. Add at least one COUNTER-METRIC that would reveal harm — error rate, customer complaints, brand-consistency failures or rework — so gains are not claimed at the expense of quality.
6. Build the dashboard with baseline, current and target columns and conditional formatting for on/off track.
7. Define the review cadence: what is reviewed weekly, what monthly, and what triggers escalation or a stop decision.

**Test it**

Every KPI has a real baseline number and a data source, at least one counter-metric is present, and your review cadence names who meets, how often and what decision they can make.

> **Note:** A standalone copy of this lab is in labs/lab-16-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 17 — Build the Stakeholder Communication and Idea-Sharing Plan

Focus: facilitate information flow among key stakeholders to empower sharing and development of innovative ideas.

Goal: Design how the innovation is communicated and how new ideas keep flowing after the pilot, so the initiative outlives its launch.

**What you'll build**

A stakeholder map, a tailored communication plan, the published one-page AI use policy, and a mechanism for capturing and triaging new ideas.   (Tools: Chat assistant, Gamma or Canva, Microsoft Teams or Slack.)

**Step-by-step**

1. Map your stakeholders on influence and interest: executive sponsors, affected staff, IT and security, legal and compliance, customers.
2. For each group define the message that matters to them, the channel, the frequency and the owner — an executive needs outcomes, an affected employee needs job impact.
3. Address the adoption concern directly: draft the honest message about what the AI will and will not change about people's jobs.
4. Publish the one-page AI use policy (derived from your Lab 14 governance charter) — approved tools, prohibited data, disclosure rules and where to ask for help — as the staff-facing artifact.
5. Design the idea-sharing mechanism: a channel, a monthly community-of-practice session and a simple intake form for new use cases.
6. Define how a submitted idea is triaged using the Lab 4 scoring rubric, so the pipeline stays consistent and fair.

**Test it**

Every stakeholder group has a tailored message, channel, frequency and owner; the AI use policy fits one page and names prohibited data; and a submitted idea has a defined path to evaluation.

> **Note:** A standalone copy of this lab is in labs/lab-17-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


### Lab 18 — CAPSTONE — Automate the Pipeline with an Agentic AI Workflow and Human Review

Focus: design and build an agentic workflow that automates the business innovation process end to end, with human review and governance built in.

Goal: The capstone. Everything you did by hand in Labs 3-12 becomes an automated agentic workflow — research, canvas, script, assets and deck — with a HUMAN REVIEW GATE before anything is published, and the Lab 14 guardrails enforced in the flow.

**What you'll build**

A working agentic workflow that takes a business idea as input, runs the research-to-content pipeline through AI agents, pauses for human approval, and delivers the finished asset set — with the run logged for audit.   (Tools: n8n (recommended), Make.com, Copilot Studio or Zapier; plus your Lab 3-11 tool accounts.)

**Step-by-step**

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

**Test it**

Your workflow runs from a submitted idea through research, evaluation, canvas and script; it PAUSES at the human review gate and only continues on approval; a rejection routes back without generating assets; every run is logged with the approver and timestamp; and you can point to where each Lab 14 guardrail is enforced.

> **Note:** A standalone copy of this lab is in labs/lab-18-*.md. Use non-confidential data throughout, and verify every AI-generated fact before relying on it.

---


## Putting It Together — The AIM Framework

The three topics form a single repeatable loop for running generative AI innovation in an organisation. Use it after the course to take any new idea from proposal to measured outcome.

**Assess**

- Investigate what is possible — the tool landscape and what comparable organisations have achieved (Labs 1-3).
- Evaluate each opportunity on business value, feasibility, data readiness, risk and strategic fit (Lab 4).
- Select the one or two opportunities that best match a stated organisational objective.

**Implement**

- Model the business case and design the solution with the Business Model Canvas and Design Thinking (Labs 5-7).
- Design the digital architecture across the data, model, orchestration, application and governance layers (Lab 8).
- Build the pilot and prove the integration pattern works (Labs 9-10).
- Plan the rollout with owners, milestones, risks and go/no-go criteria (Lab 11).

**Manage**

- Control the legal, ethical and security risks with named, owned controls (Labs 13-14).
- Measure against the pre-AI baseline, including a counter-metric that would reveal harm (Lab 14).
- Communicate with each stakeholder group and keep new ideas flowing into the pipeline (Lab 15).
- Review at the agreed cadence, then feed what you learn back into Assess.

---


## Glossary

- **Generative AI (GenAI)** — AI that creates new content — text, image, audio, video or code — from a prompt, rather than only scoring or classifying existing data.
- **Predictive AI** — AI that forecasts, scores or classifies based on patterns learned from historical labelled data.
- **Foundation model** — A large model pre-trained on a broad corpus that can be adapted to many downstream tasks.
- **Prompt** — The instruction and context given to a generative model to produce a desired output.
- **Token** — The unit of text a language model processes; models generate output one token at a time.
- **Hallucination** — Fluent, confident output from a model that is factually wrong — the reason a human review step is required.
- **RAG (Retrieval-Augmented Generation)** — Grounding a model's answers in your own documents by retrieving relevant content and supplying it with the prompt.
- **AI agent** — A system that plans and executes multi-step tasks using tools, rather than answering a single prompt.
- **Prompt injection** — An attack where hostile instructions hidden in content the model reads hijack its behaviour.
- **Shadow AI** — Staff using unapproved AI tools with company data, outside IT and compliance visibility.
- **Business Model Canvas (BMC)** — A nine-block visual template describing how an organisation creates, delivers and captures value.
- **Design Thinking** — A human-centred innovation method: Empathise, Define, Ideate, Prototype, Test.
- **Digital architecture** — The structured description of how data, models, orchestration, applications and governance fit together.
- **Baseline** — The pre-AI measurement of time, cost or quality, without which no improvement can be proven.
- **Counter-metric** — A measure tracked to reveal harm caused by an improvement — for example error or complaint rate.
- **AIM framework** — Assess, Implement, Manage — the repeatable loop for running generative AI business innovation.
- **Model AI Governance Framework** — IMDA's practical Singapore guidance for deploying AI responsibly, including generative AI.
- **AI Verify** — Singapore's AI governance testing framework and software toolkit for validating AI system behaviour.
- **PDPA** — Singapore's Personal Data Protection Act, governing consent, purpose, retention and protection of personal data.
- **EU AI Act** — The European Union's risk-based AI regulation, the first comprehensive AI law, including transparency duties.
