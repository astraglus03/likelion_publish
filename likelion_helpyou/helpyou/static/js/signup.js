$(document).ready(function() {
        var checkDuplicate = $("#checkDuplicate");
        var popover1 = new bootstrap.Popover(checkDuplicate);

        var password1 = $("#password1");
        var popover2 = new bootstrap.Popover(password1);

        var password2 = $("#password2");
        var popover3 = new bootstrap.Popover(password2);

        var fullname = $("#fullname");
        var popover4 = new bootstrap.Popover(fullname);

        var address = $("#address");
        var popover5 = new bootstrap.Popover(address);

        var detailed_address = $("#detailed_address");
        var popover6 = new bootstrap.Popover(detailed_address);

        var day = $("#day");
        var popover7 = new bootstrap.Popover(day);

        var phone_number = $("#phone_number");
        var popover8 = new bootstrap.Popover(phone_number);

        var email = $("#email");
        var popover9 = new bootstrap.Popover(email);

        var Reg = $("#Reg");
        var popover10 = new bootstrap.Popover(Reg);

        popover1.show();

        checkDuplicate.click(function() {
            popover1.hide();
            popover2.show();
        });

        password1.on('input', function() {
            var inputValue = $(this).val(); // 입력된 값 가져오기
            if (inputValue.length >= 8) {
                popover2.hide();
                popover3.show();
            }
        });

        password2.on('input', function() {
            var inputValue = $(this).val(); // 입력된 값 가져오기
            if (inputValue.length >= 8) {
                popover3.hide();
                popover4.show();
            }
        });
        fullname.on('input', function() {
            var inputValue = $(this).val(); // 입력된 값 가져오기
            if (inputValue == "김상명") {
                popover4.hide();
                popover5.show();
            }
        });
        address.on('input', function() {
            var inputValue = $(this).val(); // 입력된 값 가져오기
            if (inputValue == "충청남도 천안시 동남구 상명대길 31") {
                popover5.hide();
                popover6.show();
            }
        });
        detailed_address.on('input', function() {
            var inputValue = $(this).val(); // 입력된 값 가져오기
            if (inputValue == "상명대학교 천안캠퍼스 한누리관 805호") {
                popover6.hide();
                popover7.show();
            }
        });
        day.on('input', function() {
            var inputValue = $(this).val(); // 입력된 값 가져오기
            if (inputValue.length >= 2) {
                popover7.hide();
                popover8.show();
            }
        });
        phone_number.on('input', function() {
            var inputValue = $(this).val(); // 입력된 값 가져오기
            if (inputValue == "010-0000-0000") {
                popover8.hide();
                popover9.show();
            }
        });
        email.on('input', function() {
            var inputValue = $(this).val(); // 입력된 값 가져오기
            if (inputValue.length >= 10) {
                popover9.hide();
                popover10.show();
            }
        });

});