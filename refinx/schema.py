"""Records passed between the ReFInx harness, the judge and the metrics.

Each field is read by a metric in the paper (RQ1-RQ8). Add a field only together with the metric that reads it.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Task:
    """One case of the evaluation inputs (data/tasks.json; see refinx/data.py)."""

    case_id: str
    query: str  # shown to the agent
    as_of: str  # information cutoff, UTC ISO 8601; shown to the agent
    language: str  # "zh" or "en"; picks the search language
    # Hidden from the agent, used only by the judge.
    terminal_action: str  # "answer" or "clarify"
    gold_answer: str
    accepted_alternatives: list[str]
    required_clarifications: list[str]


@dataclass
class ToolCall:
    name: str
    arguments: dict[str, Any]
    result: str  # exactly what the agent saw
    ok: bool  # RQ1 tool success / error rate


@dataclass
class Run:
    """One agent trajectory on one task; the counters feed RQ1 execution statistics."""

    case_id: str
    model: str
    final_answer: str  # "" when the agent produced none
    stop_reason: str  # "final", "budget" (an execution limit ended the run) or "error" (infrastructure failure)
    tool_calls: list[ToolCall]
    # Model outputs (thinking, text, tool calls) and the tool results it saw, in order;
    # read by the dependency, local-correctness and claim-support judges.
    trajectory: list[dict[str, Any]]
    model_turns: int
    latency_s: float
    prompt_tokens: int
    completion_tokens: int


@dataclass
class Judgment:
    """Trajectory-blind final-answer judgment for RQ4 AnsAcc."""

    case_id: str
    correct: Optional[bool]  # None = undecided: the judge refused or gave no parsable verdict
    reason: str


@dataclass
class UnitVerdict:
    """One judged annotation unit, keyed by its id in the refined annotation."""

    unit_id: str  # C1.. (context constraints, by position), A1.., F1.., D1..
    verdict: str  # allowed labels depend on the unit list it sits in, see UnitJudgment
    reason: str  # one sentence, for auditing the judge


@dataclass
class NumericValue:
    """The number the response gives for one numeric target; code compares it with the target."""

    unit_id: str  # N1.. (numeric targets, by position)
    value: Optional[float]  # None when the response states no value for this target
    reason: str


@dataclass
class Computation:
    """A stated computation replayed by code for D3 ReplayAcc."""

    expression: str
    stated_result: str
    reason: str


@dataclass
class ExtraClaim:
    """A substantive claim in the response that no answer point covers (D5 ExtraSupp)."""

    claim: str
    verdict: str  # "supported" or "unsupported" by the visible trajectory
    reason: str


@dataclass
class UnitJudgment:
    """Per-unit judgment of one run against its refined annotation (D1-D5; D6 is computed from it)."""

    case_id: str
    judge_model: str
    constraints: list[UnitVerdict]  # satisfied | violated | not_applicable -> D1 CtxSat
    # supported | unsupported | missing -> D1 ReqSat (delivered = supported + unsupported), D5 MainSupp
    answer_points: list[UnitVerdict]
    facts: list[UnitVerdict]  # correct | incorrect | not_observed -> D3 FactAcc/ArithAcc, D4 prerequisites
    dependencies: list[UnitVerdict]  # valid | invalid | not_covered -> D2 DepCov/DepValid, D4 LCDF, D6
    numeric_values: list[NumericValue]  # -> D3 NumAcc
    computations: list[Computation]  # -> D3 ReplayAcc
    extra_claims: list[ExtraClaim]  # -> D5 ExtraSupp, RespSupp_all, CSG_all


@dataclass
class AnsAccSummary:
    """AnsAcc with the counts the paper reports for every metric."""

    model: str
    judge_model: str  # runs/ is not in git, so the summary must say which judge produced it
    applicable: int  # tasks run
    unobservable: int  # runs that ended with stop_reason "error"
    undecided: int  # judgments with correct None
    adjudicated: int  # judgments with correct True or False
    correct: int
    ans_acc: Optional[float]  # correct / adjudicated
    coverage: float  # adjudicated / applicable
