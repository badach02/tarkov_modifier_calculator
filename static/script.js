function calc() {
  let total = 0;

  document.querySelectorAll('.mod:checked').forEach((box) => {
    total += parseInt(box.dataset.v, 10);
  });

  const scoreEl = document.getElementById('score');
  const statusEl = document.getElementById('status');

  scoreEl.textContent = total;
  const valid = total > 0;

  statusEl.textContent = valid ? 'VALID' : 'INVALID';
  statusEl.className = `status-pill ${valid ? 'valid' : 'invalid'}`;
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