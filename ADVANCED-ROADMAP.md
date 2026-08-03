# Advanced Python Roadmap

A 60-day advanced track, broken into **12 components**. Built for someone who
already knows Python syntax and now wants the depth that production and senior
interviews actually test: the data model, typing, concurrency after the GIL,
memory, and architecture.

Targets **Python 3.12+**, with 3.13/3.14 features (free-threading,
subinterpreters, JIT) called out where relevant.

---

## How to use this

- **One day = one focused session** (60–120 min). Days are sequenced; components
  are mostly independent after C02.
- **Every day ends in a file, not a feeling.** If you cannot point at code you
  wrote, the day is not done.
- **Write assertions, not prints.** `assert cache.hits == 2` fails loudly when
  you are wrong. `print(cache.hits)` with the answer in a comment does not.
- **One exercise per topic.** Add an `exercises.py` with 3 failing asserts you
  have to make pass. Recall beats recognition.
- **Benchmark claims.** Any day that says "faster" or "less memory" needs a
  `timeit` or `tracemalloc` number next to it.

### Suggested layout

```
advanced/
├── 01-tooling-baseline/
├── 02-typing/
├── 03-data-model/
├── 04-iteration-functional/
├── 05-data-modeling/
├── 06-memory-performance/
├── 07-concurrency-threads/
├── 08-concurrency-async/
├── 09-testing-quality/
├── 10-architecture/
├── 11-production/
└── 12-capstone/
```

Each component folder gets a `README.md` (what you learned, in your own words),
numbered lesson files, and `exercises.py`.

---

## Prerequisites

You should be comfortable with these before Day 1. All exist in this repo
already, though several need repair first — see the audit canvas.

| Prerequisite | Repo folder | Status |
| --- | --- | --- |
| Functions, closures, decorators | `functions/` | Solid |
| Dunder methods, protocols | `dunder-methods/` | Deep — your strongest area |
| Classes, inheritance, `super()` | `oop-basics/` | Thin — no `@property`, no ABCs |
| Lists, dicts, sets, comprehensions | `data-structures/` | Solid — no tuples/`collections` |
| `try`/`except`/`else`/`finally` | `error-handling/` | Thin — no custom exceptions |
| Threading, multiprocessing, asyncio intro | `concurrency/` | Conceptual only |
| Imports and packages | `modules-imports/` | Solid |
| pytest can run | `testing/` | **Broken — fix first** |

> **Fix before Day 1:** `testing/test_calculator.py` does not import its subject
> (both tests fail), `loops-conditionals/for_loop.py` is empty,
> `error-handling/one_line_multiple.py` catches a misspelled `TyypeError`, and
> `clean-architecture/solution_depedency_inversion.py` stores the abstract class
> instead of the injected dependency. Roughly one evening of work.

---

## The 12 components

