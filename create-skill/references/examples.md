# Skill Examples

## Example 1: Bad skill → Good skill

### Bad (vague, no output definition)

```
---
name: improve-text
description: Makes text better.
---

# Improve Text

Use this to improve any text the user gives you. Make it clearer and more readable.
Fix grammar and style issues.
```

**Problems:**
- Description says nothing about when to use it
- "Makes text better" is not a rule
- No output format defined
- No checklist or process

---

### Good (specific, constrained, output-defined)

```
---
name: plain-english
description: Rewrite technical documentation for a non-technical audience. Use when the user shares docs, READMEs, or specs that need simplification.
metadata:
  trigger: User pastes technical documentation for simplification
  author: FC Global Group
---

# Plain English

Rewrite technical content so a non-technical reader understands it in one pass.

## Rules

1. **No jargon without definition.** Every technical term gets one-sentence plain definition on first use.
2. **Short sentences.** 20 words max per sentence. Split anything longer.
3. **Active voice only.** "The system sends a request" beats "A request is sent."
4. **Concrete examples.** Replace abstractions with a real-world analogy or use case.
5. **Cut preamble.** No "In order to understand X, we must first consider Y."

## Output

Rewritten text in the same structure (headers, sections) as the original.
Below the rewrite: a short changelog listing what was changed and why.

## Quick Checks

- [ ] Any term used without definition?
- [ ] Any sentence over 20 words?
- [ ] Any passive voice left?
- [ ] Any section that says nothing concrete?
```

---

## Example 2: Single-purpose skill with reference files

### Skill for code review comments

```
---
name: review-comment
description: Write a single inline PR review comment. Use when the user wants to give feedback on a specific line of code.
metadata:
  trigger: User wants to leave a code review comment on a PR
  author: FC Global Group
---

# Review Comment

Write one inline code review comment: specific, actionable, respectful.

## Rules

1. **One issue per comment.** If you see two problems, write two comments.
2. **State the fix, not just the problem.** "Consider using X instead" beats "This is wrong."
3. **No passive aggression.** No "Why would you..." or "This makes no sense."
4. **Link to docs when relevant.** If a standard applies, cite it.

## Process

1. Identify the specific issue on the specific line
2. Name the problem in one clause
3. Propose the fix in the next clause
4. Add a reference link if applicable

## Output

A single paragraph, 1-3 sentences. No headers. No bullet points.

## Examples

See [references/comment-examples.md](references/comment-examples.md).
```

---

## Example 3: Skill that chains with another skill

```
---
name: draft-and-polish
description: Write a first draft then immediately apply stop-slop rules. Use when the user wants clean AI-free prose from scratch.
metadata:
  trigger: User asks for a written piece from scratch
  author: FC Global Group
---

# Draft and Polish

Write the draft, then run /stop-slop rules on it before delivering.

## Process

1. Write the first draft based on the user's brief
2. Apply all stop-slop rules (see stop-slop/SKILL.md for full ruleset)
3. Score the result — if below 35/50, revise before delivering
4. Deliver the clean version only

## Output

Final polished text only. No drafts shown. Include the score (e.g. "Score: 41/50").
```
