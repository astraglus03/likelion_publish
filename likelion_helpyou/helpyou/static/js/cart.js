const linkedCheckboxes = document.querySelectorAll('.check-check');

function handleLinkedCheckboxChange() {
  const isChecked = this.checked;

  linkedCheckboxes.forEach((checkbox) => {
    checkbox.checked = isChecked;
  });
}

function uncheckAll() {
  linkedCheckboxes.forEach((checkbox) => {
    checkbox.checked = false;
  });
}

linkedCheckboxes.forEach((checkbox) => {
  checkbox.addEventListener('change', handleLinkedCheckboxChange);
});

linkedCheckboxes.forEach((checkbox) => {
  checkbox.addEventListener('change', () => {
    if (!linkedCheckboxes.some((checkbox) => checkbox.checked)) {
      uncheckAll();
    }
  });
});

$(document).ready(function() {
        var cartPopover = $("#cartPopover");
        var popover1 = new bootstrap.Popover(cartPopover);

        var scrollGuide = $("#scrollGuide");
        var popover2 = new bootstrap.Popover(scrollGuide);

        popover2.show();
        popover1.show();
});
