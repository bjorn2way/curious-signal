---
title: "Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley"
date: 2026-07-29 19:33:54 +0700
section: Research Summary
section_slug: research-summary
description: "Summary: Agents and Ontologies Neuro Symbolic AI Source: Transcript of a presentation by Frank Coyle Educator, Berkeley Topic: Integrating Large Language Model LLM agents with formal ontologies to create robust, \"neuro symbolic\" AI systems."
audio: /audio/2026/07/why-agentic-systems-need-ontologies-frank-coyle-uc-berkeley.mp3
duration: "3 min 9 sec"
read_time: "5 min"
primary_source: https://www.youtube.com/watch?v=Sir59K8ZDPU
signal:
  - "Core Thesis"
  - "Key Concepts & Definitions"
  - "A. Ontologies (Symbolic AI)"
---
**Source:** Transcript of a presentation by Frank Coyle (Educator, Berkeley)
**Topic:** Integrating Large Language Model (LLM) agents with formal ontologies to create robust, "neuro-symbolic" AI systems.

## 1. Core Thesis
The convergence of probabilistic AI (LLMs/Agents) and symbolic AI (Ontologies/Knowledge Graphs) creates **Neuro-Symbolic AI**. This architecture uses ontologies to provide "guardrails" for LLMs, mitigating hallucinations and ensuring logical consistency, while LLMs provide the flexible reasoning and natural language interface.

## 2. Key Concepts & Definitions

### A. Ontologies (Symbolic AI)
*   **Definition:** A formal specification of a shared conceptualization. It represents entities, their properties, and their relationships.
*   **Structure:** Graph-based (nodes and edges), superior to relational databases for flexible schema evolution (no need to redefine columns for new attributes).
*   **Construction Approaches:**
    *   **Top-Down:** Experts define domain entities and relationships (e.g., traditional expert systems).
    *   **Bottom-Up:** Entities are derived from data sources (e.g., customer reactions, logs).
*   **Existing Standards:** Do not reinvent the wheel. Leverage existing taxonomies:
    *   `schema.org` (general web data)
    *   `FOAF` (social networks)
    *   `Dublin Core` (academic/media metadata)
    *   `DBpedia` (Wikipedia’s underlying graph)

### B. Agents (Probabilistic AI)
*   **Definition:** Systems that perceive, decide, and act.
*   **Mechanism:** Operate via **loops** (Sequence, Conditionals, Iteration). This makes them Turing-complete.
*   **Limitation:** LLMs are "locked in a box"; they cannot execute code or tools directly. They only predict the next word. They must output *parameters* for tools to be executed by external code.

### C. Neuro-Symbolic Integration
*   **The Problem:** LLMs are probabilistic and prone to "hallucinations" (which the speaker argues is a feature of imagination, but a bug for strict logic).
*   **The Solution:** Use ontologies to validate LLM outputs. The ontology acts as a validator/reasoner to check if the LLM’s proposed action or data is logically consistent with the domain rules.

## 3. Technical Architecture & Implementation

### The Agent Loop with Ontological Guardrails
The speaker proposes a specific loop structure for building reliable agents:

1.  **LLM Prompting:** The agent receives a prompt and a tool definition.
2.  **Tool Parameter Generation:** The LLM determines the necessary parameters for a tool but does *not* execute it. It returns a structured request.
3.  **Validation (The "Ontology at the Ledger" Step):**
    *   Before execution, the tool parameters and expected outputs are validated against the ontology.
    *   **Role of RDFS/OWL:** These technologies sit "on the side" of the graph to enforce constraints and enable inference.
4.  **Execution:** If validation passes, the tool is executed. If it fails, the loop continues or a human is alerted.

### Key Technologies Mentioned
*   **Pydantic:** Used for **input validation** ("Pydantic at the door"). It enforces strict typing in Python (which is otherwise untyped), ensuring the LLM’s output parameters match expected data types before they reach the ontology layer.
*   **RDFS (RDF Schema):** Defines basic constraints like **Domain** and **Range**.
    *   *Example:* If `teaches` has domain `Teacher` and range `Student`, and the LLM says "Bob teaches Scooter," the system infers Bob is a Teacher and Scooter is a Student.
*   **OWL (Web Ontology Language):** Provides advanced logical reasoning capabilities.
    *   **Transitive Properties:** If A is ancestor of B, and B is ancestor of C, then A is ancestor of C.
    *   **Functional Properties:** Enforces uniqueness (e.g., a person has only one father). If the LLM suggests two different fathers for one person, the ontology flags a contradiction.
    *   **Disjoint Properties:** Ensures entities are mutually exclusive (e.g., a `Customer` cannot be a `SupportRep`). This catches errors like sending a refund to a support desk instead of the buyer.

## 4. Risks & Challenges
*   **Infinite Loops:** Agentic loops can drift or become infinite, consuming tokens and money.
*   **Hallucinations:** LLMs may generate plausible but factually incorrect or logically invalid data.
*   **Side Effects:** Agents should ideally be designed to have **no side effects** until validated. Changes to databases should only occur after ontological verification.
*   **Scalability of Symbolic AI:** Historical "Expert Systems" failed to scale due to manual knowledge engineering. The new approach mitigates this by using LLMs to help populate or navigate the ontology, rather than relying solely on manual rule creation.

## 5. Notable Implementation Guidance
1.  **Separate Concerns:** Use Pydantic for type checking (input) and Ontologies for logical validation (output/constraints).
2.  **Leverage Existing Ontologies:** Utilize `schema.org`, `DBpedia`, etc., rather than building from scratch.
3.  **Human-in-the-Loop:** If the ontology validator rejects an LLM’s proposal, route to a human or a retry mechanism.
4.  **Philosophy:** "Nothing is a mistake... there is only make." Encourage iterative building and learning by doing, rather than just reading.
5.  **Cognitive Engagement:** The speaker advocates for handwritten notes and drawing to engage sensory systems for better learning, contrasting with typing.

## 6. Resources & Contact
*   **Speaker:** Frank Coyle
*   **Email:** coil@berkeley.edu (Note: Transcript says "burkly", context implies Berkeley)
*   **Website:** codesupreme.ai
*   **Key Takeaway:** Use ontologies to keep LLMs "on their guardrails."

<details class="evidence-drawer" markdown="1">
<summary>Evidence note</summary>

The source registry contains one readable HTTP source. No private source fields are rendered.

</details>

## Sources

- [Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley](https://www.youtube.com/watch?v=Sir59K8ZDPU)
