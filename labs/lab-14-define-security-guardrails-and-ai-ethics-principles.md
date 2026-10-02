# Lab 14 — Define Security Guardrails and AI Ethics Principles

**Course:** Business Transformation with AI Agents (C997)  
**Topic 03:** Implementing and Managing Business Innovation with Generative AI Tools  
**Focus:** establish the ethical principles and technical guardrails that govern generative AI use across the organisation.  
**Tools:** Chat assistant, IMDA Model AI Governance Framework, AI Verify, your Lab 13 risk register

## Goal

Convert the risks found in Lab 13 into a working governance layer: the ethics principles the organisation commits to, and the concrete guardrails that enforce them in practice.

## What you'll build

A one-page AI governance charter: eight ethics principles with what each means in practice, plus a guardrail table mapping each risk to an input, processing, output or human control.

## Before you start

- Sign in to the tools listed above with your own free-tier account.
- Use fictitious or non-confidential material only — never enter personal, client or commercially sensitive data into a public generative AI tool.
- Verify every AI-generated fact, figure and citation before you rely on it.

## Step-by-step

1. Adopt the eight AI ETHICS PRINCIPLES and write what each means concretely for YOUR pipeline: TRANSPARENCY (users know when AI is used), FAIRNESS (no unjustified bias against any group), SAFETY (the system behaves within intended bounds), EXPLAINABILITY (decisions can be understood and justified), PRIVACY (personal data protected and minimised), SECURITY (resists misuse and attack), RESPONSIBILITY (a named human owns each outcome), AUDITABILITY (decisions are logged and reviewable).
2. TIP — a principle without a behaviour is decoration. Write each as an observable commitment: not 'we value transparency' but 'every AI-generated video carries an on-screen AI-generated label and names the tools used in the description'.
3. INPUT GUARDRAILS — define what may never enter a prompt: personal data, customer records, unreleased financials, credentials, client-identifying material. State which tools are approved for which data classification.
4. PROCESSING GUARDRAILS — defend against prompt injection: treat all retrieved or uploaded content as untrusted, never let retrieved text change the system instruction, and restrict what tools an agent may call. This matters most for the Lab 18 agentic workflow.
5. OUTPUT GUARDRAILS — define what must be checked before anything is published: factual claims verified against a source, licence terms confirmed, brand and tone reviewed, and AI disclosure applied where required.
6. HUMAN-IN-THE-LOOP GUARDRAILS — decide exactly WHERE a human must approve. Rule of thumb: require human sign-off wherever output is customer-facing, carries legal or financial weight, or cannot be reversed. Name the approver role for each gate.
7. Map each Lab 13 risk to the guardrail that mitigates it in a table (risk → guardrail type → control → owner). Any risk with no guardrail is still open — say so rather than hiding it.
8. Write the one-page charter: the eight principles, the approved-tool list, the prohibited-data list, the disclosure rule, the human approval gates and where to ask for help.

## Test it

Every principle is written as an observable behaviour, every Lab 13 red or amber risk maps to a named guardrail with an owner, and your human-approval gates are specific about who approves what before publication.

## What you learned

- Establish the ethical principles and technical guardrails that govern generative AI use across the organisation.
- You produced: A one-page AI governance charter: eight ethics principles with what each means in practice, plus a guardrail table mapping each risk to an input, processing, output or human control.
- You practised verifying and challenging AI output rather than accepting the first draft.

---

*Business Transformation with AI Agents · C997 · Tertiary Infotech Academy Pte Ltd · Version v1.0*
