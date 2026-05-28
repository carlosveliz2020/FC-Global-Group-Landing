---
name: create-skill
description: Build a new Claude Code skill from scratch. Use when the user wants to create a reusable slash command or workflow for Claude Code.
metadata:
  trigger: Creating a skill, slash command, or reusable workflow for Claude Code
  author: FC Global Group
---

# Create Skill

Build a Claude Code skill: a reusable slash command that packages a workflow, ruleset, or process into an invocable command.

## What a Skill Is

A skill is a folder with a `SKILL.md` file at its root. Claude Code reads it when the user types `/<skill-name>`. The file tells Claude what to do, what rules to follow, and what output to produce.

Skills live in:
- `~/.claude/skills/<skill-name>/` — global, available in all projects
- `.claude/skills/<skill-name>/` — local, scoped to the current project

## Process

### 1. Clarify intent

Before writing anything, answer these questions:

- What does the skill do in one sentence?
- When should it trigger? (specific user action, file type, content type)
- What does the output look like? (rewritten text, generated code, a report, a plan)
- Does it need reference files or is the SKILL.md self-contained?

### 2. Write the SKILL.md

Follow this structure exactly. See [references/template.md](references/template.md).

**Required frontmatter:**
```yaml
---
name: skill-name          # used as /skill-name in chat
description: One sentence. What it does. When to use it.
metadata:
  trigger: Specific trigger condition
  author: Name or org
---
```

**Required body sections:**
- `# Title` — matches the name
- `## What this does` — one paragraph, concrete
- `## Process` or `## Rules` — numbered steps or rule list
- `## Output` — describe what Claude produces
- `## Quick Checks` — short checklist before delivering output (optional but recommended)

### 3. Add reference files (when needed)

If the skill has lists, tables, or long reference material that would bloat SKILL.md, put them in `references/`. Link to them from SKILL.md with relative paths.

```
skill-name/
├── SKILL.md
└── references/
    ├── rules.md
    ├── examples.md
    └── checklist.md
```

### 4. Install and test

```bash
# Global install
cp -r skill-name/ ~/.claude/skills/

# Local install
cp -r skill-name/ .claude/skills/
```

Then type `/<skill-name>` in Claude Code to verify it loads and runs correctly.

## Rules for Writing Good Skills

1. **One skill, one job.** A skill that does three things does none of them well. Split complex workflows into focused skills that can chain.

2. **Describe output, not just process.** Tell Claude what the result looks like. "Produce a numbered list of X" beats "analyze and report on X."

3. **Write rules as constraints, not suggestions.** "Never use passive voice" beats "try to avoid passive voice." Claude follows hard rules.

4. **Use examples.** Before/after pairs in `references/examples.md` do more work than three paragraphs of explanation.

5. **Name the trigger exactly.** Vague triggers ("use when writing") cause the skill to run when it shouldn't. Specific triggers ("use when the user pastes prose for review") fire at the right moment.

6. **Keep SKILL.md under 200 lines.** Long files dilute focus. Move bulk content to reference files.

7. **Test with a real input.** Run the skill on actual content before shipping. A skill that works in theory but fails on real inputs is broken.

## Quick Checks

Before delivering the skill:

- Does the frontmatter have `name`, `description`, and `metadata.trigger`?
- Is the description one sentence that explains what + when?
- Are the rules written as hard constraints, not suggestions?
- Is the output section concrete enough that Claude knows what to produce?
- Does the skill name conflict with any built-in Claude Code command?
- Is the folder named exactly the same as `name` in the frontmatter?
- Did you test it with `/skill-name` in Claude Code?

## Examples

See [references/examples.md](references/examples.md) for complete before/after skill examples.
See [references/template.md](references/template.md) for a blank starter template.
