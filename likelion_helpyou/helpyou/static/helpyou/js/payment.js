const buttons = document.querySelectorAll('.payment-buttons button');
buttons.forEach(button => {
    button.addEventListener('click', () => {
        buttons.forEach(btn => {
            btn.style.borderWidth = '1px';
        });

        button.style.borderWidth = '5px';
        button.style.borderColor = 'green';
    });
});



// select
function benefit() {
  document.querySelector('.discount-card-container').style.display = 'flex';
  document.querySelector('.no-benefit-container').style.display = 'none';
  document.querySelector('.card-select').style.display = 'block';

  var selectElement = document.querySelector('.card-select select');
  selectElement.selectedIndex = 0;

  updatePriceDisplay();
}

function none() {
  document.querySelector('.discount-card-container').style.display = 'none';
  document.querySelector('.no-benefit-container').style.display = 'block';
  document.querySelector('.card-select').style.display = 'none';

  // 가격 초기화
  resetPriceDisplay();
}

// 가격 변동 업데이트
function updatePriceDisplay() {
  const selectedOption = selectElement.value;
  if (selectedOption === '0') {
    span1.style.display = 'inline';
    span2.style.display = 'none';
  } else if (selectedOption === '3000') {
    span1.style.display = 'none';
    span2.style.display = 'inline';
  } else {
    span1.style.display = 'none';
    span2.style.display = 'none';
  }
}

// 가격 초기화
function resetPriceDisplay() {
  span1.style.display = 'inline';
  span2.style.display = 'none';
}

// 할인 적용시키기
const selectElement = document.getElementById('discount');
const span1 = document.getElementById('right-total');
const span2 = document.getElementById('discount-total');

span1.style.display = 'inline';

selectElement.addEventListener('change', () => {
  updatePriceDisplay();
});

// 태훈
document.addEventListener("DOMContentLoaded", function() {
    var pGuide = document.getElementById("pGuide");
    var popover1 = new bootstrap.Popover(pGuide);

    var benefit = document.getElementById("benefit");
    var popover2 = new bootstrap.Popover(benefit);

    var payPopover = document.getElementById("payPopover");
    var popover3 = new bootstrap.Popover(payPopover);

    popover1.show();
    popover2.show();

    discount.addEventListener("click", function() {
      payPopover.removeAttribute("disabled");
      popover2.hide();
      popover3.show();
    });
  });




