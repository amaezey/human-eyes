# Quarterly Platform Review

This document exists to give four checks something to measure. Every corpus
document in `human-sourced` and `generated-ai` holds zero instances of the four
patterns below, which left their cut-offs unmeasurable rather than wrong. It sits
in `synthetic/` deliberately: it is hand-written, so it is evidence about whether
a detector fires, never about how often real prose produces the pattern.

## Platform priorities

- **Reliability:** the ingestion path drops messages under sustained load.
- **Latency:** the median response time has drifted upward for six weeks.
- Storage spend now exceeds compute spend for the first time this year.

## Where the work sits

Our data-driven approach to decision-making has produced a high-quality roadmap
that the cross-functional group can act on. The long-term plan is user-friendly
and cost-effective, and the day-to-day work is well-defined.

## Assessment notes

The passage demonstrates the author's understanding of the underlying material.
I can tell because the argument moves from evidence to claim without a gap.
In paragraph three the writer returns to the opening image, and the structure
reads as planned rather than discovered.

## Team allocations

- Platform reliability work for backend teams
- Interface refinement work for frontend teams
- Documentation and support work for platform teams

The three lines above run to the same length and share both an opening and a
closing token, which is the combination the symmetry check looks for. A list that
merely runs long, or merely repeats one word, is left alone.
