$("#dropdownMenuButton1").hover(function () {
    $("#dropdownMenuButton2, #dropdownMenuButton3").attr("aria-expanded", "false");
    $("#dropdownMenuButton2, #dropdownMenuButton3").next().removeClass("show");
    $(this).attr("aria-expanded", "true");
    $(this).next().addClass("show");
});
$("#dropdownMenuButton2").hover(function () {
    $("#dropdownMenuButton1, #dropdownMenuButton3").attr("aria-expanded", "false");
    $("#dropdownMenuButton1, #dropdownMenuButton3").next().removeClass("show");
    $(this).attr("aria-expanded", "true");
    $(this).next().addClass("show");
});
$("#dropdownMenuButton3").hover(function () {
    $("#dropdownMenuButton1, #dropdownMenuButton2").attr("aria-expanded", "false");
    $("#dropdownMenuButton1, #dropdownMenuButton2").next().removeClass("show");
    $(this).attr("aria-expanded", "true");
    $(this).next().addClass("show");
});

$(document).ready(function() {
  $(document).on("click", function(event) {
    $("#dropdownMenuButton1, #dropdownMenuButton2, #dropdownMenuButton3").attr("aria-expanded", "false");
    $("#dropdownMenuButton1, #dropdownMenuButton2, #dropdownMenuButton3").next().removeClass("show");
  });
});