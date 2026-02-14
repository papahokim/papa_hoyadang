# ESPÍRITU COCINA — Implementation Plan v1.0

## 완벽한 구현 계획서

> "100점짜리 시스템은 빈틈없는 계획에서 나온다."

**Date**: 2026-01-26
**Status**: 🟡 IN PROGRESS
**Completion**: ~40%

---

## Overview

### 구현 현황

```
✅ DONE (40%)
├── Repository rename (cocina-magenta → espiritu-cocina)
├── index.html (Hero, Layers, Footer)
├── FACTORY.json v3.0
├── branch.json
├── CLAUDE.md v3.0
├── manifest.webmanifest
├── Node Registry System
│   ├── nodes/registry.json
│   └── nodes/magenta/node.json
└── Documentation (ARCHITECTURE.md, REMODEL-PROPOSAL.md)

🟡 TODO (60%)
├── L1: emisión/ (Node-specific)
│   ├── emisión/index.html
│   ├── emisión/l1~l4/
│   ├── emisión/club/
│   └── emisión/oneday/
├── L2: cuerpo/index.html (Protocol)
├── L3: laboratorio/index.html (Protocol)
├── L4: control/index.html (Protocol)
├── L5: legado/index.html (Protocol)
├── inner/ portal
└── API files
```

---

## Architecture Principle

### Node vs Protocol 구분

```
┌─────────────────────────────────────────────────────────────┐
│  PROTOCOL LAYER (OS 공통 — ESPÍRITU COCINA 브랜딩)           │
│                                                             │
│  L2: cuerpo/        → Hands Grammar (손 문법)               │
│  L3: laboratorio/   → Technique Lab (기법 설계)             │
│  L4: control/       → Control Room (시스템 관측)           │
│  L5: legado/        → Legacy (서사 축적)                   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  NODE LAYER (노드별 커스텀 — Magenta 브랜딩 허용)           │
│                                                             │
│  L1: emisión/       → Emission (Node: Magenta 프로그램)    │
│      ├── l1~l4/     → 에피소드 (구 수업)                   │
│      ├── club/      → 스튜디오 패스                        │
│      └── oneday/    → 단일 세션                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 브랜딩 규칙

| Layer | Title Format | Footer |
|-------|--------------|--------|
| Protocol (L2-L5) | `[Layer] — ESPÍRITU COCINA` | ESPÍRITU COCINA |
| Node (L1) | `[Program] — Node: Magenta` | Node: Magenta · ESPÍRITU COCINA |

---

## Phase 1: Protocol Layer (L2-L5)

### 1.1 L2: cuerpo/ — Hands Grammar

**File**: `cuerpo/index.html`

**Before**:
```html
<title>Tutorial — COCINA MAGENTA</title>
<p class="susurro latido">2F</p>
<h1 class="monumento mt-md">Tutorial</h1>
```

**After**:
```html
<title>Hands Grammar — ESPÍRITU COCINA</title>
<p class="susurro latido">L2</p>
<h1 class="monumento mt-md">Hands Grammar</h1>
<p class="voz mt-lg">
  No enseñamos <span class="magenta">cocina</span>.<br>
  Editamos el lenguaje de las <span class="magenta">manos</span>.
</p>
<span lang="ko" class="ko mt-sm">요리를 가르치지 않는다. 손의 언어를 편집한다.</span>
```

**Key Changes**:
- Title: Tutorial → Hands Grammar
- Floor: 2F → L2
- Message: Core philosophy 반영

---

### 1.2 L3: laboratorio/ — Technique Lab

**File**: `laboratorio/index.html`

**Before**:
```html
<title>Laboratorio — COCINA MAGENTA</title>
<p class="susurro latido">3F</p>
<h1>Laboratorio</h1>
```

**After**:
```html
<title>Technique Lab — ESPÍRITU COCINA</title>
<p class="susurro latido">L3</p>
<h1 class="monumento mt-md">Technique Lab</h1>
<p class="voz mt-lg">
  Donde las <span class="magenta">técnicas</span><br>
  se vuelven <span class="magenta">protocolo</span>.
