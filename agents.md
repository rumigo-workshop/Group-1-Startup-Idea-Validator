# AGENTS.md

## 1. Project Overview & Tech Stack
- **Architecture:** [e.g., Next.js App Router frontend + FastAPI backend]
- **Package Manager:** Always use `[pnpm / uv / poetry]` — never mix `npm` or `yarn` lockfiles.
- **Key Directories:**
  - `/src/app` — Routing and UI views
  - `/src/services` — Business logic and external API calls
  - `/tests` — Unit and integration tests

## 2. Build, Lint & Test Commands
Run these commands to verify changes before finishing a task:
- **Install dependencies:** `[pnpm install]`
- **Run dev server:** `[pnpm dev]`
- **Typecheck:** `[pnpm typecheck]`
- **Lint & Format:** `[pnpm lint]`
- **Run tests:** `[pnpm test]` (Run single test file: `[pnpm test path/to/file.test.ts]`)

## 3. Code Style & Conventions
- **Strict Typing:** Avoid `any` in TypeScript / use type hints on all Python function signatures.
- **Error Handling:** Never swallow errors silently; log context and return structured error responses.
- **Imports:** Use path aliases (`@/components/...`) instead of deep relative paths (`../../../`).
- **Component/Function Size:** Keep functions focused; extract reusable logic into helper modules rather than duplicating code.

## 4. Git & Workflow Guardrails
- **Branching:** Never commit directly to `main`. Create feature branches or work on the active branch (`ai-workflows`).
- **Destructive Actions:** Never run `git push --force`, `rm -rf` on project directories, or database reset scripts without explicit user confirmation.
- **Environment Files:** Never read, print, or commit `.env` files or API keys. Use `.env.example` for reference.

## 5. Agent Behavior Rules
- **Verify Before Finishing:** After editing code, always run the typechecker and relevant test suite to confirm nothing broke.
- **Minimal Diffs:** Only modify files directly related to the task. Do not reformat unrelated files.
- **Ask When Ambiguous:** If requirements conflict or database schema migrations are needed, pause and ask before applying changes.