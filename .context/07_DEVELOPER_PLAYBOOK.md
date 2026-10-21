# 🛠️ ScholarX — Developer & AI Agent Playbook

> **Actionable recipes and procedures for extending, modifying, and debugging ScholarX.**

---

## Recipe 1: Adding or Modifying a LangGraph Pipeline Node

1. **Update State**: If the node introduces new data, add the typed field to `ScholarXState` in `backend/graph/state.py`.
2. **Implement Node Function**:
   - Create or edit the async function in `backend/graph/nodes.py`.
   - Node signature must always accept `state: ScholarXState` and return a dictionary update:
     ```python
     async def custom_node(state: ScholarXState) -> Dict[str, Any]:
         session_id = state.get("session_id", "default")
         # 1. Emit start event to EventBus
         await get_event_bus().publish(ScholarXEvent(
             session_id=session_id,
             event_type=AgentEventType.STAGE_TRANSITION,
             title="Custom Analysis Started",
             message="Executing custom node logic",
             source="CustomNode"
         ))
         # 2. Perform logic (deterministic workflow or agent)
         result = await execute_logic(state)
         # 3. Return state update
         return {"custom_field": result, "current_node": "custom_node"}
     ```
3. **Wire in Builder**: Add node and edges to `backend/graph/builder.py`:
   ```python
   builder.add_node("custom_node", custom_node)
   builder.add_edge("previous_node", "custom_node")
   builder.add_edge("custom_node", "next_node")
   ```
4. **Write Test**: Add a test in `backend/tests/test_langgraph_pipeline.py`.

---

## Recipe 2: Adding or Updating a Scholarship Deep Dossier

1. **Schema Check**: Ensure data matches `Scholarship` in `backend/schemas/scholarship.py`.
2. **Add to Regional JSON**: Edit or append to `data/scholarships/{region}.json`.
3. **Re-Seed Database**: Run:
   ```bash
   .venv/bin/python -c "from backend.db.seed import load_and_seed_scholarships; import asyncio; asyncio.run(load_and_seed_scholarships())"
   ```
4. **Verify Seed Count**: Run `.venv/bin/python scripts/doctor.py` to ensure 310+ scholarships are validated.

---

## Recipe 3: Emitting a New Real-Time SSE Event

1. **Register Event Type**: Add the new event name to `AgentEventType` in `backend/schemas/events.py`.
2. **Publish from Backend**:
   ```python
   from backend.events.bus import get_event_bus
   from backend.schemas.events import ScholarXEvent, AgentEventType, EventSeverity

   await get_event_bus().publish(ScholarXEvent(
       session_id=session_id,
       event_type=AgentEventType.SKEPTIC_CHALLENGE,
       source="SkepticAgent",
       severity=EventSeverity.CHALLENGE,
       title="Return-to-Pakistan Bond Detected",
       message="Applicant must serve 5 years in Pakistan following completion",
       payload={"scholarship_id": "fulbright_pk", "bond_years": 5}
   ))
   ```
3. **Handle on Frontend**: In `frontend/lib/store.ts` or `frontend/lib/presentation-queue.ts`, listen to the new `event_type` and trigger the appropriate spatial animation or overlay.

---

## Recipe 4: Writing and Running Tests

### Fast Unit Tests (< 1 second)
Always run after modifying schemas or utility functions:
```bash
.venv/bin/pytest backend/tests/test_schemas.py backend/tests/test_api_keys.py -v
```

### Security & Sanitization Tests
Verify that health endpoints and path traversal protections remain intact:
```bash
.venv/bin/pytest backend/tests/test_security_audit_remediation.py -v
```

### Full Test Suite
Run before completing major features:
```bash
make test
# or
.venv/bin/pytest backend/tests/ -q
```

---

## Recipe 5: Troubleshooting Common Issues

### Issue 1: Port 8000 or 3000 Already in Use
Check what process is holding the port and terminate it:
```bash
# Check port 8000
lsof -i :8000
kill -9 <PID>

# Check port 3000
lsof -i :3000
kill -9 <PID>
```

### Issue 2: SQLite Database Locked
SQLite in WAL mode should rarely lock. If locked, ensure no stray python process is holding an unclosed transaction:
```bash
ps aux | grep python
# Clear locks if needed:
sqlite3 data/scholarx_sessions.db "PRAGMA wal_checkpoint(TRUNCATE);"
```

### Issue 3: Frontend Hydration Mismatch
Check if browser localStorage has a stale session ID:
```javascript
// In browser DevTools console:
localStorage.removeItem('scholarx_session_id');
location.reload();
```

### Issue 4: API Key Rate Limits (429)
The `KeyManager` automatically places exhausted keys into a 60-second cooldown and rotates to the next key. To inspect live key health:
```bash
curl -s http://localhost:8000/api/health | python3 -m json.tool
```
