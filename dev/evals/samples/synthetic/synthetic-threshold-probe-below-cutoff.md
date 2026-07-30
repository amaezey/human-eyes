# Release Notes, Week 12

The companion to `synthetic-threshold-probe-at-cutoff.md`. That document sits at
each cut-off; this one sits one step below, so the declaration test can see the
flag turn on between them instead of assuming it does. Hand-written, and in
`synthetic/` for the same reason: it shows a detector's boundary, not a rate in
real prose.

## Changes

- **Caching:** the layer now expires entries on write rather than on a timer.

Everything else this week was routine. The scheduler picked up two configuration
fixes, and the queue drain that had been running long since March finished inside
its window twice.

## Review note

The passage demonstrates the author's understanding of the constraint, and I can
tell because the second paragraph names the tradeoff instead of restating the
goal. Nothing else in the review needed a second pass.

In paragraph two the constraint is stated once and not returned to, which is the
right call for a note this short.

Support volume held flat. The one escalation resolved without a rollback, which
is the first time that has happened this quarter.
