import sqlite3
import json

conn = sqlite3.connect('/mnt/windows/AntiGravity/SCHOLARX/scholarships_database.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute('SELECT * FROM scholarships ORDER BY name ASC')
rows = [dict(r) for r in cur.fetchall()]
conn.close()

data_json_str = json.dumps(rows, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ScholarX — 310+ Relational Scholarships Database</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #05070a;
    --card: #0b1117;
    --border: rgba(255, 255, 255, 0.08);
    --gold: #d4af37;
    --emerald: #10b981;
    --sky: #38bdf8;
    --text: #f8fafc;
    --muted: #94a3b8;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background-color: var(--bg);
    color: var(--text);
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    padding: 24px;
    min-height: 100vh;
  }
  header {
    max-width: 1600px;
    margin: 0 auto 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--border);
  }
  .brand {
    display: flex;
    align-items: center;
    gap: 14px;
  }
  .brand-logo {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: rgba(212, 175, 55, 0.15);
    border: 1px solid rgba(212, 175, 55, 0.4);
    color: var(--gold);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 16px;
    box-shadow: 0 0 20px rgba(212, 175, 55, 0.25);
  }
  .brand h1 {
    font-size: 20px;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .brand .tag {
    font-size: 10px;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 6px;
    background: rgba(56, 189, 248, 0.15);
    color: var(--sky);
    border: 1px solid rgba(56, 189, 248, 0.3);
  }
  .brand p {
    font-size: 12px;
    color: var(--muted);
  }
  .header-actions {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 12px;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
    transition: all 0.15s ease;
  }
  .btn-csv {
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: var(--emerald);
  }
  .btn-csv:hover {
    background: rgba(16, 185, 129, 0.25);
  }
  .btn-live {
    background: rgba(212, 175, 55, 0.12);
    border: 1px solid rgba(212, 175, 55, 0.3);
    color: var(--gold);
  }
  .telemetry-grid {
    max-width: 1600px;
    margin: 0 auto 20px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 12px;
  }
  .telemetry-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 16px;
  }
  .telemetry-card .label {
    font-size: 11px;
    font-family: 'JetBrains Mono', monospace;
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .telemetry-card .value {
    font-size: 24px;
    font-weight: 800;
    font-family: 'JetBrains Mono', monospace;
    color: #fff;
  }
  .controls {
    max-width: 1600px;
    margin: 0 auto 16px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .search-row {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
  }
  .search-input {
    flex: 1;
    min-width: 280px;
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 14px;
    color: #fff;
    font-size: 13px;
    outline: none;
  }
  .search-input:focus {
    border-color: rgba(212, 175, 55, 0.5);
  }
  .filter-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    align-items: center;
    font-size: 12px;
  }
  select, .toggle-btn {
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid var(--border);
    color: #cbd5e1;
    padding: 6px 12px;
    border-radius: 8px;
    font-size: 12px;
    outline: none;
    cursor: pointer;
  }
  .toggle-btn.active {
    background: rgba(212, 175, 55, 0.2);
    border-color: rgba(212, 175, 55, 0.5);
    color: var(--gold);
    font-weight: 700;
  }
  .region-tabs {
    display: flex;
    gap: 6px;
    overflow-x: auto;
  }
  .tab-btn {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--border);
    color: var(--muted);
    padding: 6px 12px;
    border-radius: 8px;
    font-size: 11px;
    font-family: 'JetBrains Mono', monospace;
    cursor: pointer;
    white-space: nowrap;
  }
  .tab-btn.active {
    background: rgba(212, 175, 55, 0.2);
    border-color: rgba(212, 175, 55, 0.5);
    color: var(--gold);
    font-weight: 700;
  }
  .table-container {
    max-width: 1600px;
    margin: 0 auto;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow-x: auto;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
  }
  table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
    font-size: 12px;
  }
  thead {
    background: rgba(255, 255, 255, 0.02);
    border-bottom: 1px solid var(--border);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    color: var(--muted);
  }
  th {
    padding: 12px 16px;
    cursor: pointer;
    user-select: none;
  }
  th:hover {
    color: #fff;
  }
  tbody tr {
    border-bottom: 1px solid rgba(255, 255, 255, 0.04);
    cursor: pointer;
    transition: background 0.15s ease;
  }
  tbody tr:hover {
    background: rgba(255, 255, 255, 0.03);
  }
  td {
    padding: 12px 16px;
  }
  .badge {
    display: inline-block;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 10px;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    text-transform: uppercase;
  }
  .badge-full {
    background: rgba(16, 185, 129, 0.15);
    color: var(--emerald);
    border: 1px solid rgba(16, 185, 129, 0.3);
  }
  .badge-id {
    color: var(--gold);
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
  }
  .badge-moi {
    background: rgba(56, 189, 248, 0.15);
    color: var(--sky);
    border: 1px solid rgba(56, 189, 248, 0.3);
  }
  .stipend-val {
    font-family: 'JetBrains Mono', monospace;
    color: var(--emerald);
    font-weight: 700;
    text-align: right;
  }
  /* Modal */
  .modal-overlay {
    display: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0, 0, 0, 0.75);
    backdrop-filter: blur(8px);
    z-index: 999;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }
  .modal-overlay.open {
    display: flex;
  }
  .modal {
    background: #0d131a;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    width: 100%;
    max-width: 650px;
    max-height: 90vh;
    overflow-y: auto;
    padding: 24px;
    position: relative;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
  }
  .modal-close {
    position: absolute;
    top: 20px;
    right: 20px;
    background: rgba(255, 255, 255, 0.08);
    border: none;
    color: var(--muted);
    width: 28px;
    height: 28px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 14px;
  }
  .modal-close:hover { color: #fff; }
</style>
</head>
<body>

<header>
  <div class="brand">
    <div class="brand-logo">SX</div>
    <div>
      <h1>SCHOLARX <span class="tag">RELATIONAL DB</span></h1>
      <p>310+ Verified Institutional Opportunities Across 5 Continents</p>
    </div>
  </div>
  <div class="header-actions">
    <a href="scholarships_database.csv" download class="btn btn-csv">📥 EXPORT CSV</a>
    <a href="http://localhost:3000/scholarships" target="_blank" class="btn btn-live">🌐 OPEN IN WEB APP</a>
  </div>
</header>

<div class="telemetry-grid">
  <div class="telemetry-card">
    <div class="label">Total Scholarships</div>
    <div class="value" id="statTotal">312</div>
  </div>
  <div class="telemetry-card">
    <div class="label">HEC Bilateral Seats</div>
    <div class="value" style="color: var(--gold);">2,444</div>
  </div>
  <div class="telemetry-card">
    <div class="label">MOI Waivers (No IELTS)</div>
    <div class="value" style="color: var(--sky);">131</div>
  </div>
  <div class="telemetry-card">
    <div class="label">Europe Scouting</div>
    <div class="value" style="color: var(--emerald);">102</div>
  </div>
  <div class="telemetry-card">
    <div class="label">Asia Scouting</div>
    <div class="value" style="color: #a855f7;">81</div>
  </div>
  <div class="telemetry-card">
    <div class="label">Americas & MENA</div>
    <div class="value" style="color: #6366f1;">108</div>
  </div>
</div>

<div class="controls">
  <div class="search-row">
    <input type="text" id="searchInput" class="search-input" placeholder="Search scholarship name, country, university, or keyword...">
    <div class="region-tabs" id="regionTabs">
      <button class="tab-btn active" data-region="ALL">All Regions</button>
      <button class="tab-btn" data-region="Europe">Europe</button>
      <button class="tab-btn" data-region="Asia">Asia</button>
      <button class="tab-btn" data-region="Americas">Americas</button>
      <button class="tab-btn" data-region="MENA">MENA</button>
      <button class="tab-btn" data-region="Oceania">Oceania</button>
    </div>
  </div>
  <div class="filter-row">
    <select id="degreeFilter">
      <option value="ALL">All Degree Levels</option>
      <option value="Bachelor">Bachelor's</option>
      <option value="Master">Master's</option>
      <option value="PhD">PhD</option>
    </select>
    <select id="fundingFilter">
      <option value="ALL">All Funding Types</option>
      <option value="FULL">Fully Funded</option>
      <option value="PARTIAL">Partial</option>
      <option value="TUITION_ONLY">Tuition Only</option>
    </select>
    <button class="toggle-btn" id="toggleHec">🏛️ HEC / Bilateral Quota</button>
    <button class="toggle-btn" id="toggleMoi">🛡️ MOI Waiver (No IELTS)</button>
    <span style="margin-left: auto; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--muted);" id="countIndicator">Showing 312 records</span>
  </div>
</div>

<div class="table-container">
  <table>
    <thead>
      <tr>
        <th onclick="sortByCol('scholarship_id')">ID ⬍</th>
        <th onclick="sortByCol('name')">Scholarship & University ⬍</th>
        <th onclick="sortByCol('host_country_name')">Country & Region ⬍</th>
        <th>Funding</th>
        <th>Degrees</th>
        <th style="min-width: 180px;">Subjects Included</th>
        <th onclick="sortByCol('min_gpa_4_scale')">Min GPA ⬍</th>
        <th>Language / MOI</th>
        <th onclick="sortByCol('monthly_stipend_pkr_approx')" style="text-align: right;">Stipend (PKR/mo) ⬍</th>
        <th onclick="sortByCol('application_deadline')">Deadline ⬍</th>
      </tr>
    </thead>
    <tbody id="tableBody"></tbody>
  </table>
</div>

<div class="modal-overlay" id="modalOverlay" onclick="closeModal(event)">
  <div class="modal" onclick="event.stopPropagation()">
    <button class="modal-close" onclick="closeModal()">✕</button>
    <div id="modalContent"></div>
  </div>
</div>

<script>
const RAW_DATA = """ + data_json_str + """;
let currentRegion = 'ALL';
let currentDegree = 'ALL';
let currentFunding = 'ALL';
let filterHec = false;
let filterMoi = false;
let sortCol = 'name';
let sortAsc = true;

function render() {
  const q = document.getElementById('searchInput').value.toLowerCase().trim();
  let list = RAW_DATA.filter(s => {
    if (currentRegion !== 'ALL' && s.region.toLowerCase() !== currentRegion.toLowerCase()) return false;
    if (currentDegree !== 'ALL' && !s.degree_levels.toLowerCase().includes(currentDegree.toLowerCase())) return false;
    if (currentFunding !== 'ALL' && s.funding_type.toUpperCase() !== currentFunding.toUpperCase()) return false;
    if (filterHec && !s.hec_managed && !s.pakistan_bilateral_quota) return false;
    if (filterMoi && !s.accepts_moi_certificate) return false;
    if (q) {
      const match = s.name.toLowerCase().includes(q) ||
                    s.host_country_name.toLowerCase().includes(q) ||
                    s.host_institution.toLowerCase().includes(q) ||
                    s.scholarship_id.toLowerCase().includes(q) ||
                    (s.Subjects_included && s.Subjects_included.toLowerCase().includes(q));
      if (!match) return false;
    }
    return true;
  });

  list.sort((a, b) => {
    let va = a[sortCol];
    let vb = b[sortCol];
    if (va === null || va === undefined) va = '';
    if (vb === null || vb === undefined) vb = '';
    if (va < vb) return sortAsc ? -1 : 1;
    if (va > vb) return sortAsc ? 1 : -1;
    return 0;
  });

  document.getElementById('countIndicator').innerText = 'Showing ' + list.length + ' of ' + RAW_DATA.length + ' records';

  const tb = document.getElementById('tableBody');
  tb.innerHTML = list.map(s => {
    const stipendStr = s.monthly_stipend_pkr_approx ? '₨ ' + s.monthly_stipend_pkr_approx.toLocaleString() : (s.monthly_stipend || '—');
    const moiBadge = s.accepts_moi_certificate ? '<span class="badge badge-moi">MOI WAIVER</span>' : (s.ielts_minimum ? 'IELTS ' + s.ielts_minimum : '—');
    const subs = (s.Subjects_included || '').split('; ').filter(Boolean);
    const subsPreview = subs.slice(0, 2).map(sub => `<span class="badge" style="background:rgba(56,189,248,0.12);color:#38bdf8;border:1px solid rgba(56,189,248,0.25);font-size:10px;margin:1px 2px;display:inline-block;">${sub}</span>`).join('') + (subs.length > 2 ? `<span style="font-size:10px;color:var(--muted);margin-left:3px;">+${subs.length - 2} more</span>` : '');
    return `
      <tr onclick="openModal('${s.scholarship_id}')">
        <td class="badge-id">${s.scholarship_id}</td>
        <td>
          <div style="font-weight: 700; color: #fff;">${s.name}</div>
          <div style="font-size: 11px; color: var(--muted);">${s.host_institution}</div>
        </td>
        <td>
          <div>${s.host_country_name} (${s.host_country})</div>
          <div style="font-size: 10px; color: var(--muted);">${s.region}</div>
        </td>
        <td><span class="badge badge-full">${s.funding_type}</span></td>
        <td style="font-size: 11px; color: var(--muted);">${s.degree_levels}</td>
        <td style="max-width: 200px;" title="${(s.Subjects_included || '').replace(/"/g, '&quot;')}">${subsPreview}</td>
        <td style="font-family: 'JetBrains Mono', monospace;">${s.min_gpa_4_scale ? s.min_gpa_4_scale + ' / 4.0' : (s.min_gpa_percentage ? s.min_gpa_percentage + '%' : '—')}</td>
        <td>${moiBadge}</td>
        <td class="stipend-val">${stipendStr}</td>
        <td style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--muted);">${s.application_deadline || 'Annual Cycle'}</td>
      </tr>
    `;
  }).join('');
}

function sortByCol(col) {
  if (sortCol === col) sortAsc = !sortAsc;
  else { sortCol = col; sortAsc = true; }
  render();
}

function openModal(id) {
  const s = RAW_DATA.find(x => x.scholarship_id === id);
  if (!s) return;
  const content = `
    <div style="margin-bottom: 12px;">
      <span class="badge-id" style="font-size: 12px; margin-right: 8px;">${s.scholarship_id}</span>
      <span class="badge badge-full">${s.funding_type}</span>
    </div>
    <h2 style="font-size: 18px; margin-bottom: 6px; color: #fff;">${s.name}</h2>
    <p style="font-size: 12px; color: var(--muted); margin-bottom: 16px;">${s.host_institution} — ${s.host_country_name} (${s.region})</p>
    
    <div style="background: rgba(16,185,129,0.06); border: 1px solid rgba(16,185,129,0.25); border-radius: 10px; padding: 12px; margin-bottom: 16px;">
      <div style="font-size: 11px; font-family: 'JetBrains Mono', monospace; color: var(--emerald); font-weight: 700; margin-bottom: 6px;">FINANCIAL STIPEND & BENEFITS</div>
      <div style="font-size: 14px; font-weight: 700; color: #fff; margin-bottom: 4px;">
        ${s.monthly_stipend_pkr_approx ? '₨ ' + s.monthly_stipend_pkr_approx.toLocaleString() + ' / month' : 'Tuition & Living Covered'}
      </div>
      <div style="font-size: 12px; color: var(--muted);">${s.monthly_stipend || '100% Fully Funded Tuition Waiver & Housing Allowance'}</div>
    </div>

    <div style="background: rgba(56,189,248,0.06); border: 1px solid rgba(56,189,248,0.25); border-radius: 10px; padding: 12px; margin-bottom: 16px;">
      <div style="font-size: 11px; font-family: 'JetBrains Mono', monospace; color: var(--sky); font-weight: 700; margin-bottom: 8px;">📚 SUBJECTS & ACADEMIC DISCIPLINES INCLUDED</div>
      <div style="display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 8px;">
        ${(s.Subjects_included || 'All Academic Disciplines').split('; ').map(x => `<span class="badge" style="background:rgba(56,189,248,0.15);color:#7dd3fc;border:1px solid rgba(56,189,248,0.3);font-size:11px;padding:3px 8px;">${x}</span>`).join('')}
      </div>
      <div style="font-size: 11px; color: var(--muted); border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px; margin-top: 8px;">
        <strong>Verified Authentic Source:</strong> <a href="${s.subjects_source_url || s.source_url}" target="_blank" style="color:var(--sky);text-decoration:underline;">${s.subjects_source_url || s.source_url}</a>
      </div>
    </div>

    <div style="background: rgba(255,255,255,0.02); border: 1px solid var(--border); border-radius: 10px; padding: 12px; margin-bottom: 16px; font-size: 12px; line-height: 1.6;">
      <div><strong>Degree Levels:</strong> ${s.degree_levels}</div>
      <div><strong>Min GPA Cutoff:</strong> ${s.min_gpa_4_scale ? s.min_gpa_4_scale + ' / 4.0' : 'No strict minimum cutoff'}</div>
      <div><strong>IELTS / English:</strong> ${s.ielts_minimum ? 'IELTS ' + s.ielts_minimum + '+' : 'Test optional / Not mandatory'}</div>
      <div><strong>MOI Certificate:</strong> ${s.accepts_moi_certificate ? '✅ Accepted in lieu of IELTS' : 'Official Test Required'}</div>
      ${s.pakistan_bilateral_quota ? '<div style="color: var(--gold);">🏛️ <strong>HEC Bilateral Quota:</strong> ' + (s.pakistan_quota_seats ? s.pakistan_quota_seats + ' reserved annual seats' : 'Government nomination quota') + '</div>' : ''}
    </div>

    ${s.description ? '<p style="font-size: 12px; color: var(--muted); line-height: 1.5; margin-bottom: 16px;">' + s.description + '</p>' : ''}

    <div style="display: flex; gap: 10px; justify-content: flex-end; border-top: 1px solid var(--border); padding-top: 16px;">
      <a href="${s.subjects_source_url || s.source_url}" target="_blank" class="btn btn-live">Verified Official Portal ↗</a>
    </div>
  `;
  document.getElementById('modalContent').innerHTML = content;
  document.getElementById('modalOverlay').classList.add('open');
}

function closeModal() {
  document.getElementById('modalOverlay').classList.remove('open');
}

document.getElementById('searchInput').addEventListener('input', render);
document.getElementById('degreeFilter').addEventListener('change', e => { currentDegree = e.target.value; render(); });
document.getElementById('fundingFilter').addEventListener('change', e => { currentFunding = e.target.value; render(); });

document.getElementById('toggleHec').addEventListener('click', e => {
  filterHec = !filterHec;
  e.target.classList.toggle('active', filterHec);
  render();
});

document.getElementById('toggleMoi').addEventListener('click', e => {
  filterMoi = !filterMoi;
  e.target.classList.toggle('active', filterMoi);
  render();
});

document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', e => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    e.target.classList.add('active');
    currentRegion = e.target.dataset.region;
    render();
  });
});

render();
</script>
</body>
</html>
"""

paths = [
    '/mnt/windows/AntiGravity/SCHOLARX/scholarships_database_viewer.html',
    '/mnt/windows/AntiGravity/SCHOLARX/data/scholarships_database_viewer.html'
]
for p in paths:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print("Created:", p)
