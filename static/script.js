// Flash message auto-dismiss
document.addEventListener('DOMContentLoaded', function () {
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.style.transition = "opacity 0.5s ease-out";
      alert.style.opacity = '0';
      setTimeout(() => alert.remove(), 500);
    }, 4000);
  });
});

// Confirm before delete/ban actions (if not already done inline)
document.querySelectorAll('form[method="POST"]').forEach(form => {
  const btn = form.querySelector('button');
  if (btn && btn.classList.contains('btn-danger')) {
    btn.addEventListener('click', (e) => {
      if (!confirm("Are you sure you want to proceed with this action?")) {
        e.preventDefault();
      }
    });
  }
});
