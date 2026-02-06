---
name: parking-lot-consensus
description: "Use this tool when you are NOT confident with a specific implementation plan, or when a request requires complex architectural reasoning before coding. This tool facilitates an internal debate to reach a high-confidence solution."
---

# Parking Lot Consensus Skill

This skill helps refine complex implementation plans or architectural decisions by simulating a debate between two AI agents and a judge. It aims to achieve a high-confidence solution through iterative critique and problem-solving.

## Usage

To use this skill, provide your initial plan or query as input. The skill will then simulate a "parking lot" debate, offering critiques and proposing solutions until a confidence score of 90% or higher is reached, or a maximum number of retries is met.

```bash
python scripts/consensus.py "{USER_QUERY}"
```