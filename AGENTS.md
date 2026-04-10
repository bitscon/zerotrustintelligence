# AGENTS

## Development Workflow - Website

The website has a dedicated development environment.

All agents MUST follow these rules:

1. Website changes MUST ONLY be made in:

   /dev/site/

2. The production site at:

   /htdocs/site/

   MUST NOT be modified by any agent.

3. The /dev/site/ directory is the ONLY location for:
   - layout changes
   - content updates
   - design refinements
   - UX adjustments

4. Deployment to production is handled manually by a human.

5. CI/CD pipelines should be ignored for website updates until further notice.

6. Any agent that modifies /htdocs/site/ directly is violating repository rules.

Repository note:
The current repository layout also contains the live site source in `/site/`. Until a human relocates production files into `/htdocs/site/`, agents MUST treat `/site/` as production-equivalent and MUST NOT modify it.

## Agent Working Directory Requirement

All agents MUST explicitly report their working directory:

1. Upon initialization or loading
2. When asked by the user
3. Before performing any file modifications

The response MUST clearly state the directory path being used.

Example:

"Current working directory: /dev/site/"

Agents operate from the repository root.

However:

- All website file modifications MUST target files under:

  /dev/site/

- The agent MAY operate from the repository root, but MUST:
  - explicitly confirm that all file paths are within /dev/site/
  - refuse to modify any file outside /dev/site/

If a requested change targets any path outside /dev/site/, the agent MUST:
- stop immediately
- report the violation
- ask for confirmation before proceeding
