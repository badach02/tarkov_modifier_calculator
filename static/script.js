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
  syncModifierStates();
}

function clearModifiers() {
  document.querySelectorAll('.mod').forEach((box) => {
    box.checked = false;
  });
  calc();
}

document.querySelectorAll('.mod').forEach((box) => {
  box.addEventListener('change', calc);
});

calc();