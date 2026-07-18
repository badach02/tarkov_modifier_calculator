const SHARE_PARAM = 'm';
const SHARE_VERSION = '1';

function modifierBoxes() {
  return Array.from(document.querySelectorAll('.mod'));
}

function modifierOrder() {
  return modifierBoxes().sort((a, b) => a.dataset.key.localeCompare(b.dataset.key));
}

function updateShareUrl() {
  const ordered = modifierOrder();
  let mask = 0n;

  ordered.forEach((box, index) => {
    if (box.checked) mask |= 1n << BigInt(index);
  });

  const url = new URL(window.location.href);
  if (mask === 0n) {
    url.searchParams.delete(SHARE_PARAM);
  } else {
    url.searchParams.set(SHARE_PARAM, `${SHARE_VERSION}-${mask.toString(16)}`);
  }
  window.history.replaceState(null, '', url);
}

function restoreFromUrl() {
  const encoded = new URL(window.location.href).searchParams.get(SHARE_PARAM);
  modifierBoxes().forEach((box) => { box.checked = false; });
  if (!encoded) return;

  const match = encoded.match(/^1-([0-9a-f]+)$/i);
  if (!match) return;

  try {
    const mask = BigInt(`0x${match[1]}`);
    const ordered = modifierOrder();
    if (mask === 0n || (mask >> BigInt(ordered.length)) !== 0n) return;
    ordered.forEach((box, index) => {
      box.checked = (mask & (1n << BigInt(index))) !== 0n;
    });
  } catch {
    modifierBoxes().forEach((box) => { box.checked = false; });
  }
}

function syncModifierStates() {
  document.querySelectorAll('.modifier-card').forEach((card) => {
    const box = card.querySelector('.mod');
    if (!box) return;

    const isChecked = box.checked;
    const value = parseInt(box.dataset.v, 10);
    const isNegative = value > 0;

    card.classList.toggle('is-selected', isChecked);
    card.classList.toggle('is-negative', isChecked && isNegative);
    card.classList.toggle('is-positive', isChecked && !isNegative);
  });
}

function calc() {
  let total = 0;

  document.querySelectorAll('.mod:checked').forEach((box) => {
    total += parseInt(box.dataset.v, 10);
  });

  const scoreEl = document.getElementById('score');
  const statusEl = document.getElementById('status');

  scoreEl.textContent = total;
  const valid = total >= 0;

  statusEl.textContent = valid ? 'VALID' : 'INVALID';
  statusEl.className = `status-pill ${valid ? 'valid' : 'invalid'}`;
  const bottomScoreEl = document.getElementById('bottom-score');
  const bottomStatusEl = document.getElementById('bottom-status');
  if (bottomScoreEl) bottomScoreEl.textContent = total;
  if (bottomStatusEl) {
    bottomStatusEl.textContent = valid ? 'VALID' : 'INVALID';
    bottomStatusEl.className = `status-pill ${valid ? 'valid' : 'invalid'}`;
  }
  syncModifierStates();
  updateShareUrl();
}

function clearModifiers() {
  document.querySelectorAll('.mod').forEach((box) => {
    box.checked = false;
  });
  calc();
}

async function copyShareLink(buttonId = 'copy-link-btn') {
  const button = document.getElementById(buttonId);
  try {
    await navigator.clipboard.writeText(window.location.href);
    button.textContent = 'Link Copied';
    setTimeout(() => { button.textContent = 'Copy Share Link'; }, 1600);
  } catch {
    button.textContent = 'Copy Failed';
    setTimeout(() => { button.textContent = 'Copy Share Link'; }, 1600);
  }
}

function exportSummary(buttonId = 'summary-btn') {
  const button = document.getElementById(buttonId);
  const selected = document.querySelector('.mod:checked');
  const score = Number.parseInt(document.getElementById('score').textContent, 10);
  if (!selected || score < 0) {
    button.textContent = selected ? 'Build Invalid' : 'Select Modifiers';
    setTimeout(() => { button.textContent = 'Export Summary'; }, 1600);
    return;
  }

  const summaryUrl = new URL('/summary', window.location.origin);
  const selection = new URL(window.location.href).searchParams.get(SHARE_PARAM);
  if (selection) summaryUrl.searchParams.set(SHARE_PARAM, selection);
  window.open(summaryUrl.toString(), '_blank', 'noopener,noreferrer');
}

restoreFromUrl();
document.querySelectorAll('.mod').forEach((box) => {
  box.addEventListener('change', calc);
});

calc();
