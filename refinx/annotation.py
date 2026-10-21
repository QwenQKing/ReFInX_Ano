"""Refined task annotation: the fields the paper's metrics read, rewritten by the annotator model.

Each field is read by a metric (D1-D5). Add a field only together with the metric that reads it.
The original gold answer, accepted alternatives and required clarifications stay in the task data.
"""
from __future__ import annotations

from dataclasses import dataclass

CONSTRAINT_KINDS = ("entity", "time", "period", "metric", "accounting_scope", "unit_currency", "assumption")
FACT_KINDS = ("fact", "arithmetic")
RELATIONS = ("entity", "time", "metric_scope", "unit_currency", "input_result_use", "evidential_support")


@dataclass
class ContextConstraint:  # D1 CtxSat
    kind: str  # one of CONSTRAINT_KINDS
    requirement: str


@dataclass
class Fact:  # D3 FactAcc / ArithAcc; prerequisites for D4 LCDF
    id: str  # "F1", "F2", ...
    kind: str  # one of FACT_KINDS
    statement: str


@dataclass
class Dependency:  # D2 DepCov / DepValid; D4 LCDF
    id: str  # "D1", "D2", ...
    relation: str  # one of RELATIONS
    prerequisites: list[str]  # Fact ids
    requirement: str


@dataclass
class AnswerPoint:  # D1 ReqSat; D5 MainSupp
    id: str  # "A1", "A2", ...
    statement: str


@dataclass
class NumericTarget:  # D3 NumAcc
    description: str
    value: float
    unit: str
    tolerance: float


@dataclass
class Annotation:
    case_id: str
    model: str  # annotator model that produced this record
    context_constraints: list[ContextConstraint]
    facts: list[Fact]
    dependencies: list[Dependency]
    answer_points: list[AnswerPoint]
    numeric_targets: list[NumericTarget]
