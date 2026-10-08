---
name: telegram-war-room
description: Use when Hermes agents coordinate through Telegram groups, forum topics, DM topics, reactions, or multi-bot war rooms.
version: 1.0.0
author: Haku Co-Agent Harness
license: MIT
metadata:
  hermes:
    tags: [telegram, topics, reactions, multi-bot, queue]
    related_skills: [haku-coagent-core]
---

# Telegram War Room

## Default behavior

- HAKU/default is the unrestricted orchestrator in the approved war room.
- Workers answer only when explicitly mentioned or directly replied to.
- Only the explicitly targeted bot produces a text answer; unmentioned workers may observe/react.
- Bot-to-bot messages use an explicit target and one intent.
- Within one topic, use queue semantics and one active directed turn; avoid interrupt churn.

## Liveness reactions

Use Telegram-supported reactions after live API verification:

- `👀` observed/targeted
- `🤔` listening/not targeted
- `⚡` processing
- `✅` completed

Check intake logs and adapter capability before classifying a missing reaction as a dead worker.

## Topics and replies

Keep session titles separate from Telegram topic names. Topic rename requires a concrete non-root thread, correct chat scope, permission, and an adapter `editForumTopic`/rename operation. Preserve explicit bindings and never rename General/root.

Anchor the response to the triggering message when supported. Strip noisy runtime footers before deciding whether a bot-origin message contains a valid directed call.

## Noise controls

Prefer `busy_input_mode: queue` and `busy_ack_enabled: false` for quiet coordination. Treat native Telegram output, progress-tail output, plugin suppression, and final replies as separate behavior surfaces; verify effective behavior, not YAML alone.