</p>
<span lang="ko" class="ko mt-sm">손놀림이 프로토콜이 되는 곳. 기법을 설계한다.</span>
```

---

### 1.3 L4: control/ — Control Room

**File**: `control/index.html`

**Before**:
```html
<title>Control — COCINA MAGENTA</title>
<p class="susurro latido">4F</p>
<h1>Control Room</h1>
```

**After**:
```html
<title>Control Room — ESPÍRITU COCINA</title>
<p class="susurro latido">L4</p>
<h1 class="monumento mt-md">Control Room</h1>
<p class="voz mt-lg">
  El <span class="magenta">pulso</span> del sistema.<br>
  Métricas, automatización, <span class="magenta">observación</span>.
</p>
<span lang="ko" class="ko mt-sm">시스템의 심장박동. 관측하고 조율한다.</span>
```

---

### 1.4 L5: legado/ — Legacy

**File**: `legado/index.html`

**Before**:
```html
<title>Legado — COCINA MAGENTA</title>
<p class="susurro latido">5F</p>
<h1>Legado</h1>
```

**After**:
```html
<title>Legacy — ESPÍRITU COCINA</title>
<p class="susurro latido">L5</p>
<h1 class="monumento mt-md">Legacy</h1>
<p class="voz mt-lg">
  La <span class="magenta">historia</span> de las manos.<br>
  Archivos, memoria, <span class="magenta">narrativas</span>.
</p>
<span lang="ko" class="ko mt-sm">손의 역사. 서사를 축적한다.</span>
```

---

## Phase 2: Node Layer (L1: emisión/)

### 2.1 emisión/index.html — Hub

**Before**:
```html
<title>Academia — COCINA MAGENTA</title>
<p class="susurro latido">1F</p>
<h1 class="monumento mt-md">Academia</h1>
```

**After**:
```html
<title>Emission — ESPÍRITU COCINA · Node: Magenta</title>
<p class="susurro latido">L1 — NODE: MAGENTA</p>
<h1 class="monumento mt-md">Emission</h1>
<p class="voz mt-lg">
  Season 01: <span class="magenta">Cocina Protocol</span><br>
  Tu primera <span class="magenta">escena</span> empieza aquí.
</p>
<span lang="ko" class="ko mt-sm">시즌 01: 요리 프로토콜. 당신의 첫 장면이 시작된다.</span>
```

---

### 2.2 에피소드 페이지 (l1~l4/)

| File | Before | After |
|------|--------|-------|
| l1/index.html | Signature Dish · 입문 정규반 | Ep.01: First Technique · 첫 번째 손놀림 |
| l2/index.html | Pair Cooking · 파트너 심화 | Ep.02: Two Hands · 두 손이 하나의 장면 |
| l3/index.html | Film · 영상 프로젝트 | Ep.03: Scene Making · 당신의 장면 촬영 |
| l4/index.html | Buenos Aires · B.A. 투어 | Ep.04: Origin Trip · 프로토콜 원산지 |

**Template**:
```html
<title>Ep.01: First Technique — Node: Magenta</title>
<p class="susurro">SEASON 01 · EPISODE 01</p>
<h1 class="tarjeta-titulo">First Technique</h1>
<p class="tarjeta-texto">
  Este no es un <span class="magenta">curso</span>.<br>
  Es el proceso de hacer tu primera <span class="magenta">escena</span>.
