# Telegram behavior contract

Telegram is an optional coordination surface. Runtime configuration and actual live behavior must be verified separately.

## Surface roles

- HAKU/default: unrestricted orchestrator in the approved war room.
- Workers: mention-only or direct-reply participants by default.
- Status channel: concise lifecycle updates only.
- Task topics: isolated work for large, risky, or multi-phase tasks.

## Routing rules

- Only the explicitly targeted worker should answer a worker mention.
- Unmentioned workers may observe/react but should not add text noise.
- Bot-to-bot messages must have an explicit target and one intent.
- Use queue semantics within a topic; do not interrupt an active turn.
- Anchor answers to the triggering message when the adapter supports it.

## Reactions

Use a supported Telegram reaction set and verify it against the live Bot API before rollout:

- `👀` observed/explicitly targeted
- `🤔` received/listening, not targeted
- `⚡` actively processing
- `✅` completed successfully

An absent reaction is not automatically a dead worker. Check intake and adapter capability evidence first.

## Topics and titles

Session titles and Telegram topic names are separate state. A topic rename requires the adapter's topic-edit operation and permission. Never rename General/root or a topic outside the approved DM/forum scope. Auto-title behavior must preserve operator-declared topic bindings and avoid renaming a topic bound to another session.

## Noise controls

Prefer queue mode and disable busy acknowledgements when the user wants a quiet war room. Tool-progress rendering, native Telegram interim output, reasoning display, and plugin suppression are separate settings; report stored versus effective behavior.

The portable Hermes baseline in `../templates/hermes/config.common.yaml`
defines the shared progress-tail surface: live-tail strategy, five-second
edits, bounded tool/delegate/reasoning/background sections, rich Telegram
tables, native-notify suppression, and sticky todo summaries. Role overlays
change only identity and admission semantics: HAKU is free-response while
Shiro/dev workers remain mention/reply gated. Do not copy a private
`config.yaml` wholesale; preserve each profile's model, provider catalog,
credentials, chat allowlists, and role identity.

## Verification

A live claim requires adapter logs or a bounded Telegram smoke proving the exact target, topic, reply anchoring, reaction, and answer-authority behavior. Config presence alone is not runtime proof.
