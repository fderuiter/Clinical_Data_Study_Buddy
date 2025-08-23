# Contributor Guide: An Agile Framework for Issues

This document outlines a metadata-driven system for managing our work, inspired by Agile methodologies. Every work item, from a high-level strategic goal to a small technical task, is a Markdown file in this directory. The relationships between them are defined by metadata in each file's YAML frontmatter.

## The Hierarchy of Work

Work is broken down into a clear hierarchy. An item's position in this hierarchy is defined by its `type`.

| Level | Type | Description | Timeframe |
| :--- | :--- | :--- | :--- |
| **Highest** | `Theme` | A high-level strategic business goal. | Quarters / Years |
| | `Initiative` | A collection of epics to achieve a theme. | Months / Quarters |
| | `Epic` | A large feature or body of work. | Weeks / Months |
| | `User Story`| A small piece of user-facing functionality. | Days / Weeks |
| | `Task` | A specific technical action for the dev team. | Hours / Days |
| **Lowest** | `Sub-task` | A granular step within a task. | Minutes / Hours |

### Other Work Types

Some work doesn't fit neatly into the hierarchy but is equally important.

| Type | Description |
| :--- | :--- |
| `Bug` | An error or flaw in the existing product. |
| `Spike` | A research task to investigate a technical question. Usually time-boxed. |
| `Chore` | Work necessary for codebase health (e.g., refactoring, CI/CD improvements). |

---

## YAML Frontmatter Structure

The metadata for each work item is defined in a YAML block at the top of the file.

```yaml
---
title: "A concise, descriptive title"
type: "Theme" | "Initiative" | "Epic" | "User Story" | "Task" | "Sub-task" | "Bug" | "Spike" | "Chore"
parent: "optional-path/to/parent-file.md"
dependencies:
  - "optional-path/to/dependency-1.md"
  - "optional-path/to/dependency-2.md"
state: "backlog" | "todo" | "in-progress" | "in-review" | "done" | "closed"
labels:
  - "frontend"
  - "backend"
  - "priority-high"
assignees:
  - "GitHubUsername"
---
```

### Key Fields Explained

-   **`type`** (Required): The most important field. It defines the item's level in the Agile hierarchy.
-   **`parent`** (Optional): The filename of the parent work item. This is how the hierarchy is built. For example, the `parent` of a `Task` should be a `User Story`. A `Theme` would have no `parent`.
-   **`dependencies`** (Optional): A list of filenames for work items that must be completed *before* this one can start. This allows for creating a task graph that is independent of the hierarchy.
-   **`state`**: The current status of the work item.
-   **`labels`**: For categorizing work (e.g., by team, component, priority).
-   **`assignees`**: The person or people responsible.

### `User Story` Format

When an item has `type: User Story`, its description in the Markdown body **must** follow this format:
> As a **[type of user]**, I want **[to perform some action]** so that **[I can achieve some goal]**.

---

## Example in Practice

Here's how the hierarchy might look for a fictional project.

**File: `00-theme-improve-customer-retention.md`**
```yaml
---
title: "Improve Customer Retention"
type: "Theme"
state: "backlog"
---
```

**File: `01-initiative-launch-loyalty-program.md`**
```yaml
---
title: "Launch a Customer Loyalty Program"
type: "Initiative"
parent: "00-theme-improve-customer-retention.md"
state: "backlog"
---
```

**File: `02-epic-build-rewards-system.md`**
```yaml
---
title: "Build a Points-Based Rewards System"
type: "Epic"
parent: "01-initiative-launch-loyalty-program.md"
state: "todo"
---
```

**File: `03-story-view-points-balance.md`**
```yaml
---
title: "View Points Balance"
type: "User Story"
parent: "02-epic-build-rewards-system.md"
state: "todo"
assignees:
  - "Jules"
---

As a **registered customer**, I want **to see my current points balance on my profile page** so that **I know how close I am to a reward**.
```

**File: `04-task-create-api-endpoint.md`**
```yaml
---
title: "Create API endpoint for points balance"
type: "Task"
parent: "03-story-view-points-balance.md"
state: "in-progress"
assignees:
  - "Jules"
---
```

**File: `05-task-add-points-to-ui.md`**
```yaml
---
title: "Add points balance to profile page UI"
type: "Task"
parent: "03-story-view-points-balance.md"
dependencies:
  - "04-task-create-api-endpoint.md"
state: "todo"
assignees:
  - "Jules"
---
```