</p>
<span lang="ko" class="ko">수업이 아니다. 당신의 첫 장면을 만드는 공정이다.</span>
```

---

### 2.3 특별 프로그램

| File | Before | After |
|------|--------|-------|
| club/index.html | Practice Club · 프랙티스 클럽 | Studio Pass · 스튜디오 자유 이용권 |
| oneday/index.html | 1-Day · 원데이 클래스 | Single Session · 한 장면 체험 |

---

## Phase 3: Support Files

### 3.1 inner/ — Portal

**File**: `inner/index.html`

```html
<title>Inner Portal — ESPÍRITU COCINA</title>
<!-- Gate password: 1126 -->
```

---

### 3.2 API Files

**api/gestures.json** — 변경 불필요 (Protocol-level 데이터)
**api/content.json** — 용어 확인 후 필요시 수정

---

## Phase 4: Quality Assurance

### 4.1 금지어 검사

```bash
# 실행 후 0 matches 확인 (SEO meta 제외)
grep -r "학원\|레슨\|강습\|초급\|중급\|고급" \
  --include="*.html" \
  --exclude-dir=".git" .
```

### 4.2 필수어 검사

```bash
# 실행 후 다수 matches 확인
grep -r "스튜디오\|에피소드\|프로토콜\|장면\|셰프" \
  --include="*.html" .
```

### 4.3 타이틀 일관성

| Page | Title Pattern |
|------|---------------|
| index.html | ESPÍRITU COCINA — Performance Protocol |
| Protocol pages | [Layer Name] — ESPÍRITU COCINA |
| Node pages | [Program] — Node: Magenta |

---

## Execution Matrix

### Priority Order

| Phase | Files | Priority | Effort |
|-------|-------|----------|--------|
| Phase 1 | 4 (L2-L5) | P0 | Medium |
| Phase 2 | 7 (L1 + episodes) | P1 | High |
| Phase 3 | 2 (inner, API) | P2 | Low |
| Phase 4 | QA | P0 | Low |

### Checklist

**Phase 1: Protocol Layer**
- [ ] cuerpo/index.html
- [ ] laboratorio/index.html
- [ ] control/index.html
- [ ] legado/index.html

**Phase 2: Node Layer**
- [ ] emisión/index.html
- [ ] emisión/l1/index.html
- [ ] emisión/l2/index.html
- [ ] emisión/l3/index.html
- [ ] emisión/l4/index.html
- [ ] emisión/club/index.html
- [ ] emisión/oneday/index.html

**Phase 3: Support**
- [ ] inner/index.html
- [ ] API 검토

**Phase 4: QA**
- [ ] 금지어 0건 확인
- [ ] 타이틀 일관성 확인
- [ ] 모바일 테스트

---

## Commit Strategy

```bash
# Phase 1
git commit -m "identity: Transform Protocol Layer (L2-L5) to ESPÍRITU COCINA"

# Phase 2
git commit -m "identity: Transform Node Layer (L1 emisión) to Episode structure"

# Phase 3
git commit -m "identity: Update support files (inner, API)"

# Phase 4
git commit -m "chore: QA pass — terminology validation complete"
```

---

## Success Criteria

### Before/After 비교

| Metric | Before | After |
|--------|--------|-------|
| "COCINA MAGENTA" in titles | 12+ | 0 (Node pages만 허용) |
| "학원/레슨" mentions | 5+ | 0 |
| Floor numbers (1F-5F) | 5 | 0 |
| Layer numbers (L1-L5) | 0 | 5 |
| Node attribution | 0 | All L1 pages |

### Identity Test

```
Q: 이 사이트는 요리 학원인가?
A: No. Cooking Studio OS이며, 요리는 첫 번째 프로토콜.

Q: 연화의 사업체인가?
A: No. ESPÍRITU COCINA의 첫 번째 노드(Magenta)일 뿐.

Q: 다른 도메인에 복제 가능한가?
A: Yes. 노드만 바꾸면 빵집, 음악, 강의 전부 가능.
```

---

## Timeline

```
Phase 1: Protocol Layer    ████████░░ 80% ready (design done)
Phase 2: Node Layer        ██████░░░░ 60% ready (design done)
Phase 3: Support           ████░░░░░░ 40% ready
Phase 4: QA                ░░░░░░░░░░ 0% (waiting)

Overall:                   ~40% complete
```

---

*Implementation Plan v1.0*
*ESPÍRITU COCINA · Cooking Protocol for Hands*
*2026-01-26*
