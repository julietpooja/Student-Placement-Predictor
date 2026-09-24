<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Placement Fit Report</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.6.0/mammoth.browser.min.js"></script>
<style>
:root{
  --bg:#F5F6F2; --panel:#FFFFFF; --ink:#1B1F23; --muted:#5C6570;
  --accent:#1F4E42; --accent-soft:#E4ECE8; --warn:#A63D2F; --warn-soft:#F3E4E0;
  --line:#DCDFD9; --radius:2px;
  padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px);
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){ } }
*{box-sizing:border-box;}
html,body{margin:0;background:var(--bg);color:var(--ink);}
body{font-family:'Inter',system-ui,sans-serif;font-size:15px;line-height:1.55;}
h1,h2,h3{font-family:'Fraunces',serif;font-weight:600;margin:0;}
.wrap{max-width:1180px;margin:0 auto;padding:36px 24px 60px;}
header.top{display:flex;align-items:baseline;justify-content:space-between;border-bottom:1px solid var(--line);padding-bottom:18px;margin-bottom:32px;gap:16px;flex-wrap:wrap;}
header.top h1{font-size:28px;letter-spacing:-0.01em;}
header.top p{margin:4px 0 0;color:var(--muted);font-size:13.5px;max-width:420px;}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start;}
@media (max-width:880px){.grid{grid-template-columns:1fr;}}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);}
.step{border-bottom:1px solid var(--line);padding:20px 22px;}
.step:last-child{border-bottom:none;}
.step .num{display:inline-block;font-family:'Fraunces',serif;font-size:13px;color:var(--accent);border:1px solid var(--accent);width:22px;height:22px;line-height:20px;text-align:center;border-radius:50%;margin-right:8px;}
.step label.title{font-weight:600;font-size:14.5px;}
.step .hint{color:var(--muted);font-size:12.5px;margin:4px 0 10px 30px;}
.field{margin-left:30px;}
input[type=text],input[type=url],textarea{
  width:100%;border:1px solid var(--line);border-radius:var(--radius);padding:10px 12px;
  font-family:'Inter',sans-serif;font-size:14px;color:var(--ink);background:#FCFCFB;
}
textarea{min-height:84px;resize:vertical;}
input:focus,textarea:focus,button:focus-visible{outline:2px solid var(--accent);outline-offset:1px;}
.row-inline{display:flex;gap:8px;margin-bottom:8px;}
.row-inline input{flex:1;}
.row-inline button.rm{border:1px solid var(--line);background:#fff;color:var(--muted);width:36px;border-radius:var(--radius);cursor:pointer;}
button.add{margin-left:30px;border:1px dashed var(--line);background:transparent;color:var(--accent);font-size:13px;padding:7px 12px;border-radius:var(--radius);cursor:pointer;font-weight:500;}
button.add:hover{background:var(--accent-soft);}
.filebox{margin-left:30px;border:1px dashed var(--line);border-radius:var(--radius);padding:14px;font-size:13px;color:var(--muted);cursor:pointer;background:#FCFCFB;}
.filebox.has-file{color:var(--ink);border-style:solid;border-color:var(--accent);}
.file-status{margin:6px 0 0 30px;font-size:12px;color:var(--muted);}
.analyze-bar{padding:20px 22px;}
button.primary{width:100%;background:var(--accent);color:#fff;border:none;padding:13px;font-size:14.5px;font-weight:600;border-radius:var(--radius);cursor:pointer;font-family:'Inter',sans-serif;}
button.primary:disabled{opacity:.55;cursor:not-allowed;}
button.primary:hover:not(:disabled){background:#173a31;}
.error-msg{color:var(--warn);font-size:12.5px;margin-top:8px;}
.report{min-height:480px;padding:24px;}
.report-empty{color:var(--muted);font-size:14px;display:flex;flex-direction:column;align-items:flex-start;justify-content:center;min-height:440px;gap:8px;}
.report-empty h3{color:var(--ink);font-size:18px;font-weight:600;}
.loading{display:flex;flex-direction:column;gap:10px;align-items:flex-start;min-height:440px;justify-content:center;color:var(--muted);font-size:14px;}
.spin{width:22px;height:22px;border:2px solid var(--line);border-top-color:var(--accent);border-radius:50%;animation:sp .8s linear infinite;}
@keyframes sp{to{transform:rotate(360deg);}}
.verdict{display:flex;align-items:center;gap:14px;margin-bottom:6px;}
.score-badge{font-family:'Fraunces',serif;font-size:34px;font-weight:700;}
.verdict-label{font-size:15px;font-weight:600;}
.verdict-sub{color:var(--muted);font-size:13px;margin:0 0 22px;}
.match .score-badge, .match .verdict-label{color:var(--accent);}
.nomatch .score-badge, .nomatch .verdict-label{color:var(--warn);}
.factor{border-top:1px solid var(--line);padding:16px 0;}
.factor-head{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px;}
.factor-head h4{font-family:'Inter',sans-serif;font-weight:600;font-size:13.5px;}
.factor-score{font-size:12.5px;font-weight:600;padding:2px 8px;border-radius:10px;}
.fs-strong{background:var(--accent-soft);color:var(--accent);}
.fs-weak{background:var(--warn-soft);color:var(--warn);}
.fs-mid{background:#EFEFEA;color:var(--muted);}
.factor p{margin:0;font-size:13.5px;color:#333;}
.factor .gap{color:var(--warn);margin-top:6px;font-size:13px;}
.factor .caveat{color:var(--muted);font-size:11.5px;margin-top:6px;font-style:italic;}
.reco{background:var(--accent-soft);border-radius:var(--radius);padding:16px;margin-top:18px;font-size:13.5px;}
.reco h4{font-size:13px;margin-bottom:8px;}
footer.note{margin-top:26px;color:var(--muted);font-size:12px;border-top:1px solid var(--line);padding-top:14px;}
</style>
</head>
<body>
<div class="wrap">
  <header class="top">
    <div>
      <h1>Placement Fit Report</h1>
      <p>Bring together a candidate's resume, GitHub, LinkedIn and coding-platform links against one job description, and get a factor-by-factor fit explanation.</p>
    </div>
  </header>

  <div class="grid">
    <div class="panel">
      <div class="step">
        <span class="num">1</span><label class="title">GitHub profile</label>
        <p class="hint">Link to the candidate's GitHub profile</p>
        <div class="field"><input type="url" id="githubLink" placeholder="https://github.com/username"></div>
      </div>

      <div class="step">
        <span class="num">2</span><label class="title">Resume</label>
        <p class="hint">PDF or DOCX — text is extracted in your browser, nothing is uploaded elsewhere</p>
        <div class="field">
          <div class="filebox" id="fileBox" tabindex="0" role="button">Click to choose a .pdf or .docx file</div>
          <input type="file" id="resumeFile" accept=".pdf,.docx" style="display:none">
          <div class="file-status" id="fileStatus"></div>
        </div>
      </div>

      <div class="step">
        <span class="num">3</span><label class="title">Coding platform profiles</label>
        <p class="hint">LeetCode, HackerRank, Codeforces, etc.</p>
        <div class="field" id="platformList"></div>
        <button class="add" id="addPlatform" type="button">+ Add platform link</button>
      </div>

      <div class="step">
        <span class="num">4</span><label class="title">Aptitude test paper</label>
        <p class="hint">Optional — upload a completed aptitude test or its scorecard (PDF or DOCX) so the aptitude factor is measured, not just inferred</p>
        <div class="field">
          <div class="filebox" id="aptitudeBox" tabindex="0" role="button">Click to choose a .pdf or .docx file</div>
          <input type="file" id="aptitudeFile" accept=".pdf,.docx" style="display:none">
          <div class="file-status" id="aptitudeStatus"></div>
        </div>
      </div>

      <div class="step">
        <span class="num">5</span><label class="title">LinkedIn profile</label>
        <p class="hint">Link to the candidate's LinkedIn</p>
        <div class="field"><input type="url" id="linkedinLink" placeholder="https://linkedin.com/in/username"></div>
      </div>

      <div class="step">
        <span class="num">6</span><label class="title">Extra profile detail</label>
        <p class="hint">Optional — paste README highlights, pinned-project blurbs, LinkedIn summary or coding-platform stats. Browser security blocks live scraping of these sites, so pasted text sharpens the read.</p>
        <div class="field"><textarea id="extraContext" placeholder="e.g. Pinned repos: a React e-commerce app with Stripe integration, 40 solved LeetCode mediums, LinkedIn headline: 'Aspiring backend engineer'..."></textarea></div>
      </div>

      <div class="step">
        <span class="num">7</span><label class="title">Job description</label>
        <p class="hint">Paste the full JD to match against</p>
        <div class="field"><textarea id="jobDesc" style="min-height:140px" placeholder="Paste the job description here..."></textarea></div>
      </div>

      <div class="analyze-bar">
        <button class="primary" id="analyzeBtn" type="button">Analyze fit</button>
        <div class="error-msg" id="errorMsg" style="display:none"></div>
      </div>
    </div>

    <div class="panel report" id="reportPanel">
      <div class="report-empty" id="reportEmpty">
        <h3>Report appears here</h3>
        <p>Fill in the resume and job description at minimum, then run the analysis. The report breaks the match down by projects, aptitude signal, soft skills, coding knowledge and problem-solving — each with the evidence behind it.</p>
      </div>
    </div>
  </div>
  <footer class="note">Resume text is parsed locally in your browser. Link fields and pasted text are passed to the model as candidate-supplied context, not independently verified.</footer>
</div>

<script>
let resumeText = "";
let aptitudeText = "";
const platformList = document.getElementById('platformList');

async function extractTextFromFile(f){
  if(f.name.toLowerCase().endsWith('.pdf')){
    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
    const buf = await f.arrayBuffer();
    const pdf = await pdfjsLib.getDocument({data:buf}).promise;
    let out = [];
    for(let i=1;i<=pdf.numPages;i++){
      const page = await pdf.getPage(i);
      const content = await page.getTextContent();
      out.push(content.items.map(it=>it.str).join(' '));
    }
    return out.join('\n');
  } else if(f.name.toLowerCase().endsWith('.docx')){
    const buf = await f.arrayBuffer();
    const result = await mammoth.extractRawText({arrayBuffer: buf});
    return result.value;
  }
  throw new Error('unsupported');
}

function addPlatformRow(){
  const row = document.createElement('div');
  row.className = 'row-inline';
  row.innerHTML = `<input type="text" class="pf-name" placeholder="Platform (e.g. LeetCode)" style="max-width:150px">
    <input type="url" class="pf-url" placeholder="Profile link">
    <button class="rm" type="button" aria-label="Remove">×</button>`;
  row.querySelector('.rm').onclick = () => row.remove();
  platformList.appendChild(row);
}
document.getElementById('addPlatform').onclick = addPlatformRow;
addPlatformRow();

const fileBox = document.getElementById('fileBox');
const fileInput = document.getElementById('resumeFile');
const fileStatus = document.getElementById('fileStatus');
fileBox.onclick = () => fileInput.click();
fileBox.onkeydown = e => { if(e.key==='Enter' || e.key===' ') fileInput.click(); };

fileInput.onchange = async () => {
  const f = fileInput.files[0];
  if(!f) return;
  fileStatus.textContent = 'Reading ' + f.name + '...';
  resumeText = "";
  try{
    resumeText = await extractTextFromFile(f);
    if(!resumeText.trim()) throw new Error('empty');
    fileBox.classList.add('has-file');
    fileBox.textContent = f.name;
    fileStatus.textContent = resumeText.length + ' characters extracted';
  }catch(err){
    fileBox.classList.remove('has-file');
    fileStatus.textContent = 'Could not read that file. Please upload a text-based .pdf or .docx.';
    resumeText = "";
  }
};

const aptitudeBox = document.getElementById('aptitudeBox');
const aptitudeInput = document.getElementById('aptitudeFile');
const aptitudeStatus = document.getElementById('aptitudeStatus');
aptitudeBox.onclick = () => aptitudeInput.click();
aptitudeBox.onkeydown = e => { if(e.key==='Enter' || e.key===' ') aptitudeInput.click(); };

aptitudeInput.onchange = async () => {
  const f = aptitudeInput.files[0];
  if(!f) return;
  aptitudeStatus.textContent = 'Reading ' + f.name + '...';
  aptitudeText = "";
  try{
    aptitudeText = await extractTextFromFile(f);
    if(!aptitudeText.trim()) throw new Error('empty');
    aptitudeBox.classList.add('has-file');
    aptitudeBox.textContent = f.name;
    aptitudeStatus.textContent = aptitudeText.length + ' characters extracted';
  }catch(err){
    aptitudeBox.classList.remove('has-file');
    aptitudeStatus.textContent = 'Could not read that file. Please upload a text-based .pdf or .docx.';
    aptitudeText = "";
  }
};

function showError(msg){
  const e = document.getElementById('errorMsg');
  e.textContent = msg; e.style.display = 'block';
}
function clearError(){
  document.getElementById('errorMsg').style.display = 'none';
}

function scoreClass(s){
  if(s >= 70) return 'fs-strong';
  if(s >= 40) return 'fs-mid';
  return 'fs-weak';
}

function renderReport(data){
  const panel = document.getElementById('reportPanel');
  const isMatch = data.overallScore >= 60;
  let html = `<div class="${isMatch?'match':'nomatch'}">
    <div class="verdict"><div class="score-badge">${data.overallScore}%</div>
      <div><div class="verdict-label">${isMatch?'Matches the role':'Does not match the role'}</div></div>
    </div>
    <p class="verdict-sub">${escapeHtml(data.summary)}</p>
  </div>`;

  const labels = {
    projects:'Project details', aptitude:'Aptitude signal',
    softSkills:'Soft skills', coding:'Coding knowledge',
    problemSolving:'Real-time problem solving'
  };
  for(const key of ['projects','aptitude','softSkills','coding','problemSolving']){
    const f = data.factors[key];
    if(!f) continue;
    html += `<div class="factor">
      <div class="factor-head"><h4>${labels[key]}</h4><span class="factor-score ${scoreClass(f.score)}">${f.score}/100</span></div>
      <p>${escapeHtml(f.evidence)}</p>
      ${f.gap ? `<p class="gap">Gap: ${escapeHtml(f.gap)}</p>` : ''}
      ${f.caveat ? `<p class="caveat">${escapeHtml(f.caveat)}</p>` : ''}
    </div>`;
  }

  if(data.recommendations && data.recommendations.length){
    html += `<div class="reco"><h4>To close the gap</h4><p>${data.recommendations.map(escapeHtml).join(' · ')}</p></div>`;
  }
  panel.innerHTML = html;
}

function escapeHtml(s){
  return (s||'').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

document.getElementById('analyzeBtn').onclick = async () => {
  clearError();
  const jobDesc = document.getElementById('jobDesc').value.trim();
  if(!resumeText){ showError('Please upload a readable resume first.'); return; }
  if(!jobDesc){ showError('Please paste a job description.'); return; }

  const github = document.getElementById('githubLink').value.trim();
  const linkedin = document.getElementById('linkedinLink').value.trim();
  const extra = document.getElementById('extraContext').value.trim();
  const platforms = Array.from(platformList.querySelectorAll('.row-inline')).map(r => {
    const n = r.querySelector('.pf-name').value.trim();
    const u = r.querySelector('.pf-url').value.trim();
    return (n||u) ? `${n||'Platform'}: ${u}` : null;
  }).filter(Boolean);

  const btn = document.getElementById('analyzeBtn');
  btn.disabled = true; btn.textContent = 'Analyzing...';
  const panel = document.getElementById('reportPanel');
  panel.innerHTML = `<div class="loading"><div class="spin"></div><div>Reading the profile against the job description...</div></div>`;

  try{
    const sample = await claude.use('sample');
    if(!sample) throw new Error('unavailable');

    const prompt = `You are an explainable placement-fit evaluator for a student/early-career candidate. Compare the candidate's material below against the job description, and return ONLY a JSON object (no markdown fences, no prose) with this exact shape:
{
 "overallScore": <0-100 integer>,
 "summary": "<1-2 sentence verdict>",
 "factors": {
   "projects": {"score":<0-100>, "evidence":"<what in their projects supports or hurts fit, cite specifics>", "gap":"<what's missing, or empty string>"},
   "aptitude": {"score":<0-100>, "evidence":"<if an aptitude test paper is supplied below, base this on its actual questions/answers/results; otherwise infer from resume achievements, academic record, project complexity>", "gap":"<or empty>", "caveat":"<if a test paper was supplied, note it's measured from that paper; otherwise say 'Inferred from available material, not a tested score.'>"},
   "softSkills": {"score":<0-100>, "evidence":"<evidence of communication, leadership, teamwork from resume/profile text>", "gap":"<or empty>"},
   "coding": {"score":<0-100>, "evidence":"<languages, frameworks, platform stats if given>", "gap":"<or empty>"},
   "problemSolving": {"score":<0-100>, "evidence":"<evidence from projects/competitive coding results>", "gap":"<or empty>", "caveat":"Inferred from static material, not a live coding assessment."}
 },
 "recommendations": ["<short actionable step>", "..."]
}
Ground every "evidence" and "gap" string in specifics from the candidate material below — name actual projects, skills, or phrases. If the profile does not match, the "gap" fields must explain why using those specifics (explainable AI).

JOB DESCRIPTION:
${jobDesc}

CANDIDATE RESUME TEXT:
${resumeText.slice(0,6000)}

CANDIDATE LINKS:
GitHub: ${github||'(not provided)'}
LinkedIn: ${linkedin||'(not provided)'}
Coding platforms: ${platforms.join('; ')||'(not provided)'}

APTITUDE TEST PAPER (questions/answers/results, if supplied):
${aptitudeText ? aptitudeText.slice(0,4000) : '(not provided — infer aptitude from resume/projects instead)'}

ADDITIONAL PASTED CONTEXT:
${extra||'(none provided)'}`;

    const result = await sample.json(prompt, {modelTier:'default'});
    renderReport(result);
  }catch(err){
    panel.innerHTML = `<div class="report-empty"><h3>Couldn't complete the analysis</h3><p>${err && err.code==='not_granted' ? 'This page needs permission to ask Claude — please allow it and try again.' : 'Something went wrong reaching the model. Please try again.'}</p></div>`;
  } finally{
    btn.disabled = false; btn.textContent = 'Analyze fit';
  }
};
</script>
</body>
</html>