| # | Component | Days | Why it matters |
| --- | --- | --- | --- |
| C01 | [Modern Baseline & Tooling](#c01--modern-baseline--tooling) | 1–4 | uv, ruff, mypy, pyproject — the 2026 default stack |
| C02 | [Typing & Static Analysis](#c02--typing--static-analysis) | 5–10 | Protocols and generics; prerequisite for Pydantic/FastAPI |
| C03 | [Data Model & Metaprogramming](#c03--data-model--metaprogramming) | 11–17 | Descriptors and metaclasses — how ORMs actually work |
| C04 | [Iteration & Functional Python](#c04--iteration--functional-python) | 18–23 | Generators, `itertools`, `functools` — memory-efficient pipelines |
| C05 | [Data Modeling](#c05--data-modeling) | 24–27 | dataclasses, Pydantic v2, enums — typed domain objects |
| C06 | [Memory & Performance](#c06--memory--performance) | 28–33 | `__slots__`, GC, profiling, zero-copy, Big-O in practice |
| C07 | [Concurrency I — Threads & Processes](#c07--concurrency-i--threads--processes) | 34–39 | The GIL, and free-threaded 3.14 where it is optional |
| C08 | [Concurrency II — Async](#c08--concurrency-ii--async) | 40–46 | `TaskGroup`, structured concurrency, backpressure |
| C09 | [Testing & Quality](#c09--testing--quality) | 47–51 | Fixtures, mocking, property-based testing, coverage |
| C10 | [Architecture & Patterns](#c10--architecture--patterns) | 52–55 | SOLID in full, repository, ports & adapters |
| C11 | [Production Python](#c11--production-python) | 56–59 | Packaging, logging, security, DB, API layers |
| C12 | [Capstone](#c12--capstone) | 60 | One service that uses all of it |

**Effort:** 60 sessions. At 5 days/week that is ~12 weeks; at 3 days/week, ~20.

### Progress

- [ ] C01 Tooling (Days 1–4)
- [ ] C02 Typing (Days 5–10)
- [ ] C03 Data model (Days 11–17)
- [ ] C04 Iteration (Days 18–23)
- [ ] C05 Data modeling (Days 24–27)
- [ ] C06 Memory & performance (Days 28–33)
- [ ] C07 Threads & processes (Days 34–39)
- [ ] C08 Async (Days 40–46)
- [ ] C09 Testing (Days 47–51)
- [ ] C10 Architecture (Days 52–55)
- [ ] C11 Production (Days 56–59)
- [ ] C12 Capstone (Day 60)

---

# C01 — Modern Baseline & Tooling

**Days 1–4** · New folder: `advanced/01-tooling-baseline/`

The ecosystem consolidated around Rust-powered tooling. `uv` replaces
pip/venv/pip-tools, `ruff` replaces flake8/isort/pylint, and `pyproject.toml`
replaces `setup.py` and loose `requirements.txt`. Doing this first means every
later component is linted and type-checked as you write it.

**Concepts:** `pyproject.toml` (PEP 621), dependency groups, lockfiles, `uv`,
`ruff` lint + format, `mypy` strict mode, `pre-commit`, editable installs,
`python -m`, semantic versioning.

| Day | Focus | Deliverable |
| --- | --- | --- |
| 1 | Project skeleton & `pyproject.toml` | Convert this repo to a real project: `pyproject.toml` with `[project]`, `[dependency-groups]`, and a `[tool.pytest.ini_options]` section. Replace `app/backend/requirements.txt` with locked deps. |
| 2 | `uv` end to end | `uv venv`, `uv add`, `uv sync`, `uv run`, `uv lock`. Recreate the `app/backend` environment with uv and commit `uv.lock`. Time `uv sync` vs `pip install -r` and record both. |
| 3 | `ruff` + `black`-style formatting | Add `[tool.ruff]` with a real rule set (`E`, `F`, `I`, `UP`, `B`, `SIM`). Run `ruff check --fix` across the whole repo. Log every category it caught — it will find the `TyypeError` typo class and unused imports. |
| 4 | `mypy` strict + `pre-commit` | `[tool.mypy]` with `strict = true`. Run it repo-wide, record the error count as a baseline you will drive to zero. Add `.pre-commit-config.yaml` running ruff + mypy, and install the hook. |

**Done when:** `uv run pytest`, `uv run ruff check`, and `uv run mypy .` all
execute from a clean clone, and the pre-commit hook blocks a deliberately broken
commit.

---

# C02 — Typing & Static Analysis

**Days 5–10** · New folder: `advanced/02-typing/`

This repo currently has **zero annotations**. Typing is the single highest-value
gap: it is a prerequisite for Pydantic, FastAPI, SQLAlchemy 2.x, and for reading
any modern library source. Protocols in particular let you get interface safety
without inheritance — the typed version of the duck typing you already use.

**Concepts:** annotations, `Optional`/`X | None`, builtin generics (`list[str]`),
`Callable`, `TypeVar`, `Generic`, PEP 695 `class Box[T]` syntax, `Protocol` and
structural typing, `runtime_checkable`, `Literal`, `Final`, `ClassVar`,
`TypedDict`, `NewType`, `Self`, `overload`, `cast`, `Any` vs `object`,
`TypeGuard`/`TypeIs`, variance, `if TYPE_CHECKING`, forward references.

| Day | Focus | Deliverable |
| --- | --- | --- |
| 5 | Annotation fundamentals | Annotate every function in `functions/` and `built-in-functions/`. Cover params, returns, `None`, `X \| None` unions, `list[int]`, `dict[str, list[int]]`, `tuple[int, ...]`. Make `mypy` pass on those two folders. |
| 6 | `Callable` and decorator typing | Type your 4 existing decorators in `functions/decorators/` properly using `Callable[..., T]`, `TypeVar`, and `ParamSpec`. This is the day you learn why `functools.wraps` matters to type checkers too. |
| 7 | Generics | `TypeVar`, bounded `TypeVar`, `Generic[T]`, and the PEP 695 `class Stack[T]:` syntax. Build a typed `Stack[T]`, `Queue[T]`, and `Result[T, E]`. |
| 8 | `Protocol` & structural typing | Write `Protocol`s for `Comparable`, `Repository`, and `SupportsClose`. Refactor `clean-architecture/` to use a `Protocol` instead of `ABC` and write up the tradeoff (no inheritance required vs no runtime enforcement). |
| 9 | Narrowing & precision types | `Literal`, `Final`, `ClassVar`, `TypedDict`, `NewType`, `Self`, `assert_never` for exhaustive `match`, `TypeIs`/`TypeGuard` custom narrowers, `@overload`. |
| 10 | Strict-mode cleanup | Drive `mypy --strict` to zero errors across the pre-existing folders. Document the 3 escape hatches (`cast`, `# type: ignore[code]`, `Any`) and when each is legitimate. |

**Done when:** `mypy --strict` reports no errors on every folder written so far,
and you can explain when a `Protocol` beats an `ABC`.

---

# C03 — Data Model & Metaprogramming

**Days 11–17** · Extends: `dunder-methods/`

Your strongest area, but it stops before the parts frameworks are built on.
`dunder-methods/` covers `__new__`, metaclasses, and the iterator protocol, yet
has no arithmetic operators, no `__hash__`, and no descriptors. Descriptors are
the missing link — they are literally how `@property`, SQLAlchemy columns, and
Pydantic fields work.

**Concepts:** `__add__`/`__radd__`/`__iadd__`, `__neg__`, `__abs__`,
`__hash__` + `__eq__` contract, `functools.total_ordering`, `__format__`,
`__index__`, `__reversed__`, descriptor protocol (`__get__`/`__set__`/
`__set_name__`/`__delete__`), data vs non-data descriptors, `@property` internals,
`__slots__`, `__init_subclass__`, `__class_getitem__`, `__getattr__` vs
`__getattribute__`, metaclasses, `abc` registration, MRO and C3 linearization,
`__copy__`/`__deepcopy__`, `__await__`, `__aiter__`/`__anext__`,
`__aenter__`/`__aexit__`.

| Day | Focus | Deliverable |
| --- | --- | --- |
| 11 | Arithmetic operators | New `dunder-methods/arithmetic/`: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__neg__`, `__abs__`. Build `Vector2D` and `Money` (with currency-mismatch errors). |
| 12 | Reflected & in-place ops | `__radd__` (why `2 * vec` needs it), `__iadd__` and how it differs from `__add__` for mutable types, `NotImplemented` as the fallback signal — connect to your existing `NotImplemented.py`. |
| 13 | Hashing & ordering | The `__eq__`/`__hash__` contract, why a mutable class should set `__hash__ = None`, `__lt__` + `@total_ordering`, sort stability. Prove a mutated dict key becomes unreachable. |
| 14 | Descriptors | `__get__`/`__set__`/`__set_name__`, data vs non-data precedence, a `Validated[T]` descriptor enforcing type + range, then reimplement `@property` from scratch as a descriptor class. |
| 15 | `__slots__` & subclass hooks | `__slots__` with a `tracemalloc`/`sys.getsizeof` comparison over 100k instances, inheritance rules with slots, `__init_subclass__` for a plugin registry, `__class_getitem__`. |
| 16 | Metaclasses in anger | Build a metaclass that auto-registers subclasses, one that validates required methods at class-creation time, and a singleton. Then write down why a decorator or `__init_subclass__` is usually the better answer. |
| 17 | `__format__` & copying | `__format__` with a custom format spec (`f"{money:>10.2f USD}"`), `__copy__`/`__deepcopy__` on a class holding a list, `__reversed__`, `__index__`. |

**Done when:** `Money` supports `+`, `-`, `*`, comparison, hashing, custom
formatting, and deep-copies correctly — with tests.

---

# C04 — Iteration & Functional Python

**Days 18–23** · New folders: `advanced/04-iteration-functional/`, extends `functions/`

`yield` appears **nowhere** in this repo. `iter_next.py` teaches the iterator
protocol the hard way (a class with manual index tracking) without ever showing
that a generator does the same thing in three lines. Generators are also the
main tool for processing data larger than RAM.

**Concepts:** `yield`, generator functions vs generator expressions, laziness,
`yield from`, `send`/`throw`/`close`, infinite generators, pipelines,
`itertools` (`chain`, `islice`, `groupby`, `product`, `permutations`,
`combinations`, `accumulate`, `cycle`, `repeat`, `tee`, `zip_longest`,
`pairwise`, `batched`), `functools` (`wraps`, `lru_cache`, `cache`, `partial`,
`reduce`, `cached_property`, `total_ordering`, `singledispatch`), `operator`
module, `*args`/`**kwargs`, keyword-only (`*`) and positional-only (`/`) params,
the mutable-default trap, LEGB scope, recursion limits.

| Day | Focus | Deliverable |
| --- | --- | --- |
| 18 | Generators | `yield` basics, generator vs list memory via `sys.getsizeof` and `tracemalloc` on 1M items, generator expressions, statefulness/one-shot exhaustion. Rewrite `dunder-methods/container-iteration/iter_next.py`'s `Playlist` as a generator and compare line counts. |
| 19 | Advanced generators | `yield from` and delegation, `send()` for coroutine-style generators, `throw`/`close`, `contextlib.closing`. Build a 4-stage lazy pipeline (read → parse → filter → aggregate) over a large file that never loads it fully. |
| 20 | `itertools` | `chain`, `islice`, `groupby` (including the must-sort-first gotcha), `product`, `permutations`, `combinations`, `accumulate`, `cycle`, `tee`, `zip_longest`, `pairwise`, `batched` (3.12+). Rewrite `data-structures/common-patterns/grouping.py` with `groupby`. |
| 21 | Function signatures in full | `*args`/`**kwargs`, the mutable-default-argument bug (with the `id()` proof), keyword-only via `*`, positional-only via `/`, argument unpacking at call sites, `lambda` vs `def`, LEGB and `nonlocal` (extends your `func_closures/`). |
| 22 | `functools` | Retrofit `wraps` into your 4 existing decorators and show `__name__`/`__doc__`/signature being restored. `lru_cache` with a memoised-fib benchmark, `cache`, `cached_property`, `partial`, `reduce`, `singledispatch`. |
| 23 | Functional composition | The `operator` module, `sorted` with composite keys via `itemgetter`/`attrgetter`, decorator stacking order, a `compose()` helper, a retry decorator with backoff, a `@timed` decorator. |

**Done when:** you can process a file larger than available RAM with a generator
pipeline and show the memory difference in numbers.

---

# C05 — Data Modeling

**Days 24–27** · New folder: `advanced/05-data-modeling/`

The bridge between C02 (typing) and C11 (production). `app/backend` already
depends on Pydantic, so this component is what makes that code legible rather
than copied.

**Concepts:** `@dataclass` (`frozen`, `order`, `slots`, `kw_only`,
`field(default_factory=...)`, `__post_init__`, `InitVar`, `fields()`, `asdict`),
`NamedTuple` vs `namedtuple` vs `TypedDict`, `Enum`/`IntEnum`/`StrEnum`/`Flag`,
`auto()`, Pydantic v2 (`BaseModel`, validators, `Field` constraints,
`model_config`, serialisation, `TypeAdapter`, `Settings`), when a plain
dataclass beats a model.

| Day | Focus | Deliverable |
| --- | --- | --- |
| 24 | Dataclasses | Rewrite `Person`, `BankAccount`, and `Book` from `dunder-methods/` as dataclasses; count the lines you deleted. Cover `frozen=True`, `order=True`, `slots=True`, `kw_only`, `default_factory` (and why `= []` is a bug), `__post_init__` validation. |
| 25 | Tuples, NamedTuple, TypedDict | The tuple gap in `data-structures/`: unpacking, star-unpacking, swapping, tuples as dict keys, immutability. Then `NamedTuple` vs `TypedDict` vs dataclass vs dict — one decision table with a reason per row. |
| 26 | Enums | `Enum`, `IntEnum`, `StrEnum` (3.11+), `Flag` for bit permissions, `auto()`, methods on enums, `@unique`. Replace every magic string/status literal in `app/backend/main.py` with an enum. |
| 27 | Pydantic v2 | `BaseModel`, `Field` constraints, `@field_validator`/`@model_validator`, computed fields, custom serialisers, `model_dump`/`model_validate`, `TypeAdapter`, `BaseSettings` for env config. Contrast validation cost vs a plain dataclass with a benchmark. |

**Done when:** every dict-shaped payload in `app/backend` is a typed model, and
you can state the dataclass-vs-Pydantic decision rule in one sentence.

---

# C06 — Memory & Performance

**Days 28–33** · New folder: `advanced/06-memory-performance/`

The component that turns "it works" into "it works at scale". Also where the
`is` vs `==` and mutable-aliasing bugs stop happening to you.

**Concepts:** reference semantics, reference counting, `sys.getrefcount`,
generational GC and `gc` module, cycles, `weakref`, `id()`, `is` vs `==`,
small-int and string interning, `copy` vs `deepcopy`, `__slots__` savings,
`tracemalloc`, `timeit`, `cProfile`/`pstats`, `sys.monitoring` (3.12+), Big-O of
each builtin structure, amortised list growth, `memoryview` and the buffer
protocol, zero-copy slicing, `bytes` vs `bytearray`, `array`, string
concatenation cost, `heapq`, `bisect`, `deque`, `functools.lru_cache` as a
performance tool.

| Day | Focus | Deliverable |
| --- | --- | --- |
| 28 | Object model & identity | `id()`, `is` vs `==`, `sys.getrefcount`, mutable default args, passing lists into functions, `copy` vs `deepcopy` on nested structures, a tuple containing a list, int/string interning surprises. Write the 5 aliasing bugs as failing-then-passing asserts. |
| 29 | Garbage collection | Reference counting vs the generational collector, creating and detecting a reference cycle, `gc.collect()`, `gc.get_stats()`, disabling GC for a hot path, `weakref` and `WeakValueDictionary` for caches. |
| 30 | Measuring memory | `sys.getsizeof` vs deep size, `tracemalloc` snapshots and diffs, `__slots__` over 100k instances, dataclass vs `__slots__` dataclass vs NamedTuple vs dict — one table of real numbers. |
| 31 | Measuring time | `timeit` (CLI and API), `perf_counter` vs `process_time` vs `monotonic`, `cProfile` + `pstats` sorting, finding a hotspot in a deliberately slow function and optimising it, then proving the win. |
| 32 | Complexity in practice | Big-O per structure, `list.index` O(n) vs `set` O(1) with timings across sizes, `dict` lookup, `deque.appendleft` vs `list.insert(0)`, amortised list growth, `heapq` for top-k, `bisect` for sorted inserts, string `+=` in a loop vs `join`. |
| 33 | Zero-copy & buffers | `memoryview`, the buffer protocol, slicing `bytes` (copy) vs `memoryview` (view), `bytearray` in-place mutation, `array`, `struct` pack/unpack, reading a large binary file without copying. |

**Done when:** `advanced/06-memory-performance/RESULTS.md` holds your own
measured numbers for every claim above — not quoted numbers.

---

# C07 — Concurrency I — Threads & Processes

**Days 34–39** · Extends: `concurrency/`

Your `concurrency/` folder has 423 lines of notes behind 133 lines of code — the
concepts are read, not felt. Nobody understands the GIL from prose; you
understand it the first time you thread a CPU-bound task and watch it get
*slower*.

This is also the area that changed most recently. **PEP 703** made the GIL
optional: free-threaded builds were experimental in 3.13 and officially supported
in 3.14, so `threading.Thread` can now run bytecode on multiple cores. It is not
the default build and won't be for several releases — so learn the GIL model
first, then learn where it no longer applies.

**Concepts:** thread vs process vs coroutine, the GIL and what releases it,
`threading.Thread`, `join`, daemon threads, race conditions, `Lock`, `RLock`,
`Semaphore`, `Event`, `Condition`, `Barrier`, deadlock and lock ordering,
`queue.Queue` for producer/consumer, `threading.local`, `concurrent.futures`
(`ThreadPoolExecutor`, `ProcessPoolExecutor`, `submit` vs `map`, `as_completed`,
exception propagation), `multiprocessing` (spawn vs fork, `Pool`, `Pipe`,
`Manager`, shared memory, pickling limits), free-threaded builds
(`sys._is_gil_enabled()`), subinterpreters (PEP 734), `atomics`-style patterns.

| Day | Focus | Deliverable |
| --- | --- | --- |
| 34 | The GIL, demonstrated | Run one CPU-bound function (a) serially, (b) in 4 threads, (c) in 4 processes. Record wall-clock for each. Then run one I/O-bound function the same three ways. Two tables, one conclusion — this replaces the prose in your `docs.txt`. |
| 35 | Race conditions & locks | A shared counter incremented by 8 threads without a lock, run 100 times, showing wrong totals. Then `Lock` fixing it. Then `RLock`, `Semaphore` for bounded access, `Event` for signalling, and a deliberate deadlock plus the lock-ordering fix. |
| 36 | Producer/consumer | `queue.Queue` with N producers and M consumers, sentinel shutdown, `task_done`/`join`, `LifoQueue` and `PriorityQueue`, bounded queues as backpressure, `threading.local`. |
| 37 | `concurrent.futures` | `ThreadPoolExecutor` vs `ProcessPoolExecutor` behind one interface, `submit` + `as_completed` vs `map`, futures with timeouts, how exceptions surface on `.result()`, cancellation limits. Fan out 50 real HTTP requests and compare against serial. |
| 38 | `multiprocessing` in depth | spawn vs fork (and why fork+threads is unsafe), what is and isn't picklable, `Pool.imap_unordered`, `Pipe`, `Manager` dicts, `shared_memory` for a large array, per-process init cost. |
| 39 | Free-threaded Python & subinterpreters | Install a 3.14 free-threaded build. Verify with `sys._is_gil_enabled()`. Re-run Day 34's CPU-bound threaded benchmark and record the speedup. Note which of your deps are C-extension-compatible. Then try `InterpreterPoolExecutor`/PEP 734 subinterpreters as the middle ground. |

**Done when:** you can choose thread vs process vs async for a given workload and
justify it with your own benchmark numbers, and you know what changes under a
free-threaded build.

---

# C08 — Concurrency II — Async

**Days 40–46** · New folder: `advanced/08-concurrency-async/`

`asycio_example.py` uses `asyncio.gather`, which is the pattern modern async code
is moving away from. `gather` leaks tasks on failure and swallows sibling errors;
`TaskGroup` (3.11+) guarantees children cannot outlive their scope. Learning
structured concurrency now removes an entire class of orphan-task bugs.

**Concepts:** coroutines vs futures vs tasks, the event loop, `asyncio.run`,
`await` points, `create_task`, `TaskGroup` and `ExceptionGroup`/`except*`,
`gather` vs `TaskGroup` vs `wait`, `as_completed`, cancellation and
`CancelledError`, shielding, `timeout`/`wait_for`, async context managers
(`__aenter__`/`__aexit__`, `@asynccontextmanager`), async iterators/generators
(`__aiter__`/`__anext__`, `async for`, `async` comprehensions), async
`Lock`/`Semaphore`/`Event`/`Queue`, bounded concurrency, rate limiting, circuit
breakers, backpressure, `run_in_executor` for blocking work, `to_thread`,
`uvloop`, graceful shutdown, `pytest-asyncio`, debug mode, common pitfalls
(blocking the loop, fire-and-forget tasks, unawaited coroutines).

| Day | Focus | Deliverable |
| --- | --- | --- |
| 40 | Event loop fundamentals | Coroutine vs task vs future, `asyncio.run` as the single entry point, what `await` actually yields to, why a bare `time.sleep` in a coroutine destroys concurrency (prove it with timings), unawaited-coroutine warnings, `asyncio.debug` mode. |
| 41 | Structured concurrency | Rewrite `concurrency/asycio_example.py` with `TaskGroup`. Then demonstrate the difference: one child raises — show `gather` leaking siblings vs `TaskGroup` cancelling them, and handle the `ExceptionGroup` with `except*`. |
| 42 | Cancellation & timeouts | `task.cancel()` and `CancelledError` propagation, `asyncio.timeout` (3.11+) vs `wait_for`, `shield`, cleanup in `finally`, why swallowing `CancelledError` is a bug, graceful shutdown on SIGINT. |
| 43 | Async iterators & context managers | `__aiter__`/`__anext__`, `async def` generators with `yield`, `async for`, async comprehensions, `@asynccontextmanager`, `AsyncExitStack`. Stream a paginated API as an async generator. |
| 44 | Async synchronisation & limits | `asyncio.Semaphore` for bounded fan-out, `asyncio.Queue` producer/consumer with backpressure, `Lock`/`Event`, a token-bucket rate limiter, a circuit breaker, retry with exponential backoff + jitter. |
| 45 | Mixing blocking & async | `run_in_executor`, `asyncio.to_thread`, offloading CPU work to a `ProcessPoolExecutor` from async code, `uvloop` benchmark, calling sync DB drivers safely, the "never block the loop" rule with a measured violation. |
| 46 | Testing & production async | `pytest-asyncio` (fixtures, event_loop scope), mocking coroutines with `AsyncMock`, testing cancellation and timeouts, structured logging with task context, health checks. Test the async endpoints in `app/backend`. |

**Done when:** you fetch 100 URLs with bounded concurrency, correct cancellation,
retries, and a timeout — using `TaskGroup`, with tests.

---

# C09 — Testing & Quality

**Days 47–51** · Extends: `testing/`, `debugging/`

Currently the weakest area in the repo: `testing/` has two tests that **both
fail** with `NameError`, and `debugging/` is a single `logging.basicConfig` call.
Everything in C01–C08 needs tests to be worth keeping.

**Concepts:** pytest architecture, `conftest.py`, fixtures (scopes,
`yield` teardown, factories, autouse), `@parametrize` (including stacked and
`pytest.param(id=...)`), `pytest.raises` and `match`, `monkeypatch`, `tmp_path`,
`caplog`, `capsys`, markers, `unittest.mock` (`Mock`, `MagicMock`, `patch`,
`side_effect`, `return_value`, `spec`, `assert_called_with`), `AsyncMock`,
fakes vs mocks vs stubs, dependency injection for testability, coverage and
branch coverage, property-based testing with Hypothesis, mutation testing,
`freezegun`, snapshot testing, `pdb`/`breakpoint()`, logging configuration
(named loggers, handlers, formatters, rotation, `dictConfig`), structured logging.

| Day | Focus | Deliverable |
| --- | --- | --- |
| 47 | pytest properly | **Fix `test_calculator.py` first** (it never imports `add`/`subtract`). Then `conftest.py`, fixture scopes with `yield` teardown, factory fixtures, autouse, `tmp_path`, `caplog`, `capsys`, markers, `-k`/`-x`/`-vv`. |
| 48 | Parametrize & exceptions | `@parametrize` with ids, stacked parametrize for a matrix, `pytest.raises(..., match=...)`, testing the custom exception hierarchy from C11, `xfail` vs `skipif`. Parametrize the `Money`/`Vector2D` classes from C03. |
| 49 | Mocking & test doubles | `Mock`/`MagicMock`, `patch` as decorator/context/`patch.object`, `side_effect` for sequences and raises, `spec`/`autospec`, `AsyncMock`. Then write the same test with a hand-rolled fake and argue which you'd keep. |
| 50 | Coverage & property-based | `pytest-cov` with branch coverage to 90%+ on your `advanced/` code, `.coveragerc` excludes, why 100% is not the goal. Then Hypothesis: `@given` strategies, and find a real edge case in a function you wrote in C04. |
| 51 | Debugging & logging | `breakpoint()`/pdb walkthrough (`n`, `s`, `c`, `l`, `p`, `pp`, `w`, `u`/`d`), post-mortem `pdb.pm()`. Then replace `basic_logging.py` with named loggers, handlers, formatters, `RotatingFileHandler`, `dictConfig`, `exc_info`, and structured JSON logs with correlation IDs. |

**Done when:** `pytest --cov` reports 90%+ on `advanced/`, and Hypothesis found at
least one bug you did not anticipate.

---

# C10 — Architecture & Patterns

**Days 52–55** · Extends: `clean-architecture/`

Your `clean-architecture/` folder covers dependency inversion — the D of SOLID —
and has a bug in the file that teaches it. This component finishes the acronym
and adds the patterns that make a codebase testable.

**Concepts:** SRP, OCP, LSP, ISP, DIP; composition over inheritance; dependency
injection (constructor, `Protocol`-based); repository pattern; unit of work;
service/use-case layer; entities vs DTOs; ports & adapters (hexagonal);
layered/clean architecture; strategy, factory, abstract factory, observer,
adapter, decorator (object form), command, singleton done right (module-level),
builder; anti-patterns (god object, anemic model, service locator, circular
dependency).

| Day | Focus | Deliverable |
| --- | --- | --- |
| 52 | SOLID in full | **Fix the DIP bug first** (`self.db = Database` should be the injected arg; callers pass a class instead of an instance; `create_order()` is never called so it fails silently). Then one file per letter, each with a before/after and a test that only passes after the refactor. |
| 53 | Repository & unit of work | One `Protocol` repository with two implementations — in-memory and sqlite — swapped by injection. Same test suite passes against both. Add a unit-of-work wrapper with commit/rollback. |
| 54 | Layering | entities → use cases → adapters → infrastructure, with the dependency rule enforced (inner layers import nothing outward). DTOs at the boundary. Write a use case tested with zero I/O. |
| 55 | Patterns worth knowing | Strategy (pricing rules), factory (parser by file type), observer (event bus), adapter (wrapping a third-party client), command with undo, module-level singleton. For each: what it buys, and when a plain function is better. |

**Done when:** your service layer's tests run with no database, no network, and
no mocks of your own code — only fakes at the boundaries.

---

# C11 — Production Python

**Days 56–59** · New folder: `advanced/11-production/`

**Concepts:** packaging (`pyproject.toml` build backends, wheels vs sdist,
console scripts, `__version__`, publishing to PyPI/TestPyPI), 12-factor config,
`BaseSettings`, secrets handling, `sqlite3` (parameterised queries,
transactions, row factories), SQLAlchemy 2.x (typed ORM, sessions, N+1,
migrations with Alembic), HTTP clients (`httpx` sync/async, timeouts, retries,
connection pooling, pagination, auth), FastAPI depth (dependency injection,
`BackgroundTasks`, middleware, lifespan, error handlers, response models),
security (input validation, SQL injection, `secrets` vs `random`, password
hashing, JWT, dependency scanning with `pip-audit`), Docker for Python
(multi-stage, non-root, layer caching), CI with GitHub Actions, observability
(structured logs, metrics, tracing).

| Day | Focus | Deliverable |
| --- | --- | --- |
| 56 | Packaging & CLI | Turn one component into an installable package: build backend, `[project.scripts]` console entry point, `argparse` or Typer CLI, `__version__`, build a wheel, install it in a fresh venv, publish to TestPyPI. |
| 57 | Databases | `sqlite3` with parameterised queries (and an injection demo of what string formatting allows), transactions and rollback, row factories. Then SQLAlchemy 2.x typed models, session lifecycle, an N+1 query found via echoed SQL and fixed with eager loading, one Alembic migration. |
| 58 | HTTP & API layers | `httpx` client with timeouts, retries, and connection reuse; consume your own `app/backend` API including pagination. Then deepen the backend: dependency injection, response models, exception handlers, middleware, lifespan startup/shutdown. |
| 59 | Security, config & CI | `BaseSettings` + `.env` (and confirming secrets are gitignored), `secrets` vs `random`, password hashing, `pip-audit`, a multi-stage non-root Dockerfile, and a GitHub Actions workflow running ruff + mypy + pytest on push. |

**Done when:** `docker build` produces a running image, and CI is green on a
pull request.

---

# C12 — Capstone

**Day 60** · New folder: `advanced/12-capstone/`

One service that touches every component. Suggested build: **a URL-monitoring
service.**

| Requirement | Component exercised |
| --- | --- |
| `pyproject.toml`, uv-locked, ruff + mypy strict clean, pre-commit | C01 |
| Fully annotated; `Protocol`-based repository interface | C02 |
| A domain value object with operators, `__hash__`, and a validating descriptor | C03 |
| Results streamed through a generator pipeline; `lru_cache` on lookups | C04 |
| Pydantic request/response models; `StrEnum` statuses; frozen dataclass entities | C05 |
| `__slots__` on hot objects; documented `timeit`/`tracemalloc` numbers | C06 |
| CPU-bound report generation in a `ProcessPoolExecutor` | C07 |
| Async checks via `TaskGroup` with a `Semaphore`, timeouts, retries, backoff | C08 |
| 90%+ branch coverage, Hypothesis on the parser, `AsyncMock` at boundaries | C09 |
| entities → use cases → adapters; swappable sqlite/in-memory repo | C10 |
| FastAPI endpoints, SQLAlchemy persistence, Docker, CI, structured logs | C11 |

**Done when:** a new reader can clone it, run `uv sync && uv run pytest`, get
green, `docker build`, and hit a working endpoint — and you can explain any
design choice in it.

---

## Milestone checks

Stop and verify at these points. If a milestone fails, repeat the component
rather than moving on.

| After | You should be able to |
| --- | --- |
| C02 (Day 10) | Pass `mypy --strict` on everything you have written, and explain `Protocol` vs `ABC` |
| C04 (Day 23) | Process a file bigger than RAM through a generator pipeline, with measured memory |
| C06 (Day 33) | Profile a slow function, optimise it, and prove the win in numbers |
| C08 (Day 46) | Fan out 100 network calls with bounded concurrency, retries, and correct cancellation |
| C10 (Day 55) | Swap a database implementation without touching a single use-case test |
| C12 (Day 60) | Ship the capstone green in CI |

---

## What this roadmap deliberately excludes

Scope discipline — these are adjacent tracks, not advanced *language* skills:

- **Data science / ML** (numpy, pandas, scikit-learn, PyTorch) — a separate path.
- **LLM/AI engineering** (RAG, LangChain, vector DBs) — build on C11 afterwards.
- **DSA interview prep** (linked lists, trees, graph algorithms) — different goal;
  C06's complexity work is the overlap.
- **Frontend** — `app/frontend` exists, but React is not Python depth.
- **Kubernetes / cloud infra** — starts where C11 ends.

---

## Reference

- [PEP 703 — Making the GIL Optional](https://peps.python.org/pep-0703/)
- [PEP 734 — Multiple Interpreters in the Stdlib](https://peps.python.org/pep-0734/)
- [PEP 695 — Type Parameter Syntax](https://peps.python.org/pep-0695/)
- [PEP 621 — Project Metadata in pyproject.toml](https://peps.python.org/pep-0621/)
- [Python Data Model reference](https://docs.python.org/3/reference/datamodel.html)
- [asyncio documentation](https://docs.python.org/3/library/asyncio.html)
- [typing documentation](https://docs.python.org/3/library/typing.html)
- [uv](https://docs.astral.sh/uv/) · [ruff](https://docs.astral.sh/ruff/) · [mypy](https://mypy.readthedocs.io/)
- [pytest](https://docs.pytest.org/) · [Hypothesis](https://hypothesis.readthedocs.io/)
- [py-free-threading compatibility tracker](https://py-free-threading.github.io/)
