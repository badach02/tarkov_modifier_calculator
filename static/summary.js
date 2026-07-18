const SUMMARY_PARAM = 'm';
const SUMMARY_VERSION = '1';

function orderedSummaryModifiers() {
  const data = JSON.parse(document.getElementById('summary-data').textContent);
  return [...data.positive, ...data.negative].sort((a, b) => a.key.localeCompare(b.key));
}

function selectedSummaryModifiers() {
  const encoded = new URL(window.location.href).searchParams.get(SUMMARY_PARAM);
  if (!encoded) return { valid: false, selected: [] };

  const match = encoded.match(/^1-([0-9a-f]+)$/i);
  if (!match) return { valid: false, selected: [] };

  try {
    const all = orderedSummaryModifiers();
    const mask = BigInt(`0x${match[1]}`);
    if (mask === 0n || (mask >> BigInt(all.length)) !== 0n) {
      return { valid: false, selected: [] };
    }
    return {
      valid: true,
      selected: all.filter((modifier, index) => (mask & (1n << BigInt(index))) !== 0n),
    };
  } catch {
    return { valid: false, selected: [] };
  }
}

function renderSummaryCard(modifier) {
  const card = document.createElement('article');
  card.className = 'summary-modifier';
  card.innerHTML = `
    <img src="/static/${modifier.icon}" alt="${modifier.name} icon" class="summary-modifier-icon">
    <div class="summary-modifier-content">
      <div class="summary-modifier-title">
        <strong>${modifier.name}</strong>
        <span>${modifier.value > 0 ? '+' : ''}${modifier.value}</span>
      </div>
      <p>${modifier.description}</p>
    </div>`;
  return card;
}

function renderSummary() {
  const result = selectedSummaryModifiers();
  const error = document.getElementById('summary-error');
  const layout = document.getElementById('summary-layout');
  if (!result.valid) {
    error.hidden = false;
    layout.hidden = true;
    return;
  }

  const positive = result.selected.filter((modifier) => modifier.value < 0);
  const negative = result.selected.filter((modifier) => modifier.value > 0);
  const total = result.selected.reduce((sum, modifier) => sum + modifier.value, 0);
  document.getElementById('summary-score').textContent = total;
  document.getElementById('positive-total').textContent = positive.reduce((sum, modifier) => sum + modifier.value, 0);
  document.getElementById('negative-total').textContent = `+${negative.reduce((sum, modifier) => sum + modifier.value, 0)}`;
  positive.forEach((modifier) => document.getElementById('positive-modifiers').appendChild(renderSummaryCard(modifier)));
  negative.forEach((modifier) => document.getElementById('negative-modifiers').appendChild(renderSummaryCard(modifier)));

  const backUrl = new URL('/', window.location.origin);
  backUrl.searchParams.set(SUMMARY_PARAM, new URL(window.location.href).searchParams.get(SUMMARY_PARAM));
  document.getElementById('back-to-calculator').href = backUrl.toString();
}

async function copySummaryLink() {
  const button = document.querySelector('.summary-actions .copy-btn');
  try {
    await navigator.clipboard.writeText(window.location.href);
    button.textContent = 'Link Copied';
    setTimeout(() => { button.textContent = 'Copy Link'; }, 1600);
  } catch {
    button.textContent = 'Copy Failed';
    setTimeout(() => { button.textContent = 'Copy Link'; }, 1600);
  }
}

renderSummary();
